---
id: L20
materia: M13
orden: 20
titulo: Cierre M13 — trazabilidad y dominio
horas: 5
semana: 5
lectura: Criterios de dominio ficha M13; trazabilidad SRS↔diagramas
evidencia: trazabilidad.md + README final; criterios de dominio autoevaluados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Matriz de trazabilidad + autoevaluación de criterios de
      dominio de la ficha.


      Cierras la materia demostrando que cada diagrama sirve a un requisito — y
      que puedes defender el monolito modular.
  - id: s2
    tipo: ejemplo
    titulo: 1. Matriz
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M13 — trazabilidad y dominio" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: trazabilidad.md + README final; criterios de dominio autoevaluados
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m13-diseno`
    comandoEsperado:
      - git add projects/m13-diseno
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m13-diseno'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Matriz de trazabilidad + autoevaluación de criterios de dominio de la
          ficha.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Criterios de dominio
    xp: 10
    cuerpo: |-
      De la ficha M13 — responde en `bitacora-cierre.md`:

      - ¿Defiendes monolito modular con trade-offs?
      - ¿Sabes dónde se valida el rol?
      - ¿Un compañero puede empezar M17 con SRS + este paquete?
  - id: s7
    tipo: explicacion
    titulo: 3. Pulido README
    xp: 10
    cuerpo: 'Estado: “Paquete listo para M17” + fecha.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.'
      - Autoevaluación de criterios de dominio en bitácora o README (honesta).
      - 'Commit `docs(m13): cierre trazabilidad y criterios de dominio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L20 — Cierre M13 — trazabilidad y dominio

**~5.0 h · Semana 5**

Cierras la materia demostrando que cada diagrama sirve a un requisito — y que puedes defender el monolito modular.

## Objetivo

Matriz de trazabilidad + autoevaluación de criterios de dominio de la ficha.

## Pasos (hazlos en orden)

### 1. Matriz (70–90 min)

`trazabilidad.md`:

| Historia SRS | UC | Diagrama / ADR |
|--------------|----|----------------|
| H-pedido-01 | UC-03 | secuencia-crear-pedido, ADR 002 |

Borra artefactos huérfanos o enlázalos.

### 2. Criterios de dominio (40–50 min)

De la ficha M13 — responde en `bitacora-cierre.md`:

- ¿Defiendes monolito modular con trade-offs?
- ¿Sabes dónde se valida el rol?
- ¿Un compañero puede empezar M17 con SRS + este paquete?

### 3. Pulido README (30 min)

Estado: “Paquete listo para M17” + fecha.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Trazabilidad requisito→diseño; autoevaluación criterios de dominio | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.
2. Autoevaluación de criterios de dominio en bitácora o README (honesta).
3. Commit `docs(m13): cierre trazabilidad y criterios de dominio`.

## Errores comunes

- Diagramas sin fila en la matriz de trazabilidad.
- Autoevaluación todo ✓ sin evidencia.
- Microservicios reintroducidos en el cierre.

## Siguiente

Materia siguiente: [M14 — Patrones](../M14-patrones.md) · L01 en `../M14/`.
