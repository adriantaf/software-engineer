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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Fijar sub-vertical + `guion-v1.md` listo para una entrevista
      real o simulada seria.


      Vitrina empieza con un problema real, no con Figma. Hoy eliges partner y
      guion.
  - id: s2
    tipo: ejemplo
    titulo: 1. Scaffold
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m12-srs/entrevistas
      cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
      cat projects/m12-srs/README.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Design partner y guion de entrevista" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: entrevistas/guion-v1.md
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

      `mkdir -p projects/m12-srs/entrevistas`
    comandoEsperado:
      - mkdir -p projects/m12-srs/entrevistas
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m12-srs/entrevistas'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Fijar sub-vertical + `guion-v1.md` listo para una entrevista real o
          simulada seria.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Producto e ICP
    xp: 10
    cuerpo: >-
      Lee [producto-saas.md](../../../producto-saas.md). En
      `entrevistas/guion-v1.md` escribe:


      - Sub-vertical (ej. barbería / consultorio / taller) — **uno**

      - Ciudad/contexto

      - Nombre o rol del design partner (puede ser anónimo)

      - Qué herramientas usa hoy (WhatsApp, libreta, Excel…)
  - id: s7
    tipo: explicacion
    titulo: 3. Guion ≥10 preguntas
    xp: 10
    cuerpo: |-
      Categorías obligatorias:

      1. Flujo de una pedido de punta a punta
      2. No-shows y recordatorios
      3. Datos de clientes que guardan (PII)
      4. Quién agenda (dueño vs staff)
      5. Dolores de cobro / adelantos (sin diseñar pagos aún)
      6. Qué **no** quieren automatizar

      Regla: preguntas abiertas (“cuéntame…”, “¿qué pasa cuando…?”).
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
