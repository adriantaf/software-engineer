---
id: L24
materia: M17
orden: 24
titulo: Smoke test post-deploy
horas: 5
semana: 6
lectura: Checklist smoke
evidencia: projects/m17-vitrina/docs/smoke-test.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Script o checklist: register/login/crear pedido en staging.

      - smoke
      - staging
      - regresión manual
  - id: s2
    tipo: ejemplo
    titulo: 1. Smoke script
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/smoke-test.md << 'EOF'
      # Smoke post-deploy
      1. GET /health → 200
      2. POST /auth/login (user demo staging)
      3. POST /pedidos → 201
      4. GET /pedidos → incluye la pedido
      Fecha: YYYY-MM-DD  Resultado: OK/FAIL
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Smoke test post-deploy" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/smoke-test.md
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
        texto: 'Script o checklist: register/login/crear pedido en staging.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Registra resultado + commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/smoke-test.md
      git commit -m "docs(m17): L24 smoke test post-deploy"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/smoke-test.md` con health+login+pedido y
        fecha/resultado.
      - 'Commit `docs(m17): L24 smoke-test-post-deploy`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L24 — Smoke test post-deploy

**~5.0 h · Semana 6**

Detecta config rota antes de la demo.

## Objetivo

Script o checklist: register/login/crear pedido en staging.

## Conceptos clave

- smoke
- staging
- regresión manual

## Pasos (hazlos en orden)

### 1. Smoke script (60–80 min)

```bash
cat > projects/m17-vitrina/docs/smoke-test.md << 'EOF'
# Smoke post-deploy
1. GET /health → 200
2. POST /auth/login (user demo staging)
3. POST /pedidos → 201
4. GET /pedidos → incluye la pedido
Fecha: YYYY-MM-DD  Resultado: OK/FAIL
EOF
```

```bash
BASE=https://TU-STAGING.example
curl -sS "$BASE/health"
curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"FROM_SECRET_MANAGER"}'
```

### 2. Registra resultado + commit (30 min)

```bash
git add projects/m17-vitrina/docs/smoke-test.md
git commit -m "docs(m17): L24 smoke test post-deploy"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Checklist smoke | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/smoke-test.md` con health+login+pedido y fecha/resultado.
2. Commit `docs(m17): L24 smoke-test-post-deploy`.

## Errores comunes

- Smoke sin fecha/resultado.
- Password de staging pegado en markdown.

## Siguiente

[L25 — Mapa OWASP Top 10 en el piloto](L25-mapa-owasp-top-10-en-el-piloto.md)
