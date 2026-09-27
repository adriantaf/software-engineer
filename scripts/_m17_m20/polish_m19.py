"""Build polished M19 BODIES + hecho/errores overrides (M09 depth)."""
from __future__ import annotations

from . import m19_lessons
from ._gen_m19_steps import STEPS
from .polish_common import build_body, default_commit

PROJ = "projects/m19-ops"

HECHO: dict[int, list[str]] = {
    1: [
        f"Existen `{PROJ}/secrets-inventory.md` y `{PROJ}/ambientes.md`",
        "Inventario **sin** valores secretos; URLs staging/prod anotadas",
    ],
    2: [
        "Dockerfile multi-stage + `.dockerignore` en el repo de la API",
        f"`{PROJ}/docker.md` documenta `docker build` exitoso",
    ],
    3: [
        "`compose.yml` (o `compose.prod.yml`) API+Postgres con volumen",
        "`docker compose up` + `/health` 200 documentados en docker.md",
    ],
    4: [
        f"`{PROJ}/docker.md` completo (build/up/down/logs) — P1",
    ],
    5: [
        f"Existe `{PROJ}/adr-hosting.md` con decisión PaaS vs VPS y consecuencias",
    ],
    6: [
        f"`{PROJ}/deploy-log.md` con URL HTTPS staging y commit/versión",
    ],
    7: [
        f"`{PROJ}/smoke-staging.md` con health+login+cita y fecha (sin passwords)",
    ],
    8: [
        f"`{PROJ}/dominios.md` + fila nueva en `deploy-log.md`",
    ],
    9: [
        f"`{PROJ}/ambientes.md` incluye checklist de promoción a prod",
    ],
    10: [
        f"`{PROJ}/runbook.md` tiene secciones versión, logs y rollback",
    ],
    11: [
        f"Existe `{PROJ}/monitoring.md` con check `/health` y canal de alerta",
    ],
    12: [
        f"Existe `{PROJ}/security-host.md` (SSH, firewall, DB no pública)",
    ],
    13: [
        f"`{PROJ}/scripts/pg_dump_daily.sh` + `{PROJ}/backup.md`",
    ],
    14: [
        f"`{PROJ}/restore-test.md` con fecha, dump usado y resultado real",
    ],
    15: [
        f"`{PROJ}/runbook.md` completo (deploy, rollback, backup, restore, URLs)",
    ],
    16: [
        f"`{PROJ}/cierre-m19.md` checklist P1–P3 + handoff URL staging",
    ],
}

ERRORES: dict[int, list[str]] = {
    1: ["Pegar JWT/passwords en markdown", "Un solo ambiente llamado ‘prod’"],
    2: ["`COPY .env` en la imagen", "Correr runtime como root"],
    3: ["Publicar puerto 5432 al host en prod-like", "Secrets bakeados en la imagen"],
    4: ["docker.md sin comandos copy-pasteables", "Marcar P1 sin `compose up` real"],
    5: ["ADR sin costos/tiempo ni Agenda Ops", "Elegir VPS sin plan de backups"],
    6: ["Deploy ‘OK’ sin URL en deploy-log", "Secrets en el Dockerfile"],
    7: ["Smoke solo health, sin login/cita", "Password en el markdown"],
    8: ["Dominio sin TLS", "DNS apuntando a IP efímera sin nota"],
    9: ["Promover con mismos secrets que staging", "Sin plan de rollback"],
    10: ["Rollback ‘reiniciar el server’ sin versión pinneada", "Logs inaccesibles documentados"],
    11: ["Monitoreo = ‘miro de vez en cuando’", "Alertas al canal equivocado sin dueño"],
    12: ["Postgres expuesto a 0.0.0.0", "SSH con password root"],
    13: ["Dumps con PII en el repo git", "Backup sin retención ni destino"],
    14: ["Restore probado en prod", "Afirmar OK sin `SELECT count`"],
    15: ["Runbook genérico de internet", "Faltan URLs o dueños"],
    16: ["Cerrar sin restore-test", "No dejar URL staging para M20/M22"],
}


def build_bodies() -> dict[int, str]:
    bodies: dict[int, str] = {}
    for i, raw in enumerate(m19_lessons.RAW, 1):
        bodies[i] = build_body(
            orden=i,
            titulo=raw["titulo"],
            horas=float(raw.get("horas", 5)),
            semana=int(raw["semana"]),
            porque=raw["porque"],
            objetivo=raw["objetivo"],
            steps=STEPS[i],
            commit_msg=default_commit("M19", i, raw["titulo"]),
            conceptos=raw.get("conceptos"),
        )
    return bodies


def patched_raw() -> list[dict]:
    out = []
    for i, raw in enumerate(m19_lessons.RAW, 1):
        r = dict(raw)
        r["hecho"] = HECHO[i]
        r["errores"] = ERRORES[i]
        out.append(r)
    return out
