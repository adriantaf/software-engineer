---
id: L07
materia: M20
orden: 7
titulo: Estados de carga en lista
horas: 5
semana: 2
lectura: UX loading skeletons
evidencia: captura en demo-login-lista.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - loading

      - error retry


      **Objetivo de esta lección:** Skeleton o spinner, deshabilitar doble tap,
      error con reintento.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Estados loading/error
    xp: 10
    cuerpo: Spinner inicial; banner error con “Reintentar”; no lista fantasma.
  - id: s3
    tipo: ejemplo
    titulo: Captura en demo doc
    xp: 10
    cuerpo: '```bash cat >> projects/m20-movil/demo-login-lista.md << ''EOF'''
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Estados de carga en lista», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Estados de carga en
          lista
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
    pregunta: ¿Es recomendable en esta lección? “Error silencioso (lista vacía falsa)."
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
        texto: 'Skeleton o spinner, deshabilitar doble tap, error con reintento.'
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
    pregunta: ¿Debes hacer esto? “Loading eterno."
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
      - Estados loading/error documentados en demo-login-lista.md.
      - 'Commit `docs(m20): L07 estados-de-carga-en-lista`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Estados de carga en lista

**~5.0 h · Semana 2**

Red móvil es lenta; la UI debe comunicarlo.

## Objetivo

Skeleton o spinner, deshabilitar doble tap, error con reintento.

## Conceptos clave

- loading
- error retry

## Pasos (hazlos en orden)

### 1. Estados loading/error (60–80 min)

Spinner inicial; banner error con “Reintentar”; no lista fantasma.

### 2. Captura en demo doc (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Estados carga
loading: …  error: … (captura redactada opcional)
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L07 estados carga lista"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | UX loading skeletons | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Estados loading/error documentados en demo-login-lista.md.
2. Commit `docs(m20): L07 estados-de-carga-en-lista`.

## Errores comunes

- Error silencioso (lista vacía falsa).
- Loading eterno.

## Siguiente

[L08 — Roles: confiar en la API, no solo en UI](L08-roles-confiar-en-la-api-no-solo-en-ui.md)
