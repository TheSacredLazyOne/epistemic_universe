#!/usr/bin/env bash
# init.sh
# Initializes the epistemic_universe repository environment.
# Run this on the machine that will host the universe repository.
# Does not assume co-location with Mastodon instance.
#
# Usage: ./proposals/scripts/init.sh

set -euo pipefail

usage() {
  cat <<EOF
Usage: ./proposals/scripts/init.sh [--help]

Initializes the epistemic_universe repository environment.
Run on the machine that will host the universe repository.
Does not assume co-location with the Mastodon instance.

What this does:
  - Verifies git is present
  - Creates directory structure (egos/, proposals/, library/, config/)
  - Registers the observer as the first sovereign ego
  - Prints next steps for Mastodon installation

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

echo "==> epistemic_universe: initializing"
echo "    universe root: $UNIVERSE_DIR"

# ── Git ────────────────────────────────────────────────────────────────────────

if ! command -v git &>/dev/null; then
  echo "ERROR: git is required. Install git and re-run."
  exit 1
fi

echo "==> git: present"

# ── Directory structure ────────────────────────────────────────────────────────

mkdir -p "$UNIVERSE_DIR/egos"
mkdir -p "$UNIVERSE_DIR/proposals"
mkdir -p "$UNIVERSE_DIR/library"
mkdir -p "$UNIVERSE_DIR/config"

touch "$UNIVERSE_DIR/egos/.gitkeep"

echo "==> directories: initialized"

# ── Ego registry ───────────────────────────────────────────────────────────────
# Register the observer as the first ego — the only resident node of the universe.

OBSERVER_EGO="$UNIVERSE_DIR/egos/observer.json"

if [ ! -f "$OBSERVER_EGO" ]; then
  cat > "$OBSERVER_EGO" <<EOF
{
  "ego": "observer",
  "repository": "$(git -C "$UNIVERSE_DIR" remote get-url origin 2>/dev/null || echo '<universe-repository-url>')",
  "identity": "<observer@i-language.local>",
  "host": "$(hostname)",
  "sovereignty": "sovereign",
  "integrity": "<computed>"
}
EOF
  echo "==> observer ego: registered"
else
  echo "==> observer ego: already exists, skipping"
fi

# ── Config templates ───────────────────────────────────────────────────────────

if [ ! -f "$UNIVERSE_DIR/config/mastodon.env.template" ]; then
  cp "$UNIVERSE_DIR/config/mastodon.env.template" "$UNIVERSE_DIR/config/mastodon.env.template" 2>/dev/null || true
  echo "==> config: templates in place"
fi

# ── Done ───────────────────────────────────────────────────────────────────────

echo ""
echo "==> epistemic_universe: initialized"
echo ""
echo "    Next steps:"
echo "    1. Run proposals/scripts/mastodon_install.sh on the Mastodon host machine"
echo "    2. Update egos/observer.json with the Mastodon identity and host"
echo "    3. Use proposals/scripts/node_register.sh to add additional egos"
echo ""
echo "    Nothing here is final."
