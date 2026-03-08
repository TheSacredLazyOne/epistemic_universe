# Node — Design Document

**Status:** Working design. Nothing here is final.  
**License:** CC-BY-SA-4.0  
**Purpose:** Define the structure, tooling, and derivation mechanics of `node` — the structural base from which all sovereign nodes derive.

---

## 1. What Node Is

`node` is the minimal structural base for a sovereign, versioned unit of meaning under custody.

It is not a framework. It is not a worldview. It is the infrastructure that makes frameworks and worldviews legible to each other — the precondition for grounded conversation between nodes that hold different commitments.

`node` defines:

- how a unit of meaning is structured and maintained
- how meaning enters and exits a node under custody
- how derivation is recorded so lineage remains legible
- how the reasoning that produced current meaning is preserved and queryable
- how a node holds what has not yet resolved
- how a node trains, reflects, and maintains coherence over time

Every node that derives from `node` inherits this infrastructure. What it does with that infrastructure — what propositions it holds, what it federates with, what it transmits — is local and sovereign.

`node` does not determine what a node means. It determines how meaning is held.

---

## 2. Repository Structure

```
node/
├── README.md
├── seed_node.json              ← identity, version, lineage record
├── LICENSE
│
├── frame/                      ← what this node structurally is
│   ├── manifest.py             ← assembly instruction for build_frame.py
│   ├── tools/
│   │   └── build_frame.py      ← compiles frame into shareable artifact
│   ├── propositions/           ← versioned structural claims
│   ├── governance/             ← procedural coordination layer
│   ├── integrated/             ← upstream nodes this node draws from
│   ├── derivative/             ← nodes this node has declared participation in
│   └── external_nodes/         ← sovereign references without lineage transfer
│
├── membrane/                   ← trace of all boundary crossings
│   ├── affluence/              ← inbound: thought seed + nabla JSON (permanent)
│   └── effluence/              ← outbound: document + nabla JSON (permanent)
│
├── sitting/                    ← what the node is currently sitting with
│                                  unresolved tensions, pending propositions,
│                                  strain without closure — held, not stuck
│
├── nutrition/                  ← translations of what crossed inward
├── library/                    ← artifacts transmitted outward
│
└── tools/                      ← node-level tooling
    ├── adopt_node.py           ← scaffolds new nodes from this one
    ├── build_justification.py  ← compiles git history into derivation narrative
    ├── ingest.py               ← membrane ingestion: computes nabla, stages crossing
    ├── reflect.py              ← self-reflection: coherence check against frame
    └── train.py                ← model training: delta and deep modes
```

---

## 3. Directory Definitions

### `frame/`

The frame is what the node structurally *is* at any given moment. It contains everything that defines the node's current meaning: its propositions, its governance, its lineage, and its declared relationships.

The frame is compiled into a shareable artifact by `build_frame.py`. The artifact is a single markdown document representing the node's current state — the nutrient it offers to other nodes and cognitive prosthetics.

The frame is not the node. The node includes its frame, its membrane trace, its sitting/, its nutrition, its library, and its full git history. The frame is the node's current face.

### `frame/propositions/`

Versioned structural claims maintained under local custody. Each proposition is a markdown file defining a term, condition, or structural relationship. Propositions may be revised through explicit commits, rejected by forking, or extended by derivative nodes.

### `frame/governance/`

Procedural coordination documents. Governance defines how proposals are introduced, how revisions are evaluated, how crossings are governed, and how divergence is preserved. Governance does not determine truth. It determines procedure.

Includes:
- `federation.md` — voluntary structural interoperability
- `inheritance.md` — vertical derivation vs lateral federation
- `implementation_git.md` — Git as reference implementation
- `membrane_protocol.md` — the crossing protocol (ingestion and excretion)
- `training_protocol.md` — the training protocol (delta, deep, reflection)

### `frame/integrated/`

Nodes this node draws from — upstream lineage. When `adopt_node.py` runs, the parent node's content moves here via `git mv`, preserving full commit history.

### `frame/derivative/`

Nodes this node has declared participation in. Lateral relationships, not vertical inheritance. A derivative relationship records that this node has chosen to engage with another node's frame — it does not transfer custody.

