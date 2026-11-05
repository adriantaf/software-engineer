---
id: L12
materia: M24
orden: 12
titulo: 'Go/no-go, cierre M24 y handoff'
horas: 5
semana: 3
lectura: Repaso ficha M24 criterios dominio
evidencia: projects/m24-emergentes/go-no-go.md + bitácora semana-03.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un ‘no’ bien fundado cumple el proyecto si el spike demostró costo/riesgo
      > valor.


      Conceptos que debes poder explicar al cerrar:


      - Go / no-go / defer

      - Issue derivado

      - Archivar spike


      **Objetivo de esta lección:** Redactar decisión go/no-go argumentada;
      actualizar backlog; cerrar prácticas P2–P3 y criterios dominio.


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
      git commit -m "docs(m24): l12 go-no-go-cierre-m24-y-handoff"
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
      git commit -m "docs(m24): l12 go-no-go-cierre-m24-y-handoff"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Go/no-go, cierre M24 y handoff», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Go/no-go, cierre M24 y
          handoff
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
          Redactar decisión go/no-go argumentada; actualizar backlog; cerrar
          prácticas P2–P3 y criterios dominio.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M24
    xp: 25
    enunciado: >-
      Cierra **Tecnologías emergentes** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: Research notes de 3 tecnologías candidatas'
      - 'P2: Criterios de adopción (costo, riesgo, valor, seguridad)'
      - 'P3: Spike de 1 semana'
      - 'Proyecto: PoC justificado (IoT, edge, realtime, etc.)'
      - projects/m24-emergentes/go-no-go.md + bitácora semana-03.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          Existe el entregable: `projects/m24-emergentes/go-no-go.md + bitácora
          semana-03.md`.
      - id: r3
        criterio: go-no-go.md publicado.
      - id: r4
        criterio: README proyecto actualizado.
      - id: r5
        criterio: Backlog M21 tocado.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m24-emergentes/go-no-go.md + bitácora
        semana-03.md`.
      - go-no-go.md publicado.
      - README proyecto actualizado.
      - Backlog M21 tocado.
    siguiente: Materia M24 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Go/no-go, cierre M24 y handoff

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/go-no-go.md + bitácora semana-03.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Redactar decisión go/no-go argumentada; actualizar backlog; cerrar prácticas P2–P3 y criterios dominio.

## Por qué empieza así

Un ‘no’ bien fundado cumple el proyecto si el spike demostró costo/riesgo > valor.

Conceptos que debes poder explicar al cerrar:

- Go / no-go / defer
- Issue derivado
- Archivar spike

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Repaso ficha M24 criterios dominio_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

`projects/m24-emergentes/go-no-go.md`: decisión, criterios, próximos pasos si go, qué archivar si no.

### 3. Laboratorio principal (90–120 min)

Cierra bitácora semana 3. README del proyecto enlaza toda la evidencia P1–P3.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l12 go-no-go-cierre-m24-y-handoff"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Repaso ficha M24 criterios dominio | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/go-no-go.md + bitácora semana-03.md`.
2. go-no-go.md publicado.
3. README proyecto actualizado.
4. Backlog M21 tocado.
5. Commit `docs(m24): l12 …` en el historial.

## Errores comunes

- Go sin plan de seguridad.
- No-go sin spike ejecutado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan.
