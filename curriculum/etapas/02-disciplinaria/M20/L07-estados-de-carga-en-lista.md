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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Skeleton o spinner, deshabilitar doble tap, error con
      reintento.


      - loading

      - error retry
  - id: s2
    tipo: ejemplo
    titulo: 1. Estados loading/error
    xp: 10
    cuerpo: Spinner inicial; banner error con “Reintentar”; no lista fantasma.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Estados de carga en lista" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: captura en demo-login-lista.md
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Error silencioso (lista vacía
      falsa)."
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
        texto: 'Skeleton o spinner, deshabilitar doble tap, error con reintento.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Captura en demo doc
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
      - Estados loading/error documentados en demo-login-lista.md.
      - 'Commit `docs(m20): L07 estados-de-carga-en-lista`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
