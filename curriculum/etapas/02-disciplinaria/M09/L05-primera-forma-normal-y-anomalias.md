---
id: L05
materia: M09
orden: 5
titulo: Primera forma normal y anomalías
horas: 5
semana: 2
lectura: 'Elmasri: 1FN, anomalías de inserción/borrado/actualización'
evidencia: er-vitrina.md sección 1FN + ejemplo de tabla mala descompuesta
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Demostrar una violación de 1FN del dominio y dejar el
      esquema (o el diseño) en 1FN con evidencia escrita.


      - Valor atómico vs lista/repetición en la misma fila.

      - Anomalías de actualización (cambiar un teléfono en N filas).

      - Anomalías de borrado (perder el único dato del cliente al borrar una
      pedido).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): 1FN y anomalias agenda"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Primera forma normal y anomalías" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: er-vitrina.md sección 1FN + ejemplo de tabla mala descompuesta
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

      `git commit -am "docs(m09): 1FN y anomalias agenda"`
    comandoEsperado:
      - 'git commit -am "docs(m09): 1FN y anomalias agenda"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "docs(m09): 1FN y anomalias agenda"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Demostrar una violación de 1FN del dominio y dejar el esquema (o el
          diseño) en 1FN con evidencia escrita.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tabla mala
    xp: 10
    cuerpo: |-
      En `er-vitrina.md` (sección Normalización), pega algo así y **explícalo**:

      | cita_id | cliente | telefonos | servicios |
      |---------|---------|-----------|-----------|
      | 1 | Ana | 646-111, 646-222 | Corte, Barba |

      Señala qué columnas no son atómicas.
  - id: s7
    tipo: explicacion
    titulo: 3. Descomposición
    xp: 10
    cuerpo: >-
      Escribe las tablas resultantes (Cliente, Telefono opcional, Servicio,
      Pedido). Compara con `001_init.sql`: ¿ya estás en 1FN? Si añadiste un
      campo lista, corrígelo con migración o nota de deuda.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Documentas una “tabla Excel” que viola 1FN (teléfonos múltiples o listas
        en una celda).
      - Muestras la descomposición a relaciones atómicas.
      - >-
        Marcas 1FN como cumplida en la tabla de normalización de
        `er-vitrina.md`.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Primera forma normal y anomalías

**~5.0 h · Semana 2**

1FN exige atributos atómicos. Las hojas de Excel del salón casi nunca lo cumplen.

## Objetivo

Demostrar una violación de 1FN del dominio y dejar el esquema (o el diseño) en 1FN con evidencia escrita.

## Conceptos

- Valor atómico vs lista/repetición en la misma fila.
- Anomalías de actualización (cambiar un teléfono en N filas).
- Anomalías de borrado (perder el único dato del cliente al borrar una pedido).

## Pasos

### 1. Lectura (45–60 min)

Capítulo/sección de 1FN y anomalías en Elmasri. Anota definiciones con tus palabras.

### 2. Tabla mala (45 min)

En `er-vitrina.md` (sección Normalización), pega algo así y **explícalo**:

| cita_id | cliente | telefonos | servicios |
|---------|---------|-----------|-----------|
| 1 | Ana | 646-111, 646-222 | Corte, Barba |

Señala qué columnas no son atómicas.

### 3. Descomposición (75 min)

Escribe las tablas resultantes (Cliente, Telefono opcional, Servicio, Pedido). Compara con `001_init.sql`: ¿ya estás en 1FN? Si añadiste un campo lista, corrígelo con migración o nota de deuda.

### 4. Anomalías (40 min)

Una fila de texto por tipo: inserción / actualización / borrado, usando el ejemplo malo.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): 1FN y anomalias agenda"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: 1FN, anomalías de inserción/borrado/actualización | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas una “tabla Excel” que viola 1FN (teléfonos múltiples o listas en una celda).
2. Muestras la descomposición a relaciones atómicas.
3. Marcas 1FN como cumplida en la tabla de normalización de `er-vitrina.md`.

## Errores comunes

- Guardar `telefonos` como `'a,b,c'` en un solo `text` “porque es más fácil”.
- Declarar 1FN sin ejemplo de anomalía.
- Normalizar de oídas sin tocar el ER.

## Siguiente

[L06 — Segunda forma normal](L06-segunda-forma-normal.md)
