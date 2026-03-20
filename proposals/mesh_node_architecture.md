# mesh_node — Repository Architecture

> Status: design proposal
> Stance: Pyrrhonistic — structural claims held provisionally until implementation confirms or revises them

---

## Core Principles

**Additive derivation** — each derived node adds a subdirectory at repo root. The parent's structure is never moved or restructured.

**Single inheritance** — `derived_from` is a single nested object. Full ancestry readable by following the chain. Multiple inheritance deliberately discouraged until a concrete use case demands it.

**`mesh_node.json` as entry point** — lives at repo root always. Current node identity, its own `directories`, and full ancestry chain in `derived_from`. All tooling starts here: `ROOT / "mesh_node.json"`.

**Every node owns a named subdirectory** — including the root node. No special cases in `build_frame.py`. `load_manifest(directory)` resolves identically for every node in the chain.

**Root `tools/` is infrastructure, not content** — `adopt_node.py`, `build_frame.py`, `git_node.py`, `setup.sh` live here. This directory is not iterated by `build_frame.py` and does not have a `manifest.py`.

**`manifest.py` per node** — each node's subdirectory contains `tools/manifest.py` listing what that node contributes to the bundle. `adopt_node.py` creates a stub; the derived node's custodian fills it in.

---

## Relation to node_architecture.md

`proposals/node_architecture.md` covers what a node is — the four components (git repo, Claude Project, I-Language Mastodon instance, E-Language Mastodon instance), the submodule library, the maturation path.

This document covers how the git repo is structured and how the tooling works. Different register, different purpose. They reference each other but neither replaces the other.

---

## Inheritance Chain

```
mesh_node                        ← root; no parent
  └── bootstrap_node             ← adds: corpus ingestion + training pipeline interface
        ├── substack_node        ← adds: Substack-specific ingest tooling
        ├── podcast_node         ← adds: audio → transcript ingest (future)
        └── pdf_node             ← adds: PDF ingest (future)
```

`bootstrap_node` and its derivatives are not designed here. This document covers `mesh_node` only.

---

## Repository Structure

```
repo_root/
├── mesh_node.json               # entry point; current node identity + ancestry chain
├── README.md
├── .gitignore
│
├── tools/                       # repo-level infrastructure; not iterated by build_frame.py
│   ├── git_node.py              # shared git utility
│   ├── adopt_node.py            # derive a new node (additive)
│   ├── build_frame.py           # build context bundle by walking mesh_node.json
│   └── setup.sh                 # install dependencies
│
└── mesh_node/                   # mesh_node's own content directory
    ├── tools/
    │   └── manifest.py          # lists what mesh_node contributes to bundle
    └── interface/
        └── callbacks.py         # base callback registry; Mastodon stub
```

After `bootstrap_node` is adopted:

```
repo_root/
├── mesh_node.json               # updated by adopt_node.py
├── README.md
├── .gitignore
├── tools/                       # unchanged
├── mesh_node/                   # unchanged
└── bootstrap_node/              # added by adopt_node.py
    ├── tools/
    │   └── manifest.py          # stub — filled out when bootstrap_node is built
    └── README.md
```

---

## mesh_node.json — Root Node

```json
{
  "name": "mesh_node",
  "type": "mesh-node",
  "description": "Base node for the epistemic mesh",
  "version": "v0.0.0",
  "repository": "https://github.com/TheSacredLazyOne/mesh_node",
  "license": "CC-BY-SA-4.0",
  "directories": ["mesh_node"],
  "derived_from": null
}
```

---

## mesh_node.json — After Adopting bootstrap_node

```json
{
  "name": "bootstrap_node",
  "type": "bootstrap-node",
  "description": "Corpus ingestion and model training interface",
  "version": "v0.0.0",
  "repository": "https://github.com/TheSacredLazyOne/bootstrap_node",
  "license": "CC-BY-SA-4.0",
  "directories": ["bootstrap_node"],
  "derived_from": {
    "node": "mesh_node",
    "repository": "https://github.com/TheSacredLazyOne/mesh_node",
    "commit": "<hash>",
    "method": "adoption",
    "directories": ["mesh_node"],
    "derived_from": null
  }
}
```

