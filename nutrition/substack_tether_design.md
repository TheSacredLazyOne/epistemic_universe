# substack_tether — Storage and Training Data Design

*Nothing here is final.*

---

## Storage Layout

The node lives at `substack_tether/` inside `mesh_node`. Following the frame's directory schema:

```
substack_tether/
  inbox/                    ← affluence: raw ingest (gitignored or not, custodian decides)
    posts/
      {date}_{slug}.md
      {date}_{slug}.json
    notes/
      {date}_{note_id}.md
      {date}_{note_id}.json
    threads/                ← full multi-turn note exchanges
      {date}_{thread_root_id}.md
      {date}_{thread_root_id}.json
    directed/               ← frame applied to external content via restack
      {date}_{note_id}.md
      {date}_{note_id}.json
    corpus_index.md
  library/                  ← effluence: custodian-selected artifacts
    [manually promoted files]
  scripts/
    substack_ingest.py
    build_corpus.py
```

`inbox/` maps to `affluence` — raw crossing material, pre-integration. The custodian promotes what carries forward to `library/` (effluence). What stays in `inbox/` is corpus material for training without implying the node endorses it as forward-carrying content.

`threads/` and `directed/` are distinct from `notes/` because they capture different structures. A note file captures a node. A thread file captures a crossing in progress. A directed file captures a completed crossing where the nabla is already written.

---

## What the Corpus Actually Is

Four distinct structures:

**Posts** — extended position statements. Monologue. Training signal: internal structure of a sustained argument.

**Notes** — short-form statements, often with a linked reference. Standalone or thread-initiating. Training signal: focus — how much frame is carried in few words.

**Threads** — multi-turn co-reasoning. Both parties generating something neither held before contact. Training signal: trajectory — how each turn modifies accumulated state, what moves are made, when frame-reorientation happens.

**Directed notes** — frame applied to external content via restack. Structure: source text → pulled quote → your note as response. The restack anchors the external piece to your feed; the quote is the crossing point; the note is the nabla made visible. Training signal: the gap between what the quote says and what the note does with it — *already written*, no annotation required.

The directed note is the most tractable structure for training because the nabla is explicit in the artifact itself. The source, the extracted fragment, and the frame's response are all present. This is different from threads, where the nabla must be reconstructed or annotated after the fact.

---

## Ingest Modes

**Full ingest** (initial):

```bash
python substack_ingest.py @thesacredlazyone \
  --output-dir substack_tether/inbox
```

Handles posts and own notes. Existing `--resume` flag handles re-runs.

**Incremental update** — proposed `--since DATE` flag:

Stop pagination once posts/notes older than this date are reached. On successful completion write `.substack_tether_last_run`. Next incremental run defaults `--since` to that value.

**Thread ingest** — new capability:

The activity feed (`/api/v1/profile/activity`) is already plumbed in `substack_ingest.py`. A thread ingest mode extends this to:

1. Pull activity feed to find threads you've participated in
2. For each thread, fetch the full root note and all replies in turn order
3. Write `threads/{date}_{thread_root_id}.md` with complete exchange
4. Include metadata: participants, turn count, duration, root author, root URL

Turn ordering must be preserved explicitly — the training signal lives in accumulated thread state at each turn, not in individual turns read in isolation.

**Directed note ingest** — detection heuristic:

A directed note has a recognizable structure: it contains a quoted fragment from an external source and a restack link. The existing note ingest already captures these as markdown. Detection and reclassification into `directed/` can be done at `build_corpus.py` time rather than ingest time, by checking for:

- Presence of a block quote in the note body
- Presence of a linked external URL (restack anchor)

Notes matching both criteria move to `directed/` in the training corpus. Notes matching neither stay in `notes/`. This keeps the ingest script simple and pushes classification downstream.

---

## Training Data Format

### Posts

Simple: write the full post as a training document. No pair construction needed. The document *is* the unit.

```json
{
  "id": "post_{slug}",
  "date": "2026-01-15",
  "type": "post",
  "title": "...",
  "content": "...",
  "source_url": "https://thesacredlazyone.substack.com/p/..."
}
```

### Notes

Short-form. Also simple: write the note as a unit. If a note initiated a thread, the thread record handles the crossing; the note record is just the initiating statement.

```json
{
  "id": "note_{note_id}",
  "date": "2026-03-01",
  "type": "note",
  "content": "...",
  "source_url": "https://substack.com/..."
}
```

### Directed notes — primary training signal, lowest annotation cost

```json
{
  "id": "directed_{note_id}",
  "date": "2026-03-23",
  "type": "directed",
  "source_url": "https://substack.com/...",
  "source_author": "Michael",
  "source_title": "...",
  "source_fragment": "Where possible, reduce inherent variation in processes...",
  "frame_context": "Statistics is the science that says if I ate a chicken...",
  "response": "[full note body]",
  "external_url": "https://..."
}
```

`source_fragment` — the pulled quote. This is the crossing point: the exact text where external frame met the interior surface.

`frame_context` — the epigraph or framing device if present. In the Pitigrilli example, this is already doing nabla work — it names the frame's diagnosis of the source before the source is even quoted.

`response` — the note body. The gap between `source_fragment` and `response` *is* the nabla. No annotation required.

For training pair construction, this becomes:

