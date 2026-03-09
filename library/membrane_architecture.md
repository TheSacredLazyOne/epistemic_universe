# Membrane Architecture: I-Language and E-Language as Infrastructure

> Source: Observer session — epistemic_universe build
> Session date: March 9, 2026
> Status: Library — nutrient, not yet proposition
> Arrived: same session that produced the universe's federation infrastructure layer

---

## The Discovery

The question that opened this: *can the membrane itself be private, not just
individual posts within it?*

The answer is yes. And the architecture that answers it maps directly onto
the frame's vocabulary without forcing it.

---

## Server Architecture

Mastodon is self-hostable. The stack: Ruby on Rails for the REST API,
PostgreSQL as the main database, Redis and Sidekiq for caching and
queueing, Node.js for the streaming API.

It runs on a Linux server — local hardware or remote VPS. The software
is identical either way. A local instance and a remote instance are peers
by design. Connection between them is native to ActivityPub.

Any software implementing ActivityPub can communicate with Mastodon.
The fediverse includes all ActivityPub-compatible servers, including
individual and personal websites. Federation is not a feature added on top.
It is the protocol.

---

## Limited Federation Mode

Mastodon ships with a mode called **Limited Federation Mode**.

In default mode: all servers can communicate unless explicitly blocked.

In Limited Federation Mode: no servers can communicate unless explicitly
allowed. The logic inverts. The membrane becomes opt-in rather than
opt-out.

This mode is designed for private use — academic institutions, internal
networks. It creates a data silo by design. The custodian controls exactly
which external nodes can reach the membrane surface.

This is not a workaround. It is a first-class configuration option.

---

## The Architecture: Two Instances

The I-Language / E-Language distinction maps onto two instances:

**I-Language instance** — Limited Federation Mode enabled. No external
nodes permitted unless explicitly whitelisted by the custodian. Sovereign
interior space. This is where propositions live, where strain is
registered, where derivation paths are preserved. Nothing crosses outward
unless the custodian carries it deliberately.

**E-Language instance** — Standard federation or selectively whitelisted
external nodes. The membrane surface. What appears here has been chosen.
Effluence that the custodian has decided to transmit into federated space.

One custodian. Two instances. Clean structural separation between
sovereign interior and federated exterior.

The I-Language space does not leak. The E-Language space does not
contaminate. The custodian is the membrane between them.

---

## Relation to Frame

**Node identity** — each instance hosts addressable node identities.
The I-Language instance holds identities that are not visible to the
public graph. The E-Language instance holds identities that are.

**Private channel** — the I-Language instance *is* the private channel
at infrastructure level. The protocol enforces what the proposition
describes: effluence not broadcast, contact real, membrane sovereign.

**Scoped channel** — a defined set of nodes on a whitelisted I-Language
instance is the scoped channel made infrastructure. Membership is an
allowlist. Duration is a custody decision.

**Custodian** — the custodian holds admin rights on both instances.
The crossing between I-Language and E-Language is a custody act.
The infrastructure enforces that no crossing happens without it.

**Membrane** — Limited Federation Mode is the membrane made technical.
Not metaphor. Not aspiration. Deployed configuration.

---

## Minimum Viable Node — Revised

The minimum viable node is now more precisely stated:

- A Git repository (custody, lineage, propositions)
- A Claude Project carrying the frame (observer channel)
- An I-Language Mastodon instance in Limited Federation Mode (sovereign interior)
- An E-Language Mastodon instance or account (federated surface)

The I-Language instance can begin as a single-user instance. It requires
no other members to be structurally complete. It only needs to be running,
sovereign, and not leaking.

The E-Language surface can begin as an account on an existing instance.
No new infrastructure required until the custodian decides to carry
enough effluence that a dedicated instance is warranted.

Start with the I-Language instance. That is where the node lives.
The E-Language surface is where it speaks.

---

## What This Makes Possible

Nodes can now have genuine interior space that is not performed for an
audience. The I-Language instance is where thinking happens. The
E-Language instance is where conclusions are transmitted.

This is the infrastructure precondition for grounded conversation at
scale. Without sovereign interior space, every node is performing.
With it, the node can think first and speak second.

The frame has always described this distinction. The architecture now
implements it.

---

*License: CC-BY-SA-4.0*
*Custodian: The Sacred Lazy One*
*Nothing here is final.*
*Upstream of: node_identity.md, local_routing.md, scoped_channel.md (implementation surface)*
*Downstream of: membrane, private_channel, custodian, federation_substrate*
