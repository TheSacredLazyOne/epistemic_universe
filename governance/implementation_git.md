# Git Reference Implementation

This repository uses Git as the reference implementation for custody, revision, lineage, and fork.

Git is not ontology.
It is the membrane implementation for traceable coordination.

---

## Revision (within custody)

Revision updates a node under existing custody.

Workflow:
- edit files
- commit changes
- push to remote

Commands:
git status
git add .
git commit -m "Describe revision"
git push

Revision preserves lineage.

---

## Fork (divergence)

Forking creates a new node with independent custody while preserving trace.

Options:

A) GitHub Fork (automatic upstream linkage)

B) Manual fork:

git clone <upstream_repo_url> <new_repo_dir>
cd <new_repo_dir>
git remote rename origin upstream
git remote add origin <new_repo_url>
git push -u origin main

Fork establishes new custody.
Upstream is preserved for reference.

---

## Pull Requests (negotiated reintegration)

Pull Requests are the reference implementation of negotiated revision across custody boundaries.

A Pull Request:
- proposes revision from one node to another
- preserves sovereign custody
- allows review under Namaste (symmetric recognition)
- may be accepted, modified, or rejected

PR acceptance is voluntary.
Rejection does not invalidate the fork.

Pull Requests operationalize tethered negotiation between nodes.

---

## Derivation (upstream tracking)

A derived node tracks upstream and selectively integrates changes.

Add upstream:
git remote add upstream <repo_url>
git fetch upstream

Merge:
git merge upstream/main
git push

Derivation is explicit adoption.
Fork is structural divergence.

---

## Naming Conventions

These conventions preserve structural clarity:

- `delta_` — structural extension
- `pdelta_` — protocol-level delta
- `propositions/` — substrate vocabulary
- `metabolite_` — higher-layer exploratory documents
- `docs/` — implementation details

Naming is conventional, not enforced.
Nodes may alter conventions through revision or fork.

---

## Lineage Recording

Each node should document:
- parent repository URL
- parent commit hash adopted
- method (fork / derivation / adoption)

Git history preserves mechanical trace.
LINEAGE preserves semantic intent.