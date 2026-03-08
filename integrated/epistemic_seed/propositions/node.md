# Node

A node is a versioned unit of custody.

A node contains:
- a protocol surface (how it participates)
- documents and claims under local custody
- explicit lineage (if derived)

A node may:
- derive from another node (vertical inheritance)
- federate with other nodes (lateral connection)
- fork (diverge while preserving trace)

**Reference implementation:** A node is represented as a Git repository (or equivalent versioned archive) so custody, lineage, and forks are mechanically legible in the integrated world.

A node is sovereign within its own repository.
Compatibility with other nodes is negotiated through shared substrate constraints, not assumed.