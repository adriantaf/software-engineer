---
id: L03
materia: M18
orden: 3
titulo: STRIDE aplicado al SaaS de menú/pedidos
horas: 5
semana: 1
lectura: STRIDE cheat sheet (una categoría por componente)
evidencia: projects/m18-appsec/stride-matrix.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La matriz obliga a nombrar amenazas antes de buscar exploits al azar.


      **Objetivo de esta lección:** Matriz STRIDE ≥4×6 en
      `projects/m18-appsec/stride-matrix.md` (login, pedidos, admin) con ≥3
      amenazas priorizadas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Plantilla STRIDE
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/stride-matrix.md <<'EOF'
      # Matriz STRIDE — Vitrina

      | Componente | S | T | R | I | D | E |
      |------------|---|---|---|---|---|---|
      | Login | | | | | | |
      | Lista pedidos | | | | | | |
      | Detalle pedido | | | | | | |
      | Admin usuarios | | | | | | |
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Relleno del dominio
    xp: 10
    cuerpo: >-
      ```markdown

      | Componente | S | T | I |

      |------------|---|---|---|

      | Login | Fuerza bruta | Tamper cookie | Leak en error |

      | Detalle pedido | — | PUT sin authz | IDOR lee notas |

      ```


      Frases concretas (no “hackeo”). Ejemplo Login/Spoofing: “fuerza bruta o
      credenciales robadas”. Incluye IDOR en detalle pedido e XSS en notas.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «STRIDE aplicado al SaaS de menú/pedidos», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de STRIDE aplicado al SaaS
          de menú/pedidos
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
    pregunta: ¿Es recomendable en esta lección? “Copiar tabla de blog sin adaptar."
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
          Matriz STRIDE ≥4×6 en `projects/m18-appsec/stride-matrix.md` (login,
          pedidos, admin) con ≥3 amenazas priorizadas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Prioriza 3 celdas
    xp: 10
    cuerpo: Marca las 3 amenazas de las semanas 2–5. Enlaza `threat-model-v0.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Matriz ≥4 filas × 6 columnas (artefacto:
        `projects/m18-appsec/stride-matrix.md`).
      - >-
        ≥3 amenazas priorizadas (artefacto:
        `projects/m18-appsec/stride-matrix.md`).
      - 'Commit `docs(m18): L03 stride-aplicado-al-crm-de-pedidos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — STRIDE aplicado al SaaS de menú/pedidos

**~5.0 h · Semana 1**

La matriz obliga a nombrar amenazas antes de buscar exploits al azar.

## Objetivo

Matriz STRIDE ≥4×6 en `projects/m18-appsec/stride-matrix.md` (login, pedidos, admin) con ≥3 amenazas priorizadas.

## Pasos

### 1. Plantilla STRIDE (25–35 min)

```bash
cat > projects/m18-appsec/stride-matrix.md <<'EOF'
# Matriz STRIDE — Vitrina

| Componente | S | T | R | I | D | E |
|------------|---|---|---|---|---|---|
| Login | | | | | | |
| Lista pedidos | | | | | | |
| Detalle pedido | | | | | | |
| Admin usuarios | | | | | | |
EOF
```
### 2. Relleno del dominio (90–110 min)

Frases concretas (no “hackeo”). Ejemplo Login/Spoofing: “fuerza bruta o credenciales robadas”. Incluye IDOR en detalle pedido e XSS en notas.

```markdown
| Componente | S | T | I |
|------------|---|---|---|
| Login | Fuerza bruta | Tamper cookie | Leak en error |
| Detalle pedido | — | PUT sin authz | IDOR lee notas |
```
### 3. Prioriza 3 celdas (30 min)

Marca las 3 amenazas de las semanas 2–5. Enlaza `threat-model-v0.md`.

```bash
printf "\n## Prioridades (rojas)\n1. ...\n2. ...\n3. ...\n" >> projects/m18-appsec/stride-matrix.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/stride-matrix.md
git commit -m "docs(m18): l03 stride crm pedidos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | STRIDE cheat sheet (una categoría por componente) | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Matriz ≥4 filas × 6 columnas (artefacto: `projects/m18-appsec/stride-matrix.md`).
2. ≥3 amenazas priorizadas (artefacto: `projects/m18-appsec/stride-matrix.md`).
3. Commit `docs(m18): L03 stride-aplicado-al-crm-de-pedidos`.

## Errores comunes

- Copiar tabla de blog sin adaptar.
- Dejar celdas vacías con ‘N/A’ en todo.

## Siguiente

[L04 — Threat model v0 y lectura OWASP Top 10](L04-threat-model-v0-y-lectura-owasp-top-10.md)
