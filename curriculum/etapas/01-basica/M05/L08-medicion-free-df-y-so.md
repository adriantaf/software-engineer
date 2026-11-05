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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana 2 observando la máquina mientras corre software, no solo
      leyendo diagramas.


      **Objetivo de esta lección:** Registrar mediciones repetibles de memoria y
      disco; correlacionar con procesos Node; redactar conclusiones sobre RAM vs
      almacenamiento en **tu** entorno.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Protocolo de medición
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m05-como-corre/
      git commit -m "docs(m05): mediciones semana 2 memoria y disco"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Baseline
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m05-como-corre/
      git commit -m "docs(m05): mediciones semana 2 memoria y disco"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Medición: free, df y observación del SO», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `mediciones-semana2.md` con protocolo, ≥3 repeticiones donde aplique,
          y síntesis.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Medición: free, df y
          observación del SO
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

      `git add projects/m05-como-corre/`
    comandoEsperado:
      - git add projects/m05-como-corre/
      - 'git commit -m "docs(m05): mediciones semana 2 memoria y disco"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m05-como-corre/'
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
          Registrar mediciones repetibles de memoria y disco; correlacionar con
          procesos Node; redactar conclusiones sobre RAM vs almacenamiento en tu
          entorno.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Carga controlada
    xp: 10
    cuerpo: >-
      Ejecuta un script que: 1. Asigne un arreglo grande en memoria (como L05).
      2. Escriba un archivo temporal grande en `projects/m05-como-corre/tmp/`
      (luego bórralo). Antes, durante y después, anota `free` y espacio en
      disco. Interpreta.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
