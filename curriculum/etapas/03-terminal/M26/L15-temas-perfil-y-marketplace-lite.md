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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Capstone. Hoy entregas **`projects/m26-capstone/temas-marketplace.md`**.


      **Objetivo de esta lección:** - ≥2 temas built-in (1 free, 1 pro/preview)
      aplicables al perfil/menú público.

      - Catálogo con **1 tema de terceros** (Free o Paid listado) instalable por
      tenant.

      - Documentar reparto a creadores; Stripe Connect real = v1.1 (no bloquea
      egreso).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Built-in
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/temas-marketplace.md
      git commit -m "docs(m26): l15 temas marketplace lite"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Terceros
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m26-capstone/temas-marketplace.md
      git commit -m "docs(m26): l15 temas marketplace lite"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Temas de perfil y marketplace lite», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Dos temas built-in + uno de terceros listado.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Temas de perfil y
          marketplace lite
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

      `git add projects/m26-capstone/temas-marketplace.md`
    comandoEsperado:
      - git add projects/m26-capstone/temas-marketplace.md
      - 'git commit -m "docs(m26): l15 temas marketplace lite"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m26-capstone/temas-marketplace.md'
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
          - ≥2 temas built-in (1 free, 1 pro/preview) aplicables al perfil/menú
          público. - Catálogo con 1 tema de terceros (Free o Paid listado)
          instalable por tenant. -…
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Billing temas
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
