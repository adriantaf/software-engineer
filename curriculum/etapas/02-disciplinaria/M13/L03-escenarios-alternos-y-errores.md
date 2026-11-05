---
id: L03
materia: M13
orden: 3
titulo: Escenarios alternos y errores
horas: 5
semana: 1
lectura: 'Larman: escenarios alternos; códigos HTTP de auth/validación'
evidencia: casos-de-uso.md con escenarios 401/403/409 por UC críticos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Extender `casos-de-uso.md` con escenarios alternos y de
      error alineados a códigos HTTP.


      M15 pedirá tests 401/403/409. Si el diseño no nombra esos caminos, los
      tests inventarán comportamiento.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige 3 UC críticos
    xp: 10
    cuerpo: >-
      ```markdown

      ### UC-03 Crear pedido


      **Feliz:** Staff autenticado, slot libre, cliente existente → 201 +
      pedido.


      **A1 — Sin autenticación:** sin cookie → **401**. No revelar si el slot
      existe.


      **A2 — Rol insuficiente:** si defines “solo owner cancela”, staff →
      **403**.


      **A3 — Conflicto de horario:** mismo slot → **409** con mensaje genérico.


      **A4 — Input inválido:** `fin < inicio` o servicio inexistente → **400** +
      campos.


      **Datos que NUNCA van en el mensaje:** emails de otros clientes, IDs
      internos de otro negocio.

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Escenarios alternos y errores" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: casos-de-uso.md con escenarios 401/403/409 por UC críticos
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Mezclar 401 (no autenticado) con 403
      (autenticado sin permiso)."
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
        texto: >-
          Extender `casos-de-uso.md` con escenarios alternos y de error
          alineados a códigos HTTP.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Plantilla por UC
    xp: 10
    cuerpo: |-
      Para cada uno, añade bajo el caso:

      ```markdown
  - id: s7
    tipo: explicacion
    titulo: UC-03 Crear pedido
    xp: 10
    cuerpo: >-
      **Feliz:** Staff autenticado, slot libre, cliente existente → 201 +
      pedido.


      **A1 — Sin autenticación:** sin cookie → **401**. No revelar si el slot
      existe.


      **A2 — Rol insuficiente:** si defines “solo owner cancela”, staff →
      **403**.


      **A3 — Conflicto de horario:** mismo slot → **409** con mensaje genérico.


      **A4 — Input inválido:** `fin < inicio` o servicio inexistente → **400** +
      campos.


      **Datos que NUNCA van en el mensaje:** emails de otros clientes, IDs
      internos de otro negocio.

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Al menos 3 UC críticos tienen escenario feliz + ≥2 alternos/error
        documentados.
      - >-
        Cada error nombra código HTTP esperado (401/403/400/409) y mensaje *sin*
        filtrar datos ajenos.
      - 'Commit `docs(m13): escenarios alternos y errores en casos de uso`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Escenarios alternos y errores

**~5.0 h · Semana 1**

El flujo feliz de “crear pedido” es el 20 %. Hoy diseñas el 80 %: sin sesión, sin permiso, slot ocupado, input inválido.

## Objetivo

Extender `casos-de-uso.md` con escenarios alternos y de error alineados a códigos HTTP.

## Por qué importa

M15 pedirá tests 401/403/409. Si el diseño no nombra esos caminos, los tests inventarán comportamiento.

## Pasos (hazlos en orden)

### 1. Elige 3 UC críticos (15 min)

Típico: `UC-01` login, `UC-03` crear pedido, `UC-04` cancelar (o listar agenda).

### 2. Plantilla por UC (90–110 min)

Para cada uno, añade bajo el caso:

```markdown
### UC-03 Crear pedido

**Feliz:** Staff autenticado, slot libre, cliente existente → 201 + pedido.

**A1 — Sin autenticación:** sin cookie → **401**. No revelar si el slot existe.

**A2 — Rol insuficiente:** si defines “solo owner cancela”, staff → **403**.

**A3 — Conflicto de horario:** mismo slot → **409** con mensaje genérico.

**A4 — Input inválido:** `fin < inicio` o servicio inexistente → **400** + campos.

**Datos que NUNCA van en el mensaje:** emails de otros clientes, IDs internos de otro negocio.
```

### 3. Tabla resumen de errores (40–50 min)

Al final de `casos-de-uso.md`:

| UC | Condición | HTTP | Mensaje (idea) |
|----|-----------|------|----------------|
| UC-03 | sin sesión | 401 | “Inicia sesión” |
| UC-03 | slot ocupado | 409 | “Horario no disponible” |

### 4. Revisa contra trust boundaries (20 min)

Abre `diagramas/trust-boundaries.md`: ¿cada error se decide en la **API**, no solo en el front?

### 5. Commit (15 min)

```bash
git add projects/m13-diseno/casos-de-uso.md
git commit -m "docs(m13): escenarios alternos y errores en casos de uso"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Flujos alternos y de error; 401 vs 403 vs 409 en APIs | [MDN — HTTP status codes](https://developer.mozilla.org/es/docs/Web/HTTP/Status) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Al menos 3 UC críticos tienen escenario feliz + ≥2 alternos/error documentados.
2. Cada error nombra código HTTP esperado (401/403/400/409) y mensaje *sin* filtrar datos ajenos.
3. Commit `docs(m13): escenarios alternos y errores en casos de uso`.

## Errores comunes

- Mezclar 401 (no autenticado) con 403 (autenticado sin permiso).
- Mensajes tipo “el cliente X de otro negocio no existe” (filtración).
- Solo escenario feliz: el diseño de M17 fallará en conflictos de horario.

## Siguiente

[L04 — Cierre P1 flujos principales](L04-cierre-p1-flujos-principales.md)
