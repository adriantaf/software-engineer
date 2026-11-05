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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** PoC o “no reproducible con ORM” en
      `projects/m18-appsec/findings/001-sqli.md` (sin PII real).


      Solo contra tu API. P2 empieza con hallazgo real; SQLi sigue vivo en ORMs
      mal usados.
  - id: s2
    tipo: ejemplo
    titulo: 1. Caza concatenación SQL
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n "\$\{|query\(|\.query\(|execute\(|raw\(|sql`" -g '!node_modules' |
      head -50

      rg -n "SELECT.*\+|WHERE.*\+" -g '*.ts' -g '*.js' | head -20 || true

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "SQLi: reproducir en tu propia API" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/findings/001-sqli.md
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
          PoC o “no reproducible con ORM” en
          `projects/m18-appsec/findings/001-sqli.md` (sin PII real).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. PoC controlada
    xp: 10
    cuerpo: >-
      Cuenta de prueba. Payload en búsqueda clientes/pedidos. **No** `DROP` en
      staging compartido.


      ```bash

      mkdir -p projects/m18-appsec/findings projects/m18-appsec/pocs

      cat > projects/m18-appsec/findings/001-sqli.md <<'EOF'

      Finding 001 — SQLi

      - Endpoint:

      - Payload (ejemplo): `' OR '1'='1`

      - Respuesta / impacto:

      - ¿ORM parametrizado? evidencia:

      - PII: ninguna en este reporte

      EOF

      Ejemplo de prueba (ajusta query param)

      curl -sG "localhost:3000/api/clientes" --data-urlencode "q=' OR '1'='1" |
      head -c 400

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
