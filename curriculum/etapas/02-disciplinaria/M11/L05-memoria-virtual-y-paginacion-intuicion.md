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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar memoria virtual/paginación a nivel operador.


      OOM y lentitud empiezan cuando no entiendes qué es RSS. Hoy el modelo
      mental.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura + esquema
    xp: 10
    cuerpo: |-
      ```bash
      free -h
      head -20 /proc/meminfo
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Memoria virtual y paginación (intuición)" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: labs/semana-02-memoria.md
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

      `git add projects/m11-so/labs/semana-02-memoria.md`
    comandoEsperado:
      - git add projects/m11-so/labs/semana-02-memoria.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m11-so/labs/semana-02-memoria.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Documentar memoria virtual/paginación a nivel operador.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Host
    xp: 10
    cuerpo: |-
      ```bash
      free -h
      head -20 /proc/meminfo
      ```

      Define MemAvailable vs swap used en tus palabras.
  - id: s7
    tipo: explicacion
    titulo: 3. Producto
    xp: 10
    cuerpo: >-
      Escenario: VPS 1 GB con API + Postgres. Qué síntomas verías antes del OOM
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
