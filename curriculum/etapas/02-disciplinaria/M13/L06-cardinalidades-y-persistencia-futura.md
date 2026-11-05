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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Actualizar `diagramas/clases.md` con cardinalidades y un
      mapa clase→tabla coherente con M09.


      Las flechas bonitas mienten si no dices *cuántos*. Hoy fijamos
      multiplicidad y el puente a tablas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Revisa M09 si existe
    xp: 10
    cuerpo: |-
      ```bash
      ls projects/m09-bases-datos/migrations 2>/dev/null
      cat projects/m09-bases-datos/er-vitrina.md 2>/dev/null | head -80
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cardinalidades y persistencia futura" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: clases.md con cardinalidades + nota de tablas/FK
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

      `ls projects/m09-bases-datos/migrations 2>/dev/null`
    comandoEsperado:
      - ls projects/m09-bases-datos/migrations 2>/dev/null
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: ls projects/m09-bases-datos/migrations 2>/dev/null'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Actualizar `diagramas/clases.md` con cardinalidades y un mapa
          clase→tabla coherente con M09.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Anota multiplicidades
    xp: 10
    cuerpo: |-
      Ejemplo piloto:

      | Asociación | Multiplicidad | Regla |
      |------------|---------------|-------|
      | Cliente–Pedido | 1 a * | toda pedido tiene un cliente |
      | Servicio–Pedido | 1 a * | MVP: un servicio por pedido |
      | Usuario–Pedido | 1 a * | quién la creó / staff asignado |

      Actualiza el Mermaid (`"1" --> "*"`).
  - id: s7
    tipo: explicacion
    titulo: 3. Sección persistencia
    xp: 10
    cuerpo: |-
      Añade a `clases.md`:

      ```markdown
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
