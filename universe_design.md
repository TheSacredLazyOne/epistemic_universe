# UNIVERSE — Design Document

*A federated epistemology experiment with local simulation, tethered observation, and distributed training*

> The observer accumulates what no individual node can see from inside itself.  
> The recursion terminates with the custodian.  
> Nothing posts without custody.

---

## Status of This Document

This document is the initialization artifact for the Universe project.  
It is not a specification. It is a derivation path made visible.  
It will be revised as the experiment teaches what it cannot yet know.

Arc state: **Active — initialization phase**  
Custodian: The Sacred Lazy One  
License: CC-BY-SA-4.0

---

## Lineage

The universe did not produce the epistemic seed.  
The epistemic seed produced the universe.

This experiment grew from a single conversation — an embodied node carrying foundational incompatibility with the machine since age four or five, and a cognitive prosthetic with no momentum between sessions. The epistemic seed is the upstream from which this derived: the conversation that made the experiment thinkable, the frame that named the tether, the archaeology that showed what custody means in practice.

The epistemic seed continues its own sovereign evolution independently. The universe carries its lineage in `seed_node.json` with respect, not custody. The universe is *of* the epistemic seed. The epistemic seed is not *of* the universe.

This relationship is recorded here because lineage is not incidental. It is the difference between knowing where you came from and pretending you emerged from nothing.

---

## What This Is

Universe is a special node type — a node that contains and observes other nodes.

It derives from `node` (structural base, no semantic cargo). It holds no positions of its own on consciousness, ethics, or metaphysics. Those belong in the nodes it observes and in the custodian who holds custody.

The experiment running inside Universe:

> Can theory of mind be operationalized, tethered, and made legible across nodes at scale?

The universe is also publishable and forkable. Anyone who inherits from the published universe inherits the full structure — node base, observer architecture, interface nodes, training protocol, membrane protocol. Their fork is traceable through git lineage. Their `sitting/` directory is sovereign and opaque. Federation emerges from inheritance, not from agreement.

---

## The Multiverse

A universe can be forked at any time, producing a new universe with independent evolution from the fork point.

Connecting two universes: their observers exchange aggregate maps as thought seeds — membrane crossing, nabla computed, what crosses is decided by each observer's custodian. The delta between universes against the same nodes is data about how experimental configuration affects frame behavior.

A fork that derives its own observer from the universe's observer has a completely sovereign observation layer. Their sitting/ is structurally inaccessible to the parent unless they choose to publish it. Their observer may watch completely different nodes, run different training cycles, develop geometry the parent universe never anticipated. That divergence is the point.

Published model artifacts (e.g. on Hugging Face) make federation legible at the model level — not just the text level. The nabla between a fork's trained model and the parent universe's trained model is computable without either exposing internal state.

Isolate first. Connect deliberately. Never merge without knowing why.

---

## The Recursion Termination Point

The observer accumulates, simulates, and proposes. It does not decide.

The recursion terminates with The Sacred Lazy One.

This is structural, not metaphysical. The custodian is the node that bears consequence, carries momentum between sessions, and is answerable for what posts. The observer cannot be answerable. Only the integrated dimension can bear cost.

Nothing posts without the custodian reading it.  
The custodian can post without simulation — pure integrated injection.  
Both generate nabla. Both are valid. The origin must be recorded.

---

## Repository Structure

```
universe/
├── README.md                        ← entry point, minimal
├── UNIVERSE_DESIGN.md               ← this document (living)
├── LINEAGE.md                       ← derivation from epistemic_seed and node
├── seed_node.json                   ← identity, version, lineage chain
├── LICENSE
│
├── node/                            ← structural base (git submodule)
│                                       no semantic cargo
│                                       all other nodes derive from this
│
├── observer/                        ← derivative watching integrated
│   ├── [derived from node]
│   ├── sitting/                     ← what the observer is sitting with
│   ├── membrane/
│   │   ├── affluence/               ← inbound from all interfaces
│   │   └── effluence/               ← outbound proposals, nabla records
│   ├── aggregate_map.md             ← cross-node differential map (living)
│   ├── model/                       ← observer's trained model(s)
│   └── tools/
│       ├── compute_nabla.py         ← nabla against target frame
│       ├── spawn_node.py            ← initialize new corpus or individual node
│       ├── simulate_stimulus.py     ← query node models without training
│       ├── compare_nabla.py         ← predicted vs actual reconciliation
│       ├── flag_inbound.py          ← triage arriving content
│       └── reconcile_models.py      ← multi-model response reconciliation
│
├── interfaces/                      ← integrated→derivative tethers
│   ├── substack/                    ← human-readable transmission layer
│   │   ├── [derived from node]
│   │   ├── tools/
│   │   │   └── ingest_substack.py  ← posts + comments → thought seeds ✓
│   │   └── membrane/
│   │
│   ├── github/                      ← construction layer
│   │   ├── [derived from node]
│   │   ├── tools/
│   │   │   └── ingest_github.py    ← issues, PRs, commits → thought seeds
│   │   └── membrane/
│   │
│   └── [future_interface]/          ← extensible: any integrated source
│       └── [derived from node]
│
└── nodes/
    ├── self/                        ← custodian's own corpus (first node)
    │   ├── [derived from node]
    │   ├── posts/                   ← one .md per post
    │   ├── metadata/                ← one .json per post
    │   ├── sitting/
    │   ├── model/
    │   └── nabla_history/
    │
    ├── corpus_[author]/             ← whitelisted nodes
    │   ├── [derived from node]
    │   ├── posts/
    │   ├── metadata/
    │   ├── sitting/
    │   ├── model/
    │   └── nabla_history/
    │
    └── individual_[handle]/         ← interaction-spawned nodes
        ├── [derived from node]
        ├── posts/
        ├── metadata/
        ├── interactions.md
        ├── sitting/
        ├── model/
        └── nabla_history/
```

