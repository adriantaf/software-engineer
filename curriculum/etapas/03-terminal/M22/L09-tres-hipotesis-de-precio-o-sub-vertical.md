---
id: L09
materia: M22
orden: 9
titulo: Tres hipótesis de precio o sub-vertical
horas: 5
semana: 3
lectura: Lean — experimentación
evidencia: projects/m22-bektor/pricing-experimentos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar tres experimentos de pricing o empaquetado y cómo
      los invalidarías con datos de demos.


      Semana 3 exige rigor: precio no es número mágico, es hipótesis.


      Conceptos que debes poder explicar al cerrar:


      - Precio.

      - Elasticidad (cualitativa).

      - Free tier.

      - Límites técnicos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l09 tres-hip-tesis-de-precio-o-sub-vertical"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tres hipótesis de precio o sub-vertical" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/pricing-experimentos.md
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
          Documentar tres experimentos de pricing o empaquetado y cómo los
          invalidarías con datos de demos.
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


      `projects/m22-bektor/pricing-experimentos.md`: 3 hipótesis (ej. Pro $499
      vs $699 MXN; límite pedidos/mes). Para cada una: señal de éxito/fracaso en
      conversaciones.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Compara alternativas: libreta, Calendly genérico, WhatsApp solo — tabla 1
      página.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/pricing-experimentos.md`.'
      - 3 hipótesis.
      - Tabla alternativas.
      - Señales éxito/fracaso.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Tres hipótesis de precio o sub-vertical

**~5 h · Semana 3**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing-experimentos.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Documentar tres experimentos de pricing o empaquetado y cómo los invalidarías con datos de demos.

## Por qué empieza así

Semana 3 exige rigor: precio no es número mágico, es hipótesis.

Conceptos que debes poder explicar al cerrar:

- Precio.
- Elasticidad (cualitativa).
- Free tier.
- Límites técnicos.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — experimentación_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

`projects/m22-bektor/pricing-experimentos.md`: 3 hipótesis (ej. Pro $499 vs $699 MXN; límite pedidos/mes). Para cada una: señal de éxito/fracaso en conversaciones.

### 3. Laboratorio principal (90–120 min)

Compara alternativas: libreta, Calendly genérico, WhatsApp solo — tabla 1 página.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l09 tres-hip-tesis-de-precio-o-sub-vertical"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — experimentación | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing-experimentos.md`.
2. 3 hipótesis.
3. Tabla alternativas.
4. Señales éxito/fracaso.
5. Commit `docs(m22): l09 …` en el historial.

## Errores comunes

- Precio sin justificación.
- Copiar USD sin MXN.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Demos 5–6 — escuchar precio en voz alta](L10-demos-5-6-escuchar-precio-en-voz-alta.md)
