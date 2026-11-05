---
id: L20
materia: M09
orden: 20
titulo: 'Reportes, seeds y cierre M09'
horas: 5
semana: 5
lectura: 'Cierre: seeds + reportes de negocio'
evidencia: seeds + reportes.md + README — cierra proyecto M09
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar `seeds/`, `reportes.md` y README en estado “otro
      humano levanta esto”.


      Cierras el **proyecto** de la materia: esquema reproducible, seeds y
      reportes útiles.
  - id: s2
    tipo: ejemplo
    titulo: 1. Seeds realistas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos
      git commit -m "docs(m09): cierre materia seeds y reportes"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Reportes, seeds y cierre M09" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: seeds + reportes.md + README — cierra proyecto M09
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

      `git add projects/m09-bases-datos`
    comandoEsperado:
      - git add projects/m09-bases-datos
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m09-bases-datos'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar `seeds/`, `reportes.md` y README en estado “otro humano levanta
          esto”.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Dos reportes
    xp: 10
    cuerpo: |-
      Completa `reportes.md`. Ideas:

      1. No-shows de los últimos 30 días por cliente.
      2. Ingresos estimados (centavos) por servicio en pedidos `completada`.

      Cada uno: pregunta → archivo SQL → salida → uso para el dueño.
  - id: s7
    tipo: explicacion
    titulo: 3. Checklist total
    xp: 10
    cuerpo: >-
      P1 `er-vitrina.md` · P2 `sql/` + `explain-notas.md` · P3 `migrations/` +
      `roles.md` · Proyecto seeds + reportes.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`seeds/001_demo.sql` (o ampliado) aplica limpio.'
      - '`reportes.md` tiene ≥2 reportes con SQL + salida.'
      - Otro dev podría recrear la BD solo con tu README (lo simulas tú).
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L20 — Reportes, seeds y cierre M09

**~5.0 h · Semana 5**

Cierras el **proyecto** de la materia: esquema reproducible, seeds y reportes útiles.

## Objetivo

Dejar `seeds/`, `reportes.md` y README en estado “otro humano levanta esto”.

## Pasos

### 1. Seeds realistas (75 min)

Amplía `seeds/001_demo.sql`: ≥5 clientes, ≥3 servicios, pedidos en varios estados (`programada`, `completada`, `no_show`, `cancelada`). Reaplica en DB limpia o tras truncate controlado.

### 2. Dos reportes (75 min)

Completa `reportes.md`. Ideas:

1. No-shows de los últimos 30 días por cliente.
2. Ingresos estimados (centavos) por servicio en pedidos `completada`.

Cada uno: pregunta → archivo SQL → salida → uso para el dueño.

### 3. Checklist total (45 min)

P1 `er-vitrina.md` · P2 `sql/` + `explain-notas.md` · P3 `migrations/` + `roles.md` · Proyecto seeds + reportes.

### 4. Simulación máquina limpia (45 min)

Sigue solo tu README (sin mirar las lecciones). Anota fricciones y arréglalas.

### 5. Commit de cierre (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): cierre materia seeds y reportes"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Cierre: seeds + reportes de negocio | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `seeds/001_demo.sql` (o ampliado) aplica limpio.
2. `reportes.md` tiene ≥2 reportes con SQL + salida.
3. Otro dev podría recrear la BD solo con tu README (lo simulas tú).

## Errores comunes

- Reportes sin pregunta de negocio.
- Seeds con datos personales reales.
- Marcar el proyecto en la UI sin `reportes.md`.

## Siguiente

Cierra la [ficha M09](../M09-bases-de-datos.md). Siguiente materia disciplinaria según tu plan.
