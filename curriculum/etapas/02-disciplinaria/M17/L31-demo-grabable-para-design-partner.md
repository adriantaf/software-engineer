---
id: L31
materia: M17
orden: 31
titulo: Demo grabable para design partner
horas: 5
semana: 8
lectura: Guion demo 10 min
evidencia: projects/m17-vitrina/docs/demo-script.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - demo

      - partner

      - staging


      **Objetivo de esta lección:** Guion demo: onboarding, pedido, WhatsApp,
      roles. URL staging y creds test.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Guion demo grabable
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/demo-script.md << 'EOF'
      # Demo design partner (≤8 min)
      1. Login owner
      2. Crear pedido
      3. Recordatorio WhatsApp
      4. Rol staff 403 admin
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Ensayo + nota
    xp: 10
    cuerpo: >-
      ```bash

      git add projects/m17-vitrina/docs/demo-script.md

      git commit -m "docs(m17): L31 demo script design partner"

      ```


      Cronometra. Anota URL staging y usuario demo (password en gestor, no en
      git).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Demo grabable para design partner», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Demo grabable para
          design partner
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

      `git add projects/m17-vitrina/docs/demo-script.md`
    comandoEsperado:
      - git add projects/m17-vitrina/docs/demo-script.md
      - 'git commit -m "docs(m17): L31 demo script design partner"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m17-vitrina/docs/demo-script.md'
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
          Guion demo: onboarding, pedido, WhatsApp, roles. URL staging y creds
          test.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git commit -m "docs(m17): L31 demo script design partner"`
    comandoEsperado:
      - 'git commit -m "docs(m17): L31 demo script design partner"'
    explicacionError: 'Esperado: git commit -m "docs(m17): L31 demo script design partner"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/demo-script.md` con guion ≤8 min y URL
        staging.
      - 'Commit `docs(m17): L31 demo-grabable-para-design-partner`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L31 — Demo grabable para design partner

**~5.0 h · Semana 8**

Validación real del MVP.

## Objetivo

Guion demo: onboarding, pedido, WhatsApp, roles. URL staging y creds test.

## Conceptos clave

- demo
- partner
- staging

## Pasos (hazlos en orden)

### 1. Guion demo grabable (50–60 min)

```bash
cat > projects/m17-vitrina/docs/demo-script.md << 'EOF'
# Demo design partner (≤8 min)
1. Login owner
2. Crear pedido
3. Recordatorio WhatsApp
4. Rol staff 403 admin
EOF
```

### 2. Ensayo + nota (40–50 min)

Cronometra. Anota URL staging y usuario demo (password en gestor, no en git).

```bash
git add projects/m17-vitrina/docs/demo-script.md
git commit -m "docs(m17): L31 demo script design partner"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Guion demo 10 min | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/demo-script.md` con guion ≤8 min y URL staging.
2. Commit `docs(m17): L31 demo-grabable-para-design-partner`.

## Errores comunes

- Guion de 30 minutos impracticable.
- Password demo en el markdown.

## Siguiente

[L32 — Cierre M17 — evidencias, dominio y handoff M19](L32-cierre-m17-evidencias-dominio-y-handoff-m19.md)
