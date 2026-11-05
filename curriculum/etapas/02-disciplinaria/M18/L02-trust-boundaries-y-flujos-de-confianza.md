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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar ≥4 límites y 3 flujos (login, crear pedido,
      deep-link WA) en `projects/m18-appsec/trust-boundaries-appsec.md`.


      M10 y M13 nombraron boundaries; hoy los operacionalizas para AppSec.
  - id: s2
    tipo: ejemplo
    titulo: 1. Ancla M13
    xp: 10
    cuerpo: >-
      ```bash

      ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13;
      parte de cero)"

      touch projects/m18-appsec/trust-boundaries-appsec.md

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Trust boundaries y flujos de confianza" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/trust-boundaries-appsec.md
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


      `ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13;
      parte de cero)"`
    comandoEsperado:
      - >-
        ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin
        M13; parte de cero)"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo
      "(sin M13; parte de cero)"
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar ≥4 límites y 3 flujos (login, crear pedido, deep-link WA)
          en `projects/m18-appsec/trust-boundaries-appsec.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tabla de límites
    xp: 10
    cuerpo: >-
      Por cada límite: origen, destino, protocolo, autenticación, datos. Mínimo
      4.


      ```markdown

      | Origen | Destino | Protocolo | Auth | Datos |

      |--------|---------|-----------|------|-------|

      | Browser | API | HTTPS | cookie/JWT | PII pedidos |

      | API | Postgres | TCP | user app | SQL |

      | API | SMTP futuro | TLS | API key | recordatorios |

      | Operador | Hosting | SSH/HTTPS | MFA | logs, .env |

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Flujos + abuso
    xp: 10
    cuerpo: >-
      ```bash

      printf "\n## Flujos\n- login:\n- crear pedido:\n- deep-link WA:\n\n##
      Abuso por límite\n" >> projects/m18-appsec/trust-boundaries-appsec.md

      ```
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