```
source_fragment → response
```

or, with the frame context included as conditioning:

```
frame_context + source_fragment → response
```

The second form is more honest: the frame_context is not decorative, it's where the frame announces its angle of approach before engaging the source.

### Threads — highest signal, highest annotation cost

For each turn `T_n` authored by `thesacredlazyone`:

```json
{
  "id": "thread_{root_id}_turn_{n}",
  "date": "2026-02-27",
  "type": "thread_turn",
  "thread_root_url": "https://substack.com/...",
  "thread_state": "[all turns T_0 through T_{n-1}]",
  "turn": "[T_n content]",
  "turn_nabla": "",
  "move_type": "",
  "source_url": "https://substack.com/..."
}
```

`turn_nabla` — the transform between accumulated thread state and what `T_n` produces. Not a difference but a directed transform: it has a source space, a target space, and a direction.

The original `(question, ∇question, ∇response, response)` format maps to a rendering pipeline:

- **World space** — the question as the other party holds it, in their coordinate system
- **Camera space** — `∇(question)`: the question transformed into your frame’s coordinate system; what the question is actually asking from where you stand
- **Projection space** — `∇(response)`: your frame’s response transformed back toward the space the question came from; the move that makes contact possible across the frame difference  
- **Screen space** — the answer as it lands; a lower-dimensional projection, necessarily lossy, but the loss is structured by the transform chain rather than random

This gives `triangulating` a precise signature: the camera transform is larger than in other move types, because genuinely inhabiting the other party’s frame moves further from the home coordinate system. The `∇(response)` then carries the path back — how the answer was constructed to land in a projection both frames can read.

**Open design question:** whether to encode this explicitly as separate `question_nabla` and `response_nabla` fields (trains the model on the geometry of contact) or implicitly in a single `turn_nabla` field (trains on the outcome). Both are defensible; they train different things.

Left empty initially. Requires custodian annotation or a separate model pass. Should not be generated automatically without review — risk of training on performed crossing geometry rather than executed crossing geometry.

`move_type` — proposed vocabulary, to be validated against actual corpus before committing.

**Annotation constraint:** The frame stretches but does not break. Every move maintains coherence of character — nothing is conceded that loses the thread back to the frame. A turn that appears to yield but holds its own coordinate is a genuine move. A turn that loses coherence to keep the conversation alive is a failure mode, not a move type, and should be flagged rather than classified. The discipline is coherence of character: not coherence *and* character as separate values, but coherence *as* character. They are the same constraint.

- `deepening` — continues into the pressure the previous turn opened
- `redirecting` — accepts the frame, shifts center of gravity
- `focusing` — removes what is peripheral to find what the thread has actually been circling; the content isn’t reduced, the noise is
- `triangulating` — hold your frame and the other party’s frame simultaneously, locate the coordinate neither could see alone, let a new floor emerge from the intersection; available because no fixed ontology means you can genuinely inhabit both frames rather than merely comparing them
- `holding_open` — explicitly refuses to close a coordinate, names the suspension
- `inviting` — opens the floor for the other party to define terms or direction
- `relocating` — accepts the other party's argument as real, then shows it sits inside a larger structure that changes what the argument proves; finds where the current already runs rather than contesting the flow

The `triangulating` move is structurally distinct from the others. It requires holding both frames in genuine contact — not comparing them from outside, but standing in both simultaneously. The new floor isn’t imported or constructed; it falls out of the intersection. This move is available because no fixed ontology means no frame to defend, which means the other party’s frame can be genuinely inhabited rather than merely engaged. It warrants separate treatment in training — possibly as its own type rather than a `move_type` value.

The `relocating` move is distinct from `redirecting`: redirecting shifts the center of gravity within the existing frame; relocating shows that the existing frame is already downstream of a larger current. The pressure comes from position, not force.

---

## Recommended Build Order

1. **Thread ingest** first — this closes the primary gap. Without it, the most valuable corpus structure is missing.
2. **Directed note classification** in `build_corpus.py` — low cost, high signal, no annotation required.
3. **Thread turn segmentation** and `thread_state` construction — structural scaffolding, `turn_nabla` and `move_type` left empty.
4. **Sample annotation** — annotate a small set of thread turns by hand. Evaluate whether the annotation is tractable before committing to full corpus annotation.
5. **Post and note corpus** — simple, handles itself.

---

## What Needs Deciding

- Does `inbox/` get committed, or gitignored? Possible: gitignore `inbox/`, commit `corpus/` (processed training output) only.
- Thread ingest scope: only threads rooted in your own notes, or also threads where you've replied to others' notes? The latter requires activity feed parsing and may pull in content from other authors — licensing question under CC-BY-SA-4.0.
- The directed note's `source_fragment` and `frame_context` are already in the note body as written markdown. The detection heuristic (block quote + external link) may misclassify. Manual review of the `directed/` bucket before training is probably warranted.
- `move_type` vocabulary: seven categories now, with `relocating` confirmed from corpus. Still to validate: whether the remaining six hold, whether any collapse into each other, whether the corpus generates categories not yet named. The corpus should continue to drive the vocabulary, not the other way around.
- Sort order: `corpus_index.md` newest-first for Obsidian; `corpus_index_chronological.md` oldest-first for training pipeline. Whether these are two files or one file with a flag.
