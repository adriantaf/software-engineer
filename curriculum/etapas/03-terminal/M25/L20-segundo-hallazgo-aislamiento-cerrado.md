---
id: L20
materia: M25
orden: 20
titulo: Segundo hallazgo aislamiento cerrado
horas: 5
semana: 5
lectura: OWASP Privacy / LFPDPPP notas (contexto)
evidencia: projects/m25-ciber/hallazgos/hallazgo-02.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Otro fix cross-tenant con test; tabla hallazgos actualizada.


      Multi-tenant amplifica impacto de una fuga; privacidad es feature de
      confianza.


      Conceptos que debes poder explicar al cerrar:


      - Retención

      - Derecho de cancelación

      - Datos por negocio
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # post-fix — mismo vector que el hallazgo-02
      curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \
        "$API/EXPORT_O_UPDATE_DE_B"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Segundo hallazgo aislamiento cerrado" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m25-ciber/hallazgos/hallazgo-02.md
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

      `curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \`
    comandoEsperado:
      - 'curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A"
      \
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Otro fix cross-tenant con test; tabla hallazgos actualizada.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Segundo hallazgo distinto
    xp: 10
    cuerpo: >-
      En `projects/m25-ciber/hallazgos/hallazgo-02.md`: debe ser **otro** vector
      (p.ej. listado, update, export) distinto a hallazgo-01.
  - id: s7
    tipo: ejemplo
    titulo: 3. Fix + test
    xp: 10
    cuerpo: |-
      ```bash
      # post-fix — mismo vector que el hallazgo-02
      curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \
        "$API/EXPORT_O_UPDATE_DE_B"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/hallazgos/hallazgo-02.md`.'
      - Documento en ruta indicada.
      - ≥2 hallazgos aislamiento cerrados acumulado.
      - 'Commit `docs(m25): l20 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L20 — Segundo hallazgo aislamiento cerrado

**~5 h · Semana 5**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hallazgos/hallazgo-02.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Otro fix cross-tenant con test; tabla hallazgos actualizada.

## Por qué empieza así

Multi-tenant amplifica impacto de una fuga; privacidad es feature de confianza.

Conceptos que debes poder explicar al cerrar:

- Retención
- Derecho de cancelación
- Datos por negocio

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Privacy / LFPDPPP notas (contexto)_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Segundo hallazgo distinto (25–35 min)

En `projects/m25-ciber/hallazgos/hallazgo-02.md`: debe ser **otro** vector (p.ej. listado, update, export) distinto a hallazgo-01.

### 3. Fix + test (100–130 min)

Repro, root cause, PR, test automatizado o curl post-fix.

```bash
# post-fix — mismo vector que el hallazgo-02
curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \
  "$API/EXPORT_O_UPDATE_DE_B"
```

Actualiza `hallazgos/README.md` con tabla acumulada (≥2 cerrados).

### 4. Regresión (25–35 min)

Confirma que hallazgo-01 sigue cerrado. Bitácora semana-05.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l20 segundo-hallazgo-aislamiento-cerrado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Privacy / LFPDPPP notas (contexto) | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hallazgos/hallazgo-02.md`.
2. Documento en ruta indicada.
3. ≥2 hallazgos aislamiento cerrados acumulado.
4. Commit `docs(m25): l20 …` en el historial.

## Errores comunes

- Política genérica sin tu producto.
- Un solo hallazgo en todo M25.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L21 — Tabletop — fuga de .env](L21-tabletop-fuga-de-env.md)
