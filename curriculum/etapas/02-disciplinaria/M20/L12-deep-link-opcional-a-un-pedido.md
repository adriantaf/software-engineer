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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Configurar esquema o ruta para abrir detalle desde
      URL/notificación futura.


      - deep link

      - routing
  - id: s2
    tipo: ejemplo
    titulo: 1. Deep link pedido
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Deep link opcional a una pedido" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/deep-link.md
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

      `git add projects/m20-movil/deep-link.md`
    comandoEsperado:
      - git add projects/m20-movil/deep-link.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m20-movil/deep-link.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Configurar esquema o ruta para abrir detalle desde URL/notificación
          futura.
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
      git add projects/m20-movil/deep-link.md
      git commit -m "feat(m20): L12 deep link pedido"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m20-movil/deep-link.md` con scheme y comando de prueba.
      - 'Commit `docs(m20): L12 deep-link-opcional-a-una-pedido`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
