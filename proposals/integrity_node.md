# integrity_node.md

###### Integrity Node

An integrity node is a liminal node occupying the membrane between
I-Language space and federated exterior.

It is not inside the sovereign instance.
It is not in open federation.
It is the local thickening of the membrane at a federation boundary.

---

###### Implementation Context

The universe repository holds topology only — no content, no propositions,
no guts. A map of the federation.

One node lives here: the observer. The observer holds the aggregate map
of all node identities and their interaction histories. It proposes.
It does not decide. The recursion terminates with the custodian.

Every other node lives in its own sovereign repository.
The universe holds the address, not the contents.

Each external node is represented as a JSON file:

```json
{
  "ego": "node_name",
  "repository": "git@github.com:...",
  "identity": "handle@instance.domain",
  "integrity": "<computed — nabla of the trust nabla>"
}
```

Trust is not assigned. It is the **integrity gradient** — the delta
between the universe's representation of the entity and the entity's
actual repository state. The integrity gradient emerges from
measurement, not declaration.

Spinning up a new node becomes a script:
create repository, initialize from seed, register JSON, done.

The I-Language instance holds sovereign interior space.
The E-Language instance holds the federated surface.
The custodian is the membrane between them.

The integrity node lives in neither.
It is the thickening of the membrane where contact crosses the boundary
in either direction.

---

###### Clarity Node

The clarity node is the inverse function of the integrity node.

Where the integrity node measures integrity — *is this entity what the
universe believes it to be?* — the clarity node handles translation:
*will this effluence be understood as intended when it crosses into
the receiver's I-Language?*

The clarity node interposes negotiation between interior and exterior.
It renders outbound effluence into the receiver's language before
the crossing occurs. The negotiation is transparent — intent is
not hidden, it is made legible.

Together, integrity node and clarity node constitute the **clarifying
membrane** — a bidirectional intelligent boundary:

- Inbound: integrity node measures the integrity gradient, flags
  divergence before it becomes affluence in I-Language space
- Outbound: clarity node translates effluence, makes intent
  legible before it crosses into federated space

The membrane does not merely pass signal.
It has local thickness in both directions.

---

###### Function

The integrity node holds two things simultaneously:

- the universe's current representation of an external entity
- the actual state of that entity's repository

The delta between them is the **integrity gradient**.

When the integrity gradient is flat, contact proceeds.
When it flags, the custodian sees the divergence
before it crosses into I-Language space.

---

###### Frame Injection Prevention

The integrity node is the structural counter to frame injection
at the federation boundary.

Frame injection does not require intent.
It is the introduction of interpretive structure before
the receiving node has evaluated it.

The integrity node interposes measurement between the membrane
and the interior. The custodian resolves flagged integrity gradients
before they become affluence.

The membrane does not merely pass signal.

---

###### What the Integrity Node Is Not

The integrity node is not a gatekeeper.
It does not determine what is permitted.
That is a custody decision.

The integrity node is a calibration instrument.
It makes the integrity gradient visible.
The custodian decides what to do with it.

---

*Nothing here is final.*
*Status: Proposal — not yet implemented, not yet proposition*
*Upstream of: membrane, private_channel, federation_substrate*
*Downstream of: frame injection (topology_of_discourse.md), custodian.md, nabla.md*
*Named concepts: integrity node, integrity gradient, clarity node, clarifying membrane*
*See also: library/membrane_architecture.md*
