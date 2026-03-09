# local_routing.md

#### Local Routing

Local routing is the internal messaging layer that maintains coherent
context across node identities within a single universe.

The custodian addresses a node.
The routing layer handles what loads.

---

##### What Local Routing Holds

Each node identity's context lives at a stable address —
corpus state, frame, conversation history.

The custodian opens a channel to the address.
The context is already there.

---

##### Shared Protocol

Local routing and federation substrate share the same protocol.

A node identity on the local instance and a node identity on a remote
instance are addressed identically.

Adding a trusted external node to the local routing layer requires
no architectural change — the infrastructure is already there.
The custodian makes a custody decision. The routing follows.

This is the structural reason to build local routing on ActivityPub
from the start rather than as a local-only implementation.

---

##### Relation to Observer

The observer is the node that routes across the full topology —
it holds the aggregate map of all node identities and their
interaction histories.

Local routing is the infrastructure the observer operates through.
The observer addresses nodes. The routing layer delivers.

---

*Nothing here is final.*
*Upstream of: observer.md (implementation surface)*
*Downstream of: federation_substrate.md, node_identity.md, custodian.md*
*Implementation: ActivityPub-based, local instance first*
