---
id: L01
materia: M19
orden: 1
titulo: Inventario de secretos y ambientes staging/prod
horas: 5
semana: 1
lectura: "Docker docs — env vars + 12-factor"
evidencia: "projects/m19-ops/secrets-inventory.md + ambientes.md"
---

# L01 — Inventario de secretos y ambientes staging/prod

**~5 h · Semana 1**

## Objetivo

Crear inventario de secretos sin valores y definir URLs/objetivo de staging y prod para Agenda Ops.

## Por qué importa

M19 empieza donde M18 dejó: nada de secretos en git antes de empaquetar.

## Conceptos

- DATABASE_URL
- SESSION_SECRET
- Stripe test futuro

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m19-ops
git ls-files | rg -i '\.env|secret|credential' || true
```

Completa `secrets-inventory.md` y `ambientes.md` según ficha M19.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l01 inventario-de-secretos-y-ambientes-stagi"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | producto-saas.md | M18 secrets |

## Hecho cuando

1. Ambos archivos existen.
2. Sin valores secretos.
3. URLs objetivo anotadas.

## Errores comunes

- Pegar JWT en markdown.
- Un solo ambiente ‘prod’.

## Siguiente

[L02 — Dockerfile multi-stage para la API](L02-dockerfile-multi-stage-para-la-api.md)
