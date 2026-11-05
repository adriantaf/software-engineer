---
id: L11
materia: M12
orden: 11
titulo: 'SRS v1, freeze y P3'
horas: 5
semana: 3
lectura: plantilla completa
evidencia: projects/m12-srs/srs-v1.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 y proyecto: el documento que M13/M17 consumen.


      **Objetivo de esta lección:** Publicar `srs-v1.md` congelado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Copiar y pulir
    xp: 10
    cuerpo: >-
      ```bash

      cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md

      ```


      Completa huecos: referencias, supuestos, dependencias (Node, Postgres),
      RNF ≥3, glosario, MoSCoW resumido.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Freeze banner
    xp: 10
    cuerpo: |-
      ```markdown
      > **Freeze v1 — YYYY-MM-DD**  
      > Cambios post-freeze → ADR o srs-v1.1 con diff explícito.
      ```

      Al inicio:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «SRS v1, freeze y P3», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: 'Instalar herramientas al azar sin evidencia de SRS v1, freeze y P3'
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

      `cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md`
    comandoEsperado:
      - cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md'
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
        texto: Publicar `srs-v1.md` congelado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Checklist P3
    xp: 10
    cuerpo: 'README: P1 entrevistas, P2 stories≥8, P3 srs-v1 con RNF.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `srs-v1.md` completo (intro, contexto, RF, RNF≥3 seguridad/privacidad,
        fuera de alcance, glosario).
      - Fecha de freeze y versión v1 anotadas.
      - 'Commit `docs(m12): l11 srs-v1 freeze p3`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — SRS v1, freeze y P3

**~5.0 h · Semana 3**

P3 y proyecto: el documento que M13/M17 consumen.

## Objetivo

Publicar `srs-v1.md` congelado.

## Pasos

### 1. Copiar y pulir (90–120 min)

```bash
cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md
```

Completa huecos: referencias, supuestos, dependencias (Node, Postgres), RNF ≥3, glosario, MoSCoW resumido.

### 2. Freeze banner (20 min)

Al inicio:

```markdown
> **Freeze v1 — YYYY-MM-DD**  
> Cambios post-freeze → ADR o srs-v1.1 con diff explícito.
```

### 3. Checklist P3 (30 min)

README: P1 entrevistas, P2 stories≥8, P3 srs-v1 con RNF.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l11 srs-v1 freeze p3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Freeze: copiar borrador → srs-v1.md; RNF seguridad ≥3 | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `srs-v1.md` completo (intro, contexto, RF, RNF≥3 seguridad/privacidad, fuera de alcance, glosario).
2. Fecha de freeze y versión v1 anotadas.
3. Commit `docs(m12): l11 srs-v1 freeze p3`.

## Errores comunes

- Seguir editando “borrador eterno” sin v1.
- RNF de seguridad ausentes.
- Glosario desalineado con M09/M17.

## Siguiente

[L12 — Revisión M13 y cierre M12](L12-revision-m13-y-cierre-m12.md)
