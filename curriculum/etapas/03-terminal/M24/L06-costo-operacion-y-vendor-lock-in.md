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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Estimar costo mensual a 10 / 100 tenants y documentar
      dependencia del vendor (migración, export).


      Vitrina es SaaS; un canal de mensajería caro por conversación puede matar
      margen.


      Conceptos que debes poder explicar al cerrar:


      - Costo marginal por tenant

      - Exit strategy

      - Fallback manual
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l06 costo-operaci-n-y-vendor-lock-in"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Costo, operación y vendor lock-in" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m24-emergentes/matriz-adopcion.md sección Costo
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
          Estimar costo mensual a 10 / 100 tenants y documentar dependencia del
          vendor (migración, export).
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


      Actualiza la matriz con escenarios de costo (tabla tenants ×
      mensajes/mes).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
