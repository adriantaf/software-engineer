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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Índice de ADRs + plantilla; lista de decisiones que faltan
      (persistencia, auth, tenant).


      Semana de decisiones. Hoy ordenas el proceso para no improvisar en M17.
  - id: s2
    tipo: ejemplo
    titulo: 1. Plantilla
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/adr
      git commit -m "docs(m13): indice ADR y plantilla"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Plantilla ADR y decisiones de diseño" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: adr/README.md índice + plantilla reutilizable
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m13-diseno/adr`
    comandoEsperado:
      - git add projects/m13-diseno/adr
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m13-diseno/adr'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Índice de ADRs + plantilla; lista de decisiones que faltan
          (persistencia, auth, tenant).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Índice
    xp: 10
    cuerpo: |-
      `adr/README.md`:

      | ADR | Título | Estado |
      |-----|--------|--------|
      | 001 | Monolito modular | Aceptado |
      | 002 | Persistencia | Borrador L14 |
      | 003 | Auth/sesión | Borrador L16 |
      | 004 | Extensibilidad tenant | Nota L15 |
  - id: s7
    tipo: explicacion
    titulo: 3. Backlog de decisiones
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
