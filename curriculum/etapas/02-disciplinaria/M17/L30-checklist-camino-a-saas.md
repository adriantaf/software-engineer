---
id: L30
materia: M17
orden: 30
titulo: Checklist camino a SaaS
horas: 5.0
semana: 8
lectura: Ficha M17 checklist
evidencia: projects/m17-agenda-ops/docs/checklist-saas.md
---

# L30 — Checklist camino a SaaS

**~5.0 h · Semana 8**

Transparencia > checkboxes mentirosos.

## Objetivo

Completar checklist ficha: tablas, roles, HTTPS, tests — gaps honestos.

## Conceptos clave

- checklist
- gap
- SaaS

## Pasos (hazlos en orden)

### 1. Checklist SaaS (70–90 min)

```bash
cat > projects/m17-agenda-ops/docs/checklist-saas.md << 'EOF'
# Camino a SaaS
- [ ] Aislamiento tenant en queries
- [ ] Billing (out of scope piloto)
- [ ] Backups (→ M19)
- [ ] Observabilidad
- [ ] Onboarding self-serve
EOF
```

Marca hecho/gap con enlace a evidencia.

### 2. Commit (15 min)

```bash
git add projects/m17-agenda-ops/docs/checklist-saas.md
git commit -m "docs(m17): L30 checklist camino saas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 checklist | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-agenda-ops/docs/checklist-saas.md` con ítems marcados o gaps enlazados.
2. Commit `docs(m17): L30 checklist-camino-a-saas`.

## Errores comunes

- Checklist todo OK sin enlaces a evidencia.
- Olvidar backups → M19.

## Siguiente

[L31 — Demo grabable para design partner](L31-demo-grabable-para-design-partner.md)
