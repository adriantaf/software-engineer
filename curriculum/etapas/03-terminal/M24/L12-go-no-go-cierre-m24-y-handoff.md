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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar decisión go/no-go argumentada; actualizar backlog;
      cerrar prácticas P2–P3 y criterios dominio.


      Un ‘no’ bien fundado cumple el proyecto si el spike demostró costo/riesgo
      > valor.


      Conceptos que debes poder explicar al cerrar:


      - Go / no-go / defer

      - Issue derivado

      - Archivar spike
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l12 go-no-go-cierre-m24-y-handoff"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Go/no-go, cierre M24 y handoff" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m24-emergentes/go-no-go.md + bitácora semana-03.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Redactar decisión go/no-go argumentada; actualizar backlog; cerrar
          prácticas P2–P3 y criterios dominio.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m24-emergentes`.


      `projects/m24-emergentes/go-no-go.md`: decisión, criterios, próximos pasos
      si go, qué archivar si no.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Cierra bitácora semana 3. README del proyecto enlaza toda la evidencia
      P1–P3.
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
