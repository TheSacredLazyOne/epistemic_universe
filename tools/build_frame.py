# tools/build_frame.py
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from typing import List

ROOT = Path(__file__).resolve().parents[1]

USAGE = dedent("""\
    Usage:
        python tools/build_frame.py [options]

    Directory flags (presence/absence controls inclusion):
        --integrated    include integrated/ (default: on)
        --no-integrated exclude integrated/
        --derivative    include derivative/ (default: on)
        --no-derivative exclude derivative/
        --library       include library/    (default: off)
        --no-library    exclude library/
        --nutrition     include nutrition/  (default: off)
        --no-nutrition  exclude nutrition/

    Other:
        --out <path>    output path relative to repo root
                        (default: dist/<node>_frame.md)

    Examples:
        python tools/build_frame.py
            -> frame + integrated + derivative (default)

        python tools/build_frame.py --library --nutrition
            -> frame + integrated + derivative + library + nutrition

        python tools/build_frame.py --no-integrated --no-derivative
            -> frame only

        python tools/build_frame.py --no-integrated --no-derivative --nutrition
            -> frame + nutrition only
""")


# ---------------------------------------------------------------------------
# Argument parsing — graceful, no argparse crash
# ---------------------------------------------------------------------------

def parse_args() -> dict:
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(USAGE)
        sys.exit(0)

    parsed = {
        "integrated": False,
        "derivative": False,
        "library":    True,
        "nutrition":  True,
        "out":        None,
    }

    flags = {
        "--integrated":    ("integrated", True),
        "--no-integrated": ("integrated", False),
        "--derivative":    ("derivative", True),
        "--no-derivative": ("derivative", False),
        "--library":       ("library",    True),
        "--no-library":    ("library",    False),
        "--nutrition":     ("nutrition",  True),
        "--no-nutrition":  ("nutrition",  False),
    }

    i = 0
    while i < len(args):
        if args[i] in flags:
            key, val = flags[args[i]]
            parsed[key] = val
            i += 1
        elif args[i] == "--out" and i + 1 < len(args):
            parsed["out"] = args[i + 1]
            i += 2
        else:
            print(f"Unknown or incomplete argument: {args[i]}\n")
            print(USAGE)
            sys.exit(1)

    return parsed


# ---------------------------------------------------------------------------
# Bundle mode label for artifact name and header
# ---------------------------------------------------------------------------

def bundle_label(args: dict) -> str:
    parts = ["frame"]
    if args["integrated"]:  parts.append("integrated")
    if args["derivative"]:  parts.append("derivative")
    if args["library"]:     parts.append("library")
    if args["nutrition"]:   parts.append("nutrition")
    return "+".join(parts)


# ---------------------------------------------------------------------------
# Git
# ---------------------------------------------------------------------------

def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "UNKNOWN"


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def load_manifest_module():
    manifest_path = ROOT / "frame" / "manifest.py"
    if not manifest_path.exists():
        print(f"Error: no frame/manifest.py found at {ROOT}")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("node_manifest", manifest_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore
    return mod


# ---------------------------------------------------------------------------
# Frame rendering
# ---------------------------------------------------------------------------

def relpath(p: Path) -> str:
    return p.resolve().relative_to(ROOT.resolve()).as_posix()


def section_for(rel: str) -> str:
    if rel.startswith("integrated/"):
        return "INTEGRATED REFERENCES"
    if rel.startswith("derivative/"):
        return "DERIVATIVE REFERENCES"
    if rel.startswith("library/"):
        return "LIBRARY"
    if rel.startswith("nutrition/"):
        return "NUTRITION"
    return "FRAME"


def dirkey(rel: str) -> str:
    p = Path(rel)
    parent = p.parent.as_posix()
    return parent if parent != "." else "ROOT"


def demote_headings(md: str, levels: int) -> str:
    out_lines: List[str] = []
    for line in md.splitlines():
        if line.startswith("#"):
            n = 0
            while n < len(line) and line[n] == "#":
                n += 1
            if 1 <= n <= 6 and n < len(line) and line[n] == " ":
                new_n = min(6, n + levels)
                line = ("#" * new_n) + line[n:]
        out_lines.append(line)
    return "\n".join(out_lines)


def render_file(src: Path) -> str:
    raw = src.read_text(encoding="utf-8").rstrip()
    suf = src.suffix.lower()

    if suf == ".md":
        return demote_headings(raw, levels=3) + "\n"

    if suf == ".json":
        try:
            obj = json.loads(raw)
            pretty = json.dumps(obj, indent=2, ensure_ascii=False).rstrip()
        except Exception:
            pretty = raw

        if src.name == "seed_node.json":
            return f"<!-- seed_node.json -->\n```json\n{pretty}\n```\n"
        return f"```json\n{pretty}\n```\n"

    return f"```text\n{raw}\n```\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()
    mod = load_manifest_module()

    # Build file list from manifest then filter by flags
    files: List[Path] = mod.build_node_frame()

    def add(dir_rel: str) -> List[Path]:
        d = ROOT / dir_rel
        if not d.exists():
            return []
        return sorted(
            [p for p in d.rglob("*.md") if p.is_file()],
            key=lambda p: str(p.relative_to(ROOT)),
        )

    if args["integrated"]:  files += add("integrated")
    if args["derivative"]:  files += add("derivative")
    if args["library"]:     files += add("library")
    if args["nutrition"]:   files += add("nutrition")

    # Deduplicate
    seen = set()
    out_files: List[Path] = []
    for p in files:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            out_files.append(p)

    label = bundle_label(args)
    default_out = f"{mod.artifact_dir()}/{mod.artifact_basename(label)}.md"
    out_rel = args["out"] or default_out

    out_path = ROOT / out_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)

    head = git_head()
    now = datetime.utcnow().isoformat(timespec="seconds") + "Z"

    parts: List[str] = []
    parts.append("# Node\n\n")
    parts.append(f"> Node: {mod.node_name()}\n")
    parts.append(f"> Repository: {mod.repository_url()}\n")
    parts.append(f"> Source commit: `{head}`\n")
    parts.append(f"> License: {mod.license_name()}\n")
    parts.append(f"> Frame schema: {mod.frame_schema()}\n")
    parts.append(f"> Generated: {now}\n")
    parts.append(f"> Bundle mode: `{label}`\n\n")
    parts.append("---\n\n")

    current_section: str | None = None
    current_dir: str | None = None

    for src in out_files:
        if not src.is_absolute():
            src = (ROOT / src).resolve()

        rel = relpath(src)
        sec = section_for(rel)

        if sec != current_section:
            current_section = sec
            current_dir = None
            parts.append(f"\n\n# {current_section}\n\n")

        dk = dirkey(rel)
        if dk != current_dir:
            current_dir = dk
            parts.append(f"\n\n## Directory: `{dk}`\n\n")

        parts.append("\n---\n\n")
        parts.append(f"### `{rel}`\n\n")
        parts.append(render_file(src))

    out_path.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {out_rel}")


if __name__ == "__main__":
    main()
