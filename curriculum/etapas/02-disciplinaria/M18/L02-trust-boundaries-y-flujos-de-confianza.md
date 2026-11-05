---
id: L02
materia: M18
orden: 2
titulo: Trust boundaries y flujos de confianza
horas: 5
semana: 1
lectura: STRIDE por boundary + M13 `trust-boundaries`
evidencia: projects/m18-appsec/trust-boundaries-appsec.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M10 y M13 nombraron boundaries; hoy los operacionalizas para AppSec.


      **Objetivo de esta lección:** Documentar ≥4 límites y 3 flujos (login,
      crear pedido, deep-link WA) en
      `projects/m18-appsec/trust-boundaries-appsec.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Ancla M13
    xp: 10
    cuerpo: >-
      ```bash

      ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13;
      parte de cero)"

      touch projects/m18-appsec/trust-boundaries-appsec.md

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Tabla de límites
    xp: 10
    cuerpo: >-
      ```markdown

      | Origen | Destino | Protocolo | Auth | Datos |

      |--------|---------|-----------|------|-------|

      | Browser | API | HTTPS | cookie/JWT | PII pedidos |

      | API | Postgres | TCP | user app | SQL |

      | API | SMTP futuro | TLS | API key | recordatorios |

      | Operador | Hosting | SSH/HTTPS | MFA | logs, .env |

      ```


      Por cada límite: origen, destino, protocolo, autenticación, datos. Mínimo
      4.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Trust boundaries y flujos de confianza», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Trust boundaries y
          flujos de confianza
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


      `ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13;
      parte de cero)"`
    comandoEsperado:
      - >-
        ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin
        M13; parte de cero)"
      - touch projects/m18-appsec/trust-boundaries-appsec.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo
      "(sin M13; parte de cero)"
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
          Documentar ≥4 límites y 3 flujos (login, crear pedido, deep-link WA)
          en `projects/m18-appsec/trust-boundaries-appsec.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Flujos + abuso
    xp: 10
    cuerpo: >-
      Para login, crear pedido y deep-link WA: datos en tránsito, auth
      requerida, fallo si se omite authz. Una pregunta de abuso por límite.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        ≥4 boundaries documentados (artefacto:
        `projects/m18-appsec/trust-boundaries-appsec.md`).
      - >-
        Pregunta de abuso por límite (artefacto:
        `projects/m18-appsec/trust-boundaries-appsec.md`).
      - 'Commit `docs(m18): L02 trust-boundaries-y-flujos-de-confianza`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Trust boundaries y flujos de confianza

**~5.0 h · Semana 1**

M10 y M13 nombraron boundaries; hoy los operacionalizas para AppSec.

## Objetivo

Documentar ≥4 límites y 3 flujos (login, crear pedido, deep-link WA) en `projects/m18-appsec/trust-boundaries-appsec.md`.

## Pasos

### 1. Ancla M13 (20–30 min)

```bash
ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13; parte de cero)"
touch projects/m18-appsec/trust-boundaries-appsec.md
```
### 2. Tabla de límites (70–90 min)

Por cada límite: origen, destino, protocolo, autenticación, datos. Mínimo 4.

```markdown
| Origen | Destino | Protocolo | Auth | Datos |
|--------|---------|-----------|------|-------|
| Browser | API | HTTPS | cookie/JWT | PII pedidos |
| API | Postgres | TCP | user app | SQL |
| API | SMTP futuro | TLS | API key | recordatorios |
| Operador | Hosting | SSH/HTTPS | MFA | logs, .env |
```
### 3. Flujos + abuso (40–50 min)

Para login, crear pedido y deep-link WA: datos en tránsito, auth requerida, fallo si se omite authz. Una pregunta de abuso por límite.

```bash
printf "\n## Flujos\n- login:\n- crear pedido:\n- deep-link WA:\n\n## Abuso por límite\n" >> projects/m18-appsec/trust-boundaries-appsec.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/trust-boundaries-appsec.md
git commit -m "docs(m18): l02 trust boundaries"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | STRIDE por boundary + M13 `trust-boundaries` | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥4 boundaries documentados (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
2. Pregunta de abuso por límite (artefacto: `projects/m18-appsec/trust-boundaries-appsec.md`).
3. Commit `docs(m18): L02 trust-boundaries-y-flujos-de-confianza`.

## Errores comunes

- Un solo boundary “internet”.
- Ignorar Postgres como activo interno.

## Siguiente

[L03 — STRIDE aplicado al SaaS de menú/pedidos](L03-stride-aplicado-al-crm-de-pedidos.md)
