#!/usr/bin/env bash
# cleanup.sh
# Graceful teardown of the Mastodon I-Language instance.
# Preserves all lineage — the repository, egos, proposals, and library
# are never touched. Only running services are stopped.
#
# Run on the machine hosting the Mastodon instance.
# Usage: sudo ./proposals/scripts/cleanup.sh

set -euo pipefail

usage() {
  cat <<EOF
Usage: sudo ./proposals/scripts/cleanup.sh [--help]

Graceful teardown of the Mastodon I-Language instance.
Stops running services only. Never touches repository, egos,
proposals, or library. Lineage is always preserved.

Run on the machine hosting the Mastodon instance.
Requires root access.

What this does:
  - Stops mastodon-web, mastodon-sidekiq, mastodon-streaming
  - Stops nginx
  - Stops redis-server
  - Prints restart command

To restart after cleanup:
  sudo systemctl start mastodon-web mastodon-sidekiq mastodon-streaming nginx redis-server

Options:
  --help    Show this message and exit

Nothing here is final.
EOF
  exit 0
}

for arg in "$@"; do
  case "$arg" in --help) usage ;; esac
done

echo "==> cleanup: beginning graceful teardown"
echo "    Services will stop. Data is preserved. Lineage is intact."
echo ""

if [ "$EUID" -ne 0 ]; then
  echo "ERROR: Run as root: sudo ./proposals/scripts/cleanup.sh"
  exit 1
fi

# ── Stop Mastodon services ────────────────────────────────────────────────────

echo "==> systemd: stopping mastodon services"

for SERVICE in mastodon-web mastodon-sidekiq mastodon-streaming; do
  if systemctl is-active --quiet "$SERVICE"; then
    systemctl stop "$SERVICE"
    echo "    stopped: $SERVICE"
  else
    echo "    not running: $SERVICE (skipping)"
  fi
done

echo "==> systemd: mastodon services stopped"

# ── Stop nginx ────────────────────────────────────────────────────────────────

echo "==> nginx: stopping"

if systemctl is-active --quiet nginx; then
  systemctl stop nginx
  echo "    stopped: nginx"
else
  echo "    not running: nginx (skipping)"
fi

# ── Stop Redis ────────────────────────────────────────────────────────────────

echo "==> redis: stopping"

if systemctl is-active --quiet redis-server; then
  systemctl stop redis-server
  echo "    stopped: redis"
else
  echo "    not running: redis (skipping)"
fi

# ── Done ──────────────────────────────────────────────────────────────────────

echo ""
echo "==> cleanup: complete"
echo ""
echo "    All services stopped."
echo "    Repository, egos, proposals, and library: untouched."
echo "    To restart: sudo systemctl start mastodon-web mastodon-sidekiq mastodon-streaming nginx redis-server"
echo ""
echo "    Nothing here is final."
