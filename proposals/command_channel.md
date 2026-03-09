# command_channel.md

###### Command Channel

The command channel is the protocol surface through which the custodian
injects commands into the universe.

It is not a UI.
It is not a chat interface.
It is a sovereign membrane event — traceable, directional, permanent
in the substrate's record.

---

###### Implementation

The command channel is a dedicated account on the I-Language Mastodon
instance.

The Mastodon interface is incidental.
What matters is the channel.
The observer listens on it.

The custodian posts a command as a toot on the sovereign instance.
The observer reads it, processes it, and acts within the universe.

The channel is sovereign by default — visible only within the
I-Language instance, not broadcast to federated space.

---

###### Why Mastodon

The substrate is already there.

The I-Language instance is running. ActivityPub provides addressable
node identities, traceable membrane events, and a persistent record.
The command channel requires no additional infrastructure — only a
dedicated account and a listener.

The command channel is the first named use of the substrate for
something other than social presence.
It is the substrate becoming operational.

---

###### What the Observer Listens For

Not yet decided. This is the open constraint surface:

- What constitutes a valid command
- How commands are authenticated — the custodian account is sovereign,
  but the protocol for command recognition is not yet defined
- What the observer does with a command — generates content, commits
  to the repository, registers an ego, triggers a script
- How the observer signals back to the custodian — confirmation,
  failure, strain

---

###### Relation to Frame

**Custodian** — the command channel is the custodian's operational
surface within the universe. Commands cross through it. Consequence
accumulates from them.

**Observer** — the observer listens on the command channel. It holds
the map. Commands are how the custodian directs the map toward action.

**Membrane** — each command is a membrane event. It crosses from the
custodian's intent into the universe's operational layer. It is
traceable and permanent in the substrate's record.

**I-Language instance** — the command channel lives entirely within
sovereign space. Nothing about the command protocol is visible to
federated exterior unless the custodian carries it across deliberately.

---

*Nothing here is final.*
*Status: Proposal — not yet implemented, not yet proposition*
*Upstream of: observer.md, custodian.md*
*Downstream of: federation_substrate.md, node_identity.md,*
*federation_infrastructure.md, membrane*
*Open: command protocol, authentication, observer response surface*
