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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El menú es el producto principal de Vitrina. Sin aislamiento aquí, el
      resto del SaaS no importa.


      Conceptos que debes poder explicar al cerrar:


      - Catálogo por tenant

      - Disponibilidad

      - Resolución de tenant en URL pública (`/t/:slug` o subdominio)


      **Objetivo de esta lección:** Categorías e ítems de menú scoped por
      tenant; perfil público solo muestra el menú del tenant resuelto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```bash

      curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"

      # crear ítem en A; intentar leerlo con TOKEN_B → 403/404

      curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_B"
      "$API/menu/items/$ITEM_A"

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Matriz
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/memoria/menu-por-tenant.md
      git commit -m "docs(m26): l10 menu-por-tenant"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Menú por tenant», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: Menú CRUD por tenant con evidencia HTTP.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Menú por tenant
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

      `curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"`
    comandoEsperado:
      - 'curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"'
      - >-
        curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_B"
        "$API/menu/items/$ITEM_A"
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -s -H "Authorization: Bearer $TOKEN_A" "$API/menu/items"'
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
          Categorías e ítems de menú scoped por tenant; perfil público solo
          muestra el menú del tenant resuelto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Verifica aislamiento
    xp: 10
    cuerpo: Perfil público del tenant A no lista ítems de B.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Menú CRUD por tenant con evidencia HTTP.
      - Perfil público A ≠ menú B.
      - Memoria en git.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
