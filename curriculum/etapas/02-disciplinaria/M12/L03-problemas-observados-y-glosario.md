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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Publicar `problemas.md` y `glosario.md` en
      `projects/m12-srs/`.


      Traduces la entrevista a problemas y lenguaje compartido.
  - id: s2
    tipo: ejemplo
    titulo: 1. Extrae problemas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
      git commit -m "docs(m12): l03 problemas y glosario"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Problemas observados y glosario" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: problemas.md y glosario.md
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

      `git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md`
    comandoEsperado:
      - git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/m12-srs/problemas.md
      projects/m12-srs/glosario.md
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Publicar `problemas.md` y `glosario.md` en `projects/m12-srs/`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Glosario
    xp: 10
    cuerpo: >-
      Términos mínimos: Cliente, Servicio, Pedido, No-show, Recordatorio, Staff,
      Owner, Bloqueo de horario, Nota privada, Adelanto (si aplica). Definición
      en 1–2 frases del partner.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
