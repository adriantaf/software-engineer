---
id: L24
materia: M08
orden: 24
titulo: Cierre M08 y evidencias
horas: 5
semana: 6
lectura: Checklist P1–P3 + proyecto; índice ≥15
evidencia: checklist + indice ≥15
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar índice ≥15, checklist de dominio y dejar el README
      raíz como mapa de evidencias.


      Cierras solo con evidencia en git: 15 problemas clasificados, sorts, DP y
      autocomplete.
  - id: s2
    tipo: ejemplo
    titulo: 1. Contar problemas
    xp: 10
    cuerpo: |-
      ```bash
      find problems -name 'enunciado.md' | wc -l
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Cierre M08 y evidencias" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: checklist + indice ≥15
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

      `find problems -name 'enunciado.md' | wc -l`
    comandoEsperado:
      - find problems -name 'enunciado.md' | wc -l
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: find problems -name ''enunciado.md'' | wc -l'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar índice ≥15, checklist de dominio y dejar el README raíz como
          mapa de evidencias.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Checklist
    xp: 10
    cuerpo: |-
      `bitacora/cierre-m08.md` con rutas:

      - P1 índice ≥15
      - P2 `sorts/README.md`
      - P3 `dp/` ×3
      - Proyecto `autocomplete/` + DISENO + CLI
  - id: s7
    tipo: explicacion
    titulo: 3. Dominio oral
    xp: 10
    cuerpo: 'Outline escrito: resuelve two-sum / ventana en voz alta con complejidad.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `indice-patrones.md` con ≥15 entradas; checklist en
        `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
      - '`npm test` verde; autocomplete documentado enlazado desde README raíz.'
      - 'Commit `docs(m08): cierre materia y evidencias`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M08 y evidencias

**~5.0 h · Semana 6**

Cierras solo con evidencia en git: 15 problemas clasificados, sorts, DP y autocomplete.

## Objetivo

Completar índice ≥15, checklist de dominio y dejar el README raíz como mapa de evidencias.

## Pasos

### 1. Contar problemas (40 min)

```bash
find problems -name 'enunciado.md' | wc -l
```

Si <15, añade los faltantes hoy (plantilla corta) o recupera de semanas previas mal indexados.

### 2. Checklist (60 min)

`bitacora/cierre-m08.md` con rutas:

- P1 índice ≥15
- P2 `sorts/README.md`
- P3 `dp/` ×3
- Proyecto `autocomplete/` + DISENO + CLI

### 3. Dominio oral (40 min)

Outline escrito: resuelve two-sum / ventana en voz alta con complejidad.

### 4. Regresión (30 min)

```bash
cd projects/m08-algoritmos && npm test
```

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): cierre materia y evidencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Autoevaluación: explicar un medio de arrays/hash en voz alta | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `indice-patrones.md` con **≥15** entradas; checklist en `bitacora/cierre-m08.md` con rutas P1/P2/P3/proyecto.
2. `npm test` verde; autocomplete documentado enlazado desde README raíz.
3. Commit `docs(m08): cierre materia y evidencias`.

## Errores comunes

- Índice inflado con filas vacías.
- Marcar P3 sin tres DP.
- Autocomplete sin complejidad de query.

## Siguiente

M08 cerrado — siguiente materia: [M09 · Bases de datos](../M09-bases-de-datos.md)
