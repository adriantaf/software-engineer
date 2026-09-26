---
id: L12
materia: M17
orden: 12
titulo: Demo roles y inicio P3 WhatsApp
horas: 5.0
semana: 3
lectura: Ficha P3 parcial
evidencia: projects/m17-agenda-ops/docs/demo-roles.md
---

# L12 — Demo roles y inicio P3 WhatsApp

**~5.0 h · Semana 3**

P3 requiere evidencia reproducible para el design partner.

## Objetivo

Grabar o documentar pasos demo: owner vs staff en acción bloqueada.

## Conceptos clave

- demo
- roles
- evidencia

## Pasos (hazlos en orden)

### 1. Guion demo roles (50–60 min)

```bash
cat > projects/m17-agenda-ops/docs/demo-roles.md << 'EOF'
# Demo roles
1. Login owner → /admin OK
2. Login staff → /admin 403 / UI oculta
3. Ambos crean cita
EOF
```

### 2. Ejecuta y anota (40–50 min)

```bash
npm run seed
# recorre el guion con dos sesiones/cookies
```

### 3. Kickoff P3 WhatsApp (30 min) + commit

Crea borrador `docs/integracion-whatsapp.md` (enlace wa.me, sin API Business obligatoria).

```bash
git add projects/m17-agenda-ops/docs
git commit -m "docs(m17): L12 demo roles inicio whatsapp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha P3 parcial | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-agenda-ops/docs/demo-roles.md` con guion owner vs staff.
2. Borrador `projects/m17-agenda-ops/docs/integracion-whatsapp.md`.
3. Commit `docs(m17): L12 demo-roles-y-inicio-p3-whatsapp`.

## Errores comunes

- Demo sin contraste owner/staff.
- Prometer WhatsApp Business API sin scope.

## Siguiente

[L13 — Scaffold front y rutas protegidas](L13-scaffold-front-y-rutas-protegidas.md)
