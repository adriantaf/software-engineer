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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Auditar P1–P3, proyecto piloto, criterios dominio, README
      final y handoff deploy M19.


      - cierre

      - handoff M19

      - dominio
  - id: s2
    tipo: ejemplo
    titulo: 1. Índice de evidencias
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/nota-cierre-m17.md << 'EOF'
      Cierre M17
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M17 — evidencias, dominio y handoff M19" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/nota-cierre-m17.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Cerrar M17 sin listar gaps."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Auditar P1–P3, proyecto piloto, criterios dominio, README final y
          handoff deploy M19.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
