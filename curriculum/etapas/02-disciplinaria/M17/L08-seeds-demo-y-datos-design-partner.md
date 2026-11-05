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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Script seed con negocio piloto, owner, staff, pedidos
      ejemplo para demo.


      - seed

      - demo

      - idempotencia
  - id: s2
    tipo: ejemplo
    titulo: 1. Script seed reproducible
    xp: 10
    cuerpo: |-
      ```ts
      // projects/m17-vitrina/scripts/seed.ts
      // owner demo + 2 staff + 5 clientes + 3 servicios + pedidos fake
      // SOLO datos sintéticos — sin PII real del design partner
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Seeds demo y datos design partner" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/scripts/seed.ts
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Seeds con PII real del design partner
      en git."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Script seed con negocio piloto, owner, staff, pedidos ejemplo para
          demo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta en README
    xp: 10
    cuerpo: >-
      ```bash

      rg -n "seed" projects/m17-vitrina/README.md || echo "añade sección Seed"

      ```


      Incluye emails demo y password **solo** en `.env.example` como
      placeholders, no secretos de staging.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
