# M17 — Aplicaciones web full-stack (Agenda Ops MVP)

Carpeta de **evidencia** del piloto web **Agenda Ops**. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Nace el piloto web: auth real, CRUD de citas/clientes/servicios, roles owner/staff, integración WhatsApp mínima y base documentada hacia multi-tenant.

## Arranque rápido

```bash
cd projects/m17-agenda-ops
cp .env.example .env   # cuando exista; nunca lo subas
# Levanta API + Postgres según stack.md
curl -sS http://localhost:3000/health
```

## Estructura esperada

```
projects/m17-agenda-ops/
├── README.md
├── stack.md                 # stack fijo (L01)
├── .env.example
├── docs/
│   ├── auth.md
│   ├── permisos.md
│   ├── ui-estados.md        # P2
│   ├── integracion-whatsapp.md  # P3
│   ├── deploy.md / smoke-test.md
│   ├── owasp-mapa.md
│   ├── adr-tenant-id.md
│   ├── checklist-saas.md
│   └── demo-script.md
├── src/ o apps/             # API + front
├── tests/                   # auth + roles
└── scripts/seed.ts
```

## Lecciones → artefactos

| Semana | Lecciones | Qué debe existir aquí |
|--------|-----------|------------------------|
| 1 | L01–L04 | `stack.md`, auth register/login/me, suite P1 |
| 2 | L05–L08 | dominio citas/clientes/servicios + seeds |
| 3 | L09–L12 | `permisos.md`, middleware 403, admin, demo-roles |
| 4 | L13–L16 | front protegido + `ui-estados.md` (P2) |
| 5 | L17–L20 | WhatsApp deep-links (P3) |
| 6 | L21–L24 | env, staging HTTPS, smoke |
| 7 | L25–L28 | OWASP mapa, headers, rate limit, CI |
| 8 | L29–L32 | ADR tenant, checklist SaaS, demo, cierre |

## Checklist (Evidencia de hecho)

- **P1 — API auth:** Registro/login + validación; tests 401/403 en README.
- **P2 — Front:** Rutas protegidas; `docs/ui-estados.md` (loading/error/vacío).
- **P3 — Admin:** Roles demostrables + `docs/integracion-whatsapp.md`.
- **Proyecto — Piloto:** Deploy HTTPS + checklist camino a SaaS marcado o gaps documentados.

## Cómo usarla

1. Abre la ficha **M17**, [producto-saas.md](../../curriculum/producto-saas.md) y la lección **L01**.
2. Sigue **L01–L32** en orden (8 × 4).
3. Mantén `stack.md` y ADRs en `docs/`; cada endpoint sensible con test de auth.
4. Marca prácticas/proyecto en la UI solo cuando exista la evidencia.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M17-aplicaciones-web.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M17/`
- Diseño previo: `projects/m13-diseno/`
- Esquema: `projects/m09-bases-datos/`
- Plan: `/materia/M17/`
