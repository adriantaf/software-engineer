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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Capturar RSS/CPU de Node y `process.memoryUsage()`.

      Mides el proceso que importa: tu runtime.
  - id: s2
    tipo: ejemplo
    titulo: 1. Proceso de muestra
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Observar RSS y CPU de Node" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/rss-node.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
      console.log(process.memoryUsage());}, 1000)' &`
    comandoEsperado:
      - >-
        node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
        console.log(process.memoryUsage());}, 1000)' &
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: node -e 'const a=[]; setInterval(()=>{a.push(Buffer.alloc(1e5));
      console.log(process.memoryUsage());}, 1000)' &
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Capturar RSS/CPU de Node y `process.memoryUsage()`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. top
    xp: 10
    cuerpo: |-
      ```bash
      una snapshot:
      ps aux --sort=-%mem | head -15
      ```

      Localiza `node` si queda alguno.
  - id: s7
    tipo: explicacion
    titulo: 3. Nota ops
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
