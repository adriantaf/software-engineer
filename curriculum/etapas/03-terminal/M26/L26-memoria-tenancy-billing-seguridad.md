---
id: L26
materia: M26
orden: 26
titulo: 'Memoria — tenancy, billing, seguridad'
horas: 5
semana: 7
lectura: secciones P2
evidencia: projects/m26-capstone/memoria/tenancy-billing-seguridad.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Memoria: tenancy + billing + seguridad con evidencias
      enlazadas.


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Narrativa tercero
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m26): l26 memoria-tenancy-billing-seguridad"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Memoria — tenancy, billing, seguridad" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/memoria/tenancy-billing-seguridad.md
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Memoria: tenancy + billing + seguridad con evidencias enlazadas.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Outline de narrativa
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`: H2
      Tenancy | Billing | Seguridad.
  - id: s7
    tipo: explicacion
    titulo: 3. Escribe para un tercero
    xp: 10
    cuerpo: >-
      Cada H2: cómo funciona en **tu** producto + 2 evidencias (path test, URL,
      PR).


      Un mentor debe entender sin tu voz en vivo. Enlaza L03, L17–L20, L21–L24.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L26 — Memoria — tenancy, billing, seguridad

**~5 h · Semana 7**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/tenancy-billing-seguridad.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Memoria: tenancy + billing + seguridad con evidencias enlazadas.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Narrativa tercero

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _secciones P2_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Outline de narrativa (25–35 min)

En `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`: H2 Tenancy | Billing | Seguridad.

### 3. Escribe para un tercero (100–120 min)

Cada H2: cómo funciona en **tu** producto + 2 evidencias (path test, URL, PR).

Un mentor debe entender sin tu voz en vivo. Enlaza L03, L17–L20, L21–L24.

### 4. Pasa el test del screenshot (25–35 min)

Si quitas tu cara del video, ¿el doc basta? Ajusta. Bitácora semana-07.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l26 memoria-tenancy-billing-seguridad"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | secciones P2 | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L27 — Registro comercial M22 y trials](L27-registro-comercial-m22-y-trials.md)
