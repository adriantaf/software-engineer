---
id: L03
materia: M12
orden: 3
titulo: Problemas observados y glosario
horas: 5
semana: 1
lectura: problemas.md + glosario del dominio
evidencia: problemas.md y glosario.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Traduces la entrevista a problemas y lenguaje compartido.


      **Objetivo de esta lección:** Publicar `problemas.md` y `glosario.md` en
      `projects/m12-srs/`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Extrae problemas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
      git commit -m "docs(m12): l03 problemas y glosario"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Glosario
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
      git commit -m "docs(m12): l03 problemas y glosario"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Problemas observados y glosario», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Problemas observados y
          glosario
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

      `git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md`
    comandoEsperado:
      - git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
      - 'git commit -m "docs(m12): l03 problemas y glosario"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/m12-srs/problemas.md
      projects/m12-srs/glosario.md
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
        texto: Publicar `problemas.md` y `glosario.md` en `projects/m12-srs/`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
      git commit -m "docs(m12): l03 problemas y glosario"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `problemas.md` con ≥6 problemas observados (evidencia → impacto →
        frecuencia).
      - '`glosario.md` con ≥8 términos del dominio alineados al partner.'
      - 'Commit `docs(m12): l03 problemas y glosario`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Problemas observados y glosario

**~5.0 h · Semana 1**

Traduces la entrevista a problemas y lenguaje compartido.

## Objetivo

Publicar `problemas.md` y `glosario.md` en `projects/m12-srs/`.

## Pasos

### 1. Extrae problemas (75 min)

Tabla:

| ID | Problema observado | Evidencia (nota) | Impacto | Frecuencia |
|----|--------------------|------------------|---------|------------|
| P-01 | Doble reserva el sábado | 00:18 | pierde cliente | semanal |

Prohibido: soluciones (“app con calendario”).

### 2. Glosario (60 min)

Términos mínimos: Cliente, Servicio, Pedido, No-show, Recordatorio, Staff, Owner, Bloqueo de horario, Nota privada, Adelanto (si aplica). Definición en 1–2 frases del partner.

### 3. Commit (15 min)

```bash
git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
git commit -m "docs(m12): l03 problemas y glosario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Problema ≠ solución; glosario pedido/servicio/cliente/pedido abandonado | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `problemas.md` con ≥6 problemas observados (evidencia → impacto → frecuencia).
2. `glosario.md` con ≥8 términos del dominio alineados al partner.
3. Commit `docs(m12): l03 problemas y glosario`.

## Errores comunes

- Escribir “necesitan dashboard” como problema.
- Glosario genérico sin el lenguaje del negocio.
- Problemas sin ancla en las notas.

## Siguiente

[L04 — Stakeholders y contexto Vitrina](L04-stakeholders-y-contexto-vitrina.md)
