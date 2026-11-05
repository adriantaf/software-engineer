---
id: L10
materia: M26
orden: 10
titulo: Menú por tenant
horas: 5
semana: 3
lectura: Modelo dominio Vitrina
evidencia: projects/m26-capstone/memoria/menu-por-tenant.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Categorías e ítems de menú scoped por tenant; perfil público
      solo muestra el menú del tenant resuelto.


      El menú es el producto principal de Vitrina. Sin aislamiento aquí, el
      resto del SaaS no importa.


      Conceptos que debes poder explicar al cerrar:


      - Catálogo por tenant

      - Disponibilidad

      - Resolución de tenant en URL pública (`/t/:slug` o subdominio)
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"

      # crear ítem en A; intentar leerlo con TOKEN_B → 403/404

      curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_B"
      "$API/menu/items/$ITEM_A"

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Menú por tenant" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m26-capstone/memoria/menu-por-tenant.md
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

      `curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"`
    comandoEsperado:
      - 'curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Categorías e ítems de menú scoped por tenant; perfil público solo
          muestra el menú del tenant resuelto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Matriz
    xp: 10
    cuerpo: 'En `memoria/menu-por-tenant.md`: create/update/list ítems × tenant A/B.'
  - id: s7
    tipo: ejemplo
    titulo: 3. Verifica aislamiento
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"

      # crear ítem en A; intentar leerlo con TOKEN_B → 403/404

      curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_B"
      "$API/menu/items/$ITEM_A"

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Menú CRUD por tenant con evidencia HTTP.
      - Perfil público A ≠ menú B.
      - Memoria en git.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Menú por tenant

**~5 h · Semana 3**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/menu-por-tenant.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Categorías e ítems de menú scoped por tenant; perfil público solo muestra el menú del tenant resuelto.

## Por qué empieza así

El menú es el producto principal de Vitrina. Sin aislamiento aquí, el resto del SaaS no importa.

Conceptos que debes poder explicar al cerrar:

- Catálogo por tenant
- Disponibilidad
- Resolución de tenant en URL pública (`/t/:slug` o subdominio)

## Pasos (hazlos en orden)

### 1. Lectura (30 min)

Relee [producto-saas](../../../producto-saas.md) — sección MVP menú.

### 2. Matriz (25 min)

En `memoria/menu-por-tenant.md`: create/update/list ítems × tenant A/B.

### 3. Verifica aislamiento (100–130 min)

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"
# crear ítem en A; intentar leerlo con TOKEN_B → 403/404
curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_B" "$API/menu/items/$ITEM_A"
```

Perfil público del tenant A no lista ítems de B.

### 4. Commit (15 min)

```bash
git add projects/m26-capstone/memoria/menu-por-tenant.md
git commit -m "docs(m26): l10 menu-por-tenant"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| producto-saas + egreso | Menú aislado | [egreso](../../../egreso.md) |
| Catálogo | M26 | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

1. Menú CRUD por tenant con evidencia HTTP.
2. Perfil público A ≠ menú B.
3. Memoria en git.

## Errores comunes

- Menú global sin `tenant_id`.
- Soft-delete sin filtrar en el perfil público.

## Siguiente

[L11 — Staff y permisos mínimos](L11-staff-y-permisos-minimos.md)
