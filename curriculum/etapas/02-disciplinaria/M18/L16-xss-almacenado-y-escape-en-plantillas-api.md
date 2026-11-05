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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.


      **Objetivo de esta lección:** Fix escape/sanitización; actualizar finding;
      filas SQLi+XSS en `projects/m18-appsec/findings-table.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Stored en notas de pedido
    xp: 10
    cuerpo: >-
      ```bash

      # Crea pedido con payload en notas (cuenta prueba)

      curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
      application/json' -b /tmp/m18-cj \
        -d '{"clienteId":"…","inicio":"2026-01-02T10:00:00Z","notas":"<img src=x onerror=alert(1)>"}'
      # Lista y verifica escape en HTML

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Fix + test
    xp: 10
    cuerpo: >-
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


      Usa textContent / escape del framework; evita `dangerouslySetInnerHTML`
      con input usuario.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «XSS almacenado y escape en plantillas/API», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de XSS almacenado y escape
          en plantillas/A…
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


      `curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
      application/json' -b /tmp/m18-cj \`
    comandoEsperado:
      - >-
        curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
        application/json' -b /tmp/m18-cj \
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -X POST localhost:3000/api/pedidos -H 'content-type:
      application/json' -b /tmp/m18-cj \
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
          Fix escape/sanitización; actualizar finding; filas SQLi+XSS en
          `projects/m18-appsec/findings-table.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tabla P2
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
