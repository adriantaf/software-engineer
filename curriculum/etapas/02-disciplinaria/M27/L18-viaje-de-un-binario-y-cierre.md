---
id: L18
materia: M27
orden: 18
titulo: Viaje de un binario y cierre M27
horas: 5
semana: 5
lectura: Síntesis proyecto
evidencia: viaje-binario.md — cierra proyecto M27
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `viaje-binario.md` + README actualizado; checklist P1–P3
      verde.


      Cierras el **proyecto**: el relato completo compile → link → run, con
      puente a M18 y a compiladores (opcional futuro).
  - id: s2
    tipo: ejemplo
    titulo: 1. Escribe el viaje
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m27): cierre viaje de un binario"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Viaje de un binario y cierre M27" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: viaje-binario.md — cierra proyecto M27
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

      `git commit -am "docs(m27): cierre viaje de un binario"`
    comandoEsperado:
      - 'git commit -am "docs(m27): cierre viaje de un binario"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "docs(m27): cierre viaje de un binario"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: '`viaje-binario.md` + README actualizado; checklist P1–P3 verde.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Checklist
    xp: 10
    cuerpo: 'P1 buffers, P2 sanitizer, P3 ABI, proyecto.'
  - id: s7
    tipo: explicacion
    titulo: 3. Simulación
    xp: 10
    cuerpo: 'Otro “yo” solo con README: ¿compila hello?'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`viaje-binario.md` existe y está enlazado.'
      - P1–P3 referenciados.
      - Commit de cierre.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L18 — Viaje de un binario y cierre M27

**~5.0 h · Semana 5**

Cierras el **proyecto**: el relato completo compile → link → run, con puente a M18 y a compiladores (opcional futuro).

## Objetivo

`viaje-binario.md` + README actualizado; checklist P1–P3 verde.

## Pasos

### 1. Escribe el viaje (120 min)

Plantilla del scaffold: pregunta → comandos → asm extracto → diagrama → riesgos → siguiente (compiladores, opcional futuro).

### 2. Checklist (60 min)

P1 buffers, P2 sanitizer, P3 ABI, proyecto.

### 3. Simulación (40 min)

Otro “yo” solo con README: ¿compila hello?

### 4. Commit de cierre (15 min)

```bash
git commit -am "docs(m27): cierre viaje de un binario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Síntesis proyecto | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `viaje-binario.md` existe y está enlazado.
2. P1–P3 referenciados.
3. Commit de cierre.

## Errores comunes

- Informe sin comandos reproducibles.
- Marcar proyecto sin asm ni diagrama.

## Siguiente

Cierra la [ficha M27](../M27-sistemas-bajo-nivel.md). Siguiente en el plan: **M12**. Compiladores quedan como estudio opcional futuro, fuera del catálogo.
