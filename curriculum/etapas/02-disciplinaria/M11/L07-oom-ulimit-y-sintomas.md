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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cuando el kernel mata tu API, el síntoma parece “se reinició solo”. Hoy lo
      reconoces.


      **Objetivo de esta lección:** Documentar límites (`ulimit`) y la firma de
      un OOM.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: ulimit
    xp: 10
    cuerpo: |-
      ```bash
      ulimit -a
      ulimit -n
      ```

      Anota open files y qué pasaría si la API abre demasiados sockets.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Señales OOM
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so/labs/oom-ulimit.md
      git commit -m "docs(m11): l07 oom ulimit"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «OOM, ulimit y síntomas», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: 'Instalar herramientas al azar sin evidencia de OOM, ulimit y síntomas'
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

      `git add projects/m11-so/labs/oom-ulimit.md`
    comandoEsperado:
      - git add projects/m11-so/labs/oom-ulimit.md
      - 'git commit -m "docs(m11): l07 oom ulimit"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m11-so/labs/oom-ulimit.md'
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
        texto: Documentar límites (`ulimit`) y la firma de un OOM.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Runbook corto
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
