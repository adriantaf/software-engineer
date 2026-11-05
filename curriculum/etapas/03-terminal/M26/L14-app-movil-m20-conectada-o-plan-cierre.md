---
id: L14
materia: M26
orden: 14
titulo: App móvil M20 conectada o plan cierre
horas: 5
semana: 4
lectura: m20-movil README
evidencia: projects/m26-capstone/mobile-gap.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** App móvil M20 conectada a API v1 **o** plan de cierre
      explícito del gap.


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Misma API

      - Staging HTTPS
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # verifica API alcanzable
      curl -sI "$API/health"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "App móvil M20 conectada o plan cierre" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/mobile-gap.md
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

      `curl -sI "$API/health"`
    comandoEsperado:
      - curl -sI "$API/health"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sI "$API/health"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          App móvil M20 conectada a API v1 **o** plan de cierre explícito del
          gap.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Estado móvil M20
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/mobile-gap.md`: ¿APK/app apunta a staging HTTPS?
      ¿misma API v1?
  - id: s7
    tipo: ejemplo
    titulo: 3. Conecta o cierra el gap
    xp: 10
    cuerpo: |-
      ```bash
      # verifica API alcanzable
      curl -sI "$API/health"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/mobile-gap.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L14 — App móvil M20 conectada o plan cierre

**~5 h · Semana 4**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/mobile-gap.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

App móvil M20 conectada a API v1 **o** plan de cierre explícito del gap.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Misma API
- Staging HTTPS

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _m20-movil README_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Estado móvil M20 (25–35 min)

En `projects/m26-capstone/mobile-gap.md`: ¿APK/app apunta a staging HTTPS? ¿misma API v1?

### 3. Conecta o cierra el gap (100–120 min)

**Conectado:** login + listar pedidos desde móvil contra staging; anota build/version.

**Gap:** plan con fecha, qué falta (CORS, auth, store), impacto en egreso.

```bash
# verifica API alcanzable
curl -sI "$API/health"
```

### 4. Decisión explícita (20–30 min)

Una frase: incluido en demo pública / diferido. Bitácora semana-04.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l14 app-m-vil-m20-conectada-o-plan-cierre"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | m20-movil README | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/mobile-gap.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L15 — Métricas M22 en producto](L15-metricas-m22-en-producto.md)
