---
id: L08
materia: M12
orden: 8
titulo: 'RNF seguridad, privacidad y P2'
horas: 5
semana: 2
lectura: Plantilla RNF + hilo seguridad
evidencia: stories.md + srs-borrador RNF (≥8 stories)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras P2 y metes seguridad en el SRS desde ya
      ([hilo](../../../hilos/seguridad.md)).


      **Objetivo de esta lección:** ≥8 stories + ≥3 RNF de seguridad/privacidad
      trazables.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Completa stories
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): l08 rnf seguridad p2"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: RNF
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): l08 rnf seguridad p2"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «RNF seguridad, privacidad y P2», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de RNF seguridad,
          privacidad y P2
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

      `git add projects/m12-srs`
    comandoEsperado:
      - git add projects/m12-srs
      - 'git commit -m "docs(m12): l08 rnf seguridad p2"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m12-srs'
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
        texto: ≥8 stories + ≥3 RNF de seguridad/privacidad trazables.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README P2
    xp: 10
    cuerpo: Marca P2 listo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`stories.md` tiene ≥8 stories con criterios (P2).'
      - >-
        `srs-borrador.md` incluye ≥3 RNF-SEC/PRIV numerados y enlazados a
        stories.
      - 'Commit `docs(m12): l08 rnf seguridad p2`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — RNF seguridad, privacidad y P2

**~5.0 h · Semana 2**

Cierras P2 y metes seguridad en el SRS desde ya ([hilo](../../../hilos/seguridad.md)).

## Objetivo

≥8 stories + ≥3 RNF de seguridad/privacidad trazables.

## Pasos

### 1. Completa stories (45 min)

Llega a ≥8 con criterios. Índice al inicio de `stories.md`.

### 2. RNF (75 min)

En `srs-borrador.md` §3.2, ejemplos:

| ID | Tipo | Descripción |
|----|------|-------------|
| RNF-SEC-01 | Seguridad | Toda ruta de negocio exige sesión; sin token → 401 |
| RNF-SEC-02 | Autorización | Staff no lee notas privadas → 403 + log |
| RNF-PRIV-01 | Privacidad | PII mínimo; single-tenant documentado |

Enlaza cada RNF a US-xx.

### 3. README P2 (20 min)

Marca P2 listo.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l08 rnf seguridad p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | RNF seguridad/privacidad trazables; single-tenant; 401/403 | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `stories.md` tiene ≥8 stories con criterios (P2).
2. `srs-borrador.md` incluye ≥3 RNF-SEC/PRIV numerados y enlazados a stories.
3. Commit `docs(m12): l08 rnf seguridad p2`.

## Errores comunes

- “Seguridad luego en M18” sin RNF.
- RNF no medibles (“máxima seguridad”).
- Stories sin permisos.

## Siguiente

[L09 — Alcance MVP y MoSCoW](L09-alcance-mvp-y-moscow.md)
