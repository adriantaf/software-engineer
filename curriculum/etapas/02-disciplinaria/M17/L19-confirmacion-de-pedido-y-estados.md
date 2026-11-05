---
id: L19
materia: M17
orden: 19
titulo: Confirmación de pedido y estados
horas: 5
semana: 5
lectura: Flujo estado pedido
evidencia: campo estado + UI
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Estados confirmada/pendiente/cancelada visibles y coherentes
      API↔UI.


      - estado

      - sincronización

      - cancelación
  - id: s2
    tipo: ejemplo
    titulo: 1. Estados de pedido
    xp: 10
    cuerpo: |-
      ```sql
      -- enum o check: pendiente | confirmada | cancelada | atendida
      ALTER TABLE pedidos ADD COLUMN estado TEXT NOT NULL DEFAULT 'pendiente';
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Confirmación de pedido y estados" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: campo estado + UI
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Estados libres sin check/enum."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. UI + tests
    xp: 10
    cuerpo: >-
      ```bash

      curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/pedidos/<id>/estado
      \
        -H 'content-type: application/json' \
        -d '{"estado":"confirmada"}'
      npm test -- pedidos

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina
      git commit -m "feat(m17): L19 confirmacion estados pedido"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Campo/enum `estado` en pedidos + PATCH autenticado; tests verdes.
      - 'Commit `docs(m17): L19 confirmacion-de-pedido-y-estados`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L19 — Confirmación de pedido y estados

**~5.0 h · Semana 5**

Staff y owner deben ver el mismo estado.

## Objetivo

Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.

## Conceptos clave

- estado
- sincronización
- cancelación

## Pasos (hazlos en orden)

### 1. Estados de pedido (60–80 min)

```sql
-- enum o check: pendiente | confirmada | cancelada | atendida
ALTER TABLE pedidos ADD COLUMN estado TEXT NOT NULL DEFAULT 'pendiente';
```

API PATCH `/pedidos/:id/estado` con authz.

### 2. UI + tests (50–60 min)

```bash
curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/pedidos/<id>/estado \
  -H 'content-type: application/json' \
  -d '{"estado":"confirmada"}'
npm test -- pedidos
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L19 confirmacion estados pedido"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Flujo estado pedido | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Campo/enum `estado` en pedidos + PATCH autenticado; tests verdes.
2. Commit `docs(m17): L19 confirmacion-de-pedido-y-estados`.

## Errores comunes

- Estados libres sin check/enum.
- Transiciones sin authz.

## Siguiente

[L20 — Cierre P3 integración WhatsApp](L20-cierre-p3-integracion-whatsapp.md)
