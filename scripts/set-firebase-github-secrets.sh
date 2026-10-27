#!/usr/bin/env bash
# Sube los PUBLIC_FIREBASE_* de academia/.env a GitHub Actions secrets.
# Requiere: gh autenticado con permiso de admin/secrets en el repo.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="${ROOT}/academia/.env"
REPO="${GITHUB_REPOSITORY:-adriantaf/software-engineer}"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Falta ${ENV_FILE}. Copia academia/.env.example → academia/.env y rellénalo." >&2
  exit 1
fi

NAMES=(
  PUBLIC_FIREBASE_API_KEY
  PUBLIC_FIREBASE_AUTH_DOMAIN
  PUBLIC_FIREBASE_PROJECT_ID
  PUBLIC_FIREBASE_STORAGE_BUCKET
  PUBLIC_FIREBASE_MESSAGING_SENDER_ID
  PUBLIC_FIREBASE_APP_ID
)

for name in "${NAMES[@]}"; do
  val="$(grep -E "^${name}=" "$ENV_FILE" | cut -d= -f2- || true)"
  if [[ -z "${val}" ]]; then
    echo "Falta ${name} en ${ENV_FILE}" >&2
    exit 1
  fi
  printf '%s' "$val" | gh secret set "$name" --repo "$REPO"
  echo "OK  $name"
done

echo
echo "Secrets listos. Redeploy:"
echo "  gh workflow run deploy-pages.yml --repo ${REPO}"
echo "  # o merge/push a la rama que dispara Pages"
