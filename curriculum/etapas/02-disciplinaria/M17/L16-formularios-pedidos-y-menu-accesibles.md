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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - form

      - a11y

      - validación


      **Objetivo de esta lección:** Crear/editar pedido y cliente con validación
      inline alineada a API.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Forms accesibles
    xp: 10
    cuerpo: |-
      ```bash
      # Tab order completo; Enter envía; error anunciado
      # Anota checklist en docs/ui-estados.md
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Verifica teclado
    xp: 10
    cuerpo: |-
      ```bash
      # Tab order completo; Enter envía; error anunciado
      # Anota checklist en docs/ui-estados.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Formularios pedidos y clientes accesibles», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Formularios pedidos y
          clientes accesibl…
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

      `git add projects/m17-vitrina`
    comandoEsperado:
      - git add projects/m17-vitrina
      - 'git commit -m "feat(m17): L16 formularios pedidos clientes a11y"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m17-vitrina'
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
        texto: Crear/editar pedido y cliente con validación inline alineada a API.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
