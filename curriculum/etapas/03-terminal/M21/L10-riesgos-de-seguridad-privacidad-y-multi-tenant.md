---
id: L10
materia: M21
orden: 10
titulo: 'Riesgos de seguridad, privacidad y multi-tenant'
horas: 5
semana: 3
lectura: Hilo seguridad + OWASP ASVS (selecto)
evidencia: projects/m21-proyectos/riesgos.md sección seguridad
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Añadir ≥2 riesgos de seguridad/privacidad (IDOR
      cross-tenant, secretos, backup sin restore) con mitigaciones enlazadas a
      M18/M25.


      Ignorar seguridad hasta M25 es exactamente el anti-patrón del plan.


      Conceptos que debes poder explicar al cerrar:


      - IDOR.

      - Secreto en repo.

      - Restore no probado.

      - Dependencia API LLM (M23).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m21): l10 riesgos-de-seguridad-privacidad-y-multi"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Riesgos de seguridad, privacidad y multi-tenant" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m21-proyectos/riesgos.md sección seguridad
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
          Añadir ≥2 riesgos de seguridad/privacidad (IDOR cross-tenant,
          secretos, backup sin restore) con mitigaciones enlazadas a M18/M25.
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
      Confirma rutas bajo `projects/m21-proyectos`.


      Extiende `projects/m21-proyectos/riesgos.md` con sección **Seguridad y
      privacidad** (≥2 filas).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Para cada uno: **cómo sabrías que ocurrió** y **evidencia de mitigación**
      (test, runbook, issue).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m21-proyectos/riesgos.md sección
        seguridad`.
      - ≥2 riesgos seguridad.
      - Evidencia mitigación citada.
      - Issue enlazado si aplica.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Riesgos de seguridad, privacidad y multi-tenant

**~5 h · Semana 3**

Vitrina se gestiona en el mismo repo. Hoy entregas **`projects/m21-proyectos/riesgos.md sección seguridad`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M21.

## Objetivo

Añadir ≥2 riesgos de seguridad/privacidad (IDOR cross-tenant, secretos, backup sin restore) con mitigaciones enlazadas a M18/M25.

## Por qué empieza así

Ignorar seguridad hasta M25 es exactamente el anti-patrón del plan.

Conceptos que debes poder explicar al cerrar:

- IDOR.
- Secreto en repo.
- Restore no probado.
- Dependencia API LLM (M23).

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) y lee **solo** lo nombrado hoy: _Hilo seguridad + OWASP ASVS (selecto)_.

Subraya 3–5 frases que puedas aplicar en Vitrina (no resúmenes genéricos). Anótalas en `projects/m21-proyectos/bitacora-m21.md` bajo fecha de hoy.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m21-proyectos`.

Extiende `projects/m21-proyectos/riesgos.md` con sección **Seguridad y privacidad** (≥2 filas).

### 3. Laboratorio principal (90–120 min)

Para cada uno: **cómo sabrías que ocurrió** y **evidencia de mitigación** (test, runbook, issue).

### 4. Endurece el entregable (40–60 min)

Cross-ref [hilo seguridad](../../hilos/seguridad.md) y issues M18 si existen.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m21): l10 riesgos-de-seguridad-privacidad-y-multi"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Guía Scrum 2020 (ES) | Hilo seguridad + OWASP ASVS (selecto) | [Scrum Guide 2020 (PDF ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) |
| Catálogo | Entrada de esta materia | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m21-proyectos/riesgos.md sección seguridad`.
2. ≥2 riesgos seguridad.
3. Evidencia mitigación citada.
4. Issue enlazado si aplica.
5. Commit `docs(m21): l10 …` en el historial.

## Errores comunes

- Mitigación ‘confío en el framework’.
- Mezclar riesgo con bug puntual sin impacto.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Tablero vivo, sprints 3–4 y DoD en práctica](L11-tablero-vivo-sprints-3-4-y-dod-en-practica.md)
