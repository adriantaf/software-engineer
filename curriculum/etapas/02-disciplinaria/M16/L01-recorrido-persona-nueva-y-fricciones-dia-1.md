---
id: L01
materia: M16
orden: 1
titulo: Recorrido persona nueva y fricciones día 1
horas: 5
semana: 1
lectura: 'Krug: no me hagas pensar; primer recorrido Vitrina'
evidencia: projects/m16-ihc/fricciones-dia-1.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Lista de fricciones en `fricciones-dia-1.md` y carpetas base
      de evidencia.


      Sin fricciones observadas, la auditoría Nielsen se vuelve checklist vacío.
  - id: s2
    tipo: ejemplo
    titulo: 1. Prepara carpeta
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
      cat projects/m16-ihc/README.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Recorrido persona nueva y fricciones día 1" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m16-ihc/fricciones-dia-1.md
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

      `mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}`
    comandoEsperado:
      - 'mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: mkdir -p
      projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Lista de fricciones en `fricciones-dia-1.md` y carpetas base de
          evidencia.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Elige superficie
    xp: 10
    cuerpo: >-
      Prototipo HTML en `prototipo/`, Figma export, o UI M17 si existe. Si no
      hay nada: crea 2–3 HTML estáticos de login + agenda + nueva pedido (L05 lo
      endurece).
  - id: s7
    tipo: explicacion
    titulo: 3. Recorrido cronometrado
    xp: 10
    cuerpo: >-
      Cronómetro: “Agendar pedido para cliente nuevo”. Anota cada duda, click
      engañoso, label confuso.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Carpeta `projects/m16-ihc/` con `fricciones-dia-1.md` (≥8 fricciones
        concretas del flujo agendar/ver agenda).
      - Cada fricción nombra pantalla/paso y quién sufre (owner vs staff nuevo).
      - 'Commit `docs(m16): fricciones dia 1 persona nueva`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Recorrido persona nueva y fricciones día 1

**~5.0 h · Semana 1**

El design partner no es tú. Hoy recorres Vitrina (prototipo o UI parcial) como persona nueva.

## Objetivo

Lista de fricciones en `fricciones-dia-1.md` y carpetas base de evidencia.

## Por qué empieza así

Sin fricciones observadas, la auditoría Nielsen se vuelve checklist vacío.

## Pasos (hazlos en orden)

### 1. Prepara carpeta (15 min)

```bash
mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
cat projects/m16-ihc/README.md
```

### 2. Elige superficie (20 min)

Prototipo HTML en `prototipo/`, Figma export, o UI M17 si existe. Si no hay nada: crea 2–3 HTML estáticos de login + agenda + nueva pedido (L05 lo endurece).

### 3. Recorrido cronometrado (60–80 min)

Cronómetro: “Agendar pedido para cliente nuevo”. Anota cada duda, click engañoso, label confuso.

### 4. Escribe fricciones-dia-1.md (70–90 min)

| ID | Paso | Fricción | Impacto percibido |
|----|------|----------|-------------------|
| F01 | Login | … | alto/medio/bajo |

### 5. Commit

`docs(m16): fricciones dia 1 persona nueva`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Escaneo y fricción en el primer uso del panel de pedidos | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Carpeta `projects/m16-ihc/` con `fricciones-dia-1.md` (≥8 fricciones concretas del flujo agendar/ver agenda).
2. Cada fricción nombra pantalla/paso y quién sufre (owner vs staff nuevo).
3. Commit `docs(m16): fricciones dia 1 persona nueva`.

## Errores comunes

- “La UI está fea” sin paso reproducible.
- Evaluar solo como desarrollador con datos seed perfectos.
- Ignorar login y estados vacíos.

## Siguiente

[L02 — Auditoría Nielsen — tres heurísticas profundas](L02-auditoria-nielsen-tres-heuristicas-profundas.md)
