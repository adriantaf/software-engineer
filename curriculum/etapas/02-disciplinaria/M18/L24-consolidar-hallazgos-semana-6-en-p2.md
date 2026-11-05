---
id: L24
materia: M18
orden: 24
titulo: Consolidar hallazgos semana 6 en P2
horas: 5
semana: 6
lectura: Repaso findings
evidencia: projects/m18-appsec/findings-table.md actualizado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `projects/m18-appsec/findings-table.md` con ≥5 filas
      PoC→fix→test (o plan fechado); sin secretos.


      Mitad del módulo: P2 debe ser visible en git (≥5 hallazgos).
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría de la tabla
    xp: 10
    cuerpo: |-
      ```bash
      wc -l projects/m18-appsec/findings/*.md
      cat projects/m18-appsec/findings-table.md
      # Completa hasta ≥5 filas (001–005 + rate limit / headers si aplica)
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Consolidar hallazgos semana 6 en P2" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/findings-table.md actualizado
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

      `cat projects/m18-appsec/findings-table.md`
    comandoEsperado:
      - cat projects/m18-appsec/findings-table.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cat projects/m18-appsec/findings-table.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          `projects/m18-appsec/findings-table.md` con ≥5 filas PoC→fix→test (o
          plan fechado); sin secretos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Cierra gaps
    xp: 10
    cuerpo: >-
      Cada fila: ID, OWASP, PoC, commit fix, test/link. Issues para abiertos con
      fecha semana 7–8.


      ```markdown

      | ID | OWASP | PoC | Commit fix | Test |

      |----|-------|-----|------------|------|

      | 001 | A03 | findings/001-sqli.md | abc123 | security/sqli |

      | 002 | XSS | findings/002-… | | |

      | 003 | A01 | findings/003-idor.md | | authz |

      | 004 | SSRF | findings/004-ssrf.md | n/a diseño | |

      | 005 | Upload | findings/005-upload.md | | |

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/findings-table.md
      git commit -m "docs(m18): l24 findings table p2"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        ≥5 filas completas o plan con 5 (artefacto:
        `projects/m18-appsec/findings-table.md actualizado`).
      - >-
        Ningún secreto en tabla (artefacto:
        `projects/m18-appsec/findings-table.md actualizado`).
      - 'Commit `docs(m18): L24 consolidar-hallazgos-semana-6-en-p2`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L24 — Consolidar hallazgos semana 6 en P2

**~5.0 h · Semana 6**

Mitad del módulo: P2 debe ser visible en git (≥5 hallazgos).

## Objetivo

`projects/m18-appsec/findings-table.md` con ≥5 filas PoC→fix→test (o plan fechado); sin secretos.

## Pasos

### 1. Auditoría de la tabla (40–50 min)

```bash
wc -l projects/m18-appsec/findings/*.md
cat projects/m18-appsec/findings-table.md
# Completa hasta ≥5 filas (001–005 + rate limit / headers si aplica)
```
### 2. Cierra gaps (80–100 min)

Cada fila: ID, OWASP, PoC, commit fix, test/link. Issues para abiertos con fecha semana 7–8.

```markdown
| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | abc123 | security/sqli |
| 002 | XSS | findings/002-… | | |
| 003 | A01 | findings/003-idor.md | | authz |
| 004 | SSRF | findings/004-ssrf.md | n/a diseño | |
| 005 | Upload | findings/005-upload.md | | |
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings-table.md
git commit -m "docs(m18): l24 findings table p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Repaso findings | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥5 filas completas o plan con 5 (artefacto: `projects/m18-appsec/findings-table.md actualizado`).
2. Ningún secreto en tabla (artefacto: `projects/m18-appsec/findings-table.md actualizado`).
3. Commit `docs(m18): L24 consolidar-hallazgos-semana-6-en-p2`.

## Errores comunes

- Hallazgos duplicados.
- PoC sin fix planificado.

## Siguiente

[L25 — npm audit y cadena de dependencias](L25-npm-audit-y-cadena-de-dependencias.md)
