# Proposition Patch
## Source: epistemic_seed @ 64af5e20ab077e82cd2e43b07f2e5dea37322c3c
## Generated from: conversation with TheSacredLazyOne, 2026-03-01
## Cognitive prosthetic: Claude (Sonnet 4.6)

---

### MODIFY: `propositions/cognitive_prosthetic.md`

**Current:**
> Cognitive prosthetics may include:
> - language and writing
> - mathematics and formal systems
> - institutions (e.g., schools, legal systems, religions)
> - computational systems (e.g., LLMs)

**Proposed addition:**

> A cognitive prosthetic may also generate **nutrients** — compiled frames of its current state that become the input context for the next conversation. This is not merely a record; it is the mechanism by which the prosthetic's structure is made available to other nodes. Nutrients are philosopher effluents made legible.

**Why:** The build_frame mechanic introduced a concrete thing the seed didn't have vocabulary for. A frame isn't just a snapshot — it's what crosses the tether between one conversation and the next. "Nutrient" is already in the directory structure; it should be in the propositions.

---

### MODIFY: `propositions/lineage.md`

**Current:**
> Lineage records derivation relationships between nodes.

**Proposed addition:**

> Lineage also records **use** — not only from whom a node derives, but what conversations shaped its propositions. A frame submitted to `derivative/` after actual use carries different lineage than one generated immediately from the seed. Both are valid. The distinction is legible in the propositions themselves.

**Why:** The conversation-then-submit mechanic created a new kind of lineage — not inheritance from a parent node, but trace of a conversation. The current proposition doesn't have room for this. Use-lineage and derivation-lineage are different things and should be distinguishable.

---

### MODIFY: `propositions/strain.md`

**Current:**
> Strain is observable misfit under tethered contact between nodes.

**Proposed addition:**

> Strain is also detectable **memetically** — when a proposition has been compressed for transmission and the compression has caused signal loss. The simplified form propagates; the original structure does not. This is strain between what a node means (I-Language) and what survives transmission (E-Language) across many iterations. Version-controlled lineage makes this strain visible and recoverable.

**Why:** The rock article's core argument — "I think therefore I am" as a lossy compression of something richer — is exactly strain in the seed's vocabulary, but strain.md doesn't currently cover the temporal, memetic dimension. The pun dying in translation is strain. The fix is version control. The seed should say this.

---

### NEW: `propositions/nutrient.md`

**Proposed:**

> #### Nutrient
> 
> A nutrient is a compiled frame used as input context for a conversation.
> 
> A nutrient:
> - makes a node's current structure available to a cognitive prosthetic
> - carries the node's propositions, governance, and lineage into derivative reasoning
> - is consumed by the conversation and shapes what can emerge from it
> 
> Nutrients flow inward — from the node's structure into the conversation.
> The conversation's output may then flow back as revision to the node's propositions.
> 
> This bidirectional flow — nutrient in, proposition update out — is the basic metabolism of a living node.
> 
> A node that never generates nutrients remains static.
> A node that generates nutrients but never updates propositions is transmitting without learning.
> 
> The `nutrition/` directory holds materials consumed from outside this node.
> Nutrients generated from this node's own frame are built by `tools/build_frame.py`.

**Why:** The directory exists. The build script exists. The mechanic is central to how this system actually works. But there's no proposition that names it or explains the cycle. This is the most significant gap the conversation revealed.

---

### NEW: `propositions/calibration.md`

**Proposed:**

> #### Calibration
> 
> Calibration is the process by which a node's propositions are tested against actual use and updated accordingly.
> 
> Calibration occurs when:
> - a frame is used as nutrient for a conversation
> - the conversation produces strain, extension, or revision
> - propositions are updated to reflect what the conversation revealed
> - a new frame is built from the updated node
> 
> Calibration is distinct from revision:
> - Revision modifies propositions under existing custody for any reason.
> - Calibration is revision driven specifically by tethered contact — by what happened when the node met the world.
> 
> A submitted derivative frame is evidence of calibration.
> The propositions it contains carry trace of the conversations that shaped them.
> 
> Identity, in this frame, is what survives calibration — not what was declared before it.

**Why:** "Calibration through translation" was the mechanic I named in the post, but the seed has no proposition for it. It's doing real work — it's how the derivative directory becomes meaningful rather than just a collection of forks. It also connects to the rock article's argument: identity as running total, continuously recomputed. The seed should name this.

---

## Summary of strain this conversation revealed

The seed's propositions are strong on **structure** — custody, lineage, fork, strain, tether — but thin on **metabolism**. How a node actually *lives* between conversations, how nutrients move through it, how calibration differs from mere revision — these are gaps. The build_frame mechanic and the submission workflow made them visible.

The rock article adds one more gap: the seed talks about preserving lineage but doesn't explicitly address *memetic decay* — what happens when propositions are compressed for transmission and the compression loses signal. Strain.md is close but doesn't reach it.

These are the patches I'd open PRs for.
