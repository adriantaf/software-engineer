---
id: L15
materia: M18
orden: 15
titulo: XSS reflejado en campos de cliente o búsqueda
horas: 5
semana: 4
lectura: XSS Prevention Cheat Sheet
evidencia: projects/m18-appsec/findings/002-xss-reflected.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** PoC reflejado en
      `projects/m18-appsec/findings/002-xss-reflected.md` (solo tu cuenta de
      prueba; sin exfiltración externa).


      XSS roba sesiones si las cookies son legibles por JS.
  - id: s2
    tipo: ejemplo
    titulo: 1. Localiza render de input
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'dangerouslySetInnerHTML|innerHTML|\$\{.*q|searchParams|mensaje' -g
      '!node_modules' | head -30

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "XSS reflejado en campos de cliente o búsqueda" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/findings/002-xss-reflected.md
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
          PoC reflejado en `projects/m18-appsec/findings/002-xss-reflected.md`
          (solo tu cuenta de prueba; sin exfiltración externa).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. PoC local
    xp: 10
    cuerpo: >-
      Payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`.
      Solo impacto local.


      ```bash

      cat > projects/m18-appsec/findings/002-xss-reflected.md <<'EOF'

      Finding 002 — XSS reflejado

      - Pantalla / query:

      - Payload:

      - ¿Ejecutó en el navegador? sí/no

      - Contexto (HTML text / attr / JS):

      EOF

      Ejemplo

      curl -sG "localhost:3000/clientes" --data-urlencode
      "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/findings/002-xss-reflected.md
      git commit -m "docs(m18): l15 poc xss reflected"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        PoC documentada (artefacto:
        `projects/m18-appsec/findings/002-xss-reflected.md`).
      - >-
        Contexto identificado (artefacto:
        `projects/m18-appsec/findings/002-xss-reflected.md`).
      - 'Commit `docs(m18): L15 xss-reflejado-en-campos-de-cliente-o-busqueda`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — XSS reflejado en campos de cliente o búsqueda

**~5.0 h · Semana 4**

XSS roba sesiones si las cookies son legibles por JS.

## Objetivo

PoC reflejado en `projects/m18-appsec/findings/002-xss-reflected.md` (solo tu cuenta de prueba; sin exfiltración externa).

## Pasos

### 1. Localiza render de input (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'dangerouslySetInnerHTML|innerHTML|\$\{.*q|searchParams|mensaje' -g '!node_modules' | head -30
```
### 2. PoC local (60–80 min)

Payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`. Solo impacto local.

```bash
cat > projects/m18-appsec/findings/002-xss-reflected.md <<'EOF'
# Finding 002 — XSS reflejado
- Pantalla / query:
- Payload:
- ¿Ejecutó en el navegador? sí/no
- Contexto (HTML text / attr / JS):
EOF
# Ejemplo
curl -sG "localhost:3000/clientes" --data-urlencode "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/002-xss-reflected.md
git commit -m "docs(m18): l15 poc xss reflected"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | XSS Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. PoC documentada (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
2. Contexto identificado (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
3. Commit `docs(m18): L15 xss-reflejado-en-campos-de-cliente-o-busqueda`.

## Errores comunes

- XSS persistente en prod sin aviso.
- Confiar en ‘React escapa todo’.

## Siguiente

[L16 — XSS almacenado y escape en plantillas/API](L16-xss-almacenado-y-escape-en-plantillas-api.md)
