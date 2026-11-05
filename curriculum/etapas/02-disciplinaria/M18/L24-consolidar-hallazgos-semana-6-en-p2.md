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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Mitad del módulo: P2 debe ser visible en git (≥5 hallazgos).


      **Objetivo de esta lección:** `projects/m18-appsec/findings-table.md` con
      ≥5 filas PoC→fix→test (o plan fechado); sin secretos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría de la tabla
    xp: 10
    cuerpo: |-
      ```bash
      wc -l projects/m18-appsec/findings/*.md
      cat projects/m18-appsec/findings-table.md
      # Completa hasta ≥5 filas (001–005 + rate limit / headers si aplica)
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Cierra gaps
    xp: 10
    cuerpo: >-
      ```markdown

      | ID | OWASP | PoC | Commit fix | Test |

      |----|-------|-----|------------|------|

      | 001 | A03 | findings/001-sqli.md | abc123 | security/sqli |

      | 002 | XSS | findings/002-… | | |

      | 003 | A01 | findings/003-idor.md | | authz |

      | 004 | SSRF | findings/004-ssrf.md | n/a diseño | |

      | 005 | Upload | findings/005-upload.md | | |

      ```


      Cada fila: ID, OWASP, PoC, commit fix, test/link. Issues para abiertos con
      fecha semana 7–8.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Consolidar hallazgos semana 6 en P2», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Consolidar hallazgos
          semana 6 en P2
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

      `cat projects/m18-appsec/findings-table.md`
    comandoEsperado:
      - cat projects/m18-appsec/findings-table.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cat projects/m18-appsec/findings-table.md'
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
          `projects/m18-appsec/findings-table.md` con ≥5 filas PoC→fix→test (o
          plan fechado); sin secretos.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
