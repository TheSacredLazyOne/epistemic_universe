# federation_infrastructure.md

###### Federation Infrastructure Scripts

A proposal for the initialization and cleanup scripts required to stand
up and tear down the epistemic_universe federation infrastructure.

---

###### What the Universe Repository Is

The universe repository holds topology only — no content, no propositions,
no guts. A map of the federation.

One node lives here: the observer. Every other node lives in its own
sovereign repository. The universe holds the address, not the contents.

---

###### What Needs Standing Up

Three things constitute the minimum viable federation environment:

**The universe repository** — initialized on whichever machine the
custodian designates. Holds the ego registry, proposals, and library.
Not necessarily co-located with anything else.

**The I-Language Mastodon instance** — a bare metal Mastodon install,
sovereign by default:
- Single user mode (no registrations)
- Limited Federation Mode (no external contact)
- Local routing only (no SSL, no public domain at initialization)

The I-Language instance runs on whichever machine within the sovereign
perimeter the custodian designates. It does not need to be co-located
with the universe repository.

**The command channel** — a dedicated sovereign account on the
I-Language instance through which the custodian injects commands into
the universe. The Mastodon interface is incidental. What matters is
the channel. The observer listens on it.

---

###### Sovereignty Is Explicit

Every node carries a sovereignty field:

```
sovereign    — fully within the custodian's trust perimeter
bridged      — connected outward at a named boundary (custody act)
federated    — open to the broader fediverse
```

Nodes may run on different machines within the sovereign perimeter.
Sovereign does not mean local hardware. It means within the custodian's
trust boundary.

The crossing from sovereign to bridged or federated is a named custody
act. It cannot happen silently. It is recorded in the ego registry and
committed to lineage.

This is the intellectual firewall.

---

###### Scripts Required

**init.sh** — initializes the universe repository environment
- Creates directory structure
- Registers the observer as the first sovereign ego
- Does not install Mastodon — machine-agnostic
- See: `proposals/scripts/init.sh`

**mastodon_install.sh** — stands up the I-Language instance
- Bare metal install (no Docker)
- Configures sovereign defaults from first run:
  single user, Limited Federation Mode, local routing
- Run on whichever machine hosts the Mastodon instance
- Does not touch the universe repository
- See: `proposals/scripts/mastodon_install.sh`

**node_register.sh** — registers a new ego in the universe
- Prompts for ego name, repository, identity, host, sovereignty
- Warns and requires explicit confirmation for non-sovereign nodes
- Writes a dated JSON file to egos/
- Prints a suggested commit message
- See: `proposals/scripts/node_register.sh`

**cleanup.sh** — graceful teardown
- Stops running services only
- Never touches repository, egos, proposals, or library
- Lineage is always preserved
- See: `proposals/scripts/cleanup.sh`

All scripts accept --help.

---

###### What Is Not Yet Decided

- The command channel protocol — how the custodian addresses the
  observer through the sovereign Mastodon account, and how the
  observer processes those commands
- The integrity node implementation — how the delta between the
  universe's representation of an entity and its actual repository
  state is computed
- The clarity node implementation — how outbound effluence is
  translated into the receiver's I-Language before crossing

---

*Nothing here is final.*
*Status: Proposal — not yet implemented*
*Upstream of: scripts/, egos/*
*Downstream of: observer.md, custodian.md, membrane,*
*integrity_node.md, library/membrane_architecture.md*
