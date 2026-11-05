---
id: L24
materia: M25
orden: 24
titulo: Security review final y cierre M25
horas: 5
semana: 6
lectura: OWASP Reporting + ficha M25
evidencia: projects/m25-ciber/security-review.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar `security-review.md`; checklist dominio; handoff
      M26.


      M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.


      Conceptos que debes poder explicar al cerrar:


      - Contención

      - Rotación credenciales

      - Post-mortem blameless
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l24 security-review-final-y-cierre-m25"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Security review final y cierre M25" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m25-ciber/security-review.md
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
        texto: Completar `security-review.md`; checklist dominio; handoff M26.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Reúne evidencias P1–P3
    xp: 10
    cuerpo: >-
      Índice en `security-review.md`: inventario, aislamiento (manual+CI), ≥2
      hallazgos cerrados, hardenings, tabletops, runbook.
  - id: s7
    tipo: explicacion
    titulo: 3. Rúbrica y riesgo residual
    xp: 10
    cuerpo: >-
      Tabla de controles: control | evidencia | residual. Declara qué **no**
      está listo para M26 demo pública.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/security-review.md`.'
      - Narrativa ≥30 min equivalente escrita.
      - security-review.md enlaza PRs y tests.
      - 'Commit `docs(m25): l24 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L24 — Security review final y cierre M25

**~5 h · Semana 6**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/security-review.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Completar `security-review.md`; checklist dominio; handoff M26.

## Por qué empieza así

M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.

Conceptos que debes poder explicar al cerrar:

- Contención
- Rotación credenciales
- Post-mortem blameless

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Reporting + ficha M25_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Reúne evidencias P1–P3 (40–50 min)

Índice en `security-review.md`: inventario, aislamiento (manual+CI), ≥2 hallazgos cerrados, hardenings, tabletops, runbook.

### 3. Rúbrica y riesgo residual (80–100 min)

Tabla de controles: control | evidencia | residual. Declara qué **no** está listo para M26 demo pública.

### 4. Handoff M26 (30–40 min)

Sección handoff: issues abiertos, tests obligatorios en CI, secretos a rotar antes de video público.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l24 security-review-final-y-cierre-m25"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Reporting + ficha M25 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/security-review.md`.
2. Narrativa ≥30 min equivalente escrita.
3. security-review.md enlaza PRs y tests.
4. Commit `docs(m25): l24 …` en el historial.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
