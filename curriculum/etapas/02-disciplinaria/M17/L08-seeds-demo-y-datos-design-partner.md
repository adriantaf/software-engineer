---
id: L08
materia: M17
orden: 8
titulo: Seeds demo y datos design partner
horas: 5
semana: 2
lectura: Fixtures reproducibles
evidencia: projects/m17-vitrina/scripts/seed.ts
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - seed

      - demo

      - idempotencia


      **Objetivo de esta lección:** Script seed con negocio piloto, owner,
      staff, pedidos ejemplo para demo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Script seed reproducible
    xp: 10
    cuerpo: |-
      ```ts
      // projects/m17-vitrina/scripts/seed.ts
      // owner demo + 2 staff + 5 clientes + 3 servicios + pedidos fake
      // SOLO datos sintéticos — sin PII real del design partner
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta en README
    xp: 10
    cuerpo: >-
      ```bash

      rg -n "seed" projects/m17-vitrina/README.md || echo "añade sección Seed"

      ```


      Incluye emails demo y password **solo** en `.env.example` como
      placeholders, no secretos de staging.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Seeds demo y datos design partner», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Seeds demo y datos
          design partner
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Seeds con PII real del design partner
      en git."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Script seed con negocio piloto, owner, staff, pedidos ejemplo para
          demo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
    xp: 10
    cuerpo: >-
      ```bash

      git add projects/m17-vitrina/scripts/seed.ts
      projects/m17-vitrina/README.md

      git commit -m "feat(m17): L08 seeds demo design partner"

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m17-vitrina/scripts/seed.ts` (o script documentado).
      - >-
        README incluye comando seed; datos solo sintéticos (artefacto:
        `projects/m17-vitrina/scripts/seed.ts`).
      - 'Commit `docs(m17): L08 seeds-demo-y-datos-design-partner`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Seeds demo y datos design partner

**~5.0 h · Semana 2**

Demo reproducible evita ‘en mi máquina sí’.

## Objetivo

Script seed con negocio piloto, owner, staff, pedidos ejemplo para demo.

## Conceptos clave

- seed
- demo
- idempotencia

## Pasos (hazlos en orden)

### 1. Script seed reproducible (70–90 min)

```ts
// projects/m17-vitrina/scripts/seed.ts
// owner demo + 2 staff + 5 clientes + 3 servicios + pedidos fake
// SOLO datos sintéticos — sin PII real del design partner
```

```bash
npx tsx scripts/seed.ts
# o: npm run seed
```

### 2. Documenta en README (20 min)

```bash
rg -n "seed" projects/m17-vitrina/README.md || echo "añade sección Seed"
```

Incluye emails demo y password **solo** en `.env.example` como placeholders, no secretos de staging.

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/scripts/seed.ts projects/m17-vitrina/README.md
git commit -m "feat(m17): L08 seeds demo design partner"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Fixtures reproducibles | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/scripts/seed.ts` (o script documentado).
2. README incluye comando seed; datos solo sintéticos (artefacto: `projects/m17-vitrina/scripts/seed.ts`).
3. Commit `docs(m17): L08 seeds-demo-y-datos-design-partner`.

## Errores comunes

- Seeds con PII real del design partner en git.
- Seed no reproducible (falta comando).

## Siguiente

[L09 — Matriz de permisos owner y staff](L09-matriz-de-permisos-owner-y-staff.md)
