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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Ocultar botones no basta: autorización server-side.


      **Objetivo de esta lección:** PoC cross-user en
      `projects/m18-appsec/findings/003-idor.md` con dos cuentas de prueba.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dos usuarios de prueba
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: PoC IDOR
    xp: 10
    cuerpo: >-
      ```bash

      CITA_ID=…  # id creado por A

      curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-b
      localhost:3000/api/pedidos/$CITA_ID

      # esperado tras fix: 403 o 404 (no 200 con datos de A)


      cat > projects/m18-appsec/findings/003-idor.md <<'EOF'

      # Finding 003 — IDOR

      - Ruta: GET/PUT /api/pedidos/:id

      - Pasos:

      - Impacto:

      - Estado:

      EOF

      ```


      A crea pedido → B intenta `GET/PUT /api/pedidos/:id`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «IDOR en pedidos y recursos por ID», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de IDOR en pedidos y
          recursos por ID
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type:
      application/json' \`
    comandoEsperado:
      - >-
        curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H
        'content-type: application/json' \
      - >-
        curl -c /tmp/m18-b -s -X POST localhost:3000/auth/login -H
        'content-type: application/json' \
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H
      'content-type: application/json' \
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
          PoC cross-user en `projects/m18-appsec/findings/003-idor.md` con dos
          cuentas de prueba.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
