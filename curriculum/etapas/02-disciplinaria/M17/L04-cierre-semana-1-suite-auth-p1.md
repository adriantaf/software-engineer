---
id: L04
materia: M17
orden: 4
titulo: Cierre semana 1 — suite auth P1
horas: 5
semana: 1
lectura: Ficha M17 P1
evidencia: projects/m17-vitrina/tests/auth.test.ts
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - P1

      - suite auth

      - logout


      **Objetivo de esta lección:** Consolidar tests auth (register, login, me,
      logout) y marcar P1 parcial en README.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Consolida suite auth
    xp: 10
    cuerpo: >-
      ```ts

      // esqueleto

      it("login → me 200", async () => { /* ... */ });

      it("me sin cookie → 401", async () => { /* ... */ });

      it("logout invalida sesión", async () => { /* ... */ });

      ```


      En `projects/m17-vitrina/tests/auth.test.ts` (o equivalente) cubre:
      register, login, me, logout, 401, password malo. Mínimo **6** tests.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta comando en README
    xp: 10
    cuerpo: |-
      ```bash
      npm test
      # anota en README la línea exacta que deja P1 verde
      ```

      Marca P1 parcial en el checklist del README de `projects/m17-vitrina/`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre semana 1 — suite auth P1», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre semana 1 — suite
          auth P1
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
      ¿Es recomendable en esta lección? “Dar P1 por hecho solo con Postman
      manual."
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
          Consolidar tests auth (register, login, me, logout) y marcar P1
          parcial en README.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit cierre semana 1
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina
      git commit -m "test(m17): L04 suite auth P1 semana 1"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/tests/auth.test.ts` (o equiv.) con ≥6 tests
        verdes.
      - README documenta el comando exacto `npm test`.
      - >-
        Checklist P1 parcial marcado en README (artefacto:
        `projects/m17-vitrina/tests/auth.test.ts`).
      - 'Commit `docs(m17): L04 cierre-semana-1-suite-auth-p1`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre semana 1 — suite auth P1

**~5.0 h · Semana 1**

P1 es puerta para todo CRUD.

## Objetivo

Consolidar tests auth (register, login, me, logout) y marcar P1 parcial en README.

## Conceptos clave

- P1
- suite auth
- logout

## Pasos (hazlos en orden)

### 1. Consolida suite auth (80–100 min)

En `projects/m17-vitrina/tests/auth.test.ts` (o equivalente) cubre: register, login, me, logout, 401, password malo. Mínimo **6** tests.

```ts
// esqueleto
it("login → me 200", async () => { /* ... */ });
it("me sin cookie → 401", async () => { /* ... */ });
it("logout invalida sesión", async () => { /* ... */ });
```

### 2. Documenta comando en README (20–30 min)

```bash
npm test
# anota en README la línea exacta que deja P1 verde
```

Marca P1 parcial en el checklist del README de `projects/m17-vitrina/`.

### 3. Commit cierre semana 1 (15 min)

```bash
git add projects/m17-vitrina
git commit -m "test(m17): L04 suite auth P1 semana 1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 P1 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/tests/auth.test.ts` (o equiv.) con ≥6 tests verdes.
2. README documenta el comando exacto `npm test`.
3. Checklist P1 parcial marcado en README (artefacto: `projects/m17-vitrina/tests/auth.test.ts`).
4. Commit `docs(m17): L04 cierre-semana-1-suite-auth-p1`.

## Errores comunes

- Dar P1 por hecho solo con Postman manual.
- Suite <6 casos o flaky.

## Siguiente

[L05 — Modelo de dominio pedidos, clientes y servicios](L05-modelo-de-dominio-pedidos-clientes-y-servicios.md)
