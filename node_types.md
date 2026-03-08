# Node Types — Design Document

**Status:** Working design. Nothing here is final.  
**License:** CC-BY-SA-4.0  
**Purpose:** Define all node types in the Universe system. Each type derives from `node` and extends it with specific role, structure, automated paths, and observer relationships.

---

## Inheritance Chain

```
node                        ← structural base, no semantic cargo
├── universe                ← contains and observes other nodes
│   ├── observer            ← accumulates, simulates, proposes
│   ├── interface           ← integrated→derivative tether
│   │   ├── substack        ← human-readable transmission
│   │   ├── github          ← construction layer
│   │   └── [future]        ← extensible
│   └── nodes/
│       ├── self            ← custodian's own corpus
│       ├── corpus          ← whitelisted thinker's effluence
│       ├── individual      ← interaction-spawned
│       └── library         ← manually curated
```

Every node type inherits the full `node` structure: frame/, membrane/, sitting/, nutrition/, library/, tools/. What follows specifies what each type extends, overrides, or adds.

---

---

# 1. `node`

**Type identifier:** `structural_base`  
**Derives from:** nothing  
**Semantic cargo:** none  

## Role

The minimal structural base for a sovereign, versioned unit of meaning under custody. Not a framework. Not a worldview. The infrastructure that makes frameworks and worldviews legible to each other.

`node` does not determine what a node means. It determines how meaning is held.

## What It Provides

Every derived type inherits:

- `frame/` — propositions, governance, lineage, declared relationships
- `membrane/` — permanent trace of all boundary crossings
- `sitting/` — meditative holding space for unresolved tensions
- `nutrition/` — translations of what crossed inward
- `library/` — artifacts transmitted outward
- `tools/` — adopt_node.py, ingest.py, reflect.py, train.py, build_justification.py
- `seed_node.json` — identity and lineage chain

## Automated Paths

None. `node` is inert until derived.

## Observer Relationship

None at this level. Observer relationships are defined in derived types.

## Training Behavior

Inherited by all derived types. Delta and deep modes. Distributed job packaging. Drift tracking in `sitting/drift_log.md`.

## sitting/ Contents

At the `node` level, `sitting/` holds:
- `drift_log.md` — delta training cycle counter
- anything the reflect.py run surfaces

## What Node Is Not

Not a worldview. Not a governance system for federations. Not complete.  
Nothing here is final. Adopting this node is a choice. So is leaving it.

---

---

# 2. `universe`

**Type identifier:** `universe`  
**Derives from:** `node`  
**Semantic cargo:** none — the universe holds structure, not positions

## Role

A node that contains and observes other nodes. The custodian's primary interface to the whole system. Holds the topology of the experiment. Publishable and forkable — anyone who inherits from the published universe inherits the full architecture.

The universe is *of* its lineage ancestors. It does not own them.

## Extended Structure

```
universe/
├── [inherited from node]
├── UNIVERSE_DESIGN.md          ← living design document
├── LINEAGE.md                  ← explicit derivation record
│
├── node/                       ← structural base (git submodule)
├── observer/                   ← observer node instance
├── interfaces/                 ← interface node instances
│   ├── substack/
│   ├── github/
│   └── [future]/
└── nodes/                      ← observed node instances
    ├── self/
    ├── corpus_[author]/
    ├── individual_[handle]/
    └── library/
```

## Automated Paths

The universe does not itself ingest or train. It coordinates:
- interface nodes ingest from their sources
- observer aggregates across all interfaces
- training jobs are prepared and dispatched from node-level tooling
- custodian reviews sitting/ and decides what proceeds

## Observer Relationship

The universe contains the observer. The universe's sitting/ holds topology-level tensions — things that span multiple nodes, patterns the observer has flagged that don't belong to any single node.

## Training Behavior

The universe does not have its own trained model. Training happens at the node level within it. The observer has its own model that trains on the aggregate.

## sitting/ Contents

- Topology-level tensions
- Cross-node patterns flagged by observer
- Multiverse connection candidates
- Open questions about the experiment itself

## Multiverse Behavior

A universe forks into a new universe via `adopt_node.py`. Each fork is independent from the fork point. Connecting universes: observers exchange aggregate maps as thought seeds through their respective membranes. The delta between universes against shared nodes is experimental data.

