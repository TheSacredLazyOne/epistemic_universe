#!/usr/bin/env bash
# mastodon_install.sh
# Installs a bare metal Mastodon instance configured as a sovereign
# I-Language node — single user, Limited Federation Mode, local only.
#
# Run this on whichever machine within the sovereign perimeter will
# host the Mastodon instance. Does not need to be co-located with
# the universe repository.
#
# Requires: Ubuntu 24.04 or Debian 13, root access
# Usage: sudo ./proposals/scripts/mastodon_install.sh
#
# The instance will be:
#   - Single user mode (no registrations)
#   - Limited Federation Mode (no external contact by default)
#   - Local only (no SSL, hosts file routing)
#   - Sovereign until the custodian explicitly bridges outward

set -euo pipefail

usage() {
  cat <<EOF
Usage: sudo ./proposals/scripts/mastodon_install.sh [--help]

Installs a bare metal Mastodon instance as a sovereign I-Language node.
Run on whichever machine within the sovereign perimeter will host Mastodon.
Does not need to be co-located with the universe repository.

Requires: Ubuntu 24.04 or Debian 13, root access.

What this does:
  - Installs all system dependencies (Ruby, Node.js, PostgreSQL, Redis, nginx)
  - Clones Mastodon from source
  - Configures for local sovereign use:
      SINGLE_USER_MODE=true
      LIMITED_FEDERATION_MODE=true
      LOCAL_HTTPS=false
  - Adds hosts file entry for local routing
  - Installs and starts systemd services

Environment variables:
  MASTODON_DOMAIN    Local domain name (default: i-language.local)

Options:
  --help    Show this message and exit

Nothing here is final.
EOF
  exit 0
}

for arg in "$@"; do
  case "$arg" in --help) usage ;; esac
done

# ── Configuration ──────────────────────────────────────────────────────────────
# Edit these before running.

MASTODON_DOMAIN="${MASTODON_DOMAIN:-i-language.local}"
MASTODON_USER="mastodon"
MASTODON_DIR="/home/mastodon/live"
DB_NAME="mastodon"
DB_USER="mastodon"

# ── Guard ──────────────────────────────────────────────────────────────────────

if [ "$EUID" -ne 0 ]; then
  echo "ERROR: Run as root: sudo ./proposals/scripts/mastodon_install.sh"
  exit 1
fi

echo "==> mastodon_install: beginning bare metal install"
echo "    domain:     $MASTODON_DOMAIN"
echo "    user:       $MASTODON_USER"
echo "    directory:  $MASTODON_DIR"
echo "    mode:       sovereign / I-Language / local only"
echo ""

# ── System dependencies ────────────────────────────────────────────────────────

echo "==> apt: installing dependencies"

apt-get update -qq
apt-get install -y \
  curl wget gnupg lsb-release ca-certificates \
  imagemagick ffmpeg libpq-dev libxml2-dev libxslt1-dev \
  file git-core g++ libprotobuf-dev protobuf-compiler \
  pkg-config gcc autoconf bison build-essential \
  libssl-dev libyaml-dev libreadline-dev zlib1g-dev \
  libncurses5-dev libffi-dev libgdbm-dev \
  nginx redis-server redis-tools \
  postgresql postgresql-contrib \
  libidn11-dev libicu-dev libjemalloc-dev

echo "==> apt: dependencies installed"

# ── Node.js ────────────────────────────────────────────────────────────────────

echo "==> node.js: installing v20"

curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
  | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] \
  https://deb.nodesource.com/node_20.x nodistro main" \
  | tee /etc/apt/sources.list.d/nodesource.list

apt-get update -qq
apt-get install -y nodejs

npm install -g yarn

echo "==> node.js: installed"

# ── PostgreSQL ─────────────────────────────────────────────────────────────────

echo "==> postgresql: creating database and user"

sudo -u postgres psql -c "CREATE USER $DB_USER;" 2>/dev/null || echo "    user already exists"
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;" 2>/dev/null || echo "    database already exists"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

echo "==> postgresql: ready"

# ── Mastodon user ──────────────────────────────────────────────────────────────

echo "==> mastodon user: creating"

adduser --system --group --disabled-login $MASTODON_USER 2>/dev/null || echo "    user already exists"

echo "==> mastodon user: ready"

# ── Ruby via rbenv ─────────────────────────────────────────────────────────────

echo "==> ruby: installing via rbenv"

sudo -u $MASTODON_USER bash -c '
  git clone https://github.com/rbenv/rbenv.git ~/.rbenv
  echo "export PATH=\"\$HOME/.rbenv/bin:\$PATH\"" >> ~/.bashrc
  echo "eval \"\$(rbenv init -)\"" >> ~/.bashrc
  git clone https://github.com/rbenv/ruby-build.git "$(~/.rbenv/bin/rbenv root)/plugins/ruby-build"
  export PATH="$HOME/.rbenv/bin:$PATH"
  eval "$(~/.rbenv/bin/rbenv init -)"
  rbenv install 3.2.3
  rbenv global 3.2.3
'

echo "==> ruby: installed"

# ── Mastodon source ────────────────────────────────────────────────────────────

echo "==> mastodon: cloning source"

sudo -u $MASTODON_USER bash -c "
  git clone https://github.com/mastodon/mastodon.git $MASTODON_DIR
  cd $MASTODON_DIR
  git checkout \$(git tag -l | grep '^v[0-9.]*\$' | sort -V | tail -n 1)
