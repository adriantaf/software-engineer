---
id: L06
materia: M25
orden: 6
titulo: Review authz — roles staff vs admin
horas: 5
semana: 2
lectura: OWASP — Identity / Authorization testing
evidencia: projects/m25-ciber/review/authz-matrix.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cosmética CSS no salva un leak entre barberías.


      Conceptos que debes poder explicar al cerrar:


      - Authn vs authz

      - tenant_id en sesión

      - Tests de regresión


      **Objetivo de esta lección:** Matriz recurso × rol × tenant; gaps en
      endpoints.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer
      $TOKEN_STAFF" \
        -X DELETE "$API/tenants/$TENANT_A/billing"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Lista recursos y roles
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l06 review-authz-roles-staff-vs-admin"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Review authz — roles staff vs admin», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Review authz — roles
          staff vs admin
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer
      $TOKEN_STAFF" \`
    comandoEsperado:
      - >-
        curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer
        $TOKEN_STAFF" \
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer
      $TOKEN_STAFF" \
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
        texto: Matriz recurso × rol × tenant; gaps en endpoints.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Matriz recurso × rol × tenant
    xp: 10
    cuerpo: >-
      Tabla: | Recurso | owner | staff | cross-tenant | Evidencia |
      |---------|-------|-------|--------------|-----------| Marca allow/deny.
      Prueba ≥2 denegaciones con curl (status esperado 403/404).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/review/authz-matrix.md`.'
      - Evidencia en ruta indicada.
      - 'Si es test: corre en CI o documenta por qué no aún.'
      - 'Commit `docs(m25): l06 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Review authz — roles staff vs admin

**~5 h · Semana 2**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/review/authz-matrix.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Matriz recurso × rol × tenant; gaps en endpoints.

## Por qué empieza así

Cosmética CSS no salva un leak entre barberías.

Conceptos que debes poder explicar al cerrar:

- Authn vs authz
- tenant_id en sesión
- Tests de regresión

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP — Identity / Authorization testing_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Lista recursos y roles (20–30 min)

En `projects/m25-ciber/review/authz-matrix.md` define roles: `owner`, `staff`, (opcional `platform`).

Lista ≥8 recursos/acciones: pedidos CRUD, clientes, servicios, billing, invites, exports.

### 3. Matriz recurso × rol × tenant (100–120 min)

Tabla:

| Recurso | owner | staff | cross-tenant | Evidencia |
|---------|-------|-------|--------------|-----------|

Marca allow/deny. Prueba ≥2 denegaciones con curl (status esperado 403/404).

```bash
curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $TOKEN_STAFF" \
  -X DELETE "$API/tenants/$TENANT_A/billing"
```

### 4. Gaps abiertos (25–35 min)

Sección **Gaps**: issues enlazados. Bitácora semana-02 con 5 líneas.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l06 review-authz-roles-staff-vs-admin"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP — Identity / Authorization testing | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/review/authz-matrix.md`.
2. Evidencia en ruta indicada.
3. Si es test: corre en CI o documenta por qué no aún.
4. Commit `docs(m25): l06 …` en el historial.

## Errores comunes

- 50 hallazgos menores y cero cross-tenant.
- tenant_id solo en frontend.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L07 — Automatizar test cross-tenant en CI](L07-automatizar-test-cross-tenant-en-ci.md)
