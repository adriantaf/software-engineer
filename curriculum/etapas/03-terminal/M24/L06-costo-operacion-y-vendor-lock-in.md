---
id: L06
materia: M24
orden: 6
titulo: 'Costo, operación y vendor lock-in'
horas: 5
semana: 2
lectura: Pricing pages + SLA del candidato elegido preliminar
evidencia: projects/m24-emergentes/matriz-adopcion.md sección Costo
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Vitrina es SaaS; un canal de mensajería caro por conversación puede matar
      margen.


      Conceptos que debes poder explicar al cerrar:


      - Costo marginal por tenant

      - Exit strategy

      - Fallback manual


      **Objetivo de esta lección:** Estimar costo mensual a 10 / 100 tenants y
      documentar dependencia del vendor (migración, export).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l06 costo-operaci-n-y-vendor-lock-in"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l06 costo-operaci-n-y-vendor-lock-in"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Costo, operación y vendor lock-in», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Costo, operación y
          vendor lock-in
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
          Estimar costo mensual a 10 / 100 tenants y documentar dependencia del
          vendor (migración, export).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: >-
      Para el candidato líder, escribe párrafo **Si el vendor sube precio 2×**
      en `matriz-adopcion.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m24-emergentes/matriz-adopcion.md
        sección Costo`.
      - Escenarios de costo documentados.
      - Párrafo exit/lock-in.
      - 'Commit `docs(m24): l06 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Costo, operación y vendor lock-in

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/matriz-adopcion.md sección Costo`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Estimar costo mensual a 10 / 100 tenants y documentar dependencia del vendor (migración, export).

## Por qué empieza así

Vitrina es SaaS; un canal de mensajería caro por conversación puede matar margen.

Conceptos que debes poder explicar al cerrar:

- Costo marginal por tenant
- Exit strategy
- Fallback manual

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Pricing pages + SLA del candidato elegido preliminar_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

Actualiza la matriz con escenarios de costo (tabla tenants × mensajes/mes).

### 3. Laboratorio principal (90–120 min)

Para el candidato líder, escribe párrafo **Si el vendor sube precio 2×** en `matriz-adopcion.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l06 costo-operaci-n-y-vendor-lock-in"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Pricing pages + SLA del candidato elegido preliminar | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/matriz-adopcion.md sección Costo`.
2. Escenarios de costo documentados.
3. Párrafo exit/lock-in.
4. Commit `docs(m24): l06 …` en el historial.

## Errores comunes

- Costo ‘gratis’ sin leer tier de producción.
- No considerar tiempo de ingeniería.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L07 — Threat sketch del candidato para spike](L07-threat-sketch-del-candidato-para-spike.md)
