---
id: L11
materia: M26
orden: 11
titulo: Staff y permisos mínimos
horas: 5
semana: 3
lectura: authz matrix
evidencia: projects/m26-capstone/memoria/roles.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Roles staff/owner mínimos documentados y aplicados.


      M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de
      tutoriales.


      Conceptos que debes poder explicar al cerrar:


      - Staff vs owner
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer
      $TOKEN_STAFF_A" \
        "$API/tenants/$TENANT_A"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Staff y permisos mínimos" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m26-capstone/memoria/roles.md
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


      `curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer
      $TOKEN_STAFF_A" \`
    comandoEsperado:
      - >-
        curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer
        $TOKEN_STAFF_A" \
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer
      $TOKEN_STAFF_A" \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Roles staff/owner mínimos documentados y aplicados.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Define roles mínimos
    xp: 10
    cuerpo: >-
      En `projects/m26-capstone/memoria/roles.md`: `owner` vs `staff` — permisos
      allow/deny (≥8 filas).
  - id: s7
    tipo: ejemplo
    titulo: 3. Aplica y prueba
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer
      $TOKEN_STAFF_A" \
        "$API/tenants/$TENANT_A"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m26-capstone/memoria/roles.md`.
      - Commit en git con mensaje docs(m26).
      - Bitácora de la semana actualizada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Staff y permisos mínimos

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/roles.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Roles staff/owner mínimos documentados y aplicados.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Staff vs owner

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _authz matrix_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Define roles mínimos (25–35 min)

En `projects/m26-capstone/memoria/roles.md`: `owner` vs `staff` — permisos allow/deny (≥8 filas).

### 3. Aplica y prueba (100–120 min)

Invite/crea staff en tenant A. Prueba acción prohibida (p.ej. borrar negocio / ver billing).

```bash
curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer $TOKEN_STAFF_A" \
  "$API/tenants/$TENANT_A"
```

Espera 403. Documenta.

### 4. Test authz (30–40 min)

Al menos un test automatizado o script documentado en CI local. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l11 staff-y-permisos-m-nimos"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | authz matrix | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/roles.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L12 — Tests regresión flujos críticos](L12-tests-regresion-flujos-criticos.md)
