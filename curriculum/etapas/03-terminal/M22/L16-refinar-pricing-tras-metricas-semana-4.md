---
id: L16
materia: M22
orden: 16
titulo: Refinar pricing tras métricas semana 4
horas: 5
semana: 4
lectura: Lean — aprendizaje acumulado
evidencia: projects/m22-bektor/pricing.md v2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Ajustar pricing con nota de versión y evidencia de
      conversaciones (no intuición sola).


      Preparas P3 final en semana 6; hoy versionas cambios.


      Conceptos que debes poder explicar al cerrar:


      - Changelog pricing.

      - Anclaje.

      - Límites Free.

      - Trial.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l16 refinar-pricing-tras-m-tricas-semana-4"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Refinar pricing tras métricas semana 4" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/pricing.md v2
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
          Ajustar pricing con nota de versión y evidencia de conversaciones (no
          intuición sola).
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
      Confirma rutas bajo `projects/m22-bektor`.


      Añade `projects/m22-bektor/pricing-changelog.md` con v1→v2 y razón (pedido
      demo #).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: Relee límites técnicos; alinea con plan Pro si incluirá FAQ IA (M23).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/pricing.md v2`.'
      - pricing-changelog.
      - pricing.md v2.
      - Evidencia demo citada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Refinar pricing tras métricas semana 4

**~5 h · Semana 4**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing.md v2`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Ajustar pricing con nota de versión y evidencia de conversaciones (no intuición sola).

## Por qué empieza así

Preparas P3 final en semana 6; hoy versionas cambios.

Conceptos que debes poder explicar al cerrar:

- Changelog pricing.
- Anclaje.
- Límites Free.
- Trial.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — aprendizaje acumulado_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Añade `projects/m22-bektor/pricing-changelog.md` con v1→v2 y razón (pedido demo #).

### 3. Laboratorio principal (90–120 min)

Relee límites técnicos; alinea con plan Pro si incluirá FAQ IA (M23).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l16 refinar-pricing-tras-m-tricas-semana-4"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — aprendizaje acumulado | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing.md v2`.
2. pricing-changelog.
3. pricing.md v2.
4. Evidencia demo citada.
5. Commit `docs(m22): l16 …` en el historial.

## Errores comunes

- Cambiar precio sin razón.
- Ignorar costo IA.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L17 — Outreach semana 5 — lote de cinco contactos](L17-outreach-semana-5-lote-de-cinco-contactos.md)