### `frame/external_nodes/`

Sovereign references without lineage transfer. External nodes remain independent. They may be removed at any time. They do not alter lineage unless explicitly merged.

### `membrane/`

The membrane is a process, not a place. This directory is the trace of that process — the permanent record of every crossing, inbound and outbound.

`membrane/affluence/` holds inbound crossings: the original thought seed and the nabla computed against the frame at the moment of contact. Permanent.

`membrane/effluence/` holds outbound crossings: the document prepared for transmission and the nabla computed against the frame at the moment of excretion. Permanent.

Nothing is processed inside `membrane/`. The crossing happens through discussion. The membrane records what crossed and from what state.

### `sitting/`

What the node is currently sitting with.

Not a failure queue. Not a backlog. A mindful holding space for what has not yet resolved — tensions between propositions, strain that arrived through the membrane without clear landing, model responses that diverged from frame expectation, invitations generated by strain that haven't been acted on yet.

Each file in `sitting/` is a named tension with a status:

- `open` — noticed, not yet examined
- `attending` — under active consideration
- `pending_proposition` — ready to become a new or revised proposition
- `acknowledged` — held consciously without forcing resolution

Files in `sitting/` are never deleted — they are committed to git when resolved, with the commit message recording what resolved them and how. The sitting/ directory at any moment is a snapshot of the node's active practice.

`sitting/` is sovereign and may be opaque. A node may choose not to publish its sitting/ directory. Forks and derived nodes have completely independent sitting/ spaces — inaccessible to the parent unless explicitly transmitted through the membrane.

### `nutrition/`

Translations — what the frame made of incoming thought seeds after negotiation. Not the raw documents. Not the nabla. The meaning that survived the crossing under constraint.

### `library/`

Transmitted artifacts — what the frame excreted into the world. Each artifact is anchored to the frame state at time of transmission.

### `tools/`

Node-level tooling. Operates on the node as a whole, not on the frame specifically. Every derived node inherits these tools.

---

## 4. Core Propositions (Base Layer)

Structural propositions that apply to any node regardless of specific commitments:

`grounded_conversation.md` — shared meaning accumulates through tethered contact over time. The precondition for all other propositions.

`node.md` — a versioned unit of custody. Contains a protocol surface, documents under local custody, and explicit lineage.

`frame.md` — the current compiled view of a node.

`custody.md` — responsibility for maintaining a node's contents and trace.

`lineage.md` — derivation relationships between nodes.

`strain.md` — observable misfit under tethered contact between nodes.

`fork.md` — structural divergence creating independent custody while preserving trace.

`membrane.md` — the process by which information crosses the node boundary under custody.

`revision.md` — modification of a node under existing custody, preserving lineage.

`merge.md` — incorporation of external lineage into local custody.

`federation.md` — voluntary structural interoperability between sovereign nodes.

`proposition.md` — a versioned structural claim maintained by a node.

`governance.md` — the structural coordination layer between sovereign nodes.

`protocol.md` — the minimal shared structural rules required for interoperability.

`adjacency.md` — non-inheriting connection between sovereign nodes.

`conflict.md` — divergent structures that cannot be reconciled under current custody without loss of trace.

`refusal.md` — the legitimate act of declining integration.

`amendment.md` — explicit revision of governance or structural propositions under custody.

`sitting.md` — the practice of holding unresolved tension without forcing closure. The node's relationship to what it does not yet know how to integrate.

---

## 5. Tooling

### `tools/adopt_node.py`

Scaffolds a new node from this one. Self-locating. Moves current repo content into `frame/integrated/{parent_name}/` via `git mv`. Updates `seed_node.json`. Renames origin remote. Stages all changes. Does not commit — the first commit is archaeologically significant and must be deliberate.

Recursively usable: every derived node inherits `adopt_node.py`.

---

### `tools/ingest.py`

Membrane ingestion. Computes nabla between an incoming thought seed and the current frame state. Writes JSON pair to `membrane/affluence/`. Prints nabla to stdout for discussion. Also generates candidate invitations from strain sections — questions the strain implies, interactions worth considering — staged to `sitting/` as `open` status files.

