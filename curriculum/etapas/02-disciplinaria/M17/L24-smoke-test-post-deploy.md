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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - smoke

      - staging

      - regresión manual


      **Objetivo de esta lección:** Script o checklist: register/login/crear
      pedido en staging.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Smoke script
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Registra resultado + commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/smoke-test.md
      git commit -m "docs(m17): L24 smoke test post-deploy"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Smoke test post-deploy», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Smoke test post-deploy
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
      - >-
        curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H 'content-type:
        application/json' \
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
        texto: 'Script o checklist: register/login/crear pedido en staging.'
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
    enunciado: >-
      Ahora el siguiente comando de la secuencia:


      `curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H 'content-type:
      application/json' \`
    comandoEsperado:
      - >-
        curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H 'content-type:
        application/json' \
    explicacionError: >-
      Esperado: curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H
      'content-type: application/json' \
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/smoke-test.md` con health+login+pedido y
        fecha/resultado.
      - 'Commit `docs(m17): L24 smoke-test-post-deploy`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
