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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Publicar `srs-v1.md` congelado.

      P3 y proyecto: el documento que M13/M17 consumen.
  - id: s2
    tipo: ejemplo
    titulo: 1. Copiar y pulir
    xp: 10
    cuerpo: |-
      ```bash
      cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "SRS v1, freeze y P3" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m12-srs/srs-v1.md
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

      `cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md`
    comandoEsperado:
      - cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Publicar `srs-v1.md` congelado.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Freeze banner
    xp: 10
    cuerpo: |-
      Al inicio:

      ```markdown
      > **Freeze v1 — YYYY-MM-DD**  
      > Cambios post-freeze → ADR o srs-v1.1 con diff explícito.
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Checklist P3
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
