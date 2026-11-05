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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Introducir interfaz `Logger` inyectable; registrar errores y
      eventos de negocio en adaptadores CLI/tests fake.


      Cierras semana 4: observabilidad mínima sin spam. Logs en el borde;
      dominio limpio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Diseño
    xp: 10
    cuerpo: |-
      ```ts
      export interface Logger {
        info(msg: string, meta?: Record<string, unknown>): void;
        error(msg: string, meta?: Record<string, unknown>): void;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Logging, diagnóstico y contratos de error" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: Logger delgado en frontera; semana 4 commit cierre
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
    pregunta: ¿Es buena práctica en esta lección? “Log en cada línea."
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
          Introducir interfaz `Logger` inyectable; registrar errores y eventos
          de negocio en adaptadores CLI/tests fake.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementaciones
    xp: 10
    cuerpo: '`ConsoleLogger`, `NoopLogger` para tests.'
  - id: s7
    tipo: explicacion
    titulo: 3. Cableado
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
