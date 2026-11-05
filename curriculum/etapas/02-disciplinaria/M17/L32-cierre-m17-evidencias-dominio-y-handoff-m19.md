---
id: L32
materia: M17
orden: 32
titulo: 'Cierre M17 — evidencias, dominio y handoff M19'
horas: 5
semana: 8
lectura: Ficha M17 criterios dominio
evidencia: projects/m17-vitrina/docs/nota-cierre-m17.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - cierre

      - handoff M19

      - dominio


      **Objetivo de esta lección:** Auditar P1–P3, proyecto piloto, criterios
      dominio, README final y handoff deploy M19.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Índice de evidencias
    xp: 10
    cuerpo: >-
      ```bash cat > projects/m17-vitrina/docs/nota-cierre-m17.md << 'EOF' #
      Cierre M17
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M17 — evidencias, dominio y handoff M19», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M17 —
          evidencias, dominio y hand…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Cerrar M17 sin listar gaps."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
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
          Auditar P1–P3, proyecto piloto, criterios dominio, README final y
          handoff deploy M19.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “No mencionar handoff Docker/secrets a M19."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M17
    xp: 25
    enunciado: >-
      Cierra **Aplicaciones web full-stack** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: API REST con auth real + validación'
      - 'P2: Front con rutas protegidas y estados de carga/error'
      - 'P3: Integración WhatsApp deep-links + panel admin con roles'
      - 'Proyecto: MVP Vitrina (piloto) listo para multi-tenant'
      - projects/m17-vitrina/docs/nota-cierre-m17.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          Existe `projects/m17-vitrina/docs/nota-cierre-m17.md` con índice de
          artefactos y handoff M19.
      - id: r3
        criterio: >-
          README P1–P3 coherente con evidencias (artefacto:
          `projects/m17-vitrina/docs/nota-cierre-m17.md`).
      - id: r4
        criterio: 'Commit `docs(m17): L32 cierre-m17-evidencias-dominio-y-handoff-m19`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/nota-cierre-m17.md` con índice de
        artefactos y handoff M19.
      - >-
        README P1–P3 coherente con evidencias (artefacto:
        `projects/m17-vitrina/docs/nota-cierre-m17.md`).
      - 'Commit `docs(m17): L32 cierre-m17-evidencias-dominio-y-handoff-m19`.'
    siguiente: Materia M17 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L32 — Cierre M17 — evidencias, dominio y handoff M19

**~5.0 h · Semana 8**

Cierras la materia más densa del plan disciplinario.

## Objetivo

Auditar P1–P3, proyecto piloto, criterios dominio, README final y handoff deploy M19.

## Conceptos clave

- cierre
- handoff M19
- dominio

## Pasos (hazlos en orden)

### 1. Índice de evidencias (50–60 min)

```bash
cat > projects/m17-vitrina/docs/nota-cierre-m17.md << 'EOF'
# Cierre M17
## Artefactos
- stack.md, docs/auth.md, permisos.md, ui-estados.md
- integracion-whatsapp.md, deploy.md, smoke-test.md
- owasp-mapa.md, adr-tenant-id.md, checklist-saas.md
## Handoff M19
Dockerfile pendiente / Compose / secrets → projects/m19-ops/
EOF
ls projects/m17-vitrina/docs
```

### 2. README proyecto + commit (40 min)

Actualiza checklist P1–P3 del README. Enlace a M19.

```bash
git add projects/m17-vitrina
git commit -m "docs(m17): L32 cierre evidencias handoff m19"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 criterios dominio | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/nota-cierre-m17.md` con índice de artefactos y handoff M19.
2. README P1–P3 coherente con evidencias (artefacto: `projects/m17-vitrina/docs/nota-cierre-m17.md`).
3. Commit `docs(m17): L32 cierre-m17-evidencias-dominio-y-handoff-m19`.

## Errores comunes

- Cerrar M17 sin listar gaps.
- No mencionar handoff Docker/secrets a M19.

## Siguiente

Materia siguiente: [M18 — Seguridad AppSec](../M18-seguridad.md) (en paralelo práctico con deploy M19).
