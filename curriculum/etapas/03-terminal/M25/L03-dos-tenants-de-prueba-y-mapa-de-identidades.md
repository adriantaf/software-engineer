---
id: L03
materia: M25
orden: 3
titulo: Dos tenants de prueba y mapa de identidades
horas: 5
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/tenants-prueba.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.


      Conceptos que debes poder explicar al cerrar:


      - Tenant de prueba realista

      - Separación de datos

      - No tenant1 genérico


      **Objetivo de esta lección:** Crear tenant A y B con usuarios staff
      distintos; documentar IDs y roles.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo — adapta a tu CLI/API; no pegues tokens
      curl -s -H "Authorization: Bearer $TOKEN" "$API/tenants" | jq '.[].id'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Define dos negocios ficticios
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l03 dos-tenants-de-prueba-y-mapa-de-identida"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dos tenants de prueba y mapa de identidades», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dos tenants de prueba y
          mapa de identid…
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

      `curl -s -H "Authorization: Bearer $TOKEN" "$API/tenants" | jq '.[].id'`
    comandoEsperado:
      - 'curl -s -H "Authorization: Bearer $TOKEN" "$API/tenants" | jq ''.[].id'''
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -H "Authorization: Bearer $TOKEN" "$API/tenants" | jq
      '.[].id'
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
          Crear tenant A y B con usuarios staff distintos; documentar IDs y
          roles.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Crea o anota IDs reales
    xp: 10
    cuerpo: >-
      En staging (preferido) o local con seed: crea tenants A y B. Documenta
      UUIDs/`tenant_id`, user ids, y un recurso de cada uno (`cita_a_id`,
      `cita_b_id`).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/tenants-prueba.md`.'
      - Sin secretos en markdown.
      - Conexión Vitrina escrita en bitácora.
      - 'Commit `docs(m25): l03 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Dos tenants de prueba y mapa de identidades

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/tenants-prueba.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Crear tenant A y B con usuarios staff distintos; documentar IDs y roles.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- Tenant de prueba realista
- Separación de datos
- No tenant1 genérico

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Define dos negocios ficticios (20–30 min)

En `projects/m25-ciber/tenants-prueba.md`:

| Tenant | Negocio | Email staff | Rol | Notas |
|--------|---------|-------------|-----|-------|

Tres filas: A (barbería), B (clínica), opcional owner platform. **Sin** passwords en claro.

### 3. Crea o anota IDs reales (90–110 min)

En staging (preferido) o local con seed: crea tenants A y B.

Documenta UUIDs/`tenant_id`, user ids, y un recurso de cada uno (`cita_a_id`, `cita_b_id`).

```bash
# ejemplo — adapta a tu CLI/API; no pegues tokens
curl -s -H "Authorization: Bearer $TOKEN" "$API/tenants" | jq '.[].id'
```

### 4. Mapa de identidades (30–40 min)

Sección **Mapa**: usuario → roles → tenant. Confirma que A no tiene membership en B. Bitácora semana-01.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l03 dos-tenants-de-prueba-y-mapa-de-identida"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/tenants-prueba.md`.
2. Sin secretos en markdown.
3. Conexión Vitrina escrita en bitácora.
4. Commit `docs(m25): l03 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L04 — Primera prueba manual cross-tenant](L04-primera-prueba-manual-cross-tenant.md)
