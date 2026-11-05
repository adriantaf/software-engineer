---
id: L06
materia: M13
orden: 6
titulo: Cardinalidades y persistencia futura
horas: 5
semana: 2
lectura: Cardinalidades 1..* / *..*; FK futuras M09
evidencia: clases.md con cardinalidades + nota de tablas/FK
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Las flechas bonitas mienten si no dices *cuántos*. Hoy fijamos
      multiplicidad y el puente a tablas.


      **Objetivo de esta lección:** Actualizar `diagramas/clases.md` con
      cardinalidades y un mapa clase→tabla coherente con M09.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Revisa M09 si existe
    xp: 10
    cuerpo: >-
      ```bash

      ls projects/m09-bases-datos/migrations 2>/dev/null

      cat projects/m09-bases-datos/er-vitrina.md 2>/dev/null | head -80

      ```


      Si no hay M09 aún, asume tablas `usuarios`, `clientes`, `servicios`,
      `orders` como en el scaffold típico.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Anota multiplicidades
    xp: 10
    cuerpo: |-
      ```bash
      ls projects/m09-bases-datos/migrations 2>/dev/null
      cat projects/m09-bases-datos/er-vitrina.md 2>/dev/null | head -80
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cardinalidades y persistencia futura», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cardinalidades y
          persistencia futura
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

      `ls projects/m09-bases-datos/migrations 2>/dev/null`
    comandoEsperado:
      - ls projects/m09-bases-datos/migrations 2>/dev/null
      - cat projects/m09-bases-datos/er-vitrina.md 2>/dev/null | head -80
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: ls projects/m09-bases-datos/migrations 2>/dev/null'
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
          Actualizar `diagramas/clases.md` con cardinalidades y un mapa
          clase→tabla coherente con M09.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Sección persistencia
    xp: 10
    cuerpo: 'Añade a `clases.md`: ```markdown'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Cada asociación en `clases.md` tiene multiplicidad explícita (1, 0..1,
        1..*, *).
      - >-
        Sección “Persistencia futura” mapea clase→tabla y FK (aunque no escribas
        SQL hoy).
      - 'Commit `docs(m13): cardinalidades y mapeo a persistencia`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Cardinalidades y persistencia futura

**~5.0 h · Semana 2**

Las flechas bonitas mienten si no dices *cuántos*. Hoy fijamos multiplicidad y el puente a tablas.

## Objetivo

Actualizar `diagramas/clases.md` con cardinalidades y un mapa clase→tabla coherente con M09.

## Pasos (hazlos en orden)

### 1. Revisa M09 si existe (25–35 min)

```bash
ls projects/m09-bases-datos/migrations 2>/dev/null
cat projects/m09-bases-datos/er-vitrina.md 2>/dev/null | head -80
```

Si no hay M09 aún, asume tablas `usuarios`, `clientes`, `servicios`, `orders` como en el scaffold típico.

### 2. Anota multiplicidades (50–60 min)

Ejemplo piloto:

| Asociación | Multiplicidad | Regla |
|------------|---------------|-------|
| Cliente–Pedido | 1 a * | toda pedido tiene un cliente |
| Servicio–Pedido | 1 a * | MVP: un servicio por pedido |
| Usuario–Pedido | 1 a * | quién la creó / staff asignado |

Actualiza el Mermaid (`"1" --> "*"`).

### 3. Sección persistencia (60–70 min)

Añade a `clases.md`:

```markdown
## Persistencia futura (M09 / M17)

| Clase | Tabla | FK |
|-------|-------|-----|
| Pedido | pedidos | cliente_id, servicio_id, usuario_id |
| … | … | … |

Índices probables: (inicio), (cliente_id), unique parcial anti-doble-booking (decidir en ADR persistencia).
```

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/clases.md
git commit -m "docs(m13): cardinalidades y mapeo a persistencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Multiplicidad en asociaciones; mapeo a FK en PostgreSQL | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Cada asociación en `clases.md` tiene multiplicidad explícita (1, 0..1, 1..*, *).
2. Sección “Persistencia futura” mapea clase→tabla y FK (aunque no escribas SQL hoy).
3. Commit `docs(m13): cardinalidades y mapeo a persistencia`.

## Errores comunes

- Pedido *—* Servicio sin aclarar si una pedido es un solo servicio (MVP).
- Cardinalidades que contradicen el ER de M09.
- “N:N pedidos-servicios” sin tabla puente pensada.

## Siguiente

[L07 — Secuencia: autenticación y sesión](L07-secuencia-autenticacion-y-sesion.md)