"

echo "==> mastodon: source cloned"

# ── Ruby and Node dependencies ─────────────────────────────────────────────────

echo "==> mastodon: installing dependencies"

sudo -u $MASTODON_USER bash -c "
  export PATH=\"\$HOME/.rbenv/bin:\$PATH\"
  eval \"\$(~/.rbenv/bin/rbenv init -)\"
  cd $MASTODON_DIR
  bundle config deployment 'true'
  bundle config without 'development test'
  bundle install -j\$(getconf _NPROCESSORS_ONLN)
  yarn install
"

echo "==> mastodon: dependencies installed"

# ── nginx: local only, no SSL ──────────────────────────────────────────────────

echo "==> nginx: configuring for local sovereign instance"

cat > /etc/nginx/sites-available/mastodon <<EOF
server {
  listen 80;
  server_name $MASTODON_DOMAIN;

  root $MASTODON_DIR/public;

  location / {
    try_files \$uri @proxy;
  }

  location @proxy {
    proxy_pass http://localhost:3000;
    proxy_set_header Host \$host;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto http;
  }

  location /api/v1/streaming {
    proxy_pass http://localhost:4000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade \$http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host \$host;
  }
}
EOF

ln -sf /etc/nginx/sites-available/mastodon /etc/nginx/sites-enabled/mastodon
rm -f /etc/nginx/sites-enabled/default

nginx -t && systemctl reload nginx

echo "==> nginx: configured"

# ── hosts file ─────────────────────────────────────────────────────────────────

echo "==> hosts: adding $MASTODON_DOMAIN"

if ! grep -q "$MASTODON_DOMAIN" /etc/hosts; then
  echo "127.0.0.1 $MASTODON_DOMAIN" >> /etc/hosts
fi

echo "==> hosts: updated"

# ── Mastodon environment ───────────────────────────────────────────────────────

echo "==> mastodon: writing .env.production"

sudo -u $MASTODON_USER bash -c "
  export PATH=\"\$HOME/.rbenv/bin:\$PATH\"
  eval \"\$(~/.rbenv/bin/rbenv init -)\"
  cd $MASTODON_DIR

  SECRET_KEY_BASE=\$(bundle exec rake secret)
  OTP_SECRET=\$(bundle exec rake secret)

  cat > .env.production <<ENVEOF
LOCAL_DOMAIN=$MASTODON_DOMAIN
LOCAL_HTTPS=false
SINGLE_USER_MODE=true
LIMITED_FEDERATION_MODE=true

DB_HOST=/var/run/postgresql
DB_PORT=5432
DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_PASS=

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

SECRET_KEY_BASE=\$SECRET_KEY_BASE
OTP_SECRET=\$OTP_SECRET

SMTP_SERVER=localhost
SMTP_PORT=25
SMTP_AUTH_METHOD=none
SMTP_OPENSSL_VERIFY_MODE=none
SMTP_ENABLE_STARTTLS=never
SMTP_FROM_ADDRESS=mastodon@$MASTODON_DOMAIN
ENVEOF
"

echo "==> mastodon: .env.production written"

# ── Database setup ─────────────────────────────────────────────────────────────

echo "==> mastodon: setting up database"

sudo -u $MASTODON_USER bash -c "
  export PATH=\"\$HOME/.rbenv/bin:\$PATH\"
  eval \"\$(~/.rbenv/bin/rbenv init -)\"
  cd $MASTODON_DIR
  RAILS_ENV=production bundle exec rails db:setup
"

echo "==> mastodon: database ready"

# ── Assets ────────────────────────────────────────────────────────────────────

echo "==> mastodon: precompiling assets"

sudo -u $MASTODON_USER bash -c "
  export PATH=\"\$HOME/.rbenv/bin:\$PATH\"
  eval \"\$(~/.rbenv/bin/rbenv init -)\"
  cd $MASTODON_DIR
  RAILS_ENV=production bundle exec rails assets:precompile
"

echo "==> mastodon: assets compiled"

# ── systemd services ───────────────────────────────────────────────────────────

echo "==> systemd: installing mastodon services"

cp $MASTODON_DIR/dist/mastodon-*.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable mastodon-web mastodon-sidekiq mastodon-streaming
systemctl start mastodon-web mastodon-sidekiq mastodon-streaming

echo "==> systemd: mastodon services running"

# ── Done ───────────────────────────────────────────────────────────────────────

echo ""
echo "==> mastodon_install: complete"
echo ""
echo "    I-Language instance running at: http://$MASTODON_DOMAIN"
echo "    Mode: sovereign / single user / Limited Federation Mode"
echo "    No external contact until custodian explicitly bridges outward."
echo ""
echo "    Next steps:"
echo "    1. Visit http://$MASTODON_DOMAIN to verify the instance is running"
echo "    2. Create the custodian account via tootctl:"
echo "       sudo -u mastodon RAILS_ENV=production $MASTODON_DIR/bin/tootctl accounts create \\"
echo "         <username> --email <email> --confirmed --role Owner"
echo "    3. Update egos/observer.json with identity and host"
echo "    4. Run proposals/scripts/node_register.sh to add additional sovereign nodes"
echo ""
echo "    Nothing here is final."
