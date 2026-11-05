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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Diseñar tipos exportados estables (`CrearLibroInput`,
      `Pagina<T>`) usando generics y utility types donde aporten.


      Cierras semana 3 integrando generics en la superficie pública que
      consumirá tu librería (semana 5).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura utility types
    xp: 10
    cuerpo: |-
      ```ts
      export interface Pagina<T> {
        items: T[];
        total: number;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Generics en APIs del dominio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: API exportada tipada; semana 3 cerrada con commit
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
      ¿Es buena práctica en esta lección? “Exportar todo el interior del
      dominio."
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
          Diseñar tipos exportados estables (`CrearLibroInput`, `Pagina<T>`)
          usando generics y utility types donde aporten.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. DTOs de entrada/salida
    xp: 10
    cuerpo: Separa entidad interna de DTO público.
  - id: s7
    tipo: ejemplo
    titulo: 3. Paginación o lista genérica
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
