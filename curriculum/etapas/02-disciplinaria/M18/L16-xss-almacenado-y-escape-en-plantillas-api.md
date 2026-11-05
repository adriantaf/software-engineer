---
id: L16
materia: M18
orden: 16
titulo: XSS almacenado y escape en plantillas/API
horas: 5
semana: 4
lectura: DOM XSS + stored XSS
evidencia: commit fix + findings/002 actualizado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Fix escape/sanitización; actualizar finding; filas SQLi+XSS
      en `projects/m18-appsec/findings-table.md`.


      El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.
  - id: s2
    tipo: ejemplo
    titulo: 1. Stored en notas de pedido
    xp: 10
    cuerpo: |-
      ```ts
      // API: devolver texto; el front escapa al render
      // Test:
      it("escapes stored XSS in notas", async () => {
        const payload = "<script>alert(1)</script>";
        await createCita({ notas: payload });
        const html = await renderListaCitas();
        expect(html).not.toContain("<script>");
        expect(html).toContain("&lt;script&gt;") // o equivalente escapado
      });
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "XSS almacenado y escape en plantillas/API" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: commit fix + findings/002 actualizado
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


      `curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
      application/json' -b /tmp/m18-cj \`
    comandoEsperado:
      - >-
        curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
        application/json' -b /tmp/m18-cj \
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
      application/json' -b /tmp/m18-cj \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Fix escape/sanitización; actualizar finding; filas SQLi+XSS en
          `projects/m18-appsec/findings-table.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Fix + test
    xp: 10
    cuerpo: >-
      Usa textContent / escape del framework; evita `dangerouslySetInnerHTML`
      con input usuario.


      ```ts

      // API: devolver texto; el front escapa al render

      // Test:

      it("escapes stored XSS in notas", async () => {
        const payload = "<script>alert(1)</script>";
        await createCita({ notas: payload });
        const html = await renderListaCitas();
        expect(html).not.toContain("<script>");
        expect(html).toContain("&lt;script&gt;") // o equivalente escapado
      });

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Tabla P2
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/findings-table.md <<'EOF'
      # Findings P2
      | ID | OWASP | PoC | Commit fix | Test |
      |----|-------|-----|------------|------|
      | 001 | A03 | findings/001-sqli.md | | |
      | 002 | A03/XSS | findings/002-xss-reflected.md | | |
      EOF
      git add -A && git commit -m "fix(m18): l16 xss stored escape"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '≥2 filas en findings-table (artefacto: `commit fix`).'
      - 'Test o verificación manual repetible (artefacto: `commit fix`).'
      - 'Commit `docs(m18): L16 xss-almacenado-y-escape-en-plantillas-api`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — XSS almacenado y escape en plantillas/API

**~5.0 h · Semana 4**

El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.

## Objetivo

Fix escape/sanitización; actualizar finding; filas SQLi+XSS en `projects/m18-appsec/findings-table.md`.

## Pasos

### 1. Stored en notas de pedido (50–60 min)

```bash
# Crea pedido con payload en notas (cuenta prueba)
curl -s -X POST localhost:3000/api/pedidos -H 'content-type: application/json' -b /tmp/m18-cj \
  -d '{"clienteId":"…","inicio":"2026-01-02T10:00:00Z","notas":"<img src=x onerror=alert(1)>"}'
# Lista y verifica escape en HTML
```
### 2. Fix + test (60–80 min)

Usa textContent / escape del framework; evita `dangerouslySetInnerHTML` con input usuario.

```ts
// API: devolver texto; el front escapa al render
// Test:
it("escapes stored XSS in notas", async () => {
  const payload = "<script>alert(1)</script>";
  await createCita({ notas: payload });
  const html = await renderListaCitas();
  expect(html).not.toContain("<script>");
  expect(html).toContain("&lt;script&gt;") // o equivalente escapado
});
```
### 3. Tabla P2 (20–30 min)

```bash
cat > projects/m18-appsec/findings-table.md <<'EOF'
# Findings P2
| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | | |
| 002 | A03/XSS | findings/002-xss-reflected.md | | |
EOF
git add -A && git commit -m "fix(m18): l16 xss stored escape"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | DOM XSS + stored XSS | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥2 filas en findings-table (artefacto: `commit fix`).
2. Test o verificación manual repetible (artefacto: `commit fix`).
3. Commit `docs(m18): L16 xss-almacenado-y-escape-en-plantillas-api`.

## Errores comunes

- strip_tags inventado.
- innerHTML con input usuario.

## Siguiente

[L17 — IDOR en pedidos y recursos por ID](L17-idor-en-pedidos-y-recursos-por-id.md)
