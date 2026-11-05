---
id: L16
materia: M17
orden: 16
titulo: Formularios pedidos y clientes accesibles
horas: 5
semana: 4
lectura: MDN forms a11y básica
evidencia: formularios create
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear/editar pedido y cliente con validación inline alineada
      a API.


      - form

      - a11y

      - validación
  - id: s2
    tipo: ejemplo
    titulo: 1. Forms accesibles
    xp: 10
    cuerpo: |-
      ```bash
      # Tab order completo; Enter envía; error anunciado
      # Anota checklist en docs/ui-estados.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Formularios pedidos y clientes accesibles" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: formularios create
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

      `git add projects/m17-vitrina`
    comandoEsperado:
      - git add projects/m17-vitrina
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m17-vitrina'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Crear/editar pedido y cliente con validación inline alineada a API.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Verifica teclado
    xp: 10
    cuerpo: |-
      ```bash
      Tab order completo; Enter envía; error anunciado
      Anota checklist en docs/ui-estados.md
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina
      git commit -m "feat(m17): L16 formularios pedidos clientes a11y"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Forms pedido/cliente con labels, errores de campo y orden de tab
        documentado.
      - 'Commit `docs(m17): L16 formularios-pedidos-y-clientes-accesibles`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Formularios pedidos y clientes accesibles

**~5.0 h · Semana 4**

Errores server mapeados a campos.

## Objetivo

Crear/editar pedido y cliente con validación inline alineada a API.

## Conceptos clave

- form
- a11y
- validación

## Pasos (hazlos en orden)

### 1. Forms accesibles (80–100 min)

Labels asociados, `aria-invalid`, mensajes de error ligados al campo. Crear pedido + cliente.

### 2. Verifica teclado (30 min)

```bash
# Tab order completo; Enter envía; error anunciado
# Anota checklist en docs/ui-estados.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L16 formularios pedidos clientes a11y"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN forms a11y básica | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Forms pedido/cliente con labels, errores de campo y orden de tab documentado.
2. Commit `docs(m17): L16 formularios-pedidos-y-clientes-accesibles`.

## Errores comunes

- Inputs sin `<label>` / placeholder como único texto.
- Errores solo en toast no asociado.

## Siguiente

[L17 — Deep links WhatsApp — diseño del mensaje](L17-deep-links-whatsapp-diseno-del-mensaje.md)
