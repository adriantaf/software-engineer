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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Guion demo: onboarding, pedido, WhatsApp, roles. URL staging
      y creds test.


      - demo

      - partner

      - staging
  - id: s2
    tipo: ejemplo
    titulo: 1. Guion demo grabable
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Demo grabable para design partner" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/demo-script.md
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

      `git add projects/m17-vitrina/docs/demo-script.md`
    comandoEsperado:
      - git add projects/m17-vitrina/docs/demo-script.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m17-vitrina/docs/demo-script.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Guion demo: onboarding, pedido, WhatsApp, roles. URL staging y creds
          test.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ensayo + nota
    xp: 10
    cuerpo: >-
      Cronometra. Anota URL staging y usuario demo (password en gestor, no en
      git).


      ```bash

      git add projects/m17-vitrina/docs/demo-script.md

      git commit -m "docs(m17): L31 demo script design partner"

      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/demo-script.md` con guion ≤8 min y URL
        staging.
      - 'Commit `docs(m17): L31 demo-grabable-para-design-partner`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
