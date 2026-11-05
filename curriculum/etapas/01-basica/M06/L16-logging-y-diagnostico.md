---
id: L16
materia: M06
orden: 16
titulo: 'Logging, diagnóstico y contratos de error'
horas: 5
semana: 4
lectura: Docs Node console vs debug; CC cap. 7 repaso
evidencia: Logger delgado en frontera; semana 4 commit cierre
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras semana 4: observabilidad mínima sin spam. Logs en el borde;
      dominio limpio.


      **Objetivo de esta lección:** Introducir interfaz `Logger` inyectable;
      registrar errores y eventos de negocio en adaptadores CLI/tests fake.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Diseño
    xp: 10
    cuerpo: |-
      ```ts
      export interface Logger {
        info(msg: string, meta?: Record<string, unknown>): void;
        error(msg: string, meta?: Record<string, unknown>): void;
      }
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Implementaciones
    xp: 10
    cuerpo: |-
      ```ts
      export interface Logger {
        info(msg: string, meta?: Record<string, unknown>): void;
        error(msg: string, meta?: Record<string, unknown>): void;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Logging, diagnóstico y contratos de error», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Dominio sin `console.log` suelto.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Logging, diagnóstico y
          contratos de err…
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
    pregunta: ¿Es recomendable en esta lección? “Log en cada línea."
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
          Introducir interfaz `Logger` inyectable; registrar errores y eventos
          de negocio en adaptadores CLI/tests fake.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cableado
    xp: 10
    cuerpo: 'Solo capa aplicación/CLI loguea Result err con meta (id, código).'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Dominio sin `console.log` suelto.
      - Logger mockeable en tests.
      - OPERACION.md breve.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Logging, diagnóstico y contratos de error

**~5 h · Semana 4**

Cierras semana 4: observabilidad mínima sin spam. Logs en el borde; dominio limpio.

## Objetivo

Introducir interfaz `Logger` inyectable; registrar errores y eventos de negocio en adaptadores CLI/tests fake.

## Pasos

### 1. Diseño (45 min)

```ts
export interface Logger {
  info(msg: string, meta?: Record<string, unknown>): void;
  error(msg: string, meta?: Record<string, unknown>): void;
}
```

### 2. Implementaciones (60 min)

`ConsoleLogger`, `NoopLogger` para tests.

### 3. Cableado (90 min)

Solo capa aplicación/CLI loguea Result err con meta (id, código).

### 4. Tests (60 min)

Fake logger cuenta invocaciones en escenarios de fallo.

### 5. Documento operación (45 min)

`OPERACION.md`: qué se loguea, qué no (PII).

### 6. Commit (15 min)

`feat(m06): logging en frontera semana 4`

## Hecho cuando

1. Dominio sin `console.log` suelto.
2. Logger mockeable en tests.
3. OPERACION.md breve.

## Errores comunes

- Log en cada línea.
- Meta con objetos enormes.

## Siguiente

[L17 — Estructura de paquete npm](L17-estructura-paquete-npm.md)
