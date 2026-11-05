---
id: L04
materia: M18
orden: 4
titulo: Threat model v0 y lectura OWASP Top 10
horas: 5
semana: 1
lectura: OWASP Top 10 (2021) — lectura completa en español
evidencia: projects/m18-appsec/owasp-top10-map.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana 1 con backlog de riesgo alineado a la industria.


      **Objetivo de esta lección:** Mapa Top 10 en
      `projects/m18-appsec/owasp-top10-map.md` + `threat-model-v0.md` con riesgo
      residual semana 1.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura Top 10
    xp: 10
    cuerpo: |-
      ```bash
      curl -sI https://owasp.org/Top10/es/ | head -5
      ```

      Lee OWASP Top 10 (2021) ES. Anota A01, A03, A07 como foco M18.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Mapa 10 filas
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/owasp-top10-map.md <<'EOF'
      # OWASP Top 10 → Vitrina

      | Id | Ejemplo Vitrina | Mitigación | Semana |
      |----|--------------------|------------|--------|
      | A01 | GET /api/pedidos/:id cross-user | authz owner | 5 |
      | A02 | secretos en repo | .env + rotación | 7 |
      | A03 | búsqueda concat SQL | params/ORM | 4 |
      | A04 | sin rate limit login | 429 | 5 |
      | A05 | cookies sin flags | Secure/HttpOnly | 3 |
      | A06 | deps vulnerables | npm audit | 7 |
      | A07 | hash débil / sesión | bcrypt + rotate | 2 |
      | A08 | integridad build | CI firmada (idea) | 8 |
      | A09 | logs sin retención | política mínima | 8 |
      | A10 | SSRF webhook futuro | allowlist | 6 |
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Threat model v0 y lectura OWASP Top 10», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Threat model v0 y
          lectura OWASP Top 10
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

      `curl -sI https://owasp.org/Top10/es/ | head -5`
    comandoEsperado:
      - 'curl -sI https://owasp.org/Top10/es/ | head -5'
      - >-
        git add projects/m18-appsec/owasp-top10-map.md
        projects/m18-appsec/threat-model-v0.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sI https://owasp.org/Top10/es/ | head -5'
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
          Mapa Top 10 en `projects/m18-appsec/owasp-top10-map.md` +
          `threat-model-v0.md` con riesgo residual semana 1.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cierra threat-model-v0
    xp: 10
    cuerpo: >-
      Sección **Riesgo residual semana 1** (3 bullets). Confirma P1 tras semana
      2 auth.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Mapa 10 filas mínimo (artefacto:
        `projects/m18-appsec/owasp-top10-map.md`).
      - >-
        threat-model-v0 actualizado (artefacto:
        `projects/m18-appsec/owasp-top10-map.md`).
      - 'Commit `docs(m18): L04 threat-model-v0-y-lectura-owasp-top-10`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Threat model v0 y lectura OWASP Top 10

**~5.0 h · Semana 1**

Cierras la semana 1 con backlog de riesgo alineado a la industria.

## Objetivo

Mapa Top 10 en `projects/m18-appsec/owasp-top10-map.md` + `threat-model-v0.md` con riesgo residual semana 1.

## Pasos

### 1. Lectura Top 10 (40–50 min)

Lee OWASP Top 10 (2021) ES. Anota A01, A03, A07 como foco M18.

```bash
curl -sI https://owasp.org/Top10/es/ | head -5
```
### 2. Mapa 10 filas (70–90 min)

```bash
cat > projects/m18-appsec/owasp-top10-map.md <<'EOF'
# OWASP Top 10 → Vitrina

| Id | Ejemplo Vitrina | Mitigación | Semana |
|----|--------------------|------------|--------|
| A01 | GET /api/pedidos/:id cross-user | authz owner | 5 |
| A02 | secretos en repo | .env + rotación | 7 |
| A03 | búsqueda concat SQL | params/ORM | 4 |
| A04 | sin rate limit login | 429 | 5 |
| A05 | cookies sin flags | Secure/HttpOnly | 3 |
| A06 | deps vulnerables | npm audit | 7 |
| A07 | hash débil / sesión | bcrypt + rotate | 2 |
| A08 | integridad build | CI firmada (idea) | 8 |
| A09 | logs sin retención | política mínima | 8 |
| A10 | SSRF webhook futuro | allowlist | 6 |
EOF
```
### 3. Cierra threat-model-v0 (25–35 min)

Sección **Riesgo residual semana 1** (3 bullets). Confirma P1 tras semana 2 auth.

```bash
printf "\n## Riesgo residual semana 1\n- Auth aún no endurecida\n- Access control por verificar\n- Deps sin audit\n" >> projects/m18-appsec/threat-model-v0.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/owasp-top10-map.md projects/m18-appsec/threat-model-v0.md
git commit -m "docs(m18): l04 threat model v0 owasp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Top 10 (2021) — lectura completa en español | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Mapa 10 filas mínimo (artefacto: `projects/m18-appsec/owasp-top10-map.md`).
2. threat-model-v0 actualizado (artefacto: `projects/m18-appsec/owasp-top10-map.md`).
3. Commit `docs(m18): L04 threat-model-v0-y-lectura-owasp-top-10`.

## Errores comunes

- Marcar ‘no aplica’ en todo.
- Atacar sitios que no controlas.

## Siguiente

[L05 — Inventario de autenticación actual](L05-inventario-de-autenticacion-actual.md)
