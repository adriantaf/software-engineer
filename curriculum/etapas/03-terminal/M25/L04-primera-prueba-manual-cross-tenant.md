---
id: L04
materia: M25
orden: 4
titulo: Primera prueba manual cross-tenant
horas: 5
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/aislamiento/prueba-manual-01.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.


      Conceptos que debes poder explicar al cerrar:


      - IDOR

      - 403 vs 404

      - Evidencia reproducible


      **Objetivo de esta lección:** Intentar leer recurso del tenant B
      autenticado como A; documentar resultado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: >-
      ```bash

      # ejemplo — adapta a tu API; redacta tokens

      curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization: Bearer
      $TOKEN_A" \
        "$API/pedidos/$CITA_B_ID"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara IDs de prueba
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l04 primera-prueba-manual-cross-tenant"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Primera prueba manual cross-tenant», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Primera prueba manual
          cross-tenant
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


      `curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization: Bearer
      $TOKEN_A" \`
    comandoEsperado:
      - >-
        curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization: Bearer
        $TOKEN_A" \
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization:
      Bearer $TOKEN_A" \
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
          Intentar leer recurso del tenant B autenticado como A; documentar
          resultado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Prueba manual IDOR
    xp: 10
    cuerpo: >-
      Autenticado como A, pide recurso de B (GET pedido / cliente). Documenta:
      Pega status + fragmento de body **redactado**. Espera 403/404; si 200 con
      datos de B → hallazgo crítico.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable:
        `projects/m25-ciber/aislamiento/prueba-manual-01.md`.
      - Sin secretos en markdown.
      - Conexión Vitrina escrita en bitácora.
      - 'Commit `docs(m25): l04 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Primera prueba manual cross-tenant

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/aislamiento/prueba-manual-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Intentar leer recurso del tenant B autenticado como A; documentar resultado.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- IDOR
- 403 vs 404
- Evidencia reproducible

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Prepara IDs de prueba (20–30 min)

Usa tenants A/B de L03. Anota en `aislamiento/prueba-manual-01.md`: `tenant_a_id`, `tenant_b_id`, `cita_b_id`, usuario A.

### 3. Prueba manual IDOR (90–110 min)

Autenticado como A, pide recurso de B (GET pedido / cliente). Documenta:

```bash
# ejemplo — adapta a tu API; redacta tokens
curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" \
  "$API/pedidos/$CITA_B_ID"
```

Pega status + fragmento de body **redactado**. Espera 403/404; si 200 con datos de B → hallazgo crítico.

### 4. Clasifica resultado (30–40 min)

Sección **Resultado**: PASS / FAIL. Si FAIL, abre issue y enlázalo. No “arregles en silencio” sin evidencia.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l04 primera-prueba-manual-cross-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/aislamiento/prueba-manual-01.md`.
2. Sin secretos en markdown.
3. Conexión Vitrina escrita en bitácora.
4. Commit `docs(m25): l04 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Review authn — sesión y tokens](L05-review-authn-sesion-y-tokens.md)
