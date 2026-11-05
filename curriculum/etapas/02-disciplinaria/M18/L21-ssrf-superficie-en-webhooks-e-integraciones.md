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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Aun sin feature URL, documentar el control evita sorpresas en M26.


      **Objetivo de esta lección:** Doc SSRF + allowlist en
      `projects/m18-appsec/findings/004-ssrf.md`. Sin escanear terceros ni
      metadata cloud en prod.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Busca fetch server-side
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'fetch\(|axios\.|got\(|request\(|http\.get' -g '!node_modules' |
      head -40

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Diseño / PoC aislada
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>

      rg -n 'fetch\(|axios\.|got\(|request\(|http\.get' -g '!node_modules' |
      head -40

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «SSRF: superficie en webhooks e integraciones», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de SSRF: superficie en
          webhooks e integrac…
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
          Doc SSRF + allowlist en `projects/m18-appsec/findings/004-ssrf.md`.
          Sin escanear terceros ni metadata cloud en prod.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “SSRF ‘para probar AWS’ en cuenta ajena."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
