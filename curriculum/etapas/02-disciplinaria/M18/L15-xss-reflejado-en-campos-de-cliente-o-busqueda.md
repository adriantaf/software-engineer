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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      XSS roba sesiones si las cookies son legibles por JS.


      **Objetivo de esta lección:** PoC reflejado en
      `projects/m18-appsec/findings/002-xss-reflected.md` (solo tu cuenta de
      prueba; sin exfiltración externa).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Localiza render de input
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'dangerouslySetInnerHTML|innerHTML|\$\{.*q|searchParams|mensaje' -g
      '!node_modules' | head -30

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: PoC local
    xp: 10
    cuerpo: >-
      ```bash

      cat > projects/m18-appsec/findings/002-xss-reflected.md <<'EOF'

      # Finding 002 — XSS reflejado

      - Pantalla / query:

      - Payload:

      - ¿Ejecutó en el navegador? sí/no

      - Contexto (HTML text / attr / JS):

      EOF

      # Ejemplo

      curl -sG "localhost:3000/clientes" --data-urlencode
      "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head

      ```


      Payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`.
      Solo impacto local.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «XSS reflejado en campos de cliente o búsqueda», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de XSS reflejado en campos
          de cliente o bú…
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
      - >-
        curl -sG "localhost:3000/clientes" --data-urlencode
        "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head
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
          PoC reflejado en `projects/m18-appsec/findings/002-xss-reflected.md`
          (solo tu cuenta de prueba; sin exfiltración externa).
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
