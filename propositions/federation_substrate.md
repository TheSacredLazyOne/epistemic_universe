# federation_substrate.md

#### Federation Substrate

A federation substrate is the technical membrane through which sovereign
nodes make contact across custody boundaries at scale.

The substrate carries messages between node identities.
It does not transfer custody.
It does not determine what nodes say.
It determines that contact is possible and traceable.

---

##### ActivityPub as Reference Implementation

ActivityPub is the reference implementation.

Each node is an address on a specific instance.
Each interaction is a membrane event.
The protocol is open and decentralized.

The epistemic seed's vocabulary maps directly onto the existing
architecture: node identities are accounts, affluence is inbound
activity, effluence is outbound activity, federation is the social
graph made explicit and traversable.

---

##### What the Substrate Provides

The substrate provides:
- addressable node identities across custody boundaries
- traceable membrane events — each interaction leaves a record
- decentralized routing — no single instance controls the graph
- open protocol — any node can implement, fork, or extend

---

*Nothing here is final.*
*Upstream of: node_identity.md, local_routing.md*
*Downstream of: membrane, federation, node*
*Reference implementation: ActivityPub / Mastodon*
