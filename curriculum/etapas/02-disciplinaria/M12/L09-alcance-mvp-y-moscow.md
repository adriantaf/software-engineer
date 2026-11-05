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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Decir “no” es un entregable. Hoy priorizas.


      **Objetivo de esta lección:** Congelar alcance MVP con MoSCoW en el
      borrador SRS.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
      git commit -m "docs(m12): l09 moscow mvp"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: MoSCoW
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
      git commit -m "docs(m12): l09 moscow mvp"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Alcance MVP y MoSCoW», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Alcance MVP y MoSCoW
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

      `git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md`
    comandoEsperado:
      - git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
      - 'git commit -m "docs(m12): l09 moscow mvp"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/m12-srs/srs-borrador.md
      projects/m12-srs/stories.md
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
        texto: Congelar alcance MVP con MoSCoW en el borrador SRS.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Capacidad
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
