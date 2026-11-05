---
id: L08
materia: M12
orden: 8
titulo: 'RNF seguridad, privacidad y P2'
horas: 5
semana: 2
lectura: Plantilla RNF + hilo seguridad
evidencia: stories.md + srs-borrador RNF (≥8 stories)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** ≥8 stories + ≥3 RNF de seguridad/privacidad trazables.


      Cierras P2 y metes seguridad en el SRS desde ya
      ([hilo](../../../hilos/seguridad.md)).
  - id: s2
    tipo: ejemplo
    titulo: 1. Completa stories
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): l08 rnf seguridad p2"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "RNF seguridad, privacidad y P2" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: stories.md + srs-borrador RNF (≥8 stories)
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

      `git add projects/m12-srs`
    comandoEsperado:
      - git add projects/m12-srs
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m12-srs'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: ≥8 stories + ≥3 RNF de seguridad/privacidad trazables.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. RNF
    xp: 10
    cuerpo: >-
      En `srs-borrador.md` §3.2, ejemplos:


      | ID | Tipo | Descripción |

      |----|------|-------------|

      | RNF-SEC-01 | Seguridad | Toda ruta de negocio exige sesión; sin token →
      401 |

      | RNF-SEC-02 | Autorización | Staff no lee notas privadas → 403 + log |

      | RNF-PRIV-01 | Privacidad | PII mínimo; single-tenant documentado |


      Enlaza cada RNF a US-xx.
  - id: s7
    tipo: explicacion
    titulo: 3. README P2
    xp: 10
    cuerpo: Marca P2 listo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`stories.md` tiene ≥8 stories con criterios (P2).'
      - >-
        `srs-borrador.md` incluye ≥3 RNF-SEC/PRIV numerados y enlazados a
        stories.
      - 'Commit `docs(m12): l08 rnf seguridad p2`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — RNF seguridad, privacidad y P2

**~5.0 h · Semana 2**

Cierras P2 y metes seguridad en el SRS desde ya ([hilo](../../../hilos/seguridad.md)).

## Objetivo

≥8 stories + ≥3 RNF de seguridad/privacidad trazables.

## Pasos

### 1. Completa stories (45 min)

Llega a ≥8 con criterios. Índice al inicio de `stories.md`.

### 2. RNF (75 min)

En `srs-borrador.md` §3.2, ejemplos:

| ID | Tipo | Descripción |
|----|------|-------------|
| RNF-SEC-01 | Seguridad | Toda ruta de negocio exige sesión; sin token → 401 |
| RNF-SEC-02 | Autorización | Staff no lee notas privadas → 403 + log |
| RNF-PRIV-01 | Privacidad | PII mínimo; single-tenant documentado |

Enlaza cada RNF a US-xx.

### 3. README P2 (20 min)

Marca P2 listo.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l08 rnf seguridad p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | RNF seguridad/privacidad trazables; single-tenant; 401/403 | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `stories.md` tiene ≥8 stories con criterios (P2).
2. `srs-borrador.md` incluye ≥3 RNF-SEC/PRIV numerados y enlazados a stories.
3. Commit `docs(m12): l08 rnf seguridad p2`.

## Errores comunes

- “Seguridad luego en M18” sin RNF.
- RNF no medibles (“máxima seguridad”).
- Stories sin permisos.

## Siguiente

[L09 — Alcance MVP y MoSCoW](L09-alcance-mvp-y-moscow.md)
