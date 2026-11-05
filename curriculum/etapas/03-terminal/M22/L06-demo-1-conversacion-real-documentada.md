---
id: L06
materia: M22
orden: 6
titulo: Demo 1 — conversación real documentada
horas: 5
semana: 2
lectura: Lean — entrevista/solución
evidencia: projects/m22-bektor/demos/demo-01.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      ‘No contestó’ no cuenta sin intento; ‘sí demo’ exige aprendizaje escrito
      el mismo día.


      Conceptos que debes poder explicar al cerrar:


      - Objeción.

      - Siguiente paso.

      - Canal.

      - Aprendizaje distinto.


      **Objetivo de esta lección:** Ejecutar primera demo o intento serio con
      negocio ICP y documentar con plantilla de la ficha.


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
      git commit -m "docs(m22): l06 demo-1-conversaci-n-real-documentada"
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
      git commit -m "docs(m22): l06 demo-1-conversaci-n-real-documentada"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Demo 1 — conversación real documentada», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Demo 1 — conversación
          real documentada
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
          Ejecutar primera demo o intento serio con negocio ICP y documentar con
          plantilla de la ficha.
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
    cuerpo: Usa URL staging. Pide **trial o segunda reunión** antes de colgar.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/demos/demo-01.md`.'
      - demo-01.md mismo día.
      - URL staging.
      - Siguiente paso concreto.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Demo 1 — conversación real documentada

**~5 h · Semana 2**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Ejecutar primera demo o intento serio con negocio ICP y documentar con plantilla de la ficha.

## Por qué empieza así

‘No contestó’ no cuenta sin intento; ‘sí demo’ exige aprendizaje escrito el mismo día.

Conceptos que debes poder explicar al cerrar:

- Objeción.
- Siguiente paso.
- Canal.
- Aprendizaje distinto.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — entrevista/solución_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Crea `projects/m22-bektor/demos/demo-01.md` con plantilla ficha (contacto, mostrado, objeción, respuesta, siguiente paso, aprendizaje).

### 3. Laboratorio principal (90–120 min)

Usa URL staging. Pide **trial o segunda reunión** antes de colgar.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l06 demo-1-conversaci-n-real-documentada"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — entrevista/solución | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-01.md`.
2. demo-01.md mismo día.
3. URL staging.
4. Siguiente paso concreto.
5. Commit `docs(m22): l06 …` en el historial.

## Errores comunes

- Demo sin producto.
- Copiar texto de blog.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L07 — Demo 2 — refinar guion y oferta](L07-demo-2-refinar-guion-y-oferta.md)
