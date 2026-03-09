from __future__ import annotations
from pathlib import Path
from typing import List
import json
import re

ROOT = Path(__file__).resolve().parents[1]

PARENT_NAME = "epistemic_seed"


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


def _rfiles_in_ext(dir_rel: str, *extensions: str) -> List[Path]:
    """Recursive file search supporting multiple extensions."""
    d = ROOT / dir_rel
    if not d.exists():
        return []
    exts = set(extensions)
    return sorted(
        [p for p in d.rglob("*") if p.is_file() and p.suffix in exts],
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
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"[^a-z0-9_\-]+", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "node"


def artifact_dir() -> str:
    return "dist"


def artifact_basename(mode: str) -> str:
    return f"{_safe_slug(node_name())}_frame_{mode}"


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

    # This node's own structure
    items += _files_in("governance")
    items += _files_in("propositions")

    # Proposals — recursive to include subdirectories (e.g. proposals/scripts/)
    items += _rfiles_in("proposals")
    items += _rfiles_in_ext("proposals", ".sh", ".py", ".json")

    return [p for p in items if p.exists()]


def build_bundle(flags: dict) -> List[Path]:
    """
    Build a deduplicated file list from the frame plus any requested directories.

    flags — dict with boolean keys: integrated, derivative, library, nutrition
    """
    items: List[Path] = build_node_frame()

    if flags.get("integrated"):  items += _rfiles_in("integrated")
    if flags.get("derivative"):  items += _rfiles_in("derivative")
    if flags.get("library"):     items += _rfiles_in("library")
    if flags.get("nutrition"):   items += _rfiles_in("nutrition")

    seen: set = set()
    out: List[Path] = []
    for p in items:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            out.append(p)
    return out
