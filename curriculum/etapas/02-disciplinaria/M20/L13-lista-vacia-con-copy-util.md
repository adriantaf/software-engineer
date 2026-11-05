---
id: L13
materia: M20
orden: 13
titulo: Lista vacía con copy útil
horas: 5
semana: 4
lectura: Empty states UX
evidencia: capturas P2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** UI cuando no hay pedidos semana; CTA coherente con producto.

      - empty state
      - copy
  - id: s2
    tipo: ejemplo
    titulo: 1. Empty state útil
    xp: 10
    cuerpo: 'Copy: “No hay pedidos hoy — crea la primera en la web o aquí”. CTA claro.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Lista vacía con copy útil" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: capturas P2
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
    pregunta: ¿Es buena práctica en esta lección? “Vacío = pantalla blanca."
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
        texto: UI cuando no hay pedidos semana; CTA coherente con producto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Evidencia P2
    xp: 10
    cuerpo: |-
      ```bash
      cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Empty state con copy útil documentado en demo-login-lista.md.
      - 'Commit `docs(m20): L13 lista-vacia-con-copy-util`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Lista vacía con copy útil

**~5.0 h · Semana 4**

P2 pide estados vacío/error.

## Objetivo

UI cuando no hay pedidos semana; CTA coherente con producto.

## Conceptos clave

- empty state
- copy

## Pasos (hazlos en orden)

### 1. Empty state útil (50–60 min)

Copy: “No hay pedidos hoy — crea la primera en la web o aquí”. CTA claro.

### 2. Evidencia P2 (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Lista vacía
Copy: …  Captura: …
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L13 lista vacia copy util"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Empty states UX | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Empty state con copy útil documentado en demo-login-lista.md.
2. Commit `docs(m20): L13 lista-vacia-con-copy-util`.

## Errores comunes

- Vacío = pantalla blanca.
- Copy técnico (‘array length 0’).

## Siguiente

[L14 — Sin red: banner y reintento](L14-sin-red-banner-y-reintento.md)
