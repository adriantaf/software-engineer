---
id: L13
materia: M18
orden: 13
titulo: 'SQLi: reproducir en tu propia API'
horas: 5
semana: 4
lectura: OWASP A03 Injection + SQLi Prevention
evidencia: projects/m18-appsec/findings/001-sqli.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Solo contra tu API. P2 empieza con hallazgo real; SQLi sigue vivo en ORMs
      mal usados.


      **Objetivo de esta lección:** PoC o “no reproducible con ORM” en
      `projects/m18-appsec/findings/001-sqli.md` (sin PII real).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Caza concatenación SQL
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n "\$\{|query\(|\.query\(|execute\(|raw\(|sql`" -g '!node_modules' |
      head -50

      rg -n "SELECT.*\+|WHERE.*\+" -g '*.ts' -g '*.js' | head -20 || true

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: PoC controlada
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m18-appsec/findings projects/m18-appsec/pocs

      cat > projects/m18-appsec/findings/001-sqli.md <<'EOF'

      # Finding 001 — SQLi

      - Endpoint:

      - Payload (ejemplo): `' OR '1'='1`

      - Respuesta / impacto:

      - ¿ORM parametrizado? evidencia:

      - PII: ninguna en este reporte

      EOF

      # Ejemplo de prueba (ajusta query param)

      curl -sG "localhost:3000/api/clientes" --data-urlencode "q=' OR '1'='1" |
      head -c 400

      ```


      Cuenta de prueba. Payload en búsqueda clientes/pedidos. **No** `DROP` en
      staging compartido.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «SQLi: reproducir en tu propia API», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de SQLi: reproducir en tu
          propia API
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
      - mkdir -p projects/m18-appsec/findings projects/m18-appsec/pocs
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
          PoC o “no reproducible con ORM” en
          `projects/m18-appsec/findings/001-sqli.md` (sin PII real).
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
      git add projects/m18-appsec/findings/001-sqli.md
      git commit -m "docs(m18): l13 poc sqli"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Finding documentado o prueba de mitigación (artefacto:
        `projects/m18-appsec/findings/001-sqli.md`).
      - 'Solo tu entorno (artefacto: `projects/m18-appsec/findings/001-sqli.md`).'
      - 'Commit `docs(m18): L13 sqli-reproducir-en-tu-propia-api`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — SQLi: reproducir en tu propia API

**~5.0 h · Semana 4**

Solo contra tu API. P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.

## Objetivo

PoC o “no reproducible con ORM” en `projects/m18-appsec/findings/001-sqli.md` (sin PII real).

## Pasos

### 1. Caza concatenación SQL (50–60 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\$\{|query\(|\.query\(|execute\(|raw\(|sql`" -g '!node_modules' | head -50
rg -n "SELECT.*\+|WHERE.*\+" -g '*.ts' -g '*.js' | head -20 || true
```
### 2. PoC controlada (60–80 min)

Cuenta de prueba. Payload en búsqueda clientes/pedidos. **No** `DROP` en staging compartido.

```bash
mkdir -p projects/m18-appsec/findings projects/m18-appsec/pocs
cat > projects/m18-appsec/findings/001-sqli.md <<'EOF'
# Finding 001 — SQLi
- Endpoint:
- Payload (ejemplo): `' OR '1'='1`
- Respuesta / impacto:
- ¿ORM parametrizado? evidencia:
- PII: ninguna en este reporte
EOF
# Ejemplo de prueba (ajusta query param)
curl -sG "localhost:3000/api/clientes" --data-urlencode "q=' OR '1'='1" | head -c 400
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/001-sqli.md
git commit -m "docs(m18): l13 poc sqli"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A03 Injection + SQLi Prevention | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Finding documentado o prueba de mitigación (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
2. Solo tu entorno (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
3. Commit `docs(m18): L13 sqli-reproducir-en-tu-propia-api`.

## Errores comunes

- SQLi en producción de terceros.
- Drop table en staging compartido.

## Siguiente

[L14 — Mitigar SQLi: queries parametrizadas y permisos DB](L14-mitigar-sqli-queries-parametrizadas-y-permisos-db.md)
