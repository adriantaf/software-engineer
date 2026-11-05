---
id: L03
materia: M24
orden: 3
titulo: Research candidatos 2 y 3
horas: 5
semana: 1
lectura: Docs oficiales candidatos 2 y 3
evidencia: projects/m24-emergentes/research/candidato-2.md y candidato-3.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Mismo estándar que candidato 1 para los otros dos
      candidatos.


      Comparar tres opciones evita enamorarte del primer tutorial que viste.


      Conceptos que debes poder explicar al cerrar:


      - Madurez del ecosistema

      - Datos fuera del perímetro

      - Operación (on-call)
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l03 research-candidatos-2-y-3"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Research candidatos 2 y 3" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m24-emergentes/research/candidato-2.md y candidato-3.md
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
        texto: Mismo estándar que candidato 1 para los otros dos candidatos.
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
      Confirma rutas bajo `projects/m24-emergentes/research`.


      Completa `candidato-2.md` y `candidato-3.md` con el mismo template que
      L02.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Tabla comparativa rápida en
      `projects/m24-emergentes/research/comparacion-v0.md` (valor, complejidad,
      riesgo).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m24-emergentes/research/candidato-2.md y
        candidato-3.md`.
      - Dos archivos research completos.
      - comparacion-v0.md con 3 filas.
      - 'Commit `docs(m24): l03 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Research candidatos 2 y 3

**~5 h · Semana 1**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/research/candidato-2.md y candidato-3.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Mismo estándar que candidato 1 para los otros dos candidatos.

## Por qué empieza así

Comparar tres opciones evita enamorarte del primer tutorial que viste.

Conceptos que debes poder explicar al cerrar:

- Madurez del ecosistema
- Datos fuera del perímetro
- Operación (on-call)

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Docs oficiales candidatos 2 y 3_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/research`.

Completa `candidato-2.md` y `candidato-3.md` con el mismo template que L02.

### 3. Laboratorio principal (90–120 min)

Tabla comparativa rápida en `projects/m24-emergentes/research/comparacion-v0.md` (valor, complejidad, riesgo).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l03 research-candidatos-2-y-3"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Docs oficiales candidatos 2 y 3 | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/research/candidato-2.md y candidato-3.md`.
2. Dos archivos research completos.
3. comparacion-v0.md con 3 filas.
4. Commit `docs(m24): l03 …` en el historial.

## Errores comunes

- Tres candidatos idénticos (solo cambia nombre).
- Ignorar si datos de clientes salen a terceros.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L04 — Cierre research semana 1 y backlog M21](L04-cierre-research-semana-1-y-backlog-m21.md)
