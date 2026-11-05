---
id: L17
materia: M18
orden: 17
titulo: IDOR en pedidos y recursos por ID
horas: 5
semana: 5
lectura: OWASP A01 Broken Access Control
evidencia: projects/m18-appsec/findings/003-idor.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** PoC cross-user en `projects/m18-appsec/findings/003-idor.md`
      con dos cuentas de prueba.


      Ocultar botones no basta: autorización server-side.
  - id: s2
    tipo: ejemplo
    titulo: 1. Dos usuarios de prueba
    xp: 10
    cuerpo: >-
      ```bash

      # Login A y B; guarda cookies separadas

      curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type:
      application/json' \
        -d '{"email":"a@test.local","password":"***"}' -o /dev/null
      curl -c /tmp/m18-b -s -X POST localhost:3000/auth/login -H 'content-type:
      application/json' \
        -d '{"email":"b@test.local","password":"***"}' -o /dev/null
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "IDOR en pedidos y recursos por ID" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/findings/003-idor.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type:
      application/json' \`
    comandoEsperado:
      - >-
        curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H
        'content-type: application/json' \
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H
      'content-type: application/json' \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          PoC cross-user en `projects/m18-appsec/findings/003-idor.md` con dos
          cuentas de prueba.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. PoC IDOR
    xp: 10
    cuerpo: >-
      A crea pedido → B intenta `GET/PUT /api/pedidos/:id`.


      ```bash

      CITA_ID=…  # id creado por A

      curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-b
      localhost:3000/api/pedidos/$CITA_ID

      esperado tras fix: 403 o 404 (no 200 con datos de A)


      cat > projects/m18-appsec/findings/003-idor.md <<'EOF'

      Finding 003 — IDOR

      - Ruta: GET/PUT /api/pedidos/:id

      - Pasos:

      - Impacto:

      - Estado:

      EOF

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/findings/003-idor.md
      git commit -m "docs(m18): l17 poc idor"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        PoC con dos usuarios (artefacto:
        `projects/m18-appsec/findings/003-idor.md`).
      - >-
        Impacto descrito (artefacto:
        `projects/m18-appsec/findings/003-idor.md`).
      - 'Commit `docs(m18): L17 idor-en-pedidos-y-recursos-por-id`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — IDOR en pedidos y recursos por ID

**~5.0 h · Semana 5**

Ocultar botones no basta: autorización server-side.

## Objetivo

PoC cross-user en `projects/m18-appsec/findings/003-idor.md` con dos cuentas de prueba.

## Pasos

### 1. Dos usuarios de prueba (20–30 min)

```bash
# Login A y B; guarda cookies separadas
curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"a@test.local","password":"***"}' -o /dev/null
curl -c /tmp/m18-b -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"b@test.local","password":"***"}' -o /dev/null
```
### 2. PoC IDOR (60–80 min)

A crea pedido → B intenta `GET/PUT /api/pedidos/:id`.

```bash
CITA_ID=…  # id creado por A
curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-b localhost:3000/api/pedidos/$CITA_ID
# esperado tras fix: 403 o 404 (no 200 con datos de A)

cat > projects/m18-appsec/findings/003-idor.md <<'EOF'
# Finding 003 — IDOR
- Ruta: GET/PUT /api/pedidos/:id
- Pasos:
- Impacto:
- Estado:
EOF
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/003-idor.md
git commit -m "docs(m18): l17 poc idor"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A01 Broken Access Control | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. PoC con dos usuarios (artefacto: `projects/m18-appsec/findings/003-idor.md`).
2. Impacto descrito (artefacto: `projects/m18-appsec/findings/003-idor.md`).
3. Commit `docs(m18): L17 idor-en-pedidos-y-recursos-por-id`.

## Errores comunes

- Probar en datos de design partner real.
- Autorización solo en front.

## Siguiente

[L18 — Autorización por rol owner vs staff](L18-autorizacion-por-rol-owner-vs-staff.md)
