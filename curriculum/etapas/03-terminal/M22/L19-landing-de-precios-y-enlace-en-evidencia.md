---
id: L19
materia: M22
orden: 19
titulo: Landing de precios y enlace en evidencia
horas: 5
semana: 5
lectura: producto-saas — página precios
evidencia: projects/m22-bektor/landing-precios.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Publicar o enlazar landing estática de precios (repo
      producto o página) y documentar URL en evidencia.


      M26 conectará Stripe; hoy el dueño debe **ver** números fuera de un MD
      privado.


      Conceptos que debes poder explicar al cerrar:


      - Landing.

      - URL pública.

      - Coherencia pricing.md.

      - CTA trial.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l19 landing-de-precios-y-enlace-en-evidencia"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Landing de precios y enlace en evidencia" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/landing-precios.md
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
          Publicar o enlazar landing estática de precios (repo producto o
          página) y documentar URL en evidencia.
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


      Crea `projects/m22-bektor/landing-precios.md` con URL HTTPS, captura o
      commit del HTML/ruta.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Debe coincidir con `projects/m22-bektor/pricing.md`. Anota fecha
      verificación.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/landing-precios.md`.'
      - URL pública.
      - Coherencia pricing.
      - Fecha verificación.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L19 — Landing de precios y enlace en evidencia

**~5 h · Semana 5**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/landing-precios.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Publicar o enlazar landing estática de precios (repo producto o página) y documentar URL en evidencia.

## Por qué empieza así

M26 conectará Stripe; hoy el dueño debe **ver** números fuera de un MD privado.

Conceptos que debes poder explicar al cerrar:

- Landing.
- URL pública.
- Coherencia pricing.md.
- CTA trial.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _producto-saas — página precios_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Crea `projects/m22-bektor/landing-precios.md` con URL HTTPS, captura o commit del HTML/ruta.

### 3. Laboratorio principal (90–120 min)

Debe coincidir con `projects/m22-bektor/pricing.md`. Anota fecha verificación.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l19 landing-de-precios-y-enlace-en-evidencia"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | producto-saas — página precios | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/landing-precios.md`.
2. URL pública.
3. Coherencia pricing.
4. Fecha verificación.
5. Commit `docs(m22): l19 …` en el historial.

## Errores comunes

- Solo MD privado.
- Precios distintos web vs doc.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L20 — Pivote Bektor → Vitrina — narrativa completa](L20-pivote-bektor-vitrina-narrativa-completa.md)
