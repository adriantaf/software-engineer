---
id: L04
materia: M13
orden: 4
titulo: Cierre P1 flujos principales
horas: 5
semana: 1
lectura: Repaso casos de uso Must; evidencia P1 ficha M13
evidencia: casos-de-uso.md consolidado (P1) + bitácora semana 1
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 de M13 es evidencia: flujos principales del Agenda en un solo archivo
      legible.


      **Objetivo de esta lección:** Consolidar `casos-de-uso.md` y dejar
      bitácora de semana 1 lista para marcar P1.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría Must
    xp: 10
    cuerpo: >-
      ```bash

      # anota a mano o con grep mental

      # ¿Cada historia Must tiene UC-xx?

      ```


      Compara `casos-de-uso.md` vs SRS: Tabla de cobertura al inicio del
      archivo: | Historia SRS | UC | ¿Errores? |
      |--------------|----|-----------| | … | UC-0x | sí/no |
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Limpieza
    xp: 10
    cuerpo: |-
      ```bash
      # anota a mano o con grep mental
      # ¿Cada historia Must tiene UC-xx?
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre P1 flujos principales», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre P1 flujos
          principales
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Marcar P1 en la UI sin el archivo
      consolidado en git."
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
        texto: >-
          Consolidar `casos-de-uso.md` y dejar bitácora de semana 1 lista para
          marcar P1.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Bitácora semana 1
    xp: 10
    cuerpo: >-
      `projects/m13-diseno/bitacora-semana-1.md`: ```markdown # Bitácora M13 —
      Semana 1
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `casos-de-uso.md` cubre historias Must del SRS con actores, UC y errores
        401/403/409 donde aplica.
      - >-
        Existe `projects/m13-diseno/bitacora-semana-1.md` (qué quedó fuera + 1
        decisión).
      - 'Commit `docs(m13): cierre P1 flujos principales`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre P1 flujos principales

**~5.0 h · Semana 1**

P1 de M13 es evidencia: flujos principales del Agenda en un solo archivo legible.

## Objetivo

Consolidar `casos-de-uso.md` y dejar bitácora de semana 1 lista para marcar P1.

## Pasos (hazlos en orden)

### 1. Auditoría Must (50–60 min)

Compara `casos-de-uso.md` vs SRS:

```bash
# anota a mano o con grep mental
# ¿Cada historia Must tiene UC-xx?
```

Tabla de cobertura al inicio del archivo:

| Historia SRS | UC | ¿Errores? |
|--------------|----|-----------|
| … | UC-0x | sí/no |

### 2. Limpieza (40–50 min)

- Elimina UC duplicados o “nice to have” sin traza.
- Unifica nombres (Cliente vs Customer).
- Asegura que login y crear pedido tienen alternos.

### 3. Bitácora semana 1 (40–50 min)

`projects/m13-diseno/bitacora-semana-1.md`:

```markdown
# Bitácora M13 — Semana 1

## Hecho
- Trust boundaries + ADR 001
- Casos de uso Must + errores

## Fuera de alcance (consciente)
- …

## Decisión que sostengo
Monolito modular porque …
```

### 4. Checklist P1 (20 min)

Según ficha: P1 = `casos-de-uso.md` cubriendo Must. Léelo en voz alta 5 minutos: ¿un compañero entiende el piloto?

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre P1 flujos principales"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Cierre de flujos Must; checklist P1 de la ficha M13 | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `casos-de-uso.md` cubre historias Must del SRS con actores, UC y errores 401/403/409 donde aplica.
2. Existe `projects/m13-diseno/bitacora-semana-1.md` (qué quedó fuera + 1 decisión).
3. Commit `docs(m13): cierre P1 flujos principales`.

## Errores comunes

- Marcar P1 en la UI sin el archivo consolidado en git.
- Dejar UC “TBD” en Must.
- Bitácora vacía o solo “avancé”.

## Siguiente

[L05 — Diagrama de clases del dominio](L05-diagrama-de-clases-del-dominio.md)
