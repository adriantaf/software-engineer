---
id: L21
materia: M18
orden: 21
titulo: 'SSRF: superficie en webhooks e integraciones'
horas: 5
semana: 6
lectura: SSRF Prevention Cheat Sheet
evidencia: projects/m18-appsec/findings/004-ssrf.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Doc SSRF + allowlist en
      `projects/m18-appsec/findings/004-ssrf.md`. Sin escanear terceros ni
      metadata cloud en prod.


      Aun sin feature URL, documentar el control evita sorpresas en M26.
  - id: s2
    tipo: ejemplo
    titulo: 1. Busca fetch server-side
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'fetch\(|axios\.|got\(|request\(|http\.get' -g '!node_modules' |
      head -40

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "SSRF: superficie en webhooks e integraciones" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/findings/004-ssrf.md
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
          Doc SSRF + allowlist en `projects/m18-appsec/findings/004-ssrf.md`.
          Sin escanear terceros ni metadata cloud en prod.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Diseño / PoC aislada
    xp: 10
    cuerpo: >-
      Si no hay feature: simula diseño. Si hay: prueba URL interna **solo en
      staging aislado**.


      ```bash

      cat > projects/m18-appsec/findings/004-ssrf.md <<'EOF'

      Finding 004 — SSRF (superficie)
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Doc SSRF con allowlist (artefacto:
        `projects/m18-appsec/findings/004-ssrf.md`).
      - 'Riesgo nombrado (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).'
      - 'Commit `docs(m18): L21 ssrf-superficie-en-webhooks-e-integraciones`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L21 — SSRF: superficie en webhooks e integraciones

**~5.0 h · Semana 6**

Aun sin feature URL, documentar el control evita sorpresas en M26.

## Objetivo

Doc SSRF + allowlist en `projects/m18-appsec/findings/004-ssrf.md`. Sin escanear terceros ni metadata cloud en prod.

## Pasos

### 1. Busca fetch server-side (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'fetch\(|axios\.|got\(|request\(|http\.get' -g '!node_modules' | head -40
```
### 2. Diseño / PoC aislada (70–90 min)

Si no hay feature: simula diseño. Si hay: prueba URL interna **solo en staging aislado**.

```bash
cat > projects/m18-appsec/findings/004-ssrf.md <<'EOF'
# Finding 004 — SSRF (superficie)
## ¿Hay URL server-side hoy?
- webhook / import / avatar: sí/no · ruta:

## Riesgo ilustrativo
`http://169.254.169.254/` (metadata) — **no probar en cloud compartido**

## Allowlist propuesta
- hosts: `hooks.stripe.com`, …
- schemata: https only
- bloqueo: link-local, RFC1918, localhost

## Estado
- N/A feature | Mitigado | Abierto
EOF
```

```ts
function assertSafeUrl(raw: string) {
  const u = new URL(raw);
  if (u.protocol !== "https:") throw new Error("scheme");
  const allow = new Set(["hooks.example.com"]);
  if (!allow.has(u.hostname)) throw new Error("host");
}
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/004-ssrf.md
git commit -m "docs(m18): l21 ssrf superficie"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | SSRF Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc SSRF con allowlist (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
2. Riesgo nombrado (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
3. Commit `docs(m18): L21 ssrf-superficie-en-webhooks-e-integraciones`.

## Errores comunes

- curl a metadata cloud en prod.
- SSRF ‘para probar AWS’ en cuenta ajena.

## Siguiente

[L22 — Subida de archivos segura](L22-subida-de-archivos-segura.md)
