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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Encapsulación protege invariantes: el exterior no muta estado inválido.


      **Objetivo de esta lección:** Usar `#privado`, `private`, `readonly` donde
      corresponda; exponer API mínima estable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura Handbook
    xp: 10
    cuerpo: 'Classes: parameter properties, `readonly`, private fields.'
  - id: s3
    tipo: ejemplo
    titulo: Auditar superficie pública
    xp: 10
    cuerpo: >-
      Lista cada export: ¿debe ser público? Reduce exports en `index.ts` si
      creaste barrel.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Encapsulación en TypeScript», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: No hay acceso directo a estructuras mutables desde fuera del módulo.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Encapsulación en
          TypeScript
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
    pregunta: '¿Es recomendable en esta lección? “`public items: Libro[]` exportado."'
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
        texto: >-
          Usar `#privado`, `private`, `readonly` donde corresponda; exponer API
          mínima estable.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Implementación
    xp: 10
    cuerpo: >-
      - Colección interna no expuesta como array mutable. - Métodos `agregar`,
      `buscar`, no `items.push` desde fuera.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - No hay acceso directo a estructuras mutables desde fuera del módulo.
      - Tests pasan usando solo API pública.
      - Documentaste decisiones de visibilidad.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
