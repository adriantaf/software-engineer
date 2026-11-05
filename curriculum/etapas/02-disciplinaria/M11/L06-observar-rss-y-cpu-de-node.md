---
id: L06
materia: M11
orden: 6
titulo: Observar RSS y CPU de Node
horas: 5
semana: 2
lectura: 'man ps, top/htop'
evidencia: labs/rss-node.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Mides el proceso que importa: tu runtime.


      **Objetivo de esta lección:** Capturar RSS/CPU de Node y
      `process.memoryUsage()`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Proceso de muestra
    xp: 10
    cuerpo: >-
      ```bash

      node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
      console.log(process.memoryUsage());}, 1000)' &

      PID=$!

      sleep 3

      ps -p $PID -o pid,pcpu,rss,vsz,cmd

      kill $PID

      ```


      Copia números a `labs/rss-node.md` e interpreta rss vs heapUsed.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: top
    xp: 10
    cuerpo: |-
      ```bash
      # una snapshot:
      ps aux --sort=-%mem | head -15
      ```

      Localiza `node` si queda alguno.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Observar RSS y CPU de Node», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Observar RSS y CPU de
          Node
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
      console.log(process.memoryUsage());}, 1000)' &`
    comandoEsperado:
      - >-
        node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
        console.log(process.memoryUsage());}, 1000)' &
      - git add projects/m11-so/labs/rss-node.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
      console.log(process.memoryUsage());}, 1000)' &
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
        texto: Capturar RSS/CPU de Node y `process.memoryUsage()`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Nota ops
    xp: 10
    cuerpo: Qué alarma pondrías en el piloto (RSS > X MB sostenido).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/rss-node.md` con mediciones de un proceso Node (ps + memoryUsage).'
      - Script o one-liner que imprime heap/rss.
      - 'Commit `docs(m11): l06 rss cpu node`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Observar RSS y CPU de Node

**~5.0 h · Semana 2**

Mides el proceso que importa: tu runtime.

## Objetivo

Capturar RSS/CPU de Node y `process.memoryUsage()`.

## Pasos

### 1. Proceso de muestra (50 min)

```bash
node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5)); console.log(process.memoryUsage());}, 1000)' &
PID=$!
sleep 3
ps -p $PID -o pid,pcpu,rss,vsz,cmd
kill $PID
```

Copia números a `labs/rss-node.md` e interpreta rss vs heapUsed.

### 2. top (30 min)

```bash
# una snapshot:
ps aux --sort=-%mem | head -15
```

Localiza `node` si queda alguno.

### 3. Nota ops (30 min)

Qué alarma pondrías en el piloto (RSS > X MB sostenido).

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/rss-node.md
git commit -m "docs(m11): l06 rss cpu node"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | RSS/VSZ; %CPU; process.memoryUsage() en Node | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/rss-node.md` con mediciones de un proceso Node (ps + memoryUsage).
2. Script o one-liner que imprime heap/rss.
3. Commit `docs(m11): l06 rss cpu node`.

## Errores comunes

- Mirar solo VSZ y asustarse.
- Medir una vez sin carga ni idle.
- No anotar unidades (kB vs MB).

## Siguiente

[L07 — OOM, ulimit y síntomas](L07-oom-ulimit-y-sintomas.md)
