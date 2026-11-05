---
id: L03
materia: M06
orden: 3
titulo: Encapsulación en TypeScript
horas: 5
semana: 1
lectura: 'Handbook TS — Classes (fields private, readonly)'
evidencia: Estado interno privado; tests no acceden a campos internos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Usar `#privado`, `private`, `readonly` donde corresponda;
      exponer API mínima estable.


      Encapsulación protege invariantes: el exterior no muta estado inválido.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura Handbook
    xp: 10
    cuerpo: 'Classes: parameter properties, `readonly`, private fields.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Encapsulación en TypeScript" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Estado interno privado; tests no acceden a campos internos
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
    pregunta: '¿Es buena práctica en esta lección? “`public items: Libro[]` exportado."'
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
          Usar `#privado`, `private`, `readonly` donde corresponda; exponer API
          mínima estable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Auditar superficie pública
    xp: 10
    cuerpo: >-
      Lista cada export: ¿debe ser público? Reduce exports en `index.ts` si
      creaste barrel.
  - id: s7
    tipo: explicacion
    titulo: 3. Implementación
    xp: 10
    cuerpo: |-
      - Colección interna no expuesta como array mutable.
      - Métodos `agregar`, `buscar`, no `items.push` desde fuera.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - No hay acceso directo a estructuras mutables desde fuera del módulo.
      - Tests pasan usando solo API pública.
      - Documentaste decisiones de visibilidad.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Encapsulación en TypeScript

**~5 h · Semana 1**

Encapsulación protege invariantes: el exterior no muta estado inválido.

## Objetivo

Usar `#privado`, `private`, `readonly` donde corresponda; exponer API mínima estable.

## Pasos

### 1. Lectura Handbook (40 min)

Classes: parameter properties, `readonly`, private fields.

### 2. Auditar superficie pública (60 min)

Lista cada export: ¿debe ser público? Reduce exports en `index.ts` si creaste barrel.

### 3. Implementación (120 min)

- Colección interna no expuesta como array mutable.
- Métodos `agregar`, `buscar`, no `items.push` desde fuera.

### 4. Tests solo vía API (90 min)

Reescribe tests que tocaban campos internos. Si necesitas inspección, método `cantidad()` o snapshot de DTO inmutable.

### 5. Nota de diseño (30 min)

En `DOMINIO.md`, sección **Encapsulación**: qué ocultaste y por qué.

## Hecho cuando

1. No hay acceso directo a estructuras mutables desde fuera del módulo.
2. Tests pasan usando solo API pública.
3. Documentaste decisiones de visibilidad.

## Errores comunes

- `public items: Libro[]` exportado.
- `#private` en todo por estética sin criterio.

## Siguiente

[L04 — Nombres y funciones pequeñas (CC 1–3)](L04-nombres-y-funciones-cc-1-3.md)
