# M17 — Aplicaciones web full-stack (Agenda Ops MVP)

Carpeta de **evidencia** del piloto web **Agenda Ops**. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

Nace el piloto web: auth real, CRUD de citas/clientes/servicios, roles owner/staff, integración WhatsApp mínima y base documentada hacia multi-tenant.

## Checklist (Evidencia de hecho)

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — API auth:** Registro/login + validación; tests 401/403 en README.
- **P2 — Front:** Rutas protegidas; `docs/ui-estados.md` (loading/error/vacío).
- **P3 — Admin:** Roles demostrables + `docs/integracion-whatsapp.md`.
- **Proyecto — Piloto:** Deploy HTTPS + checklist camino a SaaS marcado o gaps documentados.

## Cómo usarla

1. Abre la ficha **M17**, [producto-saas.md](../../curriculum/producto-saas.md) y la lección **L01**.
2. Sigue las lecciones **L01–L32** en orden (8 semanas × 4; alta profundidad).
3. Mantén `stack.md` y ADRs en `docs/`; cada endpoint sensible con test de auth.
4. Marca prácticas/proyecto en la UI solo cuando exista la evidencia.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M17-aplicaciones-web.md`
- Lecciones: `curriculum/etapas/02-disciplinaria/M17/`
- Diseño previo: `projects/m13-diseno/`
- Plan: `/materia/M17/`
