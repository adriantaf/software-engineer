"""Build polished M17 BODIES + hecho/errores overrides (M09 depth)."""
from __future__ import annotations

from . import m17_lessons
from ._gen_m17_steps import STEPS
from .polish_common import build_body, default_commit

PROJ = "projects/m17-agenda-ops"

# Exact-path Hecho items (replaces vague RAW bullets)
HECHO: dict[int, list[str]] = {
    1: [
        f"Existe `{PROJ}/` con TypeScript strict y carpetas `src/`/`tests/`/`docs/`",
        f"`{PROJ}/stack.md` lista runtime, API, ORM, front, tests y auth",
        "`GET /health` responde 200 con DB up (anotado en README sin secrets)",
    ],
    2: [
        "`POST /auth/register` crea usuario con `password_hash` (bcrypt/argon2)",
        "Test 201 feliz y 400 email inválido en suite auth",
        "Respuesta 201 **no** incluye el hash",
    ],
    3: [
        f"`{PROJ}/docs/auth.md` documenta cookie HttpOnly o JWT-cookie",
        "`POST /auth/login` + `GET /me` 200 con sesión; sin cookie → 401",
        "Tests cubren login→me y 401",
    ],
    4: [
        f"Existe `{PROJ}/tests/auth.test.ts` (o equiv.) con ≥6 tests verdes",
        "README documenta el comando exacto `npm test`",
        "Checklist P1 parcial marcado en README",
    ],
    5: [
        "Migraciones aplicadas: tablas `clientes`, `servicios`, `citas` visibles",
        f"Reglas puras en `{PROJ}/src/domain/` (o equivalente)",
    ],
    6: [
        "`POST /citas` y `GET /citas` con auth; 401 sin sesión",
        "Tests 201, 400 horario y (si aplica) 409 solapamiento",
    ],
    7: [
        "CRUD `/clientes` y `/servicios` autenticados",
        "Tests mínimos create/list (+ delete owner-only si aplica)",
    ],
    8: [
        f"Existe `{PROJ}/scripts/seed.ts` (o script documentado)",
        "README incluye comando seed; datos solo sintéticos",
    ],
    9: [
        f"Existe `{PROJ}/docs/permisos.md` con matriz owner/staff y rutas",
    ],
    10: [
        "Middleware `authorize(roles)` aplicado a rutas sensibles",
        "Tests 403 (staff en acción owner) e IDOR básico si aplica",
    ],
    11: [
        "Ruta `/admin` (o equiv.) lista/gestiona staff; staff recibe 403",
    ],
    12: [
        f"Existe `{PROJ}/docs/demo-roles.md` con guion owner vs staff",
        f"Borrador `{PROJ}/docs/integracion-whatsapp.md`",
    ],
    13: [
        "Front scaffold en `apps/web` (o ruta en stack.md) con rutas protegidas",
    ],
    14: [
        "UI login/logout funcional; cookie de sesión desaparece tras logout",
    ],
    15: [
        f"Existe `{PROJ}/docs/ui-estados.md` con loading/error/vacío para listas",
    ],
    16: [
        "Forms cita/cliente con labels, errores de campo y orden de tab documentado",
    ],
    17: [
        f"`{PROJ}/docs/integracion-whatsapp.md` define plantilla wa.me + helper testeado",
    ],
    18: [
        "Botón recordatorio en ficha cita abre wa.me; evidencia en doc WhatsApp",
    ],
    19: [
        "Campo/enum `estado` en citas + PATCH autenticado; tests verdes",
    ],
    20: [
        f"`{PROJ}/docs/integracion-whatsapp.md` completo; P3 marcado en README",
    ],
    21: [
        f"`{PROJ}/.env.example` lista vars con comentarios; `.env` no tracked",
    ],
    22: [
        f"`{PROJ}/docs/deploy.md` incluye URL staging alcanzable",
    ],
    23: [
        "HTTPS válido en staging; `GET /health` externo 200 documentado en deploy.md",
    ],
    24: [
        f"`{PROJ}/docs/smoke-test.md` con health+login+cita y fecha/resultado",
    ],
    25: [
        f"`{PROJ}/docs/owasp-mapa.md` cubre ≥A01–A05 con control o gap",
    ],
    26: [
        "Headers de seguridad visibles en `curl -sSI`; CORS allowlist (no `*`)",
    ],
    27: [
        "`POST /auth/login` responde 429 tras ráfaga; test o script lo demuestra",
    ],
    28: [
        "Workflow CI **o** `scripts/ci-auth.sh` deja suite auth verde de forma reproducible",
    ],
    29: [
        f"Existe `{PROJ}/docs/adr-tenant-id.md` con contexto/decisión/consecuencias",
    ],
    30: [
        f"Existe `{PROJ}/docs/checklist-saas.md` con ítems marcados o gaps enlazados",
    ],
    31: [
        f"Existe `{PROJ}/docs/demo-script.md` con guion ≤8 min y URL staging",
    ],
    32: [
        f"Existe `{PROJ}/docs/nota-cierre-m17.md` con índice de artefactos y handoff M19",
        "README P1–P3 coherente con evidencias",
    ],
}

