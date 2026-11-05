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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - tenant_id

      - ADR

      - single-tenant piloto


      **Objetivo de esta lección:** ADR: dónde va `tenant_id`/`negocio_id`,
      migración futura, queries siempre filtradas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: ADR tenant_id
    xp: 10
    cuerpo: >-
      ```bash cat > projects/m17-vitrina/docs/adr-tenant-id.md << 'EOF' # ADR:
      tenant_id / multi-negocio
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «ADR tenant_id y modelo multi-negocio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de ADR tenant_id y modelo
          multi-negocio
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
    pregunta: ¿Es recomendable en esta lección? “ADR genérico sin Vitrina."
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
          ADR: dónde va `tenant_id`/`negocio_id`, migración futura, queries
          siempre filtradas.
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
    pregunta: ¿Debes hacer esto? “Implementar multi-tenant completo sin necesidad."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/adr-tenant-id.md` con
        contexto/decisión/consecuencias.
      - 'Commit `docs(m17): L29 adr-tenant-id-y-modelo-multi-negocio`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
