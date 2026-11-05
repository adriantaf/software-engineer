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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El piloto se rompe en los bordes. Hoy los conviertes en stories.


      **Objetivo de esta lección:** Ampliar `stories.md` hacia ≥8 con casos de
      borde del dominio.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Brainstorm bordes
    xp: 10
    cuerpo: |-
      ```text
      When intento crear pedido que solapa servicio+recurso
      Then API responde 409 y no persiste
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Escribe stories
    xp: 10
    cuerpo: |-
      ```text
      When intento crear pedido que solapa servicio+recurso
      Then API responde 409 y no persiste
      ```

      Cada una con criterios. Ejemplo conflicto:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Historias de vacío, duplicados y conflicto», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Historias de vacío,
          duplicados y confli…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Solo happy path."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Ampliar `stories.md` hacia ≥8 con casos de borde del dominio.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Conteo P2
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
