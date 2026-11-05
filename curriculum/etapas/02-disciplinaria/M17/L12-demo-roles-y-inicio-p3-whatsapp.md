---
id: L12
materia: M17
orden: 12
titulo: Demo roles y inicio P3 WhatsApp
horas: 5
semana: 3
lectura: Ficha P3 parcial
evidencia: projects/m17-vitrina/docs/demo-roles.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - demo

      - roles

      - evidencia


      **Objetivo de esta lección:** Grabar o documentar pasos demo: owner vs
      staff en acción bloqueada.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Guion demo roles
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/demo-roles.md << 'EOF'
      # Demo roles
      1. Login owner → /admin OK
      2. Login staff → /admin 403 / UI oculta
      3. Ambos crean pedido
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Ejecuta y anota
    xp: 10
    cuerpo: |-
      ```bash
      npm run seed
      # recorre el guion con dos sesiones/cookies
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Demo roles y inicio P3 WhatsApp», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Demo roles y inicio P3
          WhatsApp
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

      `npm run seed`
    comandoEsperado:
      - npm run seed
      - git add projects/m17-vitrina/docs
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm run seed'
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
        texto: 'Grabar o documentar pasos demo: owner vs staff en acción bloqueada.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Kickoff P3 WhatsApp (30 min) + commit
    xp: 10
    cuerpo: >-
      Crea borrador `docs/integracion-whatsapp.md` (enlace wa.me, sin API
      Business obligatoria).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/demo-roles.md` con guion owner vs
        staff.
      - Borrador `projects/m17-vitrina/docs/integracion-whatsapp.md`.
      - 'Commit `docs(m17): L12 demo-roles-y-inicio-p3-whatsapp`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Demo roles y inicio P3 WhatsApp

**~5.0 h · Semana 3**

P3 requiere evidencia reproducible para el design partner.

## Objetivo

Grabar o documentar pasos demo: owner vs staff en acción bloqueada.

## Conceptos clave

- demo
- roles
- evidencia

## Pasos (hazlos en orden)

### 1. Guion demo roles (50–60 min)

```bash
cat > projects/m17-vitrina/docs/demo-roles.md << 'EOF'
# Demo roles
1. Login owner → /admin OK
2. Login staff → /admin 403 / UI oculta
3. Ambos crean pedido
EOF
```

### 2. Ejecuta y anota (40–50 min)

```bash
npm run seed
# recorre el guion con dos sesiones/cookies
```

### 3. Kickoff P3 WhatsApp (30 min) + commit

Crea borrador `docs/integracion-whatsapp.md` (enlace wa.me, sin API Business obligatoria).

```bash
git add projects/m17-vitrina/docs
git commit -m "docs(m17): L12 demo roles inicio whatsapp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha P3 parcial | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/demo-roles.md` con guion owner vs staff.
2. Borrador `projects/m17-vitrina/docs/integracion-whatsapp.md`.
3. Commit `docs(m17): L12 demo-roles-y-inicio-p3-whatsapp`.

## Errores comunes

- Demo sin contraste owner/staff.
- Prometer WhatsApp Business API sin scope.

## Siguiente

[L13 — Scaffold front y rutas protegidas](L13-scaffold-front-y-rutas-protegidas.md)