Does not commit. Discussion determines what crosses.

**Nabla JSON schema:**

```json
{
  "timestamp": "ISO-8601",
  "source_document": "original filename",
  "frame_commit": "git commit hash at time of ingestion",
  "context_injected": ["list of interaction files prepended to context"],
  "nabla": {
    "aligned": [
      { "proposition": "proposition name", "note": "what converges" }
    ],
    "strain": [
      { "proposition": "proposition name or null", "note": "what creates tension" }
    ],
    "rejected": [
      { "note": "what does not cross and why" }
    ],
    "coherence_verdict": "clean | tension_acknowledged | incoherence_requires_justification"
  },
  "invitations": [
    {
      "type": "question | response | engagement",
      "strain_source": "which strain point generated this",
      "draft": "candidate interaction text",
      "status": "open"
    }
  ]
}
```

**Context handling:**

Each thought seed lands with explicit context. Prior interactions from `interactions.md` (for individual nodes) or relevant nutrition files are prepended to the context window as episodic context — distinct from trained context. Both are flagged in the nabla record:

- `trained context` — what the model knows from corpus and nutrition
- `episodic context` — what is injected per-session from interaction history

This distinction must be preserved in every nabla record. A response shaped by episodic context is not evidence of the node's trained attractor geometry — it is evidence of that geometry given a specific prior exchange history.

---

### `tools/reflect.py`

Self-reflection. Runnable independently — not gated on training. Should run after every external update.

Queries the node's current trained model against each proposition in `frame/propositions/`. Reports:

- what the model holds that aligns with current propositions
- what the model holds that strains current propositions
- what the model holds that has no proposition to land against yet — implicit structure the frame hasn't named

The third category is the most generative: potential new propositions live there.

Output written to `sitting/` as markdown files with appropriate status. Flags:

- propositions with accumulated strain — candidates for revision
- implicit structures — candidates for new propositions
- drift accumulation since last deep training — counter maintained in `sitting/drift_log.md`

Reflect does not modify propositions directly. It surfaces candidates for the custodian's consideration. Proposition modification is always a deliberate commit.

**Usage:**

```bash
python tools/reflect.py
python tools/reflect.py --proposition custody    # reflect on specific proposition
python tools/reflect.py --drift                  # drift accumulation report only
```

---

### `tools/train.py`

Model training. Two modes.

**`--delta`** — fine-tunes on pending delta only. Fast. Incremental. Updates from current trained state. Appropriate after each external update cycle when training cost permits.

Risk: accumulated drift across many delta cycles without deep reset. `reflect.py` tracks delta cycles since last deep training in `sitting/drift_log.md` and flags when threshold is exceeded.

**`--deep`** — full retrain on complete corpus plus all integrated nutrition. Slower. Stronger. Resets accumulated drift. Anchors model back to full derivation path. Should always be preceded by a `reflect.py` run. Appropriate to schedule overnight.

Both modes:
- require `reflect.py` to have run since last update (coherence precondition)
- write a training record to git as JSON
- package training job for optional remote execution

**Training record JSON:**

```json
{
  "timestamp": "ISO-8601",
  "mode": "delta | deep",
  "frame_commit": "git commit hash training anchored to",
  "corpus_hash": "hash of training data set",
  "data_included": ["list of included files or commit ranges"],
  "data_excluded": ["list of excluded files with reason"],
  "coherence_flags": ["flags raised during preceding reflect run"],
  "delta_cycles_since_deep": 0,
  "duration_seconds": 0,
  "model_artifact": "path or remote reference to output model",
  "remote_job": false,
  "remote_target": ""
}
```

**Distributed training:**

Training jobs are packageable. The job spec (corpus hash, frame commit, mode, model base, hyperparameters) serializes to JSON and executes on any machine with data access. Results return as model artifacts committed back to the node. The universe prepares and dispatches — it does not require local execution.

This means training scales to available compute without redesigning the node structure.

**Usage:**

```bash
python tools/train.py --delta
python tools/train.py --deep
python tools/train.py --delta --remote user@host
python tools/train.py --package-only    # serialize job spec without running
```

