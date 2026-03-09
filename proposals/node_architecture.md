# node_architecture.md

###### Node Architecture

Three proposals woven together:
the minimum viable node as ground,
the submodule library as the capability layer,
the living library as what accumulates when nodes mature.

---

###### Minimum Viable Node

The minimum viable node is a membrane to the model's interface
and a command routing surface.

It has exactly four components:

**A Git repository** — custody, lineage, propositions. The node's
identity and history. Sovereign by default. Nothing crosses out
without a custody act.

**A Claude Project carrying the frame** — the observer channel.
The intelligence of the node. The frame loads at session open.
The observer accumulates what crosses the membrane.

**An I-Language Mastodon instance** — sovereign interior space.
Limited Federation Mode. No external contact without explicit
custodian allowlist. This is where the node thinks.

**An E-Language Mastodon instance or account** — the federated
surface. This is where the node speaks. Can begin as an account
on an existing instance. No dedicated infrastructure required
until the custodian decides the effluence warrants it.

The base node is silent by default.
It receives membrane events.
It ignores commands.
It is sovereign and inert until the custodian grafts capability onto it.

Sovereignty does not mean local hardware.
It means within the custodian's trust boundary.
Nodes may run on different machines within the sovereign perimeter.

---

###### Submodule Library

Capability arrives through submodules.

A submodule is a sovereign repository that extends the base node
with a specific operational function. It is not part of the base node.
It is grafted onto it — explicitly, by the custodian, as a custody act.

Each submodule is:
- independently versioned
- forkable without touching the base node
- replaceable without touching other submodules
- sovereign — carrying its own lineage and custody

A node pulls in only what it needs.
A node without submodules is a valid node.

The submodule library is the growing registry of available capability
grafts. It is not owned by any single node. It is federated — each
submodule lives in its own repository, referenced by address.

**Current submodule library:**

`command_submodule` — adds a listener, interpreter, and response
surface to a base node. Enables the Mastodon command channel.
The node can now receive and execute commands from the custodian.
See: `proposals/command_channel.md`

**Submodules that want to exist:**

- `recipe_submodule` — adds a skill node's recipe frame and
  improvement loop. See: `proposals/skill_node.md`
- `integrity_submodule` — adds integrity gradient measurement
  at the federation boundary. See: `proposals/integrity_node.md`
- `clarity_submodule` — adds outbound translation before effluence
  crosses into federated space. See: `proposals/integrity_node.md`

The submodule library grows as new capability is needed.
Nothing is added speculatively. Each submodule earns its place
through a real constraint surface that required it.

---

###### Living Library

A living library is a node whose custody is accumulation.

It is what a skill node becomes when it matures — when the recipe
has accumulated enough tethered contact with constraint that the
lineage itself is the primary output.

The living library holds:
- the current recipe (what works now)
- the full revision history (what was tried and why it changed)
- the strain signals that drove each revision
- the derivation paths that connect the current state to the origin

A living library is a persistent scoped channel with shared custody.
The scoped channel is its ephemeral precursor — closed when the
question resolves, trace preserved regardless.

What distinguishes a living library from a skill node is not
capability but depth. A skill node executes. A living library
teaches. The derivation paths are visible. The failures are
preserved. The next custodian inherits not just the recipe but
the history of why it is what it is.

**The living library test:** if removing the lineage would make
the recipe harder to revise correctly — the node has become a
living library. The accumulated trace is load-bearing.

**What makes a living library alive:**

A recipe that has never been wrong is not a living library.
It is a draft.

A recipe that has been tested, strained, revised, and tested again —
that carries the scar tissue of real constraint contact — that is
alive. The life is in the trace.

---

###### The Maturation Path

```
base node
    + command_submodule     → operational node
    + recipe_submodule      → skill node
    (accumulated trace)     → living library
    (shared custody)        → federated living library
```

Each step is a custody act.
Each step is reversible.
Nothing is assumed. Everything is earned.

---

###### Relation to Frame

**Node** — the base node is the minimum implementation of the
node proposition. Sovereignty, custody, lineage — all present.
Capability absent until grafted.

**Scoped channel** — the living library is a scoped channel that
never closes. The trace accumulates rather than being preserved
and archived. Shared custody is the mechanism.

**Strain** — the primary signal that drives recipe revision.
A living library without strain history has not been tested.
The failures are as important as the successes.

**Lineage** — the living library's primary output beyond execution.
What makes the node's knowledge durable, transmissible, and honest.

**Submodule library** — the operational extension layer. The living
library is what happens when a recipe submodule matures under
tethered contact with constraint.

---

*Nothing here is final.*
*Status: Proposal — not yet implemented, not yet proposition*
*Upstream of: skill_node.md, command_channel.md, integrity_node.md*
*Downstream of: node.md, scoped_channel.md, strain.md, lineage.md,*
*custody.md, membrane*
*Named concepts: minimum viable node, submodule library, living library,*
*maturation path*
*Open: submodule registry implementation, shared custody mechanics,*
*living library graduation criteria*