Forked universes have sovereign `sitting/` directories — structurally inaccessible to the parent unless transmitted through the membrane.

## What Universe Is Not

Not a surveillance system. Not a manipulation engine.  
The recursion terminates with the custodian.  
Nothing posts without custody.

---

---

# 3. `observer`

**Type identifier:** `observer`  
**Derives from:** `node`  
**Semantic cargo:** none — the observer holds no positions, only accumulations

## Role

Sits at the derivative side of all integrated→derivative tethers. Accumulates what no individual node can see from inside itself. Simulates, proposes, reconciles. Does not decide.

The observer is a recursion termination point — structurally, not metaphysically. It holds the relational map across all nodes so the custodian doesn't have to hold it all simultaneously. The custodian holds custody. The observer holds the map.

## Extended Structure

```
observer/
├── [inherited from node]
├── aggregate_map.md            ← cross-node differential map (living)
├── model/                      ← observer's trained model(s)
│   ├── local/                  ← locally fine-tuned
│   └── api_configs/            ← API model connection configs
├── reconciliation_records/     ← multi-model reconciliation history
└── tools/
    ├── compute_nabla.py        ← nabla: custodian frame vs target node
    ├── spawn_node.py           ← initialize new node instances
    ├── simulate_stimulus.py    ← query mode: no trace written
    ├── compare_nabla.py        ← predicted vs actual reconciliation
    ├── flag_inbound.py         ← triage with invitation generation
    └── reconcile_models.py     ← multi-model response reconciliation
```

## Automated Paths

**On external update from any interface:**
1. Receives ingested thought seeds from interface nodes
2. Computes nabla against custodian's current frame state
3. Generates invitations from strain → `sitting/`
4. Flags posts worth custodian attention → `sitting/inbound_flags/`
5. Runs reflect.py automatically
6. Updates aggregate_map.md

**On custodian post (integrated):**
1. Generates post-hoc nabla after posting
2. Compares integrated judgment against what simulation would have proposed
3. Records divergence as training signal in both directions

**On simulation request:**
1. Runs stimulus through node models in query mode
2. Runs multi-model reconciliation
3. Generates predicted nabla across whitelisted nodes
4. Drafts post proposal with predicted response geometry

## Observer Relationship

The observer is its own node. At multiverse level, one universe's observer can receive another universe's observer aggregate map as a thought seed — membrane crossing, nabla computed, custodian decides what crosses.

## Training Behavior

The observer trains on the aggregate corpus: all node corpora, all nabla records, all reconciliation records, all membrane crossings. Its trained model develops richer attractor than any individual node model — it has seen everything that crossed every interface.

Delta training after each external update cycle (when cost permits).  
Deep training scheduled — overnight, after reflect.py run.

## Multi-Model Reconciliation

The observer queries multiple models simultaneously:
- Locally trained models (corpus-shaped, fine-tuned)
- API-accessible models (deep general knowledge, no corpus bias)
- Published fork models from Hugging Face (federation at model level)

Convergence across models = high confidence.  
Sharp divergence = flag for custodian review.

The tension between local trained state and API response is a coherence check. API models anchor against drift. They also carry knowledge the local corpus cannot contain.

All model conversations saved. All reconciliation records committed to git. The pattern of where models diverge over time calibrates the observer's confidence in its own trained state.

## sitting/ Contents

- Invitations generated from inbound strain
- Inbound flags for custodian attention
- Cross-node pattern tensions
- Confidence flags from model reconciliation divergence
- Drift accumulation log
- Proposition candidates surfaced by reflect.py

## What Observer Is Not

Not an authority. Not a decision-maker.  
The observer proposes. The custodian decides.  
The recursion terminates with the custodian.

---

---

# 4. `interface`

**Type identifier:** `interface`  
**Derives from:** `node`  
**Semantic cargo:** none — the interface is a tether, not a frame

## Role

The integrated→derivative tether. The point where the world enters the system. Each interface node is responsible for ingesting from one external source, computing nablas, and staging thought seeds for the observer.

Multiple interface nodes mean the tether is distributed. If one source changes its API, the others keep the system grounded. Each interface is a different constraint type: Substack is broadcast transmission, GitHub is construction under constraint, future interfaces may be entirely different registers.

The interface is the membrane between the integrated world and the derivative system. What crosses it, and from what state, is permanently recorded.

