---
id: L07
materia: M12
orden: 7
titulo: 'Historias de vacío, duplicados y conflicto'
horas: 5
semana: 2
lectura: Casos borde negocio pedidos
evidencia: stories.md ampliado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Ampliar `stories.md` hacia ≥8 con casos de borde del
      dominio.


      El piloto se rompe en los bordes. Hoy los conviertes en stories.
  - id: s2
    tipo: ejemplo
    titulo: 1. Brainstorm bordes
    xp: 10
    cuerpo: |-
      ```text
      When intento crear pedido que solapa servicio+recurso
      Then API responde 409 y no persiste
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Historias de vacío, duplicados y conflicto" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: stories.md ampliado
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Solo happy path."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Ampliar `stories.md` hacia ≥8 con casos de borde del dominio.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe stories
    xp: 10
    cuerpo: |-
      Cada una con criterios. Ejemplo conflicto:

      ```text
      When intento crear pedido que solapa servicio+recurso
      Then API responde 409 y no persiste
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Conteo P2
    xp: 10
    cuerpo: Cuenta stories con criterios; anota cuántas faltan para ≥8.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        ≥3 stories nuevas de borde (vacío/duplicado/conflicto/pedido
        abandonado).
      - Total de stories camino a ≥8 (completa faltantes si hace falta).
      - 'Commit `docs(m12): l07 stories borde`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Historias de vacío, duplicados y conflicto

**~5.0 h · Semana 2**

El piloto se rompe en los bordes. Hoy los conviertes en stories.

## Objetivo

Ampliar `stories.md` hacia ≥8 con casos de borde del dominio.

## Pasos

### 1. Brainstorm bordes (40 min)

Lista: agenda vacía, slot ocupado, cliente duplicado por teléfono, cancelación tardía, pedido abandonado, nota privada, staff sin permiso.

### 2. Escribe stories (90 min)

Cada una con criterios. Ejemplo conflicto:

```text
When intento crear pedido que solapa servicio+recurso
Then API responde 409 y no persiste
```

### 3. Conteo P2 (20 min)

Cuenta stories con criterios; anota cuántas faltan para ≥8.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l07 stories borde"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Agenda vacía, cliente duplicado, conflicto de horario, pedido abandonado | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥3 stories nuevas de borde (vacío/duplicado/conflicto/pedido abandonado).
2. Total de stories camino a ≥8 (completa faltantes si hace falta).
3. Commit `docs(m12): l07 stories borde`.

## Errores comunes

- Solo happy path.
- Conflicto de horario sin regla explícita.
- Duplicados de cliente sin criterio de match (teléfono/nombre).

## Siguiente

[L08 — RNF seguridad, privacidad y P2](L08-rnf-seguridad-privacidad-y-p2.md)
