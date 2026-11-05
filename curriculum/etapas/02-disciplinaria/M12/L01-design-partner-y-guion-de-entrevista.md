---
id: L01
materia: M12
orden: 1
titulo: Design partner y guion de entrevista
horas: 5
semana: 1
lectura: plantilla.md + producto-saas.md
evidencia: entrevistas/guion-v1.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Vitrina empieza con un problema real, no con Figma. Hoy eliges partner y
      guion.


      **Objetivo de esta lección:** Fijar sub-vertical + `guion-v1.md` listo
      para una entrevista real o simulada seria.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Scaffold
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m12-srs/entrevistas
      cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
      cat projects/m12-srs/README.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Producto e ICP
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): l01 guion entrevista"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Design partner y guion de entrevista», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Design partner y guion
          de entrevista
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

      `mkdir -p projects/m12-srs/entrevistas`
    comandoEsperado:
      - mkdir -p projects/m12-srs/entrevistas
      - cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m12-srs/entrevistas'
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
          Fijar sub-vertical + `guion-v1.md` listo para una entrevista real o
          simulada seria.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Guion ≥10 preguntas
    xp: 10
    cuerpo: >-
      Categorías obligatorias: 1. Flujo de una pedido de punta a punta 2.
      No-shows y recordatorios 3. Datos de clientes que guardan (PII) 4. Quién
      agenda (dueño vs staff) 5. Dolores de cobro / adelantos (sin diseñar pagos
      aún) 6. Qué **no** quieren automatizar Regla: preguntas abiertas
      (“cuéntame…”, “¿qué pasa cuando…?”).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Sub-vertical elegido y escrito (no se cambia en M12).
      - >-
        `entrevistas/guion-v1.md` con ≥10 preguntas abiertas (flujo pedidos,
        pedido abandonados, datos sensibles).
      - 'Commit `docs(m12): l01 guion entrevista`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Design partner y guion de entrevista

**~5.0 h · Semana 1**

Vitrina empieza con un problema real, no con Figma. Hoy eliges partner y guion.

## Objetivo

Fijar sub-vertical + `guion-v1.md` listo para una entrevista real o simulada seria.

## Pasos (hazlos en orden)

### 1. Scaffold (15 min)

```bash
mkdir -p projects/m12-srs/entrevistas
cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
cat projects/m12-srs/README.md
```

### 2. Producto e ICP (45–60 min)

Lee [producto-saas.md](../../../producto-saas.md). En `entrevistas/guion-v1.md` escribe:

- Sub-vertical (ej. barbería / consultorio / taller) — **uno**
- Ciudad/contexto
- Nombre o rol del design partner (puede ser anónimo)
- Qué herramientas usa hoy (WhatsApp, libreta, Excel…)

### 3. Guion ≥10 preguntas (75–90 min)

Categorías obligatorias:

1. Flujo de una pedido de punta a punta
2. No-shows y recordatorios
3. Datos de clientes que guardan (PII)
4. Quién agenda (dueño vs staff)
5. Dolores de cobro / adelantos (sin diseñar pagos aún)
6. Qué **no** quieren automatizar

Regla: preguntas abiertas (“cuéntame…”, “¿qué pasa cuando…?”).

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l01 guion entrevista"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | ICP, design partner, alcance piloto single-tenant Vitrina | [producto-saas.md](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Sub-vertical elegido y escrito (no se cambia en M12).
2. `entrevistas/guion-v1.md` con ≥10 preguntas abiertas (flujo pedidos, pedido abandonados, datos sensibles).
3. Commit `docs(m12): l01 guion entrevista`.

## Errores comunes

- Empezar por pantallas UI.
- Preguntas cerradas tipo “¿te gustaría una app?”.
- Cambiar de barbería a clínica a mitad de semana.

## Siguiente

[L02 — Entrevista y notas timestamp](L02-entrevista-y-notas-timestamp.md)
