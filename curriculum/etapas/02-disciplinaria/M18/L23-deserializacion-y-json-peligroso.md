---
id: L23
materia: M18
orden: 23
titulo: Deserialización y JSON peligroso
horas: 5
semana: 6
lectura: Deserialization + API hardening
evidencia: projects/m18-appsec/docs/json-trust.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `projects/m18-appsec/docs/json-trust.md`: endpoints +
      schema; límite de body; ≥1 mejora commitada.


      Node rara vez hace Java deserialization, pero prototype pollution y lógica
      sí.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario JSON bodies
    xp: 10
    cuerpo: |-
      ```ts
      app.use(express.json({ limit: "100kb" }));

      // zod: strip o strict
      const CitaInput = z.object({
        clienteId: z.string().uuid(),
        inicio: z.string().datetime(),
        notas: z.string().max(2000).optional(),
      }).strict();
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Deserialización y JSON peligroso" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/docs/json-trust.md
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

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          `projects/m18-appsec/docs/json-trust.md`: endpoints + schema; límite
          de body; ≥1 mejora commitada.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Límite + rechazo campos extra
    xp: 10
    cuerpo: >-
      ```ts

      app.use(express.json({ limit: "100kb" }));


      // zod: strip o strict

      const CitaInput = z.object({
        clienteId: z.string().uuid(),
        inicio: z.string().datetime(),
        notas: z.string().max(2000).optional(),
      }).strict();

      ```


      ```bash

      Payload enorme → 413

      python3 - <<'PY'

      print('{"x":"' + ('a'*200000) + '"}')

      PY | curl -s -o /dev/null -w "%{http_code}\n" -X POST
      localhost:3000/api/pedidos \
        -H 'content-type: application/json' -b /tmp/m18-cj --data-binary @-
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/docs/json-trust.md
      git commit -m "fix(m18): l23 json trust limits"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Lista endpoints + validación (artefacto:
        `projects/m18-appsec/docs/json-trust.md`).
      - >-
        Límite tamaño body (artefacto:
        `projects/m18-appsec/docs/json-trust.md`).
      - 'Commit `docs(m18): L23 deserializacion-y-json-peligroso`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L23 — Deserialización y JSON peligroso

**~5.0 h · Semana 6**

Node rara vez hace Java deserialization, pero prototype pollution y lógica sí.

## Objetivo

`projects/m18-appsec/docs/json-trust.md`: endpoints + schema; límite de body; ≥1 mejora commitada.

## Pasos

### 1. Inventario JSON bodies (40–50 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "express\.json|bodyParser|z\.object|Joi\.|safeParse" -g '!node_modules' | head -40
cat > projects/m18-appsec/docs/json-trust.md <<'EOF'
# JSON trust
| Endpoint | Schema (zod/joi/…) | Límite body | Notas |
|----------|--------------------|-------------|-------|
| POST /auth/login | | | |
| POST /api/pedidos | | | |
EOF
```
### 2. Límite + rechazo campos extra (60–80 min)

```ts
app.use(express.json({ limit: "100kb" }));

// zod: strip o strict
const CitaInput = z.object({
  clienteId: z.string().uuid(),
  inicio: z.string().datetime(),
  notas: z.string().max(2000).optional(),
}).strict();
```

```bash
# Payload enorme → 413
python3 - <<'PY'
print('{"x":"' + ('a'*200000) + '"}')
PY | curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/pedidos \
  -H 'content-type: application/json' -b /tmp/m18-cj --data-binary @-
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/json-trust.md
git commit -m "fix(m18): l23 json trust limits"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Deserialization + API hardening | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Lista endpoints + validación (artefacto: `projects/m18-appsec/docs/json-trust.md`).
2. Límite tamaño body (artefacto: `projects/m18-appsec/docs/json-trust.md`).
3. Commit `docs(m18): L23 deserializacion-y-json-peligroso`.

## Errores comunes

- Aceptar cualquier JSON.
- Confiar en tipos TS solo compile-time.

## Siguiente

[L24 — Consolidar hallazgos semana 6 en P2](L24-consolidar-hallazgos-semana-6-en-p2.md)
