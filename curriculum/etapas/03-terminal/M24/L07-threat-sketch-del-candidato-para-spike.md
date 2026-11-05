---
id: L07
materia: M24
orden: 7
titulo: Threat sketch del candidato para spike
horas: 5
semana: 2
lectura: Webhook security + secret management
evidencia: projects/m24-emergentes/spike/threat-sketch.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Emergente ≠ inseguro por defecto, pero sí suele traer webhooks y tokens
      nuevos.


      Conceptos que debes poder explicar al cerrar:


      - Firma HMAC webhooks

      - PII en mensajes

      - Principio mínimo privilegio


      **Objetivo de esta lección:** Una página de amenazas del integración
      elegida: secretos, replay, PII en payloads, supply chain.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l07 threat-sketch-del-candidato-para-spike"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l07 threat-sketch-del-candidato-para-spike"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Threat sketch del candidato para spike», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Threat sketch del
          candidato para spike
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
          Una página de amenazas del integración elegida: secretos, replay, PII
          en payloads, supply chain.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: 'Lista secretos nuevos (nombres, no valores) en tabla.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m24-emergentes/spike/threat-sketch.md`.'
      - threat-sketch.md ≥1 página.
      - Secretos nombrados sin valores.
      - 'Commit `docs(m24): l07 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Threat sketch del candidato para spike

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/threat-sketch.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Una página de amenazas del integración elegida: secretos, replay, PII en payloads, supply chain.

## Por qué empieza así

Emergente ≠ inseguro por defecto, pero sí suele traer webhooks y tokens nuevos.

Conceptos que debes poder explicar al cerrar:

- Firma HMAC webhooks
- PII en mensajes
- Principio mínimo privilegio

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Webhook security + secret management_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/threat-sketch.md`: actores, datos que cruzan el límite, ≥5 amenazas, mitigaciones previstas en el spike.

### 3. Laboratorio principal (90–120 min)

Lista secretos nuevos (nombres, no valores) en tabla.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l07 threat-sketch-del-candidato-para-spike"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Webhook security + secret management | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/threat-sketch.md`.
2. threat-sketch.md ≥1 página.
3. Secretos nombrados sin valores.
4. Commit `docs(m24): l07 …` en el historial.

## Errores comunes

- Spike sin pensar en replay.
- Loguear payloads con teléfonos reales.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L08 — Plan del spike — hipótesis, alcance y éxito](L08-plan-del-spike-hipotesis-alcance-y-exito.md)
