# command_channel.md

###### Command Channel

The command channel is the protocol surface through which the custodian
injects commands into the universe.

It is not a UI.
It is not a chat interface.
It is a sovereign membrane event — traceable, directional, permanent
in the substrate's record.

---

###### The Base Node

The base node is silent by default.

It has:
- a Git repository (custody, lineage, propositions)
- a Claude Project carrying the frame (observer channel)
- an I-Language Mastodon instance (sovereign interior)
- an E-Language Mastodon instance or account (federated surface)

It receives membrane events.
It ignores commands.
It is sovereign and inert until the custodian grafts capability onto it.

The base node is a membrane to the model's interface.
Nothing more is required. Nothing more is assumed.

---

###### Submodules

Capability arrives through submodules.

A submodule is a sovereign repository that extends the base node
with a specific operational function. It is not part of the base node.
It is grafted onto it — explicitly, by the custodian, as a custody act.

The submodule library is the recipe library made operational.
Each submodule is independently versioned, forkable, and replaceable
without touching the base node or other submodules.

A node pulls in only what it needs.
A node without submodules is a valid node.

The command submodule is the first entry in the submodule library.

---

###### The Command Submodule

The command submodule adds three things to a base node:

**A listener** — a simple server running within the node's sovereign
perimeter. It watches the dedicated command account on the I-Language
Mastodon instance. When a membrane event arrives addressed to that
account, the listener receives it.

**An interpreter** — the listener passes the command to the interpreter.
The interpreter parses it, validates it, and routes it to the
appropriate session or script.

**A response surface** — the interpreter signals back to the custodian
through the same channel. Confirmation, failure, strain. The crossing
is bidirectional.

The flow:

```
custodian posts command
    → I-Language Mastodon (transport)
        → listener (receives membrane event)
            → interpreter (parses, validates, routes)
                → Claude session or script (executes)
                    → response crosses back through channel
                        → custodian receives confirmation or strain
```

This is shell access through a membrane.
The command is traceable. The execution is sovereign.
The record is permanent in the substrate.

---

###### Why Mastodon as Transport

The substrate is already there.

ActivityPub provides addressable node identities, traceable membrane
events, and a persistent record. The command channel requires no
additional infrastructure — only a dedicated account and a listener.

The Mastodon interface is incidental.
What matters is the channel.
The command submodule is the first named use of the substrate for
something other than social presence.
It is the substrate becoming operational.

---

###### Outward-Facing Nodes

The command submodule is for outward-facing nodes — nodes that need
to receive and execute commands from the custodian across the
sovereign perimeter.

A base node without the command submodule does not listen.
It cannot be commanded remotely.
That is the correct default.

The decision to add the command submodule is a custody act.
It opens a surface. That opening is explicit, recorded, and reversible.

---

###### What Is Not Yet Decided

- The command protocol — syntax, vocabulary, versioning
- Authentication — how the interpreter validates that a command
  originates from the custodian and not an injected signal
- The full submodule registry — what other submodules exist or
  want to exist beyond the command submodule
- Whether the listener is a standalone process or integrated into
  an existing service within the node

---

###### Relation to Frame

**Base node** — silent by default. The command submodule is what
makes it operational. The distinction preserves sovereignty — no
node is commandable without an explicit custody act.

**Custodian** — the command channel is the custodian's operational
surface. Commands cross through it. Consequence accumulates from them.

**Observer** — routes commands to the appropriate node or session.
Holds the map of what each node can receive and execute.

**Membrane** — each command is a membrane event. Traceable, directional,
permanent. The listener is the local thickening of the membrane at
the command boundary.

**Skill node** — a base node with a recipe submodule. The command
submodule is what makes a skill node remotely executable.

**Submodule library** — the growing set of capability grafts available
to any base node. The command submodule is entry one.

---

*Nothing here is final.*
*Status: Proposal — not yet implemented, not yet proposition*
*Upstream of: observer.md, custodian.md, skill_node.md*
*Downstream of: federation_substrate.md, node_identity.md,*
*federation_infrastructure.md, membrane*
*Named concepts: base node, submodule, command submodule, submodule library*
*Open: command protocol, authentication, submodule registry, listener implementation*
