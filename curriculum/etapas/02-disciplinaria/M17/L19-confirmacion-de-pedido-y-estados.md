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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - estado

      - sincronización

      - cancelación


      **Objetivo de esta lección:** Estados confirmada/pendiente/cancelada
      visibles y coherentes API↔UI.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Estados de pedido
    xp: 10
    cuerpo: |-
      ```sql
      -- enum o check: pendiente | confirmada | cancelada | atendida
      ALTER TABLE pedidos ADD COLUMN estado TEXT NOT NULL DEFAULT 'pendiente';
      ```

      API PATCH `/pedidos/:id/estado` con authz.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: UI + tests
    xp: 10
    cuerpo: >-
      ```bash

      curl -sS -b /tmp/ao.ck -X PATCH http://localhost:3000/pedidos/<id>/estado
      \
        -H 'content-type: application/json' \
        -d '{"estado":"confirmada"}'
      npm test -- pedidos

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Confirmación de pedido y estados», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Confirmación de pedido
          y estados
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Estados libres sin check/enum."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
