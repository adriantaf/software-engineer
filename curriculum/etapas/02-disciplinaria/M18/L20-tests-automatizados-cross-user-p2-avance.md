---
id: L20
materia: M18
orden: 20
titulo: Tests automatizados cross-user (P2 avance)
horas: 5
semana: 5
lectura: Testing access control
evidencia: tests en repo producto + projects/m18-appsec/findings-table.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 pide hallazgo→fix→test; hoy consolidas access control.


      **Objetivo de esta lección:** ≥2 tests authz (cross-user + rol) +
      `projects/m18-appsec/findings-table.md` con ≥3 filas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Fixture dos usuarios
    xp: 10
    cuerpo: |-
      ```ts
      // tests/security/authz-cross-user.test.ts
      async function login(email: string) { /* cookie jar / token */ }

      it("B cannot read A's pedido", async () => {
        const a = await login("a@test.local");
        const b = await login("b@test.local");
        const pedido = await a.post("/api/pedidos", { /* … */ });
        const res = await b.get(`/api/pedidos/${pedido.id}`);
        expect([403, 404]).toContain(res.status);
      });

      it("staff cannot patch settings", async () => {
        const staff = await login("staff@test.local");
        const res = await staff.patch("/api/settings", { tz: "UTC" });
        expect(res.status).toBe(403);
      });
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Corre tests + actualiza tabla
    xp: 10
    cuerpo: |-
      ```bash
      npm test -- --testPathPattern=authz || npm test -- security
      # Actualiza findings-table: 001–003 + rate limit
      rg -n '^\|' projects/m18-appsec/findings-table.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests automatizados cross-user (P2 avance)», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests automatizados
          cross-user (P2 avan…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Tests que mockean auth siempre true."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
          ≥2 tests authz (cross-user + rol) +
          `projects/m18-appsec/findings-table.md` con ≥3 filas.
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
      git add -A && git commit -m "test(m18): l20 authz cross-user"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '≥2 tests authz verdes (artefacto: `tests en repo producto`).'
      - 'findings-table ≥3 filas (artefacto: `tests en repo producto`).'
      - 'Commit `docs(m18): L20 tests-automatizados-cross-user-p2-avance`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Tests automatizados cross-user (P2 avance)

**~5.0 h · Semana 5**

P2 pide hallazgo→fix→test; hoy consolidas access control.

## Objetivo

≥2 tests authz (cross-user + rol) + `projects/m18-appsec/findings-table.md` con ≥3 filas.

## Pasos

### 1. Fixture dos usuarios (30–40 min)

```ts
// tests/security/authz-cross-user.test.ts
async function login(email: string) { /* cookie jar / token */ }

it("B cannot read A's pedido", async () => {
  const a = await login("a@test.local");
  const b = await login("b@test.local");
  const pedido = await a.post("/api/pedidos", { /* … */ });
  const res = await b.get(`/api/pedidos/${pedido.id}`);
  expect([403, 404]).toContain(res.status);
});

it("staff cannot patch settings", async () => {
  const staff = await login("staff@test.local");
  const res = await staff.patch("/api/settings", { tz: "UTC" });
  expect(res.status).toBe(403);
});
```
### 2. Corre tests + actualiza tabla (60–80 min)

```bash
npm test -- --testPathPattern=authz || npm test -- security
# Actualiza findings-table: 001–003 + rate limit
rg -n '^\|' projects/m18-appsec/findings-table.md
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "test(m18): l20 authz cross-user"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Testing access control | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥2 tests authz verdes (artefacto: `tests en repo producto`).
2. findings-table ≥3 filas (artefacto: `tests en repo producto`).
3. Commit `docs(m18): L20 tests-automatizados-cross-user-p2-avance`.

## Errores comunes

- Tests que mockean auth siempre true.
- Un solo usuario en tests.

## Siguiente

[L21 — SSRF: superficie en webhooks e integraciones](L21-ssrf-superficie-en-webhooks-e-integraciones.md)
