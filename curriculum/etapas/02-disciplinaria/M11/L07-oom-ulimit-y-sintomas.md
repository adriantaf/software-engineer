---
id: L07
materia: M11
orden: 7
titulo: 'OOM, ulimit y síntomas'
horas: 5
semana: 2
lectura: Silberschatz OOM + ulimit man
evidencia: labs/oom-ulimit.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar límites (`ulimit`) y la firma de un OOM.


      Cuando el kernel mata tu API, el síntoma parece “se reinició solo”. Hoy lo
      reconoces.
  - id: s2
    tipo: ejemplo
    titulo: 1. ulimit
    xp: 10
    cuerpo: |-
      ```bash
      ulimit -a
      ulimit -n
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "OOM, ulimit y síntomas" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: labs/oom-ulimit.md
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

      `git add projects/m11-so/labs/oom-ulimit.md`
    comandoEsperado:
      - git add projects/m11-so/labs/oom-ulimit.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m11-so/labs/oom-ulimit.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Documentar límites (`ulimit`) y la firma de un OOM.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Señales OOM
    xp: 10
    cuerpo: |-
      En `labs/oom-ulimit.md` documenta (sin tumbar el host):

      - exit code 137 (128+9 SIGKILL) en contenedores
      - `dmesg | grep -i oom` (si tienes permiso)
      - restart loops en compose
  - id: s7
    tipo: explicacion
    titulo: 3. Runbook corto
    xp: 10
    cuerpo: >-
      Pasos si Vitrina cae por memoria: mirar RSS, logs PG, bajar concurrency,
      subir RAM o limitar cgroup.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/oom-ulimit.md` con `ulimit -a` anotado y escenarios OOM.'
      - 'Lista de síntomas (exit 137, dmesg OOM, contenedor reiniciando).'
      - 'Commit `docs(m11): l07 oom ulimit`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — OOM, ulimit y síntomas

**~5.0 h · Semana 2**

Cuando el kernel mata tu API, el síntoma parece “se reinició solo”. Hoy lo reconoces.

## Objetivo

Documentar límites (`ulimit`) y la firma de un OOM.

## Pasos

### 1. ulimit (30 min)

```bash
ulimit -a
ulimit -n
```

Anota open files y qué pasaría si la API abre demasiados sockets.

### 2. Señales OOM (60 min)

En `labs/oom-ulimit.md` documenta (sin tumbar el host):

- exit code 137 (128+9 SIGKILL) en contenedores
- `dmesg | grep -i oom` (si tienes permiso)
- restart loops en compose

### 3. Runbook corto (40 min)

Pasos si Vitrina cae por memoria: mirar RSS, logs PG, bajar concurrency, subir RAM o limitar cgroup.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/oom-ulimit.md
git commit -m "docs(m11): l07 oom ulimit"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | OOM killer; ulimit -n/-v; síntomas en logs | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/oom-ulimit.md` con `ulimit -a` anotado y escenarios OOM.
2. Lista de síntomas (exit 137, dmesg OOM, contenedor reiniciando).
3. Commit `docs(m11): l07 oom ulimit`.

## Errores comunes

- Forzar OOM en máquina compartida sin cuidado.
- Ignorar file descriptors (`ulimit -n`) en APIs con muchas conexiones.
- Culpar “Node lento” cuando es thrashing.

## Siguiente

[L08 — cgroups y memoria en contenedores](L08-cgroups-y-memoria-en-contenedores.md)
