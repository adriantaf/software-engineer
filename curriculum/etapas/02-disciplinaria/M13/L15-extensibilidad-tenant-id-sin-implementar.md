---
id: L15
materia: M13
orden: 15
titulo: Extensibilidad tenant_id sin implementar
horas: 5
semana: 4
lectura: producto-saas.md multi-tenant; nota de extensibilidad
evidencia: adr/004-extensibilidad-tenant.md o seccion en arquitectura.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Nota de extensibilidad legible por el yo-de-M17/M19.


      El camino a SaaS pide `tenant_id` después. Hoy dejas el gancho **sin**
      construir el edificio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lee producto-saas
    xp: 10
    cuerpo: 'Sección evolución técnica: piloto single-tenant → tenants.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Extensibilidad tenant_id sin implementar" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: adr/004-extensibilidad-tenant.md o seccion en arquitectura.md
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Implementar multi-tenant completo en
      diseño día 1."
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
        texto: Nota de extensibilidad legible por el yo-de-M17/M19.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe la nota
    xp: 10
    cuerpo: |-
      `adr/004-extensibilidad-tenant.md`:

      ```markdown
      Nota — Extensibilidad multi-tenant
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Documento que explica single-tenant del piloto y *dónde* se añadirá
        `tenant_id` (tablas/capas).
      - >-
        Lista explícita de lo que NO implementas aún (billing, onboarding
        multi-negocio).
      - 'Commit `docs(m13): nota extensibilidad tenant_id`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — Extensibilidad tenant_id sin implementar

**~5.0 h · Semana 4**

El camino a SaaS pide `tenant_id` después. Hoy dejas el gancho **sin** construir el edificio.

## Objetivo

Nota de extensibilidad legible por el yo-de-M17/M19.

## Pasos (hazlos en orden)

### 1. Lee producto-saas (25 min)

Sección evolución técnica: piloto single-tenant → tenants.

### 2. Escribe la nota (80–100 min)

`adr/004-extensibilidad-tenant.md`:

```markdown
# Nota — Extensibilidad multi-tenant

## Ahora (piloto)
Un negocio design partner. `negocioId` implícito o constante de config.

## Después
Columna `tenant_id` en clientes, servicios, pedidos, usuarios.
Queries siempre filtran por tenant. Tests IDOR cross-tenant en M15/M18.

## Qué no hacemos hoy
Stripe, onboarding self-serve, N esquemas Postgres.
```

### 3. Marca en clases.md (30 min)

Comentario: “candidato a tenant_id” en entidades de negocio.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): nota extensibilidad tenant_id"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Single-tenant ahora; dónde encajará tenant_id después | [Producto SaaS — evolución técnica](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Documento que explica single-tenant del piloto y *dónde* se añadirá `tenant_id` (tablas/capas).
2. Lista explícita de lo que NO implementas aún (billing, onboarding multi-negocio).
3. Commit `docs(m13): nota extensibilidad tenant_id`.

## Errores comunes

- Implementar multi-tenant completo en diseño día 1.
- Ignorar tenant y luego reescribir todo el esquema.
- Poner tenant_id solo en el front.

## Siguiente

[L16 — ADR auth y sesión](L16-adr-auth-y-sesion.md)
