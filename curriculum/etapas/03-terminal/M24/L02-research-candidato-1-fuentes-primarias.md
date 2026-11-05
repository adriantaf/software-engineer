---
id: L02
materia: M24
orden: 2
titulo: Research candidato 1 — fuentes primarias
horas: 5
semana: 1
lectura: Documentación oficial del candidato 1 (pricing + límites)
evidencia: projects/m24-emergentes/research/candidato-1.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar candidato 1 con enlaces oficiales, pricing,
      regiones, rate limits y al menos una limitación crítica.


      Sin docs del vendor no puedes puntuar seguridad ni costo en la matriz.


      Conceptos que debes poder explicar al cerrar:


      - Rate limits

      - Webhook security

      - Vendor lock-in
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l02 research-candidato-1-fuentes-primarias"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Research candidato 1 — fuentes primarias" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m24-emergentes/research/candidato-1.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar candidato 1 con enlaces oficiales, pricing, regiones, rate
          limits y al menos una limitación crítica.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m24-emergentes/research`.


      Completa `projects/m24-emergentes/research/candidato-1.md` con secciones:
      **Problema**, **Docs**, **Precio**, **Límites**, **Seguridad
      (secretos/webhooks)**, **Crítica**.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: Incluye ≥5 bullets accionables y ≥2 URLs oficiales (no blogs).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m24-emergentes/research/candidato-1.md`.'
      - candidato-1.md completo.
      - ≥1 limitación honesta citada.
      - Sin pegar API keys.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Research candidato 1 — fuentes primarias

**~5 h · Semana 1**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/research/candidato-1.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Documentar candidato 1 con enlaces oficiales, pricing, regiones, rate limits y al menos una limitación crítica.

## Por qué empieza así

Sin docs del vendor no puedes puntuar seguridad ni costo en la matriz.

Conceptos que debes poder explicar al cerrar:

- Rate limits
- Webhook security
- Vendor lock-in

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Documentación oficial del candidato 1 (pricing + límites)_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/research`.

Completa `projects/m24-emergentes/research/candidato-1.md` con secciones: **Problema**, **Docs**, **Precio**, **Límites**, **Seguridad (secretos/webhooks)**, **Crítica**.

### 3. Laboratorio principal (90–120 min)

Incluye ≥5 bullets accionables y ≥2 URLs oficiales (no blogs).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l02 research-candidato-1-fuentes-primarias"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Documentación oficial del candidato 1 (pricing + límites) | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/research/candidato-1.md`.
2. candidato-1.md completo.
3. ≥1 limitación honesta citada.
4. Sin pegar API keys.
5. Commit `docs(m24): l02 …` en el historial.

## Errores comunes

- Solo marketing del vendor.
- Omitir costo por conversación/mensaje.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L03 — Research candidatos 2 y 3](L03-research-candidatos-2-y-3.md)