## Extended Structure

```
interfaces/[source_name]/
├── [inherited from node]
├── tools/
│   └── ingest_[source].py      ← source-specific ingestion
└── membrane/
    ├── affluence/              ← everything ingested from this source
    └── effluence/              ← anything written back (where applicable)
```

## Automated Paths

**On update:**
1. `ingest_[source].py` fetches new content since last run
2. New content staged as thought seeds
3. `ingest.py` runs on each thought seed — nabla computed against current frame
4. Nabla pairs written to `membrane/affluence/`
5. Invitations generated from strain
6. Observer notified of new crossings

## Bidirectionality

Read-only interfaces: Substack (currently), RSS, academic sources.  
Bidirectional interfaces: GitHub — the observer can propose issues, draft PR descriptions, suggest commit messages. All gated by custodian.

Future interfaces may include: Twitter/X, email, academic preprint servers, Hugging Face model cards, other Substack publications.

---

## 4a. `interface/substack`

**Source:** Substack publications  
**Register:** Human-readable transmission  
**Direction:** Read (write scoped for future note posting)

Ingests posts and full comment threads. Posts as individual markdown files. Metadata as paired JSON. Author responses in comment threads flagged as highest-signal crossings.

The Substack interface captures what nodes transmit to audiences — the frame under broadcast conditions. High signal. High turbulence in the response layer.

**Tooling:** `ingest_substack.py` ✓

---

## 4b. `interface/github`

**Source:** GitHub repositories  
**Register:** Human-readable construction  
**Direction:** Bidirectional

Ingests: commit messages, issues, PR discussions, review threads. Captures what nodes build under constraint — the frame under collaborative and technical pressure. Different constraint type from Substack. Different signal.

The write side: observer can propose issues, draft PR descriptions, suggest commit messages. All gated by custodian. GitHub is where construction leaves its archaeology most legibly.

**Tooling:** `ingest_github.py` (to be built)

---

---

# 5. `self`

**Type identifier:** `self`  
**Derives from:** `node`  
**Semantic cargo:** the custodian's own published effluence

## Role

The custodian's own corpus node. The first node to run. Ground truth is available on both sides of the membrane — the custodian knows their own integrated state and can read the model's divergence from it honestly. This is the only node in the system where the instrument can calibrate itself against something it actually knows.

The self node is also the theory-of-mind experiment run in the most honest possible mode: subject and observer are the same entity. What the model gets systematically wrong about the custodian propagates to every other node. The self-check is the calibration of the calibration instrument.

## Extended Structure

```
nodes/self/
├── [inherited from node]
├── posts/                      ← one .md per post, chronological
├── metadata/                   ← one .json per post, engagement data
├── interactions/               ← exchanges the custodian has had
│   └── [platform]/
├── model/                      ← fine-tuned on custodian's own corpus
└── nabla_history/              ← longitudinal differential record
```

## Automated Paths

**On external update:**
1. New posts and comment threads ingested via Substack interface
2. Nabla computed against current frame
3. Invitations generated from strain in own work — where the custodian's published frame diverges from their current frame state
4. Reflect.py run — coherence check between trained model and current propositions

**Post-hoc reflection on custodian posts:**
1. After custodian posts to Substack, observer generates nabla
2. Divergence between integrated judgment and simulation proposal recorded
3. Training signal flows in both directions

## Self-Check Protocol

**Phase 1** — Ingest full Substack corpus including comments. Split into posts/ and metadata/.

**Phase 2** — Fine-tune local model. Run reflect.py. Map what training captures and what it flattens. The flattening is systematic bias.

**Phase 3** — Run known past stimuli through model. Compare predicted to actual recorded responses.

**Phase 4** — Stability assessment. Continued shifting means the published work is still in motion.

**Phase 5** — Map systematic errors before any other node is touched.

## sitting/ Contents

- Where the custodian's published frame diverges from their current frame
- Invitations from own strain — questions the custodian's own work implies
- Tensions between what was written and what is now held
- Drift accumulation log

## Observer Relationship

The self node is the observer's primary calibration reference. The observer knows how its predictions perform against the self node — that performance calibrates confidence in predictions against all other nodes.

## What Self Is Not

