---
id: L05
materia: M20
orden: 5
titulo: Lista de pedidos autenticada
horas: 5
semana: 2
lectura: ListView / FlatList patterns
evidencia: projects/m20-movil/demo-login-lista.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - Authorization header

      - JSON parse

      - orden


      **Objetivo de esta lección:** GET pedidos con token; mostrar fecha,
      cliente, servicio, estado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: GET /pedidos autenticado
    xp: 10
    cuerpo: |-
      ```bash
      # Misma cookie/Bearer que web — documenta el esquema en stack-movil.md
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos"
      ```

      Lista en UI con fecha/cliente/servicio.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Evidencia P1
    xp: 10
    cuerpo: |-
      ```bash
      # Misma cookie/Bearer que web — documenta el esquema en stack-movil.md
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lista de pedidos autenticada», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lista de pedidos
          autenticada
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

      `curl -sS -b /tmp/st.ck "$API_BASE/pedidos"`
    comandoEsperado:
      - curl -sS -b /tmp/st.ck "$API_BASE/pedidos"
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS -b /tmp/st.ck "$API_BASE/pedidos"'
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
        texto: 'GET pedidos con token; mostrar fecha, cliente, servicio, estado.'
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
    pregunta: ¿Debes hacer esto? “Sin auth header/cookie."
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
      - >-
        `projects/m20-movil/demo-login-lista.md` registra lista de pedidos
        contra API real (P1).
      - 'Commit `docs(m20): L05 lista-de-pedidos-autenticada`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Lista de pedidos autenticada

**~5.0 h · Semana 2**

P1 M20: login + lista evidenciada.

## Objetivo

GET pedidos con token; mostrar fecha, cliente, servicio, estado.

## Conceptos clave

- Authorization header
- JSON parse
- orden

## Pasos (hazlos en orden)

### 1. GET /pedidos autenticado (80–100 min)

```bash
# Misma cookie/Bearer que web — documenta el esquema en stack-movil.md
curl -sS -b /tmp/st.ck "$API_BASE/pedidos"
```

Lista en UI con fecha/cliente/servicio.

### 2. Evidencia P1 (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Lista pedidos
Fecha demo: …  API: staging …  Resultado: OK
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L05 lista pedidos autenticada"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | ListView / FlatList patterns | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/demo-login-lista.md` registra lista de pedidos contra API real (P1).
2. Commit `docs(m20): L05 lista-de-pedidos-autenticada`.

## Errores comunes

- Lista desde JSON local fingiendo API.
- Sin auth header/cookie.

## Siguiente

[L06 — Pull-to-refresh y paginación simple](L06-pull-to-refresh-y-paginacion-simple.md)
