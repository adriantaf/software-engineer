---
id: L08
materia: M15
orden: 8
titulo: IDOR y roles — casos 403
horas: 5
semana: 2
lectura: IDOR; autorización por dueño/rol
evidencia: tests HTTP 403 IDOR + rol insuficiente
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Hilo seguridad: el piloto single-tenant aún puede tener IDOR entre
      usuarios/roles.


      **Objetivo de esta lección:** Automatizar 403 (P1 capa API completa).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`test(m15): idor y roles 403`'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «IDOR y roles — casos 403», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de IDOR y roles — casos
          403
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Devolver 200 con body vacío (silencio
      peligroso sin política)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: Automatizar 403 (P1 capa API completa).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: >-
      ¿Debes hacer esto? “Mensajes que revelan existencia de recurso ajeno sin
      decisión consciente."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Test: usuario A no lee/modifica pedido de B → 403 (o 404 documentado).'
      - 'Test: rol insuficiente → 403.'
      - 'Commit `test(m15): idor y roles 403`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — IDOR y roles — casos 403

**~5.0 h · Semana 2**

Hilo seguridad: el piloto single-tenant aún puede tener IDOR entre usuarios/roles.

## Objetivo

Automatizar 403 (P1 capa API completa).

## Pasos (hazlos en orden)

### 1. Fixtures de dos usuarios (40 min)

### 2. Tests IDOR + rol (80–100 min)

### 3. Actualiza piramide.md (20 min)

### 4. Commit

`test(m15): idor y roles 403`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | 403: IDOR de pedido ajena y rol staff vs owner | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Test: usuario A no lee/modifica pedido de B → 403 (o 404 documentado).
2. Test: rol insuficiente → 403.
3. Commit `test(m15): idor y roles 403`.

## Errores comunes

- Devolver 200 con body vacío (silencio peligroso sin política).
- Mensajes que revelan existencia de recurso ajeno sin decisión consciente.
- Solo test de UI ocultando botón.

## Siguiente

[L09 — Workflow GitHub Actions — esqueleto](L09-workflow-github-actions-esqueleto.md)
