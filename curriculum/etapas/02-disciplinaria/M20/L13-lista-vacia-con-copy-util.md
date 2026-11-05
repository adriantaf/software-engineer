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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - empty state

      - copy


      **Objetivo de esta lección:** UI cuando no hay pedidos semana; CTA
      coherente con producto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Empty state útil
    xp: 10
    cuerpo: 'Copy: “No hay pedidos hoy — crea la primera en la web o aquí”. CTA claro.'
  - id: s3
    tipo: ejemplo
    titulo: Evidencia P2
    xp: 10
    cuerpo: '```bash cat >> projects/m20-movil/demo-login-lista.md << ''EOF'''
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lista vacía con copy útil», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lista vacía con copy
          útil
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Vacío = pantalla blanca."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: UI cuando no hay pedidos semana; CTA coherente con producto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Copy técnico (‘array length 0’)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Empty state con copy útil documentado en demo-login-lista.md.
      - 'Commit `docs(m20): L13 lista-vacia-con-copy-util`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
