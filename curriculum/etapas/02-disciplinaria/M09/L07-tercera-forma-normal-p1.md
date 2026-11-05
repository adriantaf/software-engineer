---
id: L07
materia: M09
orden: 7
titulo: Tercera forma normal (P1)
horas: 5
semana: 2
lectura: 'Elmasri: 3FN / intro BCNF'
evidencia: er-vitrina.md en 3FN — cierra P1
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      3FN elimina dependencias transitivas. Con esto cierras la práctica **P1**.


      **Objetivo de esta lección:** Dejar `er-vitrina.md` en 3FN con
      justificación y enlazarlo como evidencia P1 en el README.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): er en 3FN cierra P1"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Caza transitivas
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): er en 3FN cierra P1"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tercera forma normal (P1)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tercera forma normal
          (P1)
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

      `git commit -am "docs(m09): er en 3FN cierra P1"`
    comandoEsperado:
      - 'git commit -am "docs(m09): er en 3FN cierra P1"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m09): er en 3FN cierra P1"'
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
          Dejar `er-vitrina.md` en 3FN con justificación y enlazarlo como
          evidencia P1 en el README.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Congela el ER 3FN
    xp: 10
    cuerpo: >-
      Actualiza diagrama + tabla de normalización. Añade fecha y una frase: “P1
      lista porque…”.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Documentas al menos una dependencia transitiva evitada o eliminada.
      - Tabla de normalización en `er-vitrina.md` marca 1FN–3FN.
      - README indica que P1 (ER hasta 3FN) está listo.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Tercera forma normal (P1)

**~5.0 h · Semana 2**

3FN elimina dependencias transitivas. Con esto cierras la práctica **P1**.

## Objetivo

Dejar `er-vitrina.md` en 3FN con justificación y enlazarlo como evidencia P1 en el README.

## Pasos

### 1. Lectura (45–60 min)

3FN e intro a BCNF. Diferencia en una frase tuya: 3FN vs BCNF.

### 2. Caza transitivas (60 min)

Ejemplo a analizar: `cliente_id → codigo_postal → ciudad → estado`. Si modelaras dirección completa, ¿qué tablas salen?

Para Vitrina MVP: decide si dirección es necesaria día 1. Si no, escríbelo como fuera de alcance (eso también es diseño).

### 3. Congela el ER 3FN (75 min)

Actualiza diagrama + tabla de normalización. Añade fecha y una frase: “P1 lista porque…”.

### 4. Checklist P1 en README (30 min)

Marca mentalmente (y en texto) que `er-vitrina.md` cumple el criterio de la ficha M09.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): er en 3FN cierra P1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: 3FN / intro BCNF | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas al menos una dependencia transitiva evitada o eliminada.
2. Tabla de normalización en `er-vitrina.md` marca 1FN–3FN.
3. README indica que P1 (ER hasta 3FN) está listo.

## Errores comunes

- Guardar `ciudad` y `estado` redundantes con una tabla de códigos postales a medias.
- Declarar 3FN sin mencionar dependencias transitivas.
- Cerrar P1 sin diagrama actualizado.

## Siguiente

[L08 — Trade-offs de desnormalización](L08-trade-offs-de-desnormalizacion.md)
