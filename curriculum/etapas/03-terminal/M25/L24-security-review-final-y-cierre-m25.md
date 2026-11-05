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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.


      Conceptos que debes poder explicar al cerrar:


      - Contención

      - Rotación credenciales

      - Post-mortem blameless


      **Objetivo de esta lección:** Completar `security-review.md`; checklist
      dominio; handoff M26.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l24 security-review-final-y-cierre-m25"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Reúne evidencias P1–P3
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l24 security-review-final-y-cierre-m25"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Security review final y cierre M25», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Security review final y
          cierre M25
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/'
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
        texto: Completar `security-review.md`; checklist dominio; handoff M26.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M25
    xp: 25
    enunciado: >-
      Cierra **Ciberseguridad aplicada** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Inventario de activos y superficie (prod/staging SaaS)'
      - 'P2: Security review con pruebas cross-tenant obligatorias'
      - 'P3: Tabletop de incidente (.env / fuga) documentado'
      - 'Proyecto: Security review SaaS (aislamiento multi-tenant) + hardening'
      - projects/m25-ciber/security-review.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: 'Existe el entregable: `projects/m25-ciber/security-review.md`.'
      - id: r3
        criterio: Narrativa ≥30 min equivalente escrita.
      - id: r4
        criterio: security-review.md enlaza PRs y tests.
      - id: r5
        criterio: 'Commit `docs(m25): l24 …` en el historial.'
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
    siguiente: Materia M25 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
