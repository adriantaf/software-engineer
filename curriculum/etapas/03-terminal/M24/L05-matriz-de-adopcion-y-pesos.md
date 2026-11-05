---
id: L05
materia: M24
orden: 5
titulo: Matriz de adopción y pesos
horas: 5
semana: 2
lectura: Criterios M24 + threat modeling ligero
evidencia: projects/m24-emergentes/matriz-adopcion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear matriz con criterios ponderados: valor ICP, costo,
      riesgo ops, seguridad, fit M26.


      P2 obliga a explicitar trade-offs antes de escribir código del spike.


      Conceptos que debes poder explicar al cerrar:


      - Peso ≥ hype

      - Columna seguridad

      - Score transparente
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l05 matriz-de-adopci-n-y-pesos"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Matriz de adopción y pesos" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m24-emergentes/matriz-adopcion.md
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
          Crear matriz con criterios ponderados: valor ICP, costo, riesgo ops,
          seguridad, fit M26.
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


      En `projects/m24-emergentes/matriz-adopcion.md` define pesos (suma 100%).
      Filas = candidatos; columnas = criterios.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Documenta **cómo** puntuas (1–5) con ejemplos por celda del candidato más
      fuerte.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m24-emergentes/matriz-adopcion.md`.'
      - Matriz con pesos y ≥3 candidatos.
      - Columna seguridad no vacía.
      - 'Commit `docs(m24): l05 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Matriz de adopción y pesos

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/matriz-adopcion.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Crear matriz con criterios ponderados: valor ICP, costo, riesgo ops, seguridad, fit M26.

## Por qué empieza así

P2 obliga a explicitar trade-offs antes de escribir código del spike.

Conceptos que debes poder explicar al cerrar:

- Peso ≥ hype
- Columna seguridad
- Score transparente

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Criterios M24 + threat modeling ligero_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

En `projects/m24-emergentes/matriz-adopcion.md` define pesos (suma 100%). Filas = candidatos; columnas = criterios.

### 3. Laboratorio principal (90–120 min)

Documenta **cómo** puntuas (1–5) con ejemplos por celda del candidato más fuerte.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l05 matriz-de-adopci-n-y-pesos"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Criterios M24 + threat modeling ligero | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/matriz-adopcion.md`.
2. Matriz con pesos y ≥3 candidatos.
3. Columna seguridad no vacía.
4. Commit `docs(m24): l05 …` en el historial.

## Errores comunes

- Todos 5/5 sin justificación.
- Olvidar costo mensual estimado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Costo, operación y vendor lock-in](L06-costo-operacion-y-vendor-lock-in.md)
