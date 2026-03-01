#!/usr/bin/env python3
"""
adopt_node.py — Node Adoption Script

Adopts a new node from the current node by:
  1. Reading parent state from frame/manifest.py and seed_node.json
  2. Moving parent content into integrated/{parent_name}/ via git mv
  3. Scaffolding new node structure at ROOT
  4. Writing new seed_node.json with nested derived_from lineage
  5. Writing new frame/manifest.py
  6. Performing git remote surgery
  7. Staging all changes

Usage (from repo root or tools/ directory):
    python tools/adopt_node.py \
        --name        <new_node_name> \
        --repo        <github_url_of_new_node> \
        --type        <node_type> \
        --description "<one_line_description>"

Arguments:
    --name          Name of the new node (required)
                    e.g. the_sacred_lazy_one

    --repo          GitHub URL where the new node will live (required)
                    e.g. https://github.com/TheSacredLazyOne/the_sacred_lazy_one

    --type          Node type (required)
                    e.g. discipline_node, epistemic-protocol, reasoning_engine

    --description   One-line description of the new node (required)

Parent node and output location are inferred from the script's own path.
Derivation method is always recorded as 'adoption'.

This script is recursively usable — each adopted node inherits it in tools/.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

# ---------------------------------------------------------------------------
# Locate ROOT
# ---------------------------------------------------------------------------

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = TOOLS_DIR.parent

USAGE = dedent("""\
    Usage:
        python tools/adopt_node.py \\
            --name        <new_node_name> \\
            --repo        <github_url> \\
            --type        <node_type> \\
            --description "<description>"

    Arguments:
        --name          Name of the new node (required)
        --repo          GitHub URL where the new node will live (required)
        --type          Node type (required)
                        e.g. discipline_node, epistemic-protocol, reasoning_engine
        --description   One-line description (required)

    Example:
        python tools/adopt_node.py \\
            --name        the_sacred_lazy_one \\
            --repo        https://github.com/TheSacredLazyOne/the_sacred_lazy_one \\
            --type        discipline_node \\
            --description "A discipline node for radical pluralism"