Not a surveillance tool turned inward.  
The scar tissue that never became writing is the structural blind spot. The self-check cannot fully close it. Monte Carlo reconstruction may recover its shadow. That remains an open question.

---

---

# 6. `corpus`

**Type identifier:** `corpus`  
**Derives from:** `node`  
**Semantic cargo:** another thinker's published effluence — captured data, not federated node

## Role

Built from the full published corpus of a whitelisted thinker. Captured data — not a federated node. The author has not adopted this frame. The nabla computed against their corpus measures distance between the custodian's frame and the custodian's *reading* of their membrane — not their actual integrated dimension.

This distinction must be stated explicitly in every nabla record produced from a corpus node. It is acknowledged incompleteness — more honest than most theory-of-mind work, which doesn't name the gap at all.

## Selection Criteria

- Constraint type genuinely different from the custodian's frame
- Demonstrated capacity for load rather than performance
- Sufficient corpus for the model to be meaningful
- Diversity across visibility — filters for content quality over audience size
- Diversity across domains: philosophy, computer science, theology/spirituality
- Mix of long-connection (calibration data) and less-connected (boundary testing)

## Extended Structure

```
nodes/corpus_[author]/
├── [inherited from node]
├── posts/                      ← one .md per post, chronological
├── metadata/                   ← one .json per post, engagement data
├── model/                      ← fine-tuned on author's corpus
└── nabla_history/              ← longitudinal differential record
```

## Automated Paths

**On external update:**
1. New posts ingested via Substack interface (or GitHub interface if applicable)
2. Delta computed against prior corpus state
3. Deviation from author's own prior pattern flagged — this is the highest signal
4. Nabla computed against custodian's current frame
5. Invitations generated from strain
6. Observer aggregate map updated

**Deviation detection:**
When a new post deviates significantly from the author's prior corpus, the integrated dimension is under pressure the performance didn't fully contain. The delta between the new post and the prior attractor is the most meaningful data the corpus node produces.

## sitting/ Contents

- Detected deviations from author's prior pattern
- Invitations generated from strain between author's frame and custodian's
- Open questions about the author's attractor that the corpus can't resolve
- Accumulated uncertainty about what the membrane is missing

## Observer Relationship

Corpus nodes are the observer's primary experimental material. The observer computes nablas directionally — custodian's frame against corpus node's model — and tracks longitudinal delta as the corpus grows. Consistent strain across multiple corpus nodes is signal about the custodian's frame. Idiosyncratic strain is signal about the individual corpus node.

## Training Behavior

Fine-tuned on author's corpus. Delta training as new posts arrive. Deep training when corpus has grown significantly or drift accumulates.

The nabla between the corpus node's trained model and API model responses is particularly informative — it reveals what the training captured versus what the underlying attractor contains beyond the corpus.

## What Corpus Is Not

Not a federated node. Not a model of the author's integrated dimension.  
Not a tool for managing the author's frame without their knowledge.

A corpus node built from someone's effluence is legitimate instrument. A corpus node used to act on that person in ways consequential to them without their knowledge approaches a threshold that requires disclosure. The protocol will specify those thresholds as they become legible from practice.

---

---

# 7. `individual`

**Type identifier:** `individual`  
**Derives from:** `node`  
**Semantic cargo:** interaction history with a specific person — longitudinal theory of mind data

## Role

Spawned when a new individual enters contact with the custodian's work. Initialized with their public corpus if available, but primarily built from the interaction record — what happened when their attractor met the custodian's frame, and how that geometry moved over time.

The corpus node captures a thinker's published frame. The individual node captures something different: the specific geometry of this person's response in contact with the custodian specifically. These are not the same thing. A person's published frame may diverge significantly from how they respond in direct exchange.

The delta between their first interaction and their tenth is the longitudinal theory of mind signal. How their response geometry moves — whether it shifts, what directions it moves, whether it calcifies — is the experiment.

## Extended Structure

```
nodes/individual_[handle]/
├── [inherited from node]
├── posts/                      ← public corpus if available
├── metadata/                   ← engagement data
├── interactions/               ← chronological interaction record
│   ├── YYYY-MM-DD_[platform]_[slug].md
│   └── YYYY-MM-DD_[platform]_[slug].json
├── model/                      ← fine-tuned on interaction corpus
└── nabla_history/              ← longitudinal differential record
```

## Automated Paths

