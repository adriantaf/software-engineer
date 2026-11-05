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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Node rara vez hace Java deserialization, pero prototype pollution y lógica
      sí.


      **Objetivo de esta lección:** `projects/m18-appsec/docs/json-trust.md`:
      endpoints + schema; límite de body; ≥1 mejora commitada.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario JSON bodies
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n "express\.json|bodyParser|z\.object|Joi\.|safeParse" -g
      '!node_modules' | head -40

      cat > projects/m18-appsec/docs/json-trust.md <<'EOF'

      # JSON trust

      | Endpoint | Schema (zod/joi/…) | Límite body | Notas |

      |----------|--------------------|-------------|-------|

      | POST /auth/login | | | |

      | POST /api/pedidos | | | |

      EOF

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Límite + rechazo campos extra
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Deserialización y JSON peligroso», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Deserialización y JSON
          peligroso
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

      `cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>`
    comandoEsperado:
      - cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>'
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
          `projects/m18-appsec/docs/json-trust.md`: endpoints + schema; límite
          de body; ≥1 mejora commitada.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