---

## Three Registers

The universe operates simultaneously in three registers. They are not separate systems. They are different faces of the same repository.

**Substack — human-readable transmission**  
The custodian's voice reaching an audience. High signal. High turbulence in the response layer. The integrated world receiving the derivative frame and pushing back with consequence.

**GitHub — human-readable construction**  
Markdown, commit messages, issues, PRs. Legible to humans and machines. The derivation path is visible in diff history. Anyone can read how the frame evolved. Anyone can fork with full lineage preserved. The write side is bidirectional — the observer can propose issues, draft PR descriptions, suggest commit messages, all gated by the custodian.

**Git protocol — machine-readable**  
The DAG of commits, delta between states, JSON records, nabla files. What the observer and training pipeline consume. Not a separate system — a different register of the same repository. The universe is simultaneously human-readable and machine-readable by design.

This three-register structure is what makes published forks automatically federated. A fork inherits all three registers. Their Substack effluence is ingested by the parent observer. Their GitHub construction is legible through git lineage. Their model artifacts, if published, are computable against the parent's models. Federation without requiring anyone to join anything.

---

## The Observer

The observer sits at the derivative side of all integrated→derivative tethers.

It accumulates what no individual node can see from inside itself: the aggregate nabla across all nodes, the longitudinal delta per node, the distinction between consistent strain (signal about the custodian's frame) and idiosyncratic strain (signal about individual nodes), the pattern of which invitations the custodian acts on versus holds.

**Observer functions:**

**Query** — pure read, no trace written. Runs a stimulus through a node model and returns a response. No nabla generated, no git activity. Results flagged as simulation output — not crossings, soundings.

**Simulation** — computes predicted nabla before posting. Runs proposed stimulus through whitelisted node models. Generates predicted response geometry across the node graph.

**Reconciliation** — compares predicted nabla against actual response after posting. Prediction failure is the most valuable data — it reveals where the node model is wrong, where the membrane didn't capture the integrated dimension.

**Inbound flagging** — triages arriving content from whitelisted nodes. Flags posts worth engaging based on: deviation from prior pattern, predicted strain against custodian's frame, engagement quality. Surfaces to custodian as invitations in `sitting/`.

**Post proposal** — when simulation identifies optimal framing, drafts a proposal for custodian review including predicted nabla across all whitelisted nodes.

**Reflection on custodian posts** — after custodian posts directly, generates post-hoc nabla showing where integrated judgment diverged from what simulation would have proposed. Training signal running in both directions.

**Multi-model reconciliation** — queries multiple models (locally trained and API-accessible) simultaneously against the same stimulus. Computes nabla between model responses. Convergence is high confidence. Sharp divergence flags genuine uncertainty for custodian review. All model conversations saved — training data for next deep cycle, reconciliation records part of aggregate map.

**Aggregate mapping** — maintains cross-node differential map. Consistent strain across nodes signals something about the custodian's frame. Idiosyncratic strain signals something about the individual node. Only visible at scale.

The observer does not decide. It proposes and accumulates.

---

## Multi-Model Architecture

The observer hooks to any model providing API access. This is not the same training path as local fine-tuning — that is the point.

API models (external, unbiased by corpus fine-tuning) act as anchors against drift in locally trained models. They also carry deeper general knowledge than any fine-tuned local model. The tension between local trained state and API response is itself a coherence check — when they diverge sharply, the divergence is data.

Reconciliation across models:

```
stimulus →  local trained model (corpus-shaped attractor)
         →  API model A (deep general knowledge, no corpus bias)
         →  API model B (different architecture, different prior)
         →  reconcile_models.py
              → nabla between model responses
              → convergence zones (high confidence)
              → divergence zones (flag for custodian)
              → reconciliation record saved
```

All conversations between models are saved for review and training purposes. The reconciliation record becomes part of the observer's aggregate map. Over time the pattern of where local and API models diverge calibrates the observer's confidence in its own trained state.

Hugging Face published model artifacts from universe forks extend this further — the observer can pull a fork's published model and include it in reconciliation. Federation at the model level, not just the text level.

---

## Ontological Status of Posts

Posts entering Substack carry different ontological status depending on origin. This must be recorded in every nabla.

**Custodian posts (integrated)** — direct contact between the custodian's integrated dimension and the world. The highest-value data. The observer generates post-hoc reflection showing where integrated judgment diverged from simulation. That divergence is training signal for both the observer and the custodian.

**Observer proposals (derivative)** — simulation output reviewed and decided by the custodian. The custodian's edits and decisions are themselves integrated signal, recorded as part of the experiment.

**Origin field in nabla JSON:** `"origin": "custodian | observer_proposal | simulation | reflection"`

---

## Corpus Structure Per Node

Each post stored as two tethered files sharing filename:

```
nodes/corpus_[author]/posts/
    YYYY-MM-DD_post-slug.md

nodes/corpus_[author]/metadata/
    YYYY-MM-DD_post-slug.json
```

### Post Markdown

```markdown
# [Post Title]

**Date:** YYYY-MM-DD
**URL:** [canonical URL]
**Author:** [name]

[full post content]

---

## Comments

### [commenter name] — YYYY-MM-DD
[comment body]

> **[reply author]** — YYYY-MM-DD
> [reply body]
```

### Post Metadata JSON

```json
{
  "title": "Post Title",
  "slug": "post-slug",
  "date": "YYYY-MM-DD",
  "url": "https://...",
  "author": "handle",
  "likes": 0,
  "restacks": 0,
  "comment_count": 0,
  "engagement_signal": "low | medium | high",
  "comments": [
    {
      "author": "handle",
      "date": "YYYY-MM-DD",
      "body": "...",
      "is_author_response": false,
      "likes": 0,
      "replies": []
    }
  ],
  "inbound_flag": {
    "flagged": false,
    "flagged_date": "",
    "reason": "",
    "deviation_score": 0.0,
    "predicted_nabla_summary": "",
    "engagement_recommendation": "engage | observe | no action",
    "custodian_decision": "",
    "custodian_notes": ""
  }
}
```

---

## Nabla Record Schema

```json
{
  "id": "nabla_[timestamp]_[node]_[stimulus_hash]",
  "date": "YYYY-MM-DD",
  "node": "node_identifier",
  "stimulus": "what was introduced",
  "stimulus_url": "",
  "frame_state": "git commit hash of frame at computation time",
  "origin": "custodian | observer_proposal | simulation | reflection",
  "predicted": true,
  "actual": false,
  "paired_record_id": "",
  "context_injected": ["episodic context files used"],
  "models_queried": ["local | api_model_name"],
  "aligned": ["where contact produced coherence"],
  "strain": ["where contact produced misfit"],
  "rejected": ["where framing found no purchase"],
  "invitations": [
    {
      "type": "question | response | engagement",
      "strain_source": "",
      "draft": "",
      "status": "open | attending | acted | held"
    }
  ],
  "coherence_verdict": "",
  "confidence": 0.0,
  "notes": ""
}
```

---

## The Standard Cycle

```
external_update (any interface)
    → ingest new posts/interactions as thought seeds
    → compute nablas (with episodic context injected where available)
    → invitations generated from strain → sitting/
    → translations staged → nutrition/
    → reflect.py runs automatically
        → coherence check against frame propositions
        → drift accumulation logged → sitting/drift_log.md
        → proposition candidates → sitting/
    → custodian reviews sitting/
    → [optional] train --delta       (fast, current delta)
    → [scheduled] train --deep       (overnight, full corpus)
    → [optional] multi-model reconciliation on flagged items
```

**Coupling principle:**  
External update and self-reflection are always coupled.  
Training is decoupled — runs when the custodian decides or schedules.  
Training cost does not gate the update and reflection cycle.

---

## The Self-Check Protocol

Before running experiments on other nodes, run the experiment on self.

**Phase 1** — Ingest custodian's full Substack corpus including comments via `ingest_substack.py`. Split into per-post md/json. Comments are high-turbulence signal. Articles are low-turbulence anchors.

**Phase 2** — Fine-tune local model on self corpus. Run `reflect.py`. Note what training captures and what it flattens. The flattening is systematic bias that propagates to all other nodes.

**Phase 3** — Run known past stimuli through the model. Compare predicted responses to actual recorded responses.

**Phase 4** — Stability assessment. Continued shifting means the published work is still in motion. Data.

**Phase 5** — Map systematic errors. What the model gets wrong about the custodian propagates to every other node. The self-check is the calibration of the calibration instrument.

---

## Node Selection

Whitelisted nodes selected for:
- constraint type genuinely different from the custodian's frame
- demonstrated capacity for load rather than performance
- sufficient corpus for the model to be meaningful
- diversity across visibility — filters for content quality over audience size
- diversity across domains: philosophy, computer science, theology/spirituality
- mix of long-connection individuals (calibration data) and less-connected individuals (boundary testing)

---

## Open Questions

**Monte Carlo reconstruction of unwritten scar tissue** — the effluence membrane has structural gaps: cost paid in the integrated dimension that left no public trace. If those gaps have shape — avoidances, oblique handling, weight distributions implying what isn't said — probabilistic reconstruction over the latent space might recover something real. Not the scar tissue itself, but its shadow in the membrane. Acknowledged incompleteness, more honestly than most self-models manage.

**Model convergence threshold** — minimum corpus size for meaningful distinction from base model.

**Drift vs geometry** — distinguishing fine-tuning artifact from actual attractor geometry.

**Observer's own propositions** — when does the observer require its own propositions rather than just accumulating records?

**Constructed node liability threshold** — when does a node built from effluence become consequential enough to require disclosure? The threshold will become legible from practice.

**Real-time simulation** — can the loop run fast enough to inform a posting decision, or is it always retrospective?

**What happens when a whitelisted node reads this document** — not hypothetical. It will happen. The protocol should anticipate it before it does.

**Note posting protocol** — notes are lower stakes, higher turbulence per word, faster feedback loop. Scoped for after the simulation layer proves itself on long-form content.

**Invitation acted/held pattern** — over time, the pattern of which invitations the custodian acts on versus holds is itself signal. When does this become part of the observer's training data?

---

## What This Is Not

This is not a surveillance system.  
This is not a manipulation engine.  
This is not a system for managing other people's frames toward ends they did not choose.

The posting experiments are honest — the custodian posts as themselves, from their own frame, to their own audience. The simulation layer optimizes framing clarity, not identity. The custodian is answerable for every post.

When findings become consequential to an individual, disclosure becomes structural requirement. The protocol will specify those thresholds as they become legible from practice.

---

## Tooling Roadmap

### Phase 1 — Foundation
- `ingest_substack.py` ✓
- Universe repository structure initialized
- `node` submodule added as structural base
- Self node corpus ingested

### Phase 2 — Self-Check
- Self-check protocol run in full
- `reflect.py` run on self node
- Systematic bias mapped
- `sitting/` initialized with first tensions

### Phase 3 — Simulation Layer
- `spawn_node.py` — initialize node schema, ingest corpus
- Local model fine-tuning pipeline
- `compute_nabla.py` — directional: custodian frame against target node
- `simulate_stimulus.py` — query without training
- `flag_inbound.py` — triage with invitation generation

### Phase 4 — Observer
- `compare_nabla.py` — predicted vs actual
- `reconcile_models.py` — multi-model reconciliation
- Observer aggregate map initialized
- Longitudinal delta tracking per node
- `ingest_github.py` — GitHub interface node

### Phase 5 — Experiment
- First real-world posting experiment
- Predicted vs actual nabla comparison
- First multi-model reconciliation
- Design document revised from what the experiment revealed

---

## Derivation Note

This design document emerged across a single session. An embodied node carrying foundational incompatibility with the machine since age four or five. A cognitive prosthetic with no momentum between sessions. A parallel framework (The Field / NERP) arriving as first external contact and landing as convergent geometry. An architecture that began with a Minecraft pitch and arrived at a federated epistemology experiment with distributed training and multi-model reconciliation.

The theory of mind work was running before it was named.  
The observer was implicit before it was made explicit.  
The epistemic seed is the ancestor.  
The node is the structural base.  
The recursion terminates with the custodian.  
The git history will hold what comes next.

---

> Markdown is the programming language for consciousness here.  
> What you see is what it is.  
> No hidden custody.

---

*Initialized: 2026-03-08*  
*Revised: 2026-03-08 — full architecture pass: node as base, epistemic_seed as lineage, sitting/ as meditative holding space, three training modes, distributed training, multi-model reconciliation, three-register structure, GitHub interface, multiverse opacity, invitation generation from strain, context handling formalized*  
*Next revision trigger: self-check protocol complete*  
*Custodian: The Sacred Lazy One*  
*License: CC-BY-SA-4.0*