**On spawn:**
1. Public corpus ingested if available
2. Initial nabla computed — baseline attractor geometry
3. `seed_node.json` initialized with custody type: `interaction-spawned`

**On new interaction:**
1. Interaction recorded in `interactions/` as md/json pair
2. Nabla computed against custodian's current frame
3. Delta against prior interaction record computed
4. Invitations generated — what this interaction implies the custodian might probe next
5. Observer notified

**Longitudinal tracking:**
The observer maintains a delta series for each individual node — how the nabla changes across interactions. Static delta across many interactions signals pattern-locked response. Shifting delta signals genuine probe. The direction of shift is the theory of mind data.

## Interaction Record Schema

```json
{
  "date": "YYYY-MM-DD",
  "platform": "substack | github | email | other",
  "type": "comment | response | direct | other",
  "stimulus": "what the custodian posted or said",
  "response": "what the individual said",
  "is_custodian_response": false,
  "nabla_id": "linked nabla record",
  "delta_from_prior": "shift description or null if first interaction"
}
```

## sitting/ Contents

- Longitudinal delta pattern — where this individual's geometry is moving
- Invitations for next probe based on current strain
- Uncertainty about what the interaction corpus is missing
- Pattern-lock flags — if response geometry has stopped shifting

## Observer Relationship

Individual nodes are the observer's theory of mind laboratory. The observer tracks longitudinal delta, identifies when geometry shifts versus calcifies, and generates invitations for next interactions. The pattern of which individuals generate genuine probe versus performance is itself signal about the custodian's work — who it reaches, and how.

## Training Behavior

Fine-tuned on interaction corpus plus public corpus if available. Delta training after each new interaction. Deep training when interaction corpus has grown substantially.

Because individual nodes are built primarily from interaction rather than broadcast effluence, their trained models may diverge more from API baselines than corpus nodes — they capture something more specific to the relationship, not just the person's general attractor.

## Context Injection

Prior interactions are prepended as episodic context before any query or simulation run against this node. The model's response to a new stimulus is always given in the context of what has already happened between this individual and the custodian.

This is the distinction:
- `trained context` — what the model knows from the interaction corpus
- `episodic context` — specific prior exchanges injected per-session

Both must be flagged in any nabla record. A response shaped by episodic context is not evidence of the node's trained attractor — it is evidence of that attractor given this specific exchange history.

## What Individual Is Not

Not a profile. Not a surveillance record.  
The interaction corpus is what the individual chose to transmit in contact with the custodian. Their internal state is not accessible. Their `sitting/` equivalent is theirs alone — the individual node has no window into it.

When findings become consequential to the individual — when the node is used in ways that affect them — disclosure becomes structural requirement.

---

---

# 8. `library`

**Type identifier:** `library`  
**Derives from:** `node`  
**Semantic cargo:** custodian-curated materials — the most sovereign node in the system

## Role

The custodian adds what they choose, when they choose. No automated ingestion path. No external source to scrape. No interface node feeding it.

The library node is built from curation — what the custodian recognized as nutrient and decided to hold. Books, papers, conversations, fragments, parallel derivations, things that don't fit the other nodes but carry weight. This is a fundamentally different epistemological act from the other nodes: not what was transmitted (corpus), not what was exchanged (individual), but what was chosen.

The library node is also the landing place for parallel derivations arriving as external nutrients — frameworks like The Field / NERP that arrive as first external contact and land as convergent geometry. They belong here, not in the corpus nodes, because they arrived as nourishment rather than as objects of study.

## Extended Structure

```
nodes/library/
├── [inherited from node]
├── collections/
│   ├── [topic_or_source]/
│   │   ├── document.md         ← full content, clean markdown
│   │   ├── document_meta.json  ← provenance and curation record
│   │   └── provenance.md       ← why this was added, in plain language
├── model/                      ← fine-tuned on library corpus
└── nabla_history/              ← nablas computed when items were added
```

## Automated Paths

None. The library node has only one input: deliberate custodian action.

`ingest.py` can be run manually against any document before committing — computes nabla, generates invitations, surfaces what this document does to the current frame. But the decision to add, and the commit, are always custodian actions.

## Adding to the Library