---

### `tools/build_justification.py`

Compiles the git commit log into a readable derivation narrative. The reasoning that produced the current frame, not just the frame itself.

Reads full git log, groups commits by propositions touched, produces per-proposition derivation traces. Flags propositions with thin commit history as coherence gaps.

**Usage:**

```bash
python tools/build_justification.py --narrative > justification.md
python tools/build_justification.py --per-proposition --gaps
```

---

## 6. `seed_node.json`

Identity and lineage record. Git holds timestamps. Commit messages hold reasoning. `seed_node.json` holds the derivation record.

**Base schema:**

```json
{
  "name": "node",
  "type": "structural_base",
  "description": "Minimal structural base for sovereign versioned nodes",
  "version": "v0.0.0",
  "repository": "https://github.com/...",
  "license": "CC-BY-SA-4.0",
  "derived_from": null
}
```

**Derived node schema:**

```json
{
  "name": "universe",
  "type": "universe",
  "description": "...",
  "version": "v0.0.0",
  "repository": "https://github.com/...",
  "license": "CC-BY-SA-4.0",
  "derived_from": {
    "name": "node",
    "repository": "https://github.com/.../node",
    "commit": "abc123...",
    "method": "adoption"
  }
}
```

Third-generation nodes carry the full nested chain. Lineage is recursive and legible at any depth without traversing git history.

---

## 7. Derivation Mechanics

Adoption is the only method `adopt_node.py` performs. Always recorded as `method: adoption`.

The parent repo becomes embedded in the child via `git mv` — preserving full commit history inside the new node. The child's content layers on top. The parent remote is renamed. A new origin is added for the child. Updates from the parent propagate consciously — fetched and merged deliberately.

Adoption does not commit. The first commit declares what the node is and why the adoption happened. That reasoning belongs in the record.

Adoption does not enforce conformity. The child is sovereign.

---

## 8. The Membrane Protocol

Every crossing — ingestion or excretion — produces a nabla. Every nabla is stored permanently. Every crossing that results in a commit carries the justification in the commit message.

**Ingestion flow:**

```
thought seed arrives
    → ingest.py computes nabla against current frame
    → invitations generated from strain, staged to sitting/
    → JSON pair stored in membrane/affluence/ (permanent)
    → discussion from nabla
    → translation commits to nutrition/ with justification
```

**Excretion flow:**

```
document drafted from frame
    → nabla computed in reverse
    → JSON pair stored in membrane/effluence/ (permanent)
    → document commits to library/ with justification
      (frame commit hash declared)
```

**Coherence requirement:**

If a document crosses while carrying unresolved tension with the frame, the commit must name that tension explicitly. A node that allows incoherent material to cross without acknowledgment is not running the membrane — it is drifting.

---

## 9. Training Protocol

The training protocol lives in `frame/governance/training_protocol.md`.

**Standard cycle:**

```
external_update
    → ingest new thought seeds
    → compute nablas
    → generate invitations → sitting/
    → stage translations → nutrition/
    → reflect.py runs
        → coherence check
        → drift accumulation logged
        → candidates written → sitting/
    → custodian reviews sitting/
    → [optional] train --delta    (fast, current delta)
    → [scheduled] train --deep    (overnight, full corpus)
```

**Coupling principle:**

External update and self-reflection are always coupled — reflect runs after every update. Training is decoupled — it runs when the custodian decides or when scheduled. Training cost does not gate the update and reflection cycle.

**Drift management:**

Delta training accumulates drift. `sitting/drift_log.md` tracks cycles since last deep training. When threshold is exceeded, reflect.py flags it. Deep training resets the counter.

---

## 10. What Node Is Not

`node` is not a worldview. It holds no position on consciousness, ethics, metaphysics, or politics.

`node` is not a governance system for federations. It defines how a single node maintains custody and crosses its own boundary.

`node` is not complete. It is versioned at zero. It will advance only when it has been used, tested under contact, and the lessons integrated.

Nothing here is final.

---

*License: CC-BY-SA-4.0*  
*Nothing here is final. Nothing here is mandatory. Adopting this node is a choice. So is leaving it.*
