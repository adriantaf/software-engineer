---
id: L08
materia: M17
orden: 8
titulo: Seeds demo y datos design partner
horas: 5.0
semana: 2
lectura: Fixtures reproducibles
evidencia: projects/m17-agenda-ops/scripts/seed.ts
---

# L08 — Seeds demo y datos design partner

**~5.0 h · Semana 2**

Demo reproducible evita ‘en mi máquina sí’.

## Objetivo

Script seed con negocio piloto, owner, staff, citas ejemplo para demo.

## Conceptos clave

- seed
- demo
- idempotencia

## Pasos (hazlos en orden)

### 1. Script seed reproducible (70–90 min)

```ts
// projects/m17-agenda-ops/scripts/seed.ts
// owner demo + 2 staff + 5 clientes + 3 servicios + citas fake
// SOLO datos sintéticos — sin PII real del design partner
```

```bash
npx tsx scripts/seed.ts
# o: npm run seed
```

### 2. Documenta en README (20 min)

```bash
rg -n "seed" projects/m17-agenda-ops/README.md || echo "añade sección Seed"
```

Incluye emails demo y password **solo** en `.env.example` como placeholders, no secretos de staging.

### 3. Commit (15 min)

```bash
git add projects/m17-agenda-ops/scripts/seed.ts projects/m17-agenda-ops/README.md
git commit -m "feat(m17): L08 seeds demo design partner"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Fixtures reproducibles | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-agenda-ops/scripts/seed.ts` (o script documentado).
2. README incluye comando seed; datos solo sintéticos (artefacto: `projects/m17-agenda-ops/scripts/seed.ts`).
3. Commit `docs(m17): L08 seeds-demo-y-datos-design-partner`.

## Errores comunes

- Seeds con PII real del design partner en git.
- Seed no reproducible (falta comando).

## Siguiente

[L09 — Matriz de permisos owner y staff](L09-matriz-de-permisos-owner-y-staff.md)