And `substack_node` after adopting from `bootstrap_node`:

```json
{
  "name": "substack_node",
  "type": "substack-node",
  "description": "Substack corpus ingestion and bootstrap training",
  "version": "v0.0.0",
  "repository": "https://github.com/TheSacredLazyOne/substack_node",
  "license": "CC-BY-SA-4.0",
  "directories": ["substack_node"],
  "derived_from": {
    "node": "bootstrap_node",
    "repository": "https://github.com/TheSacredLazyOne/bootstrap_node",
    "commit": "<hash>",
    "method": "adoption",
    "directories": ["bootstrap_node"],
    "derived_from": {
      "node": "mesh_node",
      "repository": "https://github.com/TheSacredLazyOne/mesh_node",
      "commit": "<hash>",
      "method": "adoption",
      "directories": ["mesh_node"],
      "derived_from": null
    }
  }
}
```

---

## mesh_node/tools/manifest.py

All manifests use `parents[1]` — relative to the node's own directory. No special casing. Repo-root files (`mesh_node.json`, `README.md`) are handled directly by `build_frame.py`, which already knows the root.

```python
# mesh_node/tools/manifest.py
from __future__ import annotations
from pathlib import Path

NODE_DIR = Path(__file__).resolve().parents[1]

def files() -> list[Path]:
    """Return files this node contributes to the context bundle."""
    items: list[Path] = []

    items.append(NODE_DIR / "interface" / "callbacks.py")

    return [p for p in items if p.exists()]
```

Stub created by `adopt_node.py` in every derived node's directory — same shape, same `parents[1]`:

```python
# <node_name>/tools/manifest.py
# Stub — fill in what this node contributes to the context bundle.
from __future__ import annotations
from pathlib import Path

NODE_DIR = Path(__file__).resolve().parents[1]

def files() -> list[Path]:
    """Return files this node contributes to the context bundle."""
    return []
```

---

## tools/build_frame.py

Handles repo-root files directly, then reads `mesh_node.json` and walks the `derived_from` chain ancestor-first, calling each node's `<directory>/tools/manifest.py`. No special cases in `load_manifest`.

```python
# tools/build_frame.py
from __future__ import annotations
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_manifest(directory: str) -> list[Path]:
    """Load and call manifest.py from a node directory."""
    manifest_path = ROOT / directory / "tools" / "manifest.py"
    if not manifest_path.exists():
        return []
    spec = importlib.util.spec_from_file_location("manifest", manifest_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.files()

def walk_chain(node: dict) -> list[Path]:
    """Recursively walk derived_from chain, ancestors first, current node last."""
    items: list[Path] = []

    if node.get("derived_from"):
        items += walk_chain(node["derived_from"])

    for directory in node.get("directories", []):
        items += load_manifest(directory)

    return items

def build() -> list[Path]:
    # Repo-root files first — always included regardless of node depth
    items: list[Path] = [
        ROOT / "mesh_node.json",
        ROOT / "README.md",
    ]

    mesh_node = json.loads((ROOT / "mesh_node.json").read_text())
    items += walk_chain(mesh_node)

    return [p for p in items if p.exists()]

if __name__ == "__main__":
    for f in build():
        print(f)
```

---

## tools/git_node.py

Thin shared utility. All tools call into this rather than making raw subprocess calls. Every derived node inherits it.

