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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** GET pedidos con token; mostrar fecha, cliente, servicio,
      estado.


      - Authorization header

      - JSON parse

      - orden
  - id: s2
    tipo: ejemplo
    titulo: 1. GET /pedidos autenticado
    xp: 10
    cuerpo: |-
      ```bash
      # Misma cookie/Bearer que web — documenta el esquema en stack-movil.md
      curl -sS -b /tmp/st.ck "$API_BASE/pedidos"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Lista de pedidos autenticada" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/demo-login-lista.md
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

      `curl -sS -b /tmp/st.ck "$API_BASE/pedidos"`
    comandoEsperado:
      - curl -sS -b /tmp/st.ck "$API_BASE/pedidos"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sS -b /tmp/st.ck "$API_BASE/pedidos"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'GET pedidos con token; mostrar fecha, cliente, servicio, estado.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Evidencia P1
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
      - >-
        `projects/m20-movil/demo-login-lista.md` registra lista de pedidos
        contra API real (P1).
      - 'Commit `docs(m20): L05 lista-de-pedidos-autenticada`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
