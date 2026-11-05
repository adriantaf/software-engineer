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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Consolidar tests auth (register, login, me, logout) y marcar
      P1 parcial en README.


      - P1

      - suite auth

      - logout
  - id: s2
    tipo: ejemplo
    titulo: 1. Consolida suite auth
    xp: 10
    cuerpo: |-
      ```ts
      // esqueleto
      it("login → me 200", async () => { /* ... */ });
      it("me sin cookie → 401", async () => { /* ... */ });
      it("logout invalida sesión", async () => { /* ... */ });
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre semana 1 — suite auth P1" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/tests/auth.test.ts
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
      ¿Es buena práctica en esta lección? “Dar P1 por hecho solo con Postman
      manual."
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
          Consolidar tests auth (register, login, me, logout) y marcar P1
          parcial en README.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta comando en README
    xp: 10
    cuerpo: |-
      ```bash
      npm test
      anota en README la línea exacta que deja P1 verde
      ```

      Marca P1 parcial en el checklist del README de `projects/m17-vitrina/`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit cierre semana 1
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
