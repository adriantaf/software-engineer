---
id: L01
materia: M25
orden: 1
titulo: Inventario de activos SaaS prod y staging
horas: 5
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/inventario.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Listar URLs, repos, DB, colas, webhooks Stripe, CI y
      clasificar sin secretos.


      M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.


      Conceptos que debes poder explicar al cerrar:


      - Superficie de ataque

      - Staging ≠ prod

      - Activo sin dueño = riesgo
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p
      projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Inventario de activos SaaS prod y staging" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m25-ciber/inventario.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `mkdir -p
      projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}`
    comandoEsperado:
      - >-
        mkdir -p
        projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: mkdir -p
      projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Listar URLs, repos, DB, colas, webhooks Stripe, CI y clasificar sin
          secretos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Crea carpetas de evidencia
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p
      projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}

      ```


      Lee `projects/m25-ciber/README.md` y anota URLs de staging/prod que ya
      tengas (M19).
  - id: s7
    tipo: explicacion
    titulo: 3. Inventario sin secretos
    xp: 10
    cuerpo: >-
      Crea `projects/m25-ciber/inventario.md` con tabla:


      | Activo | Tipo | Ambiente | Dueño | Notas |

      |--------|------|----------|-------|-------|


      Incluye ≥8 filas: API Vitrina, panel, Postgres, dominio, CI, webhook
      Stripe, storage/backups, repo. **Sin** passwords ni API keys.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/inventario.md`.'
      - Sin secretos en markdown.
      - Conexión Vitrina escrita en bitácora.
      - 'Commit `docs(m25): l01 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Inventario de activos SaaS prod y staging

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/inventario.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Listar URLs, repos, DB, colas, webhooks Stripe, CI y clasificar sin secretos.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- Superficie de ataque
- Staging ≠ prod
- Activo sin dueño = riesgo

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Crea carpetas de evidencia (15–20 min)

```bash
mkdir -p projects/m25-ciber/{aislamiento,review,hardening,logging,abuso,alertas,privacidad,tabletop,hallazgos,bitacora}
```

Lee `projects/m25-ciber/README.md` y anota URLs de staging/prod que ya tengas (M19).

### 3. Inventario sin secretos (90–120 min)

Crea `projects/m25-ciber/inventario.md` con tabla:

| Activo | Tipo | Ambiente | Dueño | Notas |
|--------|------|----------|-------|-------|

Incluye ≥8 filas: API Vitrina, panel, Postgres, dominio, CI, webhook Stripe, storage/backups, repo. **Sin** passwords ni API keys.

### 4. Marca superficie de ataque (40–50 min)

Añade sección **Superficie** con 5 endpoints o entradas de datos (login, pedidos CRUD, webhooks, exports). Bitácora `bitacora/semana-01.md` con 5 líneas.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l01 inventario-de-activos-saas-prod-y-stagin"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/inventario.md`.
2. Sin secretos en markdown.
3. Conexión Vitrina escrita en bitácora.
4. Commit `docs(m25): l01 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — Clasificación de datos por tenant](L02-clasificacion-de-datos-por-tenant.md)
