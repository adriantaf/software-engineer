---
id: L15
materia: M26
orden: 15
titulo: Temas de perfil y marketplace lite
horas: 5
semana: 4
lectura: producto-saas — temas Free/Pro + catálogo
evidencia: projects/m26-capstone/temas-marketplace.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** - ≥2 temas built-in (1 free, 1 pro/preview) aplicables al
      perfil/menú público.

      - Catálogo con **1 tema de terceros** (Free o Paid listado) instalable por
      tenant.

      - Documentar reparto a creadores; Stripe Connect real = v1.1 (no bloquea
      egreso).


      Capstone. Hoy entregas **`projects/m26-capstone/temas-marketplace.md`**.
  - id: s2
    tipo: ejemplo
    titulo: 1. Built-in
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/temas-marketplace.md
      git commit -m "docs(m26): l15 temas marketplace lite"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Temas de perfil y marketplace lite" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m26-capstone/temas-marketplace.md
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

      `git add projects/m26-capstone/temas-marketplace.md`
    comandoEsperado:
      - git add projects/m26-capstone/temas-marketplace.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m26-capstone/temas-marketplace.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          - ≥2 temas built-in (1 free, 1 pro/preview) aplicables al perfil/menú
          público.

          - Catálogo con **1 tema de terceros** (Free o Paid listado)…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Terceros
    xp: 10
    cuerpo: >-
      Publica un tema “de terceros” en el catálogo (puede ser tuyo con autor
      distinto). Instalación por tenant deja evidencia en
      `temas-marketplace.md`.
  - id: s7
    tipo: explicacion
    titulo: 3. Billing temas
    xp: 10
    cuerpo: >-
      Si el tema es Paid: checkout a la **plataforma** (Stripe test). Anota en
      el doc el % de reparto previsto (Connect = post-egreso).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Dos temas built-in + uno de terceros listado.
      - Un tenant demo con tema instalado distinto al default.
      - Doc de marketplace en git.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — Temas de perfil y marketplace lite

**~5 h · Semana 4**

Capstone. Hoy entregas **`projects/m26-capstone/temas-marketplace.md`**.

## Objetivo

- ≥2 temas built-in (1 free, 1 pro/preview) aplicables al perfil/menú público.
- Catálogo con **1 tema de terceros** (Free o Paid listado) instalable por tenant.
- Documentar reparto a creadores; Stripe Connect real = v1.1 (no bloquea egreso).

## Formato de paquete (mínimo)

```
themes/<slug>/
  theme.json   # name, version, author, price_cents, preview
  styles.css   # o tokens
  README.md
```

## Pasos

### 1. Built-in (60–90 min)

Dos temas en el repo de la app; el tenant Free solo instala el free.

### 2. Terceros (60–90 min)

Publica un tema “de terceros” en el catálogo (puede ser tuyo con autor distinto). Instalación por tenant deja evidencia en `temas-marketplace.md`.

### 3. Billing temas (30 min)

Si el tema es Paid: checkout a la **plataforma** (Stripe test). Anota en el doc el % de reparto previsto (Connect = post-egreso).

### 4. Commit

```bash
git add projects/m26-capstone/temas-marketplace.md
git commit -m "docs(m26): l15 temas marketplace lite"
```

## Hecho cuando

1. Dos temas built-in + uno de terceros listado.
2. Un tenant demo con tema instalado distinto al default.
3. Doc de marketplace en git.

## Errores comunes

- Marketplace de apps completo (fuera de alcance).
- Bloquear egreso por Connect/payouts.

## Siguiente

[L16 — Demo interna semana 4 — flujos completos](L16-demo-interna-semana-4-flujos-completos.md)
