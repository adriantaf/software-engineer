# M18 — Seguridad del software (AppSec)

Carpeta de **evidencia** AppSec sobre **tu** Agenda Ops. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Amenazas → PoC en **tu** app → fix → test. Solo staging/local propio.

## Estructura esperada

```
projects/m18-appsec/
├── README.md
├── threat-model-v0.md / threat-model-v1.md   # P1
├── hallazgos.md                              # P2 ≥5
├── informe-appsec.md                         # Proyecto
├── docs/
│   ├── auth-inventario.md
│   ├── checklist-cookies-csrf.md
│   ├── rotacion-secretos.md
│   └── npm-audit.md
├── pocs/          # pasos PoC (sin secretos)
├── fixes/         # notas → commits del repo app
├── tests/         # o enlaces a tests security.*
└── ci/            # workflow o script P3
```

## Lecciones → artefactos

| Semana | Foco | Artefacto |
|--------|------|-----------|
| 1 | STRIDE / Top 10 | threat-model-v0 |
| 2 | Auth hashing / sesión | threat-model-v1 (P1) |
| 3 | Cookies / CSRF | checklist staging |
| 4 | SQLi / XSS | pocs + fixes |
| 5 | IDOR / roles / rate limit | tests cross-user |
| 6 | SSRF / uploads / JSON | hallazgos ≥5 (P2) |
| 7 | deps / secrets / CSP | audit + headers |
| 8 | CI + informe | P3 + informe + ≥3 tests |

## Checklist (Evidencia de hecho)

- **P1 — STRIDE:** Documento de threat model v1.
- **P2 — ≥5 hallazgos:** Tabla PoC → commit fix → test.
- **P3 — CI:** Lint+test+audit (+ grep secretos).
- **Proyecto — Informe:** `informe-appsec.md` + PRs hardening.

## Cómo usarla

1. Abre la ficha **M18** y L01.
2. Trabaja siempre sobre el repo de Agenda Ops (M17); aquí dejas el rastro AppSec.
3. Marca prácticas solo con evidencia enlazada.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M18-seguridad.md`
- Hilo: `curriculum/hilos/seguridad.md`
- App: `projects/m17-agenda-ops/`
- Plan: `/materia/M18/`
