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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Llamar PATCH/POST que la API expone; deshabilitar si 403.

      - mutation
      - optimistic UI opcional
  - id: s2
    tipo: ejemplo
    titulo: 1. Acciones cancelar/atendida
    xp: 10
    cuerpo: |-
      ```bash
      curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \
        -H 'content-type: application/json' \
        -d '{"estado":"cancelada"}'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Acciones permitidas: cancelar / atendida" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: commit si API expone
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

      `curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \`
    comandoEsperado:
      - curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado" \
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/pedidos/<id>/estado"
      \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Llamar PATCH/POST que la API expone; deshabilitar si 403.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L11 acciones cancelar atendida"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Acciones cancelar/atendida llaman API; 403 manejado (artefacto: `commit
        si API expone`).
      - 'Commit `docs(m20): L11 acciones-permitidas-cancelar-atendida`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
