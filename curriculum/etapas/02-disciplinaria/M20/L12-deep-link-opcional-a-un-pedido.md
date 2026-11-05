---
id: L12
materia: M20
orden: 12
titulo: Deep link opcional a una pedido
horas: 5
semana: 3
lectura: Deep linking intro
evidencia: projects/m20-movil/deep-link.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - deep link

      - routing


      **Objetivo de esta lección:** Configurar esquema o ruta para abrir detalle
      desde URL/notificación futura.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Deep link pedido
    xp: 10
    cuerpo: >-
      ```bash

      # Android intent-filter / iOS universal link — scheme
      agendaops://pedido/<id>

      cat > projects/m20-movil/deep-link.md << 'EOF'

      # Deep links

      Scheme: agendaops://pedido/:id

      Prueba: adb shell am start -a android.intent.action.VIEW -d
      "agendaops://pedido/UUID"

      EOF

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil/deep-link.md
      git commit -m "feat(m20): L12 deep link pedido"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Deep link opcional a una pedido», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Deep link opcional a
          una pedido
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

      `git add projects/m20-movil/deep-link.md`
    comandoEsperado:
      - git add projects/m20-movil/deep-link.md
      - 'git commit -m "feat(m20): L12 deep link pedido"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m20-movil/deep-link.md'
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
        texto: >-
          Configurar esquema o ruta para abrir detalle desde URL/notificación
          futura.
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

      `git commit -m "feat(m20): L12 deep link pedido"`
    comandoEsperado:
      - 'git commit -m "feat(m20): L12 deep link pedido"'
    explicacionError: 'Esperado: git commit -m "feat(m20): L12 deep link pedido"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m20-movil/deep-link.md` con scheme y comando de prueba.
      - 'Commit `docs(m20): L12 deep-link-opcional-a-una-pedido`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Deep link opcional a una pedido

**~5.0 h · Semana 3**

Preparación recordatorios WhatsApp futuro.

## Objetivo

Configurar esquema o ruta para abrir detalle desde URL/notificación futura.

## Conceptos clave

- deep link
- routing

## Pasos (hazlos en orden)

### 1. Deep link pedido (60–80 min)

```bash
# Android intent-filter / iOS universal link — scheme agendaops://pedido/<id>
cat > projects/m20-movil/deep-link.md << 'EOF'
# Deep links
Scheme: agendaops://pedido/:id
Prueba: adb shell am start -a android.intent.action.VIEW -d "agendaops://pedido/UUID"
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil/deep-link.md
git commit -m "feat(m20): L12 deep link pedido"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Deep linking intro | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m20-movil/deep-link.md` con scheme y comando de prueba.
2. Commit `docs(m20): L12 deep-link-opcional-a-una-pedido`.

## Errores comunes

- Deep link sin documentación de prueba.
- Abrir http genérico sin ruta.

## Siguiente

[L13 — Lista vacía con copy útil](L13-lista-vacia-con-copy-util.md)