ERRORES: dict[int, list[str]] = {
    1: ["Subir `.env` con passwords", "Cambiar framework sin ADR", "Health 200 sin ping a DB documentado"],
    2: ["MD5/SHA sin salt como ‘hash’", "Loguear password o hash en claro", "Devolver `password_hash` en JSON"],
    3: ["JWT en localStorage sin justificar XSS", "`GET /me` sin auth devuelve 200", "Devolver row completo con hash"],
    4: ["Dar P1 por hecho solo con Postman manual", "Suite <6 casos o flaky"],
    5: ["Lógica de horario solo en controllers", "Tablas sin FK a cliente/servicio"],
    6: ["Listar citas sin autenticación", "Ignorar timezone / guardar strings locales ambiguos"],
    7: ["DELETE servicio sin chequear rol", "Teléfonos reales de clientes en seeds de test"],
    8: ["Seeds con PII real del design partner en git", "Seed no reproducible (falta comando)"],
    9: ["Matriz genérica sin rutas del piloto", "Permisos solo ‘en la cabeza’"],
    10: ["Check de rol solo en el front", "Hardcodear `userId` en el middleware"],
    11: ["Admin usable por staff", "Invitar staff sin audit/nota"],
    12: ["Demo sin contraste owner/staff", "Prometer WhatsApp Business API sin scope"],
    13: ["Rutas ‘protegidas’ solo ocultando links", "Front sin TypeScript / fuera de stack.md"],
    14: ["Logout solo limpia estado React y deja cookie", "Form sin mensaje de 401"],
    15: ["Spinner eterno sin timeout/error", "Vacío idéntico a error"],
    16: ["Inputs sin `<label>` / placeholder como único texto", "Errores solo en toast no asociado"],
    17: ["Pegar teléfonos reales en el repo", "Texto wa.me sin `encodeURIComponent`"],
    18: ["Botón que llama API Business inexistente", "Abrir wa.me con PII extra innecesaria"],
    19: ["Estados libres sin check/enum", "Transiciones sin authz"],
    20: ["Marcar P3 sin botón + doc", "Doc genérico sin flujo del piloto"],
    21: ["Commitear `.env`", "Secrets horneados en código"],
    22: ["URL staging solo en chat, no en `docs/deploy.md`", "Secrets en variables del Dockerfile"],
    23: ["Usar `curl -k` como ‘HTTPS OK’", "Health solo en localhost"],
    24: ["Smoke sin fecha/resultado", "Password de staging pegado en markdown"],
    25: ["Tabla OWASP vacía o copy-paste sin controles del repo", "Ignorar Broken Access Control"],
    26: ["`Access-Control-Allow-Origin: *` en prod", "Sin `helmet`/equivalente y sin nota"],
    27: ["Rate limit solo en memoria sin doc de multi-instancia", "429 sin test"],
    28: ["‘Corre en mi laptop’ sin script/CI", "CI que no ejecuta tests auth"],
    29: ["ADR genérico sin Agenda Ops", "Implementar multi-tenant completo sin necesidad"],
    30: ["Checklist todo OK sin enlaces a evidencia", "Olvidar backups → M19"],
    31: ["Guion de 30 minutos impracticable", "Password demo en el markdown"],
    32: ["Cerrar M17 sin listar gaps", "No mencionar handoff Docker/secrets a M19"],
}


def build_bodies() -> dict[int, str]:
    bodies: dict[int, str] = {}
    for i, raw in enumerate(m17_lessons.RAW, 1):
        titulo = raw["titulo"]
        if titulo.endswith(".md") and "stack.md" in titulo:
            titulo = "Scaffold Agenda Ops — API, DB y stack"
        bodies[i] = build_body(
            orden=i,
            titulo=titulo,
            horas=float(raw.get("horas", 5)),
            semana=int(raw["semana"]),
            porque=raw["porque"],
            objetivo=raw["objetivo"],
            steps=STEPS[i],
            commit_msg=default_commit("M17", i, titulo),
            conceptos=raw.get("conceptos"),
            por_que_asi=None,
        )
    return bodies


def patched_raw() -> list[dict]:
    out = []
    for i, raw in enumerate(m17_lessons.RAW, 1):
        r = dict(raw)
        if r["titulo"].endswith(".md") and "stack.md" in r["titulo"]:
            r["titulo"] = "Scaffold Agenda Ops — API, DB y stack"
        r["hecho"] = HECHO[i]
        r["errores"] = ERRORES[i]
        out.append(r)
    return out
