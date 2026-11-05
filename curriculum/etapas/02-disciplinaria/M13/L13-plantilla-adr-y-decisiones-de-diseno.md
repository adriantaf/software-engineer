---
id: L13
materia: M13
orden: 13
titulo: Plantilla ADR y decisiones de diseño
horas: 5
semana: 4
lectura: Plantilla ADR M01; índice de decisiones pendientes
evidencia: adr/README.md índice + plantilla reutilizable
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Semana de decisiones. Hoy ordenas el proceso para no improvisar en M17.


      **Objetivo de esta lección:** Índice de ADRs + plantilla; lista de
      decisiones que faltan (persistencia, auth, tenant).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Plantilla
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/adr
      git commit -m "docs(m13): indice ADR y plantilla"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Índice
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/adr
      git commit -m "docs(m13): indice ADR y plantilla"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Plantilla ADR y decisiones de diseño», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Plantilla ADR y
          decisiones de diseño
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git add projects/m13-diseno/adr`
    comandoEsperado:
      - git add projects/m13-diseno/adr
      - 'git commit -m "docs(m13): indice ADR y plantilla"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m13-diseno/adr'
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
          Índice de ADRs + plantilla; lista de decisiones que faltan
          (persistencia, auth, tenant).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Backlog de decisiones
    xp: 10
    cuerpo: >-
      Lista 5 preguntas abiertas (¿ORM?, ¿calcula fin el server?, ¿soft-delete
      pedidos?).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`adr/README.md` lista ADR 001 y placeholders 002–004 con estado.'
      - Existe `adr/PLANTILLA.md` (o equivalente) copiable.
      - 'Commit `docs(m13): indice ADR y plantilla`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Plantilla ADR y decisiones de diseño

**~5.0 h · Semana 4**

Semana de decisiones. Hoy ordenas el proceso para no improvisar en M17.

## Objetivo

Índice de ADRs + plantilla; lista de decisiones que faltan (persistencia, auth, tenant).

## Pasos (hazlos en orden)

### 1. Plantilla (30–40 min)

`projects/m13-diseno/adr/PLANTILLA.md` con secciones Contexto / Decisión / Consecuencias / Alternativas rechazadas.

### 2. Índice (40–50 min)

`adr/README.md`:

| ADR | Título | Estado |
|-----|--------|--------|
| 001 | Monolito modular | Aceptado |
| 002 | Persistencia | Borrador L14 |
| 003 | Auth/sesión | Borrador L16 |
| 004 | Extensibilidad tenant | Nota L15 |

### 3. Backlog de decisiones (50–60 min)

Lista 5 preguntas abiertas (¿ORM?, ¿calcula fin el server?, ¿soft-delete pedidos?).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/adr
git commit -m "docs(m13): indice ADR y plantilla"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | ADR: contexto, decisión, consecuencias; índice vivo | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `adr/README.md` lista ADR 001 y placeholders 002–004 con estado.
2. Existe `adr/PLANTILLA.md` (o equivalente) copiable.
3. Commit `docs(m13): indice ADR y plantilla`.

## Errores comunes

- ADRs de 3 líneas sin consecuencias.
- Decisiones en chats/Discord sin archivo.
- Índice que no enlaza archivos reales.

## Siguiente

[L14 — ADR persistencia y modelo de datos](L14-adr-persistencia-y-modelo-de-datos.md)
