---
id: L06
materia: M09
orden: 6
titulo: Segunda forma normal
horas: 5
semana: 2
lectura: 'Elmasri: 2FN, dependencia parcial'
evidencia: Ejemplo PK compuesta + eliminación de dependencia parcial
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      2FN elimina dependencias parciales de una clave compuesta. Aunque uses
      UUID, debes saber detectar el antipatrón.


      **Objetivo de esta lección:** Explicar 2FN con un ejemplo del dominio
      (líneas de pedido o staff+día) y justificar por qué tu esquema actual
      cumple o qué cambiarías.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): segunda forma normal"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Caso que viola 2FN
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): segunda forma normal"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Segunda forma normal», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Segunda forma normal
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

      `git commit -am "docs(m09): segunda forma normal"`
    comandoEsperado:
      - 'git commit -am "docs(m09): segunda forma normal"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m09): segunda forma normal"'
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
          Explicar 2FN con un ejemplo del dominio (líneas de pedido o staff+día)
          y justificar por qué tu esquema actual cumple o qué cambiarías.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tu esquema real
    xp: 10
    cuerpo: >-
      Revisa PKs de `001_init.sql`. Con surrogate keys, 2FN suele cumplirse si
      no repites atributos del padre. Confirma por escrito: “no hay atributos
      que dependan de parte de la clave porque…”.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Documentas un caso con PK compuesta que viola 2FN (inventado o
        histórico).
      - Muestras tablas resultantes en 2FN.
      - Actualizas la fila 2FN en `er-vitrina.md`.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Segunda forma normal

**~5.0 h · Semana 2**

2FN elimina dependencias parciales de una clave compuesta. Aunque uses UUID, debes saber detectar el antipatrón.

## Objetivo

Explicar 2FN con un ejemplo del dominio (líneas de pedido o staff+día) y justificar por qué tu esquema actual cumple o qué cambiarías.

## Pasos

### 1. Lectura (45 min)

Dependencia funcional y 2FN en Elmasri.

### 2. Caso que viola 2FN (60 min)

Imagina tabla `cita_detalle` con PK `(cita_id, servicio_id)` y columnas `nombre_servicio`, `precio_serv`. `nombre_servicio` depende solo de `servicio_id` → viola 2FN.

Escríbelo en `er-vitrina.md` con la descomposición correcta (tabla `servicios` + hechos de la pedido).

### 3. Tu esquema real (60 min)

Revisa PKs de `001_init.sql`. Con surrogate keys, 2FN suele cumplirse si no repites atributos del padre. Confirma por escrito: “no hay atributos que dependan de parte de la clave porque…”.

### 4. Mini ejercicio SQL (45 min)

Inserta un servicio y una pedido; actualiza el nombre del servicio; verifica que las pedidos históricas **siguen** viendo el nombre nuevo vía JOIN (trade-off que verás en L08 — snapshot de precio).

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): segunda forma normal"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: 2FN, dependencia parcial | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas un caso con PK compuesta que viola 2FN (inventado o histórico).
2. Muestras tablas resultantes en 2FN.
3. Actualizas la fila 2FN en `er-vitrina.md`.

## Errores comunes

- Decir “ya estoy en 2FN” solo porque usas UUID surrogate sin analizar dependencias.
- Meter `nombre_cliente` en una tabla con PK `(cita_id, servicio_id)` y dejarlo así.
- Confundir 2FN con “tener índices”.

## Siguiente

[L07 — Tercera forma normal (P1)](L07-tercera-forma-normal-p1.md)
