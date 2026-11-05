---
id: L08
materia: M05
orden: 8
titulo: 'Medición: free, df y observación del SO'
horas: 5
semana: 2
lectura: Apuntes semana 2 + man free/df o documentación equivalente
evidencia: projects/m05-como-corre/mediciones-semana2.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Registrar mediciones repetibles de memoria y disco;
      correlacionar con procesos Node; redactar conclusiones sobre RAM vs
      almacenamiento en **tu** entorno.


      Cierras la semana 2 observando la máquina mientras corre software, no solo
      leyendo diagramas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Protocolo de medición
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m05-como-corre/
      git commit -m "docs(m05): mediciones semana 2 memoria y disco"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Medición: free, df y observación del SO" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m05-como-corre/mediciones-semana2.md
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

      `git add projects/m05-como-corre/`
    comandoEsperado:
      - git add projects/m05-como-corre/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m05-como-corre/'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Registrar mediciones repetibles de memoria y disco; correlacionar con
          procesos Node; redactar conclusiones sobre RAM vs almacenamiento en *…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Baseline
    xp: 10
    cuerpo: 'Con el sistema idle, captura memoria y disco. Pega salidas recortadas.'
  - id: s7
    tipo: explicacion
    titulo: 3. Carga controlada
    xp: 10
    cuerpo: >-
      Ejecuta un script que:


      1. Asigne un arreglo grande en memoria (como L05).

      2. Escriba un archivo temporal grande en `projects/m05-como-corre/tmp/`
      (luego bórralo).


      Antes, durante y después, anota `free` y espacio en disco. Interpreta.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `mediciones-semana2.md` con protocolo, ≥3 repeticiones donde aplique, y
        síntesis.
      - Commit con evidencia de la semana 2.
      - Puedes explicar RAM vs disco sin usar la palabra “magia”.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Medición: `free`, `df` y observación del SO

**~5 h · Semana 2**

Cierras la semana 2 observando la máquina mientras corre software, no solo leyendo diagramas.

## Objetivo

Registrar mediciones repetibles de memoria y disco; correlacionar con procesos Node; redactar conclusiones sobre RAM vs almacenamiento en **tu** entorno.

## Pasos

### 1. Protocolo de medición (45 min)

En `mediciones-semana2.md` define:

- SO y hardware (CPU cores, RAM total, tipo disco si lo sabes).
- Herramientas: `free -h`, `df -h`, `ps`, `htop`/`top`.
- Regla: cada medición **≥3 repeticiones**; anotar min/med/max o rango.

### 2. Baseline (60 min)

Con el sistema idle, captura memoria y disco. Pega salidas recortadas.

### 3. Carga controlada (90 min)

Ejecuta un script que:

1. Asigne un arreglo grande en memoria (como L05).
2. Escriba un archivo temporal grande en `projects/m05-como-corre/tmp/` (luego bórralo).

Antes, durante y después, anota `free` y espacio en disco. Interpreta.

### 4. Síntesis semana 2 (60 min)

Sección **“En mis palabras”**: RAM vs disco, caché, page cache — 2 párrafos académicos.

### 5. Commit (15 min)

```bash
git add projects/m05-como-corre/
git commit -m "docs(m05): mediciones semana 2 memoria y disco"
```

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Man pages | `free`, `df` |
| Tus L05–L07 | Apuntes en `projects/m05-como-corre/` |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. `mediciones-semana2.md` con protocolo, ≥3 repeticiones donde aplique, y síntesis.
2. Commit con evidencia de la semana 2.
3. Puedes explicar RAM vs disco sin usar la palabra “magia”.

## Errores comunes

- Pegar megabytes de salida sin interpretación.
- No borrar archivos temporales gigantes del repo.

## Siguiente

[L09 — Binario, hex y conversiones](L09-binario-hex-y-conversiones.md)
