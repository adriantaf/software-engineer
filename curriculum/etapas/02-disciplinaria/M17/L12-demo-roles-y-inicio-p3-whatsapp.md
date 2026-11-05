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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Grabar o documentar pasos demo: owner vs staff en acción
      bloqueada.


      - demo

      - roles

      - evidencia
  - id: s2
    tipo: ejemplo
    titulo: 1. Guion demo roles
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Demo roles y inicio P3 WhatsApp" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/demo-roles.md
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

      `npm run seed`
    comandoEsperado:
      - npm run seed
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm run seed'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Grabar o documentar pasos demo: owner vs staff en acción bloqueada.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ejecuta y anota
    xp: 10
    cuerpo: |-
      ```bash
      npm run seed
      recorre el guion con dos sesiones/cookies
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Kickoff P3 WhatsApp (30 min) + commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs
      git commit -m "docs(m17): L12 demo roles inicio whatsapp"
      ```
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
