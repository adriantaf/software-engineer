---
id: L31
materia: M17
orden: 31
titulo: Demo grabable para design partner
horas: 5.0
semana: 8
lectura: Guion demo 10 min
evidencia: projects/m17-vitrina/docs/demo-script.md
---

# L31 — Demo grabable para design partner

**~5.0 h · Semana 8**

Validación real del MVP.

## Objetivo

Guion demo: onboarding, pedido, WhatsApp, roles. URL staging y creds test.

## Conceptos clave

- demo
- partner
- staging

## Pasos (hazlos en orden)

### 1. Guion demo grabable (50–60 min)

```bash
cat > projects/m17-vitrina/docs/demo-script.md << 'EOF'
# Demo design partner (≤8 min)
1. Login owner
2. Crear pedido
3. Recordatorio WhatsApp
4. Rol staff 403 admin
EOF
```

### 2. Ensayo + nota (40–50 min)

Cronometra. Anota URL staging y usuario demo (password en gestor, no en git).

```bash
git add projects/m17-vitrina/docs/demo-script.md
git commit -m "docs(m17): L31 demo script design partner"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Guion demo 10 min | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/demo-script.md` con guion ≤8 min y URL staging.
2. Commit `docs(m17): L31 demo-grabable-para-design-partner`.

## Errores comunes

- Guion de 30 minutos impracticable.
- Password demo en el markdown.

## Siguiente

[L32 — Cierre M17 — evidencias, dominio y handoff M19](L32-cierre-m17-evidencias-dominio-y-handoff-m19.md)
