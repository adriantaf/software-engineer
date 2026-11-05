---
id: L12
materia: M06
orden: 12
titulo: Generics en APIs del dominio
horas: 5
semana: 3
lectura: 'Repaso Generics + Handbook Utility Types (Partial, Pick)'
evidencia: API exportada tipada; semana 3 cerrada con commit
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras semana 3 integrando generics en la superficie pública que
      consumirá tu librería (semana 5).


      **Objetivo de esta lección:** Diseñar tipos exportados estables
      (`CrearLibroInput`, `Pagina<T>`) usando generics y utility types donde
      aporten.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura utility types
    xp: 10
    cuerpo: |-
      ```ts
      export interface Pagina<T> {
        items: T[];
        total: number;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: DTOs de entrada/salida
    xp: 10
    cuerpo: |-
      ```ts
      export interface Pagina<T> {
        items: T[];
        total: number;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Generics en APIs del dominio», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: '`src/index.ts` exporta API coherente y documentada.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Generics en APIs del
          dominio
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
    pregunta: ¿Es recomendable en esta lección? “Exportar todo el interior del dominio."
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
          Diseñar tipos exportados estables (`CrearLibroInput`, `Pagina<T>`)
          usando generics y utility types donde aporten.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Paginación o lista genérica
    xp: 10
    cuerpo: |-
      ```ts
      export interface Pagina<T> {
        items: T[];
        total: number;
      }
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`src/index.ts` exporta API coherente y documentada.'
      - Generics aparecen donde evitan duplicación real.
      - Tests de contratos públicos.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Generics en APIs del dominio

**~5 h · Semana 3**

Cierras semana 3 integrando generics en la superficie pública que consumirá tu librería (semana 5).

## Objetivo

Diseñar tipos exportados estables (`CrearLibroInput`, `Pagina<T>`) usando generics y utility types donde aporten.

## Pasos

### 1. Lectura utility types (45 min)

`Partial`, `Pick`, `Omit` — solo los que uses.

### 2. DTOs de entrada/salida (90 min)

Separa entidad interna de DTO público.

### 3. Paginación o lista genérica (90 min)

```ts
export interface Pagina<T> {
  items: T[];
  total: number;
}
```

### 4. Documentación TSDoc (60 min)

Comentarios en exports públicos (una línea útil cada uno).

### 5. Commit cierre semana 3 (15 min)

`feat(m06): API publica tipada semana 3`

## Hecho cuando

1. `src/index.ts` exporta API coherente y documentada.
2. Generics aparecen donde evitan duplicación real.
3. Tests de contratos públicos.

## Errores comunes

- Exportar todo el interior del dominio.
- Utility types ilegibles anidados.

## Siguiente

[L13 — Errores como diseño (CC cap. 7)](L13-errores-como-diseno.md)
