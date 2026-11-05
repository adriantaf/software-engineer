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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Automatizar 403 (P1 capa API completa).


      Hilo seguridad: el piloto single-tenant aún puede tener IDOR entre
      usuarios/roles.
  - id: s2
    tipo: ejemplo
    titulo: 4. Commit
    xp: 10
    cuerpo: '`test(m15): idor y roles 403`'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "IDOR y roles — casos 403" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: tests HTTP 403 IDOR + rol insuficiente
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
      ¿Es buena práctica en esta lección? “Devolver 200 con body vacío (silencio
      peligroso sin política)."
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
        texto: Automatizar 403 (P1 capa API completa).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Test: usuario A no lee/modifica pedido de B → 403 (o 404 documentado).'
      - 'Test: rol insuficiente → 403.'
      - 'Commit `test(m15): idor y roles 403`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