""")


# ---------------------------------------------------------------------------
# Argument parsing — graceful, no argparse crash
# ---------------------------------------------------------------------------

def parse_args() -> dict:
    args = sys.argv[1:]

    if not args or "--help" in args or "-h" in args:
        print(USAGE)
        sys.exit(0)

    parsed = {}
    keys = ["--name", "--repo", "--type", "--description"]
    i = 0
    while i < len(args):
        if args[i] in keys and i + 1 < len(args):
            parsed[args[i].lstrip("-")] = args[i + 1]
            i += 2
        else:
            print(f"Unknown or incomplete argument: {args[i]}\n")
            print(USAGE)
            sys.exit(1)

    missing = [k for k in ["name", "repo", "type", "description"] if k not in parsed]
    if missing:
        print(f"Missing required arguments: {', '.join('--' + m for m in missing)}\n")
        print(USAGE)
        sys.exit(1)

    return parsed


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def git(args: list[str], cwd: Path = ROOT, check: bool = True) -> str:
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check,
    )
    return result.stdout.strip()


def git_head() -> str:
    try:
        return git(["rev-parse", "HEAD"])
    except subprocess.CalledProcessError:
        return "UNKNOWN"


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    git(["mv", str(src.relative_to(ROOT)), str(dst.relative_to(ROOT))])


# ---------------------------------------------------------------------------
# Load parent manifest
# ---------------------------------------------------------------------------

def load_manifest(root: Path):
    manifest_path = root / "frame" / "manifest.py"
    if not manifest_path.exists():
        print(f"Error: no frame/manifest.py found at {root}")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("parent_manifest", manifest_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore
    return mod


# ---------------------------------------------------------------------------
# Read derived_from chain from seed_node.json
# ---------------------------------------------------------------------------

def read_derived_from(root: Path) -> dict | None:
    p = root / "seed_node.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data.get("derived_from", None)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Write new seed_node.json
# ---------------------------------------------------------------------------

def write_seed_node(
    name: str,
    node_type: str,
    description: str,
    repo: str,
    license_name: str,
    parent_name: str,
    parent_repo: str,
    parent_commit: str,
    parent_derived_from: dict | None,
) -> None:
    derived_from: dict = {
        "node": parent_name,
        "repository": parent_repo,
        "commit": parent_commit,
        "method": "adoption",
    }
    if parent_derived_from:
        derived_from["derived_from"] = parent_derived_from

    data = {
        "name": name,
        "type": node_type,
        "description": description,
        "version": "v0.0.0",
        "repository": repo,
        "license": license_name,
        "derived_from": derived_from,
    }

    p = ROOT / "seed_node.json"
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  Wrote seed_node.json")


# ---------------------------------------------------------------------------
# Write new README.md
# ---------------------------------------------------------------------------

def write_readme(name: str, description: str, parent_name: str) -> None:
    content = dedent(f"""\
        # {name}

        {description}

        Version: v0.0.0

        Inherited from: [{parent_name}](./integrated/{parent_name}/README.md)
    """)
    (ROOT / "README.md").write_text(content, encoding="utf-8")
    print(f"  Wrote README.md")


# ---------------------------------------------------------------------------
# Write directory README placeholders
# ---------------------------------------------------------------------------

def write_dir_readme(dir_rel: str, title: str, description: str) -> None:
    d = ROOT / dir_rel
    d.mkdir(parents=True, exist_ok=True)
    p = d / "README.md"
    if not p.exists():
        p.write_text(f"# {title}\n\n{description}\n", encoding="utf-8")
        print(f"  Created {dir_rel}/README.md")


# ---------------------------------------------------------------------------
# Write new frame/manifest.py
# ---------------------------------------------------------------------------

def write_manifest(parent_name: str) -> None:
    frame_dir = ROOT / "frame"
    frame_dir.mkdir(exist_ok=True)

    content = dedent(f'''\
        from __future__ import annotations
        from pathlib import Path
        from typing import List
        import json
        import re

        ROOT = Path(__file__).resolve().parents[1]

        PARENT_NAME = "{parent_name}"


        def _files_in(dir_rel: str) -> List[Path]:
            d = ROOT / dir_rel
            if not d.exists():
                return []
            return sorted(
                [p for p in d.iterdir() if p.is_file() and p.suffix == ".md"],
                key=lambda p: p.name,
            )


        def _rfiles_in(dir_rel: str) -> List[Path]:
            d = ROOT / dir_rel
            if not d.exists():
                return []
            return sorted(
                [p for p in d.rglob("*.md") if p.is_file()],
                key=lambda p: str(p.relative_to(ROOT)),
            )


        # ---------------------------------------------------------------------------
        # Manifest-owned metadata
        # ---------------------------------------------------------------------------

        def frame_schema() -> str:
            return "v0"


        def node_name() -> str:
            p = ROOT / "seed_node.json"
            if not p.exists():
                return "node"
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                name = data.get("name")
                return str(name).strip() if isinstance(name, str) and name.strip() else "node"
            except Exception:
                return "node"


        def _safe_slug(s: str) -> str:
            s = (s or "").strip().lower()
            s = re.sub(r"\\s+", "_", s)
            s = re.sub(r"[^a-z0-9_\\-]+", "", s)
            s = re.sub(r"_+", "_", s).strip("_")
            return s or "node"


        def artifact_dir() -> str:
            return "dist"


        def artifact_basename(mode: str) -> str:
            return f"{{_safe_slug(node_name())}}_frame_{{mode}}"


        def repository_url() -> str | None:
            p = ROOT / "seed_node.json"
            if not p.exists():
                return None
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                repo = data.get("repository")
                return str(repo).strip() if isinstance(repo, str) and repo.strip() else None
            except Exception:
                return None


        def license_name() -> str:
            p = ROOT / "seed_node.json"
            if p.exists():
                try:
                    data = json.loads(p.read_text(encoding="utf-8"))
                    lic = data.get("license")
                    if isinstance(lic, str) and lic.strip():
                        return lic.strip()
                except Exception:
                    pass
            return "CC-BY-SA-4.0"


        def derived_seed_node_info() -> dict | None:
            """Returns derived_from block for child nodes to nest."""
            p = ROOT / "seed_node.json"
            if not p.exists():
                return None
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                return data.get("derived_from", None)
            except Exception:
                return None


        # ---------------------------------------------------------------------------
        # Frame definition
        # ---------------------------------------------------------------------------

        def build_node_frame() -> List[Path]:
            items: List[Path] = []

            # Identity
            items += [ROOT / "seed_node.json"]

            # Root docs
            for name in ["README.md"]:
                p = ROOT / name
                if p.exists():
                    items.append(p)

            # This node\'s own structure
            items += _files_in("governance")
            items += _files_in("propositions")

            # Inherited structure from parent
            items += _files_in(f"integrated/{{PARENT_NAME}}/governance")
            items += _files_in(f"integrated/{{PARENT_NAME}}/propositions")

            return [p for p in items if p.exists()]


        def build_bundle(mode: str) -> List[Path]:
            items = build_node_frame()

            if mode == "integrated":
                items += _rfiles_in("integrated")
            elif mode == "derivative":
                items += _rfiles_in("derivative")
            elif mode == "library":
                items += _rfiles_in("library")
            elif mode == "nutrition":
                items += _rfiles_in("nutrition")
            elif mode == "all":
                items += _rfiles_in("integrated")
                items += _rfiles_in("derivative")
                items += _rfiles_in("library")
                items += _rfiles_in("nutrition")
            elif mode != "none":
                raise ValueError(f"Unknown bundle mode: {{mode}}")

            seen = set()
            out: List[Path] = []
            for p in items:
                rp = p.resolve()
                if rp in seen:
                    continue
                seen.add(rp)
                out.append(p)
            return out
    ''')

    (frame_dir / "manifest.py").write_text(content, encoding="utf-8")
    print(f"  Wrote frame/manifest.py")


# ---------------------------------------------------------------------------
# Git remote surgery
# ---------------------------------------------------------------------------

def git_remote_surgery(parent_name: str, new_repo: str) -> None:
    remotes = git(["remote"]).splitlines()

    if "origin" in remotes:
        if parent_name in remotes:
            print(f"  Warning: remote '{parent_name}' already exists, skipping rename")
        else:
            git(["remote", "rename", "origin", parent_name])
            print(f"  Renamed remote: origin → {parent_name}")
    else:
        print(f"  No origin remote found, skipping rename")

    git(["remote", "add", "origin", new_repo])
    print(f"  Added remote: origin → {new_repo}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()

    name        = args["name"]
    repo        = args["repo"]
    node_type   = args["type"]
    description = args["description"]

    print(f"\nAdopting '{name}' from current node at {ROOT}\n")

    # STEP 1 — Read parent state
    manifest       = load_manifest(ROOT)
    parent_name    = manifest.node_name()
    parent_repo    = manifest.repository_url() or ""
    parent_license = manifest.license_name()
    parent_derived = read_derived_from(ROOT)
    parent_commit  = git_head()
    short_commit   = parent_commit[:12] if parent_commit != "UNKNOWN" else "UNKNOWN"

    print(f"  Parent node:   {parent_name}")
    print(f"  Parent repo:   {parent_repo}")
    print(f"  Parent commit: {short_commit}")
    print()

    # STEP 2 — git mv parent content into integrated/{parent_name}/
    print(f"Moving parent content to integrated/{parent_name}/...")

    integrated_base = ROOT / "integrated" / parent_name
    frame_files = manifest.build_node_frame()

    for src in frame_files:
        if not src.exists():
            continue
        rel = src.relative_to(ROOT)
        dst = integrated_base / rel
        git_mv(src, dst)
        print(f"  git mv {rel} → integrated/{parent_name}/{rel}")

    # Move frame/ directory
    src_frame = ROOT / "frame"
    dst_frame = integrated_base / "frame"
    if src_frame.exists():
        git_mv(src_frame, dst_frame)
        print(f"  git mv frame/ → integrated/{parent_name}/frame/")

    # Move seed_node.json if not already moved via frame_files
    src_seed = ROOT / "seed_node.json"
    if src_seed.exists():
        dst_seed = integrated_base / "seed_node.json"
        git_mv(src_seed, dst_seed)
        print(f"  git mv seed_node.json → integrated/{parent_name}/seed_node.json")

    print()

    # STEP 3 — Scaffold new node directories
    print("Scaffolding new node structure...")

    gitignore = ROOT / ".gitignore"
    ignore_entry = "__pycache__/\n*.pyc\n"
    if gitignore.exists():
        if "__pycache__" not in gitignore.read_text():
            gitignore.write_text(gitignore.read_text() + ignore_entry)
    else:
        gitignore.write_text(ignore_entry)
    print(f"  Wrote .gitignore")

    write_dir_readme(
        "propositions", "Propositions",
        "Structural claims maintained by this node.\n\n"
        "Divergence is handled structurally through revision, lineage, or fork.",
    )
    write_dir_readme(
        "governance", "Governance",
        "Procedural coordination layer for this node.",
    )
    write_dir_readme(
        "library", "Library",
        "Derivative work flowing outward from this node into the derivative world.\n\n"
        "Ordered by emergence, not by topic.",
    )
    write_dir_readme(
        "nutrition", "Nutrition",
        "Integrative work flowing inward — nourishment that fed this node's formation.\n\n"
        "External frameworks, contact with other nodes, things metabolized from outside.",
    )
    print()

    # STEP 4 — Write new root files
    print("Writing new node root files...")
    write_seed_node(
        name=name,
        node_type=node_type,
        description=description,
        repo=repo,
        license_name=parent_license,
        parent_name=parent_name,
        parent_repo=parent_repo,
        parent_commit=parent_commit,
        parent_derived_from=parent_derived,
    )
    write_readme(name, description, parent_name)
    print()

    # STEP 5 — Write new manifest
    print("Writing new frame/manifest.py...")
    write_manifest(parent_name)
    print()

    # STEP 6 — Git remote surgery
    print("Updating git remotes...")
    git_remote_surgery(parent_name, repo)
    print()

    # STEP 7 — Stage all changes
    print("Staging all changes...")
    git(["add", "."])
    print("  git add .")
    print()

    print("=" * 60)
    print(f"Node '{name}' adopted from '{parent_name}' @ {short_commit}")
    print("=" * 60)
    print()
    print("Review staged changes:")
    print("  git status")
    print("  git diff --staged")
    print()
    print("Then commit:")
    print(f"  git commit -m 'Adopt {name} from {parent_name} @ {short_commit}'")
    print()
    print("Then push:")
    print(f"  git push -u origin main")


if __name__ == "__main__":
    main()
