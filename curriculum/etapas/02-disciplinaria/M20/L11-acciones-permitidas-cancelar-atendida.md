---
id: L11
materia: M20
orden: 11
titulo: 'Acciones permitidas: cancelar / atendida'
horas: 5
semana: 3
lectura: Mutations HTTP
evidencia: commit si API expone
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - mutation

      - optimistic UI opcional


      **Objetivo de esta lección:** Llamar PATCH/POST que la API expone;
      deshabilitar si 403.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Acciones cancelar/atendida
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \
        -H 'content-type: application/json' \
        -d '{"estado":"cancelada"}'
      ```

      Botones solo si el rol/API lo permiten; maneja 403.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L11 acciones cancelar atendida"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Acciones permitidas: cancelar / atendida», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Acciones permitidas:
          cancelar / atendida
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

      `curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \`
    comandoEsperado:
      - curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \
      - git add projects/m20-movil
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado"
      \
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
        texto: Llamar PATCH/POST que la API expone; deshabilitar si 403.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git add projects/m20-movil`
    comandoEsperado:
      - git add projects/m20-movil
    explicacionError: 'Esperado: git add projects/m20-movil'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Acciones cancelar/atendida llaman API; 403 manejado (artefacto: `commit
        si API expone`).
      - 'Commit `docs(m20): L11 acciones-permitidas-cancelar-atendida`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Acciones permitidas: cancelar / atendida

**~5.0 h · Semana 3**

Solo acciones que el backend autoriza.

## Objetivo

Llamar PATCH/POST que la API expone; deshabilitar si 403.

## Conceptos clave

- mutation
- optimistic UI opcional

## Pasos (hazlos en orden)

### 1. Acciones cancelar/atendida (70–90 min)

```bash
curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \
  -H 'content-type: application/json' \
  -d '{"estado":"cancelada"}'
```

Botones solo si el rol/API lo permiten; maneja 403.

### 2. Commit (15 min)

```bash
git add projects/m20-movil
git commit -m "feat(m20): L11 acciones cancelar atendida"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Mutations HTTP | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Acciones cancelar/atendida llaman API; 403 manejado (artefacto: `commit si API expone`).
2. Commit `docs(m20): L11 acciones-permitidas-cancelar-atendida`.

## Errores comunes

- Cambiar estado solo en memoria local.
- No manejar 403.

## Siguiente

[L12 — Deep link opcional a una pedido](L12-deep-link-opcional-a-una-pedido.md)
