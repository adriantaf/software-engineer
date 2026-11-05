---
id: L03
materia: M14
orden: 3
titulo: 'Singleton: cuándo NO usarlo'
horas: 5
semana: 1
lectura: Singleton — abusos; DI como alternativa
evidencia: docs/anti-singleton.md + ejemplo DI vs global
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Anti-patrón documentado + alternativa con inyección de
      dependencias simple.


      Aprender patrones incluye rechazarlos. Hoy documentas por qué Vitrina no
      necesita Singleton de “AppContext”.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lee Singleton
    xp: 10
    cuerpo: 'Enfócate en problemas: estado global, orden de init, tests acoplados.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Singleton: cuándo NO usarlo" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: docs/anti-singleton.md + ejemplo DI vs global
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
      ¿Es buena práctica en esta lección? ““Nunca uses Singleton” sin matiz (a
      veces un cache read-only está bien)."
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
          Anti-patrón documentado + alternativa con inyección de dependencias
          simple.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe anti-singleton.md
    xp: 10
    cuerpo: >-
      Incluye: “conexión DB como Singleton” vs “pasar `pool` al Repository”;
      “Config.getInstance()” vs `loadConfig()` en main.
  - id: s7
    tipo: explicacion
    titulo: 3. Mini demo
    xp: 10
    cuerpo: >-
      `src/examples/di-clock.ts`: reloj inyectable para tests (servirá en M15).
      Sin `getInstance()`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `docs/anti-singleton.md` explica ≥2 razones para no usarlo en DB/config
        del piloto.
      - >-
        Código de contraste: módulo con export de instancia vs factory/DI
        inyectable en tests.
      - 'Commit `docs(m14): anti-singleton y alternativa DI`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Singleton: cuándo NO usarlo

**~5.0 h · Semana 1**

Aprender patrones incluye rechazarlos. Hoy documentas por qué Vitrina no necesita Singleton de “AppContext”.

## Objetivo

Anti-patrón documentado + alternativa con inyección de dependencias simple.

## Pasos (hazlos en orden)

### 1. Lee Singleton (40–50 min)

Enfócate en problemas: estado global, orden de init, tests acoplados.

### 2. Escribe anti-singleton.md (60–70 min)

Incluye: “conexión DB como Singleton” vs “pasar `pool` al Repository”; “Config.getInstance()” vs `loadConfig()` en main.

### 3. Mini demo (50–60 min)

`src/examples/di-clock.ts`: reloj inyectable para tests (servirá en M15). Sin `getInstance()`.

### 4. Commit (15 min)

`docs(m14): anti-singleton y alternativa DI`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Cuándo Singleton duele (tests, estado global) y qué usar en su lugar | [Refactoring.Guru — Singleton (ES)](https://refactoring.guru/es/design-patterns/singleton) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `docs/anti-singleton.md` explica ≥2 razones para no usarlo en DB/config del piloto.
2. Código de contraste: módulo con export de instancia vs factory/DI inyectable en tests.
3. Commit `docs(m14): anti-singleton y alternativa DI`.

## Errores comunes

- “Nunca uses Singleton” sin matiz (a veces un cache read-only está bien).
- Singleton de conexión PG que impide tests paralelos — y aún así lo adoptas.
- Documento sin ejemplo de código.

## Siguiente

[L04 — Cierre semana 1 — creacionales y bitácora](L04-cierre-semana-1-creacionales-y-bitacora.md)
