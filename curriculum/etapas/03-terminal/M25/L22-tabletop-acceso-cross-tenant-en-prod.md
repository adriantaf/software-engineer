---
id: L22
materia: M25
orden: 22
titulo: Tabletop — acceso cross-tenant en prod
horas: 5
semana: 6
lectura: OWASP Reporting + ficha M25
evidencia: projects/m25-ciber/tabletop/cross-tenant-incident.md
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


      **Objetivo de esta lección:** Simulación: reporte cliente; contención;
      fix.


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
      git commit -m "docs(m25): l22 tabletop-acceso-cross-tenant-en-prod"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Escenario cross-tenant en prod
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l22 tabletop-acceso-cross-tenant-en-prod"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tabletop — acceso cross-tenant en prod», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tabletop — acceso
          cross-tenant en prod
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
        texto: 'Simulación: reporte cliente; contención; fix.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Timeline de contención
    xp: 10
    cuerpo: >-
      T+0 … T+120: verificar, deshabilitar endpoint/feature flag, notificar,
      rotar si aplica, comunicar. Roles: tú = on-call. Sin copiar blog genérico
      — usa tus URLs/servicios.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable:
        `projects/m25-ciber/tabletop/cross-tenant-incident.md`.
      - Narrativa ≥30 min equivalente escrita.
      - security-review.md enlaza PRs y tests.
      - 'Commit `docs(m25): l22 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L22 — Tabletop — acceso cross-tenant en prod

**~5 h · Semana 6**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/tabletop/cross-tenant-incident.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Simulación: reporte cliente; contención; fix.

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

### 2. Escenario cross-tenant en prod (30–40 min)

En `projects/m25-ciber/tabletop/cross-tenant-incident.md`: cliente B reporta ver datos de A. Define detección inicial.

### 3. Timeline de contención (90–110 min)

T+0 … T+120: verificar, deshabilitar endpoint/feature flag, notificar, rotar si aplica, comunicar.

Roles: tú = on-call. Sin copiar blog genérico — usa tus URLs/servicios.

### 4. Acciones y dueños (25–35 min)

Checklist ≥8 acciones con evidencia esperada. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l22 tabletop-acceso-cross-tenant-en-prod"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Reporting + ficha M25 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/tabletop/cross-tenant-incident.md`.
2. Narrativa ≥30 min equivalente escrita.
3. security-review.md enlaza PRs y tests.
4. Commit `docs(m25): l22 …` en el historial.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L23 — Runbook de respuesta incidentes](L23-runbook-de-respuesta-incidentes.md)