```python
# tools/git_node.py
from __future__ import annotations
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _run(args: list[str], cwd: Path = ROOT) -> str:
    return subprocess.check_output(["git"] + args, cwd=cwd, text=True).strip()

def head() -> str:
    try:
        return _run(["rev-parse", "HEAD"])
    except subprocess.CalledProcessError:
        return "UNKNOWN"

def remotes() -> list[str]:
    return _run(["remote"]).splitlines()

def remote_add(name: str, url: str) -> None:
    _run(["remote", "add", name, url])

def remote_rename(old: str, new: str) -> None:
    _run(["remote", "rename", old, new])

def stage(paths: list[str] | None = None) -> None:
    _run(["add"] + (paths or ["."]))

def commit(message: str, confirm: bool = True) -> None:
    if confirm:
        print(f"\nProposed commit message:\n\n  {message}\n")
        response = input("Apply? [y/N] ").strip().lower()
        if response != "y":
            print("Commit cancelled.")
            return
    _run(["commit", "-m", message])
```

---

## tools/adopt_node.py

Additive only. Does not move or restructure the parent.

**What it does:**
1. Reads current identity from `ROOT / "mesh_node.json"`
2. Records current HEAD via `git_node.head()`
3. Creates `<new_node>/tools/` directory at repo root
4. Writes stub `<new_node>/tools/manifest.py`
5. Writes `<new_node>/README.md`
6. Updates root `README.md` — appends link to `<new_node>/README.md` under an Inheritance section; creates the section if it does not yet exist
7. Updates `mesh_node.json` — new node becomes current; previous identity moves into `derived_from` with its `directories`
8. Updates git remote via `git_node` — renames `origin` to parent name; adds new `origin`
9. Stages all changes via `git_node.stage()`
10. Prompts for commit via `git_node.commit()`

**Root README.md after two adoptions:**

```markdown
# mesh_node

Base node for the epistemic mesh.

## Inheritance

- [mesh_node](mesh_node/README.md)
- [bootstrap_node](bootstrap_node/README.md)
```

The Inheritance section grows with each adoption. The generic description at the top is written once and never touched by `adopt_node.py`.

**Usage:**
```
python tools/adopt_node.py \
    --name        bootstrap_node \
    --repo        https://github.com/TheSacredLazyOne/bootstrap_node \
    --type        bootstrap-node \
    --description "Corpus ingestion and model training interface"
```

---

## mesh_node/interface/callbacks.py — Mastodon Stub

```python
# mesh_node/interface/callbacks.py
# Stub — Mastodon integration not yet implemented.
# Shape defined here so submodules have a consistent surface to graft onto.

from __future__ import annotations

_registry: dict[str, list] = {}

def register(event_type: str, handler) -> None:
    """Register a handler for an event type. Called by submodules at graft time."""
    _registry.setdefault(event_type, []).append(handler)

def dispatch(event_type: str, payload: dict) -> None:
    """Dispatch an event to all registered handlers. Called by the Mastodon listener."""
    for handler in _registry.get(event_type, []):
        handler(payload)

def registered_events() -> list[str]:
    """Return list of event types with registered handlers."""
    return list(_registry.keys())
```

---

## Mastodon Architecture — Stubs

Two instances (or accounts) per node. Not yet implemented. Recorded here so the shape is visible when implementation begins.

**I-Language instance** — sovereign interior. Limited Federation Mode. Custodian-only allowlist. Command channel lives here. Where the node receives instructions.

**E-Language instance or account** — federated surface. Where the node publishes. Can begin as an account on an existing Mastodon instance; dedicated infrastructure deferred until warranted.

**command_submodule** — not yet designed. When implemented: adds a Mastodon listener that calls `interface/callbacks.dispatch()` for each inbound event. Sovereign repository; grafted by the custodian as a custody act.

---

*Nothing here is final.*
*Status: Proposal — not yet implemented, not yet proposition*
*Upstream of: bootstrap_node, substack_node, command_submodule*
*Downstream of: node_architecture.md*
*Named concepts: additive derivation, mesh_node.json, manifest.py per node, root tools as infrastructure*
*Open: command_submodule design, setup.sh language, inheritance chain versioning strategy*
