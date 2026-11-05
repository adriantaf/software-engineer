---
id: L07
materia: M19
orden: 7
titulo: 'Smoke test: login, pedido y health externo'
horas: 5
semana: 2
lectura: Runbook borrador
evidencia: projects/m19-ops/smoke-staging.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Ejecutar checklist smoke desde fuera de tu laptop: login,
      crear pedido, GET /health.


      - smoke test

      - datos prueba
  - id: s2
    tipo: ejemplo
    titulo: 1. Smoke staging
    xp: 10
    cuerpo: >-
      ```bash

      BASE=https://TU-STAGING.example

      curl -sS "$BASE/health"

      curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \
        -H 'content-type: application/json' \
        -d '{"email":"owner@demo.local","password":"***"}'
      curl -sS -b /tmp/st.ck -X POST "$BASE/pedidos" -H 'content-type:
      application/json' -d '{...}'

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Smoke test: login, pedido y health externo" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/smoke-staging.md
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

      `curl -sS "$BASE/health"`
    comandoEsperado:
      - curl -sS "$BASE/health"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sS "$BASE/health"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Ejecutar checklist smoke desde fuera de tu laptop: login, crear
          pedido, GET /health.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta smoke-staging.md
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/smoke-staging.md << 'EOF'
      Smoke staging
      Fecha: …  Health: OK  Login: OK  Pedido: OK
      EOF
      git add projects/m19-ops/smoke-staging.md
      git commit -m "docs(m19): L07 smoke staging login pedido"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/smoke-staging.md` con health+login+pedido y fecha (sin
        passwords).
      - 'Commit `docs(m19): L07 smoke-test-login-pedido-y-health-externo`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Smoke test: login, pedido y health externo

**~5.0 h · Semana 2**

‘Contenedor verde’ ≠ producto usable.

## Objetivo

Ejecutar checklist smoke desde fuera de tu laptop: login, crear pedido, GET /health.

## Conceptos clave

- smoke test
- datos prueba

## Pasos (hazlos en orden)

### 1. Smoke staging (60–80 min)

```bash
BASE=https://TU-STAGING.example
curl -sS "$BASE/health"
curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \
  -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"***"}'
curl -sS -b /tmp/st.ck -X POST "$BASE/pedidos" -H 'content-type: application/json' -d '{...}'
```

**No** pegues el password en el markdown.

### 2. Documenta smoke-staging.md (30 min)

```bash
cat > projects/m19-ops/smoke-staging.md << 'EOF'
# Smoke staging
Fecha: …  Health: OK  Login: OK  Pedido: OK
EOF
git add projects/m19-ops/smoke-staging.md
git commit -m "docs(m19): L07 smoke staging login pedido"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Runbook borrador | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/smoke-staging.md` con health+login+pedido y fecha (sin passwords).
2. Commit `docs(m19): L07 smoke-test-login-pedido-y-health-externo`.

## Errores comunes

- Smoke solo health, sin login/pedido.
- Password en el markdown.

## Siguiente

[L08 — Dominios y deploy-log semana 2](L08-dominios-y-deploy-log-semana-2.md)
