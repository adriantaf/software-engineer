---
id: L01
materia: M03
orden: 1
titulo: Lógica proposicional y tablas de verdad
horas: 2.5
semana: 1
lectura: "Rosen Cap. 1.1–1.2 — proposiciones, conectivos, tablas de verdad"
evidencia: "projects/m03-discretas/apuntes/logica-proposicional.md + src/logic.ts (implica) + commit"
---

# L01 — Lógica proposicional y tablas de verdad

**~2.5 h · Semana 1**

Primera lección de M03: instalas la carpeta de evidencia, construyes tablas de verdad a mano y verificas la implicación en TypeScript.

## Objetivo

Definir proposición y conectivos (∧, ∨, ¬); construir tablas de verdad de forma sistemática; implementar `implica` y comprobar los cuatro casos de `P → Q`.

## Por qué empieza así

Sin distinguir proposición de enunciado vago, las demostraciones posteriores se vuelven “suena bien”. La tabla de verdad es la **prueba mecánica** de que entiendes los conectivos.

## Pasos (hazlos en orden)

### 1. Proyecto y bitácora (20–25 min)

Desde la raíz del repo:

```bash
mkdir -p projects/m03-discretas/src projects/m03-discretas/apuntes projects/m03-discretas/grafos
cd projects/m03-discretas
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init
```

En `tsconfig.json` deja `"strict": true`. Añade en `package.json`:

```json
"scripts": {
  "test": "vitest run",
  "tsx": "tsx"
}
```

### 2. Apuntes: proposiciones (30–40 min)

Crea `projects/m03-discretas/apuntes/logica-proposicional.md` con:

- Definición de **proposición** (oración con valor de verdad V/F).
- Tres ejemplos que **sí** son proposiciones y tres que **no** (preguntas, órdenes, enunciados con variable libre sin cuantificar).
- Tablas de verdad completas para `P ∧ Q`, `P ∨ Q`, `¬P` (4 filas cada una, columnas intermedias si ayuda).

No copies tablas de internet sin rellenarlas tú.

### 3. Implicación en papel (25–30 min)

En el mismo archivo, tabla de verdad de `P → Q`. Escribe en una frase por qué `F → V` y `F → F` son verdaderas (definición material).

### 4. Implementación mínima (30–40 min)

`projects/m03-discretas/src/logic.ts`:

```ts
export function implica(p: boolean, q: boolean): boolean {
  return !p || q;
}

export function y(p: boolean, q: boolean): boolean {
  return p && q;
}

export function o(p: boolean, q: boolean): boolean {
  return p || q;
}

export function no(p: boolean): boolean {
  return !p;
}
```

`projects/m03-discretas/src/logic.test.ts`: un test por fila de la tabla de `implica` (4 casos).

```bash
npm test
```

### 5. Commit (10 min)

```bash
git add projects/m03-discretas
git commit -m "feat(m03): tablas de verdad e implicación en TS"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Rosen | Cap. 1.1–1.2 (proposiciones, conectivos) | Misma edición ES; si el número difiere, busca “Lógica proposicional” |
| Plan | [Cómo estudiar](../../../como-estudiar.md) (regla 40/30/30) | — |
| Catálogo | Entrada M03 | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. Existe `apuntes/logica-proposicional.md` con las tres tablas (∧, ∨, ¬) y la de →.
2. `src/logic.ts` exporta los conectivos y `npm test` pasa en `implica`.
3. Puedes decir en voz alta qué hace `¬(P ∧ Q)` sin mirar la tabla (aunque luego la verifiques).

## Errores comunes

- Confundir “oración en español” con proposición (falta valor de verdad).
- Implementar `implica` como `p && q`.
- Tablas con solo 2 filas o sin el caso `F,F` de la implicación.

## Siguiente

[L02 — Implicación, equivalencias y leyes](L02-implicacion-equivalencias-y-leyes.md)
