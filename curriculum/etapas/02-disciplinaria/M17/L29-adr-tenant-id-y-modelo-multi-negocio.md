---
id: L29
materia: M17
orden: 29
titulo: ADR tenant_id y modelo multi-negocio
horas: 5
semana: 8
lectura: producto-saas multi-tenant
evidencia: projects/m17-vitrina/docs/adr-tenant-id.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** ADR: dónde va `tenant_id`/`negocio_id`, migración futura,
      queries siempre filtradas.


      - tenant_id

      - ADR

      - single-tenant piloto
  - id: s2
    tipo: ejemplo
    titulo: 1. ADR tenant_id
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/adr-tenant-id.md << 'EOF'
      ADR: tenant_id / multi-negocio
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "ADR tenant_id y modelo multi-negocio" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/adr-tenant-id.md
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
    pregunta: ¿Es buena práctica en esta lección? “ADR genérico sin Vitrina."
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
          ADR: dónde va `tenant_id`/`negocio_id`, migración futura, queries
          siempre filtradas.
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
        Existe `projects/m17-vitrina/docs/adr-tenant-id.md` con
        contexto/decisión/consecuencias.
      - 'Commit `docs(m17): L29 adr-tenant-id-y-modelo-multi-negocio`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L29 — ADR tenant_id y modelo multi-negocio

**~5.0 h · Semana 8**

M26 depende de esta decisión; M17 la prepara.

## Objetivo

ADR: dónde va `tenant_id`/`negocio_id`, migración futura, queries siempre filtradas.

## Conceptos clave

- tenant_id
- ADR
- single-tenant piloto

## Pasos (hazlos en orden)

### 1. ADR tenant_id (70–90 min)

```bash
cat > projects/m17-vitrina/docs/adr-tenant-id.md << 'EOF'
# ADR: tenant_id / multi-negocio
## Contexto
Piloto single-tenant hoy; camino a SaaS.
## Decisión
Columna/negocio_id nullable ahora; queries siempre filtradas cuando presente.
## Consecuencias
...
EOF
```

### 2. Marca código futuro (30 min)

```ts
// TODO(tenant): filtrar por negocio_id en listados
```

```bash
git add projects/m17-vitrina/docs/adr-tenant-id.md
git commit -m "docs(m17): L29 adr tenant_id multi-negocio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | producto-saas multi-tenant | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/adr-tenant-id.md` con contexto/decisión/consecuencias.
2. Commit `docs(m17): L29 adr-tenant-id-y-modelo-multi-negocio`.

## Errores comunes

- ADR genérico sin Vitrina.
- Implementar multi-tenant completo sin necesidad.

## Siguiente

[L30 — Checklist camino a SaaS](L30-checklist-camino-a-saas.md)
