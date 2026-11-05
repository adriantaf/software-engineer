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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin fricciones observadas, la auditoría Nielsen se vuelve checklist vacío.


      **Objetivo de esta lección:** Lista de fricciones en `fricciones-dia-1.md`
      y carpetas base de evidencia.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Prepara carpeta
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
      cat projects/m16-ihc/README.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Elige superficie
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
      cat projects/m16-ihc/README.md
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Recorrido persona nueva y fricciones día 1», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Recorrido persona nueva
          y fricciones dí…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}`
    comandoEsperado:
      - 'mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}'
      - cat projects/m16-ihc/README.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: mkdir -p
      projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
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
          Lista de fricciones en `fricciones-dia-1.md` y carpetas base de
          evidencia.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Recorrido cronometrado
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
