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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - smoke test

      - datos prueba


      **Objetivo de esta lección:** Ejecutar checklist smoke desde fuera de tu
      laptop: login, crear pedido, GET /health.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Smoke staging
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


      **No** pegues el password en el markdown.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta smoke-staging.md
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/smoke-staging.md << 'EOF'
      # Smoke staging
      Fecha: …  Health: OK  Login: OK  Pedido: OK
      EOF
      git add projects/m19-ops/smoke-staging.md
      git commit -m "docs(m19): L07 smoke staging login pedido"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Smoke test: login, pedido y health externo», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Smoke test: login,
          pedido y health exte…
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

      `curl -sS "$BASE/health"`
    comandoEsperado:
      - curl -sS "$BASE/health"
      - curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS "$BASE/health"'
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
          Ejecutar checklist smoke desde fuera de tu laptop: login, crear
          pedido, GET /health.
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

      `curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \`
    comandoEsperado:
      - curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \
    explicacionError: 'Esperado: curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" \'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/smoke-staging.md` con health+login+pedido y fecha (sin
        passwords).
      - 'Commit `docs(m19): L07 smoke-test-login-pedido-y-health-externo`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
