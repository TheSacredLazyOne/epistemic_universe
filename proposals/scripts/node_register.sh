#!/usr/bin/env bash
# node_register.sh
# Registers a new ego in the universe ego registry.
# The sovereignty field is explicit — the custodian names the boundary.
#
# Usage: ./proposals/scripts/node_register.sh

set -euo pipefail

usage() {
  cat <<EOF
Usage: ./proposals/scripts/node_register.sh [--help]

Registers a new ego in the universe ego registry.
The sovereignty field is explicit — the custodian names the boundary.
Non-sovereign crossings require confirmation before the ego is written.

What this does:
  - Prompts for ego name, repository, identity, host, and sovereignty
  - Warns and requires explicit confirmation for non-sovereign nodes
  - Writes a dated JSON file to egos/<name>.json
  - Prints a suggested commit message

Sovereignty levels:
  sovereign    Fully within the custodian's trust perimeter
  bridged      Connected outward at a named boundary (custody act)
  federated    Open to the broader fediverse

Options:
  --help    Show this message and exit

Nothing here is final.
EOF
  exit 0
}

for arg in "$@"; do
  case "$arg" in --help) usage ;; esac
done

UNIVERSE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EGOS_DIR="$UNIVERSE_DIR/egos"

echo "==> node_register: new ego"
echo ""

# ── Prompt ────────────────────────────────────────────────────────────────────

read -rp "ego name (slug, no spaces): " EGO_NAME
read -rp "repository URL: " EGO_REPO
read -rp "identity (handle@instance.domain): " EGO_IDENTITY
read -rp "host (IP or hostname within sovereign perimeter): " EGO_HOST
echo ""
echo "sovereignty:"
echo "  sovereign  — fully within custodian's trust perimeter"
echo "  bridged    — connected outward at a named boundary (custody act required)"
echo "  federated  — open to the broader fediverse"
echo ""
read -rp "sovereignty [sovereign/bridged/federated]: " EGO_SOVEREIGNTY

# ── Validate sovereignty ───────────────────────────────────────────────────────

case "$EGO_SOVEREIGNTY" in
  sovereign|bridged|federated) ;;
  *)
    echo "ERROR: sovereignty must be sovereign, bridged, or federated"
    exit 1
    ;;
esac

# ── Warn on non-sovereign ──────────────────────────────────────────────────────

if [ "$EGO_SOVEREIGNTY" != "sovereign" ]; then
  echo ""
  echo "  WARNING: This node crosses a sovereignty boundary."
  echo "  sovereignty: $EGO_SOVEREIGNTY"
  echo "  This is a named custody act. It will be recorded in the registry."
  echo ""
  read -rp "Confirm crossing (yes to proceed): " CONFIRM
  if [ "$CONFIRM" != "yes" ]; then
    echo "Aborted. No ego registered."
    exit 0
  fi
fi

# ── Write ego JSON ─────────────────────────────────────────────────────────────

EGO_FILE="$EGOS_DIR/${EGO_NAME}.json"

if [ -f "$EGO_FILE" ]; then
  echo "ERROR: ego already exists at $EGO_FILE"
  exit 1
fi

cat > "$EGO_FILE" <<EOF
{
  "ego": "$EGO_NAME",
  "repository": "$EGO_REPO",
  "identity": "$EGO_IDENTITY",
  "host": "$EGO_HOST",
  "sovereignty": "$EGO_SOVEREIGNTY",
  "integrity": "<computed>",
  "registered": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF

echo ""
echo "==> ego registered: $EGO_FILE"
echo ""
echo "    ego:         $EGO_NAME"
echo "    repository:  $EGO_REPO"
echo "    identity:    $EGO_IDENTITY"
echo "    host:        $EGO_HOST"
echo "    sovereignty: $EGO_SOVEREIGNTY"
echo ""
echo "    Commit this file to preserve the lineage of this registration."
echo "    Suggested commit: feat(egos): register $EGO_NAME [$EGO_SOVEREIGNTY]"
echo ""
echo "    Nothing here is final."
