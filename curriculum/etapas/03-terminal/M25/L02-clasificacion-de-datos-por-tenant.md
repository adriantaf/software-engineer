---
id: L02
materia: M25
orden: 2
titulo: Clasificación de datos por tenant
horas: 5
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/clasificacion-datos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Etiquetar datos (PII pedidos, credenciales, billing
      metadata) y flujo entre componentes.


      M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.


      Conceptos que debes poder explicar al cerrar:


      - PII mínima

      - tenant_id como control

      - Logs y PII
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l02 clasificaci-n-de-datos-por-tenant"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Clasificación de datos por tenant" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m25-ciber/clasificacion-datos.md
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
        texto: >-
          Etiquetar datos (PII pedidos, credenciales, billing metadata) y flujo
          entre componentes.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario de tipos de dato
    xp: 10
    cuerpo: >-
      En `projects/m25-ciber/clasificacion-datos.md` crea tabla:


      | Tipo | Ejemplos | Tabla/campo (si sabes) | Quién accede | Retención |

      |------|----------|------------------------|--------------|-----------|


      Filas mínimas: PII cliente (nombre/tel), credenciales, `tenant_id`,
      metadata billing Stripe, logs de app, backups.
  - id: s7
    tipo: explicacion
    titulo: 3. Flujos entre componentes
    xp: 10
    cuerpo: |-
      Añade sección **Flujos** con 4 diagramas en prosa (o mermaid):

      1. Login → sesión → `tenant_id`
      2. Crear pedido → DB
      3. Webhook Stripe → actualización plan
      4. Export/soporte → datos salientes

      Marca dónde un leak cruzaría tenants.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/clasificacion-datos.md`.'
      - Sin secretos en markdown.
      - Conexión Vitrina escrita en bitácora.
      - 'Commit `docs(m25): l02 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Clasificación de datos por tenant

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/clasificacion-datos.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Etiquetar datos (PII pedidos, credenciales, billing metadata) y flujo entre componentes.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- PII mínima
- tenant_id como control
- Logs y PII

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Inventario de tipos de dato (25–35 min)

En `projects/m25-ciber/clasificacion-datos.md` crea tabla:

| Tipo | Ejemplos | Tabla/campo (si sabes) | Quién accede | Retención |
|------|----------|------------------------|--------------|-----------|

Filas mínimas: PII cliente (nombre/tel), credenciales, `tenant_id`, metadata billing Stripe, logs de app, backups.

### 3. Flujos entre componentes (90–110 min)

Añade sección **Flujos** con 4 diagramas en prosa (o mermaid):

1. Login → sesión → `tenant_id`
2. Crear pedido → DB
3. Webhook Stripe → actualización plan
4. Export/soporte → datos salientes

Marca dónde un leak cruzaría tenants.

### 4. Reglas de minimización (30–40 min)

Sección **Reglas**: ≥5 bullets (qué no loguear, qué no exportar por defecto, retención demo). Bitácora `bitacora/semana-01.md`.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l02 clasificaci-n-de-datos-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/clasificacion-datos.md`.
2. Sin secretos en markdown.
3. Conexión Vitrina escrita en bitácora.
4. Commit `docs(m25): l02 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L03 — Dos tenants de prueba y mapa de identidades](L03-dos-tenants-de-prueba-y-mapa-de-identidades.md)
