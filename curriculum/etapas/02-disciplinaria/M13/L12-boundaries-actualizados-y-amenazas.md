---
id: L12
materia: M13
orden: 12
titulo: Boundaries actualizados y amenazas
horas: 5
semana: 3
lectura: Trust boundaries + amenazas alto nivel; cierre P3
evidencia: trust-boundaries.md actualizado (P3) + notas de amenaza
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Actualizar `diagramas/trust-boundaries.md` y dejar P3
      evidenciable.


      Cierras P3: el diagrama de L01 ahora refleja capas, DTOs y contenedores
      reales.
  - id: s2
    tipo: ejemplo
    titulo: 1. Relee L01 + arquitectura
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): boundaries actualizados y amenazas P3"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Boundaries actualizados y amenazas" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: trust-boundaries.md actualizado (P3) + notas de amenaza
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
        texto: Actualizar `diagramas/trust-boundaries.md` y dejar P3 evidenciable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tabla de amenazas
    xp: 10
    cuerpo: |-
      | Amenaza | Límite | Mitigación de diseño |
      |---------|--------|----------------------|
      | IDOR pedido | API→DB | filtro por dueño/negocio en queries |
      | Session hijack | Browser→API | Cookie Secure/HttpOnly; logout |
      | Mass assignment | Browser→API | DTO allowlist |
      | SQLi | API→DB | parametrized queries / ORM |
  - id: s7
    tipo: explicacion
    titulo: 3. Checklist P3
    xp: 10
    cuerpo: 'Ficha: `trust-boundaries.md` con límites y notas de amenaza.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `trust-boundaries.md` actualizado con capas/C4 y ≥3 amenazas con
        mitigación de diseño.
      - 'P3 cumplido: boundaries con límites y notas de amenaza.'
      - 'Commit `docs(m13): boundaries actualizados y amenazas P3`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Boundaries actualizados y amenazas

**~5.0 h · Semana 3**

Cierras P3: el diagrama de L01 ahora refleja capas, DTOs y contenedores reales.

## Objetivo

Actualizar `diagramas/trust-boundaries.md` y dejar P3 evidenciable.

## Pasos (hazlos en orden)

### 1. Relee L01 + arquitectura (30 min)

Marca desactualizaciones (¿apareció el mail? ¿sesión?).

### 2. Tabla de amenazas (70–90 min)

| Amenaza | Límite | Mitigación de diseño |
|---------|--------|----------------------|
| IDOR pedido | API→DB | filtro por dueño/negocio en queries |
| Session hijack | Browser→API | Cookie Secure/HttpOnly; logout |
| Mass assignment | Browser→API | DTO allowlist |
| SQLi | API→DB | parametrized queries / ORM |

### 3. Checklist P3 (20 min)

Ficha: `trust-boundaries.md` con límites y notas de amenaza.

### 4. Bitácora semana 3 (30 min)

`bitacora-semana-3.md`: capas + amenaza que más te preocupa.

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): boundaries actualizados y amenazas P3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Amenazas en límites; IDOR, sesión, validación | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `trust-boundaries.md` actualizado con capas/C4 y ≥3 amenazas con mitigación de diseño.
2. P3 cumplido: boundaries con límites y notas de amenaza.
3. Commit `docs(m13): boundaries actualizados y amenazas P3`.

## Errores comunes

- Lista OWASP Top 10 pegada sin relación a tus cajas.
- Mitigaciones solo “usaremos HTTPS” sin authz en API.
- P3 marcado con el archivo de L01 sin actualizar.

## Siguiente

[L13 — Plantilla ADR y decisiones de diseño](L13-plantilla-adr-y-decisiones-de-diseno.md)