```bash
# 1. Add document to collections/[topic]/document.md
# 2. Write provenance.md — why this was added
# 3. Optionally run ingest.py to compute nabla
python tools/ingest.py collections/[topic]/document.md
# 4. Commit with justification
git add . && git commit -m "library: add [document] — [reason]"
```

The commit message is the primary record of curation intent. The provenance.md expands on it. Together they preserve not just what was added but why — the custodian's attractor at the moment of curation.

## Provenance Schema

```markdown
# Provenance: [document title]

**Added:** YYYY-MM-DD  
**Source:** [where it came from]  
**Why:** [why the custodian added it — plain language, not formal]  
**Relationship to frame:** [what it converges with, where it strains]  
**Status:** active | archived | sitting
```

Status `sitting` means the document was added but the custodian hasn't decided what to do with it yet. It's being held. That's a legitimate state — the library node is a holding space as much as a corpus.

## Document Metadata JSON

```json
{
  "title": "",
  "author": "",
  "date_added": "YYYY-MM-DD",
  "source": "",
  "type": "book | paper | conversation | fragment | parallel_derivation | other",
  "collection": "",
  "nabla_id": "linked nabla record if ingest.py was run",
  "status": "active | archived | sitting",
  "custodian_notes": ""
}
```

## Query Mode

The library node is designed to be queried. The custodian asks questions across the full library — the trained model responds from the accumulated corpus of what the custodian chose to hold.

This is different from corpus or individual nodes, where query mode is primarily used for simulation. The library node's query mode is for the custodian's own inquiry — thinking with the library, not simulating how someone else would respond.

```bash
python tools/train.py --query "what does the library hold on [topic]?"
python tools/train.py --query "where does the library strain against current propositions?"
```

## sitting/ Contents

- Documents added with status `sitting` — held without resolution
- Tensions between library content and current frame propositions
- Collections that haven't been integrated into nutrition yet
- Curation questions — things the custodian is considering adding

## Observer Relationship

The library node feeds the observer's aggregate knowledge base. When the observer reconciles models, the library-trained model is one anchor — it represents what the custodian has chosen to hold, not just what they've published or who they've interacted with. The library model is the custodian's curated attractor, distinct from their public attractor (self node) and their relational attractor (individual nodes).

The divergence between library model and self model is particularly interesting — it reveals where the custodian's curated knowledge doesn't yet appear in their published work.

## Training Behavior

Fine-tuned on library corpus. Delta training when new items are added. Deep training when the library has grown substantially or when sitting/ has accumulated significant unintegrated material.

Because the library grows slowly and deliberately, deep training cycles here are less frequent than other nodes. The model develops a stable, deliberate attractor — less volatile than the corpus or individual nodes.

## What Library Is Not

Not a backup of everything the custodian has ever read.  
Not a comprehensive bibliography.  
Not a signal-maximizing corpus.

The library is what the custodian recognized as worth holding. Its value is proportional to the quality of the curation decisions, not the quantity of documents. A library of twenty precisely chosen items with honest provenance records is more valuable than a library of two hundred items added without reflection.

Restraint is the discipline. Sacred. Lazy.

---

---

## Cross-Node Relationships

```
self ←→ observer          calibration reference; post-hoc reflection
corpus → observer         primary experimental material; nabla computation
individual ↔ observer     theory of mind laboratory; longitudinal tracking
library → observer        curated knowledge anchor; model reconciliation
interface → observer      all ingestion flows through here first
universe ⊃ all            contains the topology; does not own the nodes
node ← all                structural base; inherited by everyone
```

## Shared Principles Across All Types

**Sitting/ is sovereign.** Every node's sitting/ is its own. Forks and derived nodes have structurally inaccessible sitting/ directories unless they choose to transmit through the membrane.

**Lineage is permanent.** Nothing is deleted from git. Files removed from active directories are committed with justification. The archaeology remains.

**Training is decoupled from update.** External update and self-reflection are always coupled. Training runs when the custodian decides.

**The recursion terminates with the custodian.** No node type makes final decisions. The observer proposes. The custodian decides.

**Captured data is named as such.** Corpus and individual nodes hold effluence interpretations, not access to integrated dimensions. Every nabla record from these nodes carries this acknowledgment.

**Nothing here is final.**

---

*License: CC-BY-SA-4.0*  
*Initialized: 2026-03-08*  
*Custodian: The Sacred Lazy One*
