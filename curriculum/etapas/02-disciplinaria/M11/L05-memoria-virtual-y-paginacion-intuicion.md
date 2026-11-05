---
id: L05
materia: M11
orden: 5
titulo: Memoria virtual y paginación (intuición)
horas: 5
semana: 2
lectura: Silberschatz — memoria virtual
evidencia: labs/semana-02-memoria.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      OOM y lentitud empiezan cuando no entiendes qué es RSS. Hoy el modelo
      mental.


      **Objetivo de esta lección:** Documentar memoria virtual/paginación a
      nivel operador.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura + esquema
    xp: 10
    cuerpo: |-
      ```bash
      free -h
      head -20 /proc/meminfo
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Host
    xp: 10
    cuerpo: |-
      ```bash
      free -h
      head -20 /proc/meminfo
      ```

      Define MemAvailable vs swap used en tus palabras.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Memoria virtual y paginación (intuición)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Memoria virtual y
          paginación (intuición)
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

      `git add projects/m11-so/labs/semana-02-memoria.md`
    comandoEsperado:
      - git add projects/m11-so/labs/semana-02-memoria.md
      - 'git commit -m "docs(m11): l05 memoria virtual"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m11-so/labs/semana-02-memoria.md'
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
        texto: Documentar memoria virtual/paginación a nivel operador.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Producto
    xp: 10
    cuerpo: >-
      Escenario: VPS 1 GB con API + Postgres. Qué síntomas verías antes del OOM
      killer.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/semana-02-memoria.md` explica virtual vs RSS vs swap en lenguaje
        propio.
      - Comandos `free -h` / `/proc/meminfo` (o equivalente) anotados.
      - 'Commit `docs(m11): l05 memoria virtual`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Memoria virtual y paginación (intuición)

**~5.0 h · Semana 2**

OOM y lentitud empiezan cuando no entiendes qué es RSS. Hoy el modelo mental.

## Objetivo

Documentar memoria virtual/paginación a nivel operador.

## Pasos

### 1. Lectura + esquema (60 min)

En `labs/semana-02-memoria.md`: página, page fault (suave/duro), por qué un proceso “pide” más de la RAM física.

### 2. Host (40 min)

```bash
free -h
head -20 /proc/meminfo
```

Define MemAvailable vs swap used en tus palabras.

### 3. Producto (30 min)

Escenario: VPS 1 GB con API + Postgres. Qué síntomas verías antes del OOM killer.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-02-memoria.md
git commit -m "docs(m11): l05 memoria virtual"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Espacio virtual vs físico; páginas; swap/thrashing intuición | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-02-memoria.md` explica virtual vs RSS vs swap en lenguaje propio.
2. Comandos `free -h` / `/proc/meminfo` (o equivalente) anotados.
3. Commit `docs(m11): l05 memoria virtual`.

## Errores comunes

- Equivaler “memoria virtual” con “archivo swap” solamente.
- Diagramas copiados sin explicación.
- Ignorar qué pasa cuando el VPS de Vitrina thrashing-ea.

## Siguiente

[L06 — Observar RSS y CPU de Node](L06-observar-rss-y-cpu-de-node.md)
