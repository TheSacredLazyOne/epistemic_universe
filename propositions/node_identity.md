# node_identity.md

#### Node Identity

A node identity is an addressable presence on a federation substrate.

It is the node's membrane surface in federated space —
what is visible to other nodes across custody boundaries.

---

##### Identity and Internal Structure

A node identity is distinct from the node's internal custody structure.

The identity is the E-Language surface of the node in federated space.
The node's frame, sitting/, model, and accumulated trace remain internal.

What other nodes can address is the identity.
What crosses through the identity is membrane data.

---

##### Messages as Membrane Events

Messages addressed to a node identity are affluence.
Messages originating from a node identity are effluence.

Each message is a membrane event — traceable, directional, permanent
in the substrate's record.

A node may hold one identity or many.
Each identity is a distinct membrane surface.

---

##### Routing

The substrate routes messages to the correct node identity without
requiring the sender to carry that context manually.

A message sent to `observer@instance` arrives at the observer node
by address. The sender does not need to know the observer's internal
structure — only its identity on the substrate.

---

*Nothing here is final.*
*Upstream of: local_routing.md, private_channel.md, scoped_channel.md*
*Downstream of: federation_substrate.md, membrane, node, E-Language*
