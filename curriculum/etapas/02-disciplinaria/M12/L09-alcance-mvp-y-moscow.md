---
id: L09
materia: M12
orden: 9
titulo: Alcance MVP y MoSCoW
horas: 5
semana: 3
lectura: producto-saas fases + priorización
evidencia: srs-borrador alcance MoSCoW
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Congelar alcance MVP con MoSCoW en el borrador SRS.

      Decir “no” es un entregable. Hoy priorizas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
      git commit -m "docs(m12): l09 moscow mvp"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Alcance MVP y MoSCoW" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: srs-borrador alcance MoSCoW
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

      `git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md`
    comandoEsperado:
      - git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/m12-srs/srs-borrador.md
      projects/m12-srs/stories.md
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Congelar alcance MVP con MoSCoW en el borrador SRS.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. MoSCoW
    xp: 10
    cuerpo: >-
      | US | MoSCoW | Justificación 1 línea |

      |----|--------|----------------------|


      Must típicos: auth owner, clientes, pedidos CRUD básico, agenda del día.
      Won't: multi-tenant, Stripe, IA, app móvil nativa.
  - id: s7
    tipo: explicacion
    titulo: 3. Capacidad
    xp: 10
    cuerpo: Escribe supuestos de velocidad (1 dev) y qué cae si algo Must se atrasa.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Tabla MoSCoW de todas las US + lista explícita Won't (multi-tenant,
        billing, IA…).
      - 'Párrafo: por qué el Must cabe en ~4 semanas de build hacia M17.'
      - 'Commit `docs(m12): l09 moscow mvp`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Alcance MVP y MoSCoW

**~5.0 h · Semana 3**

Decir “no” es un entregable. Hoy priorizas.

## Objetivo

Congelar alcance MVP con MoSCoW en el borrador SRS.

## Pasos

### 1. Inventario (30 min)

Lista US-xx existentes.

### 2. MoSCoW (75 min)

| US | MoSCoW | Justificación 1 línea |
|----|--------|----------------------|

Must típicos: auth owner, clientes, pedidos CRUD básico, agenda del día. Won't: multi-tenant, Stripe, IA, app móvil nativa.

### 3. Capacidad (40 min)

Escribe supuestos de velocidad (1 dev) y qué cae si algo Must se atrasa.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
git commit -m "docs(m12): l09 moscow mvp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | MVP 4 semanas build; Must/Should/Could/Won't | [producto-saas.md](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla MoSCoW de todas las US + lista explícita Won't (multi-tenant, billing, IA…).
2. Párrafo: por qué el Must cabe en ~4 semanas de build hacia M17.
3. Commit `docs(m12): l09 moscow mvp`.

## Errores comunes

- Todo es Must.
- Won't vacío.
- MVP que incluye pagos + IA + multi-sucursal.

## Siguiente

[L10 — Requisitos funcionales en SRS](L10-requisitos-funcionales-en-srs.md)
