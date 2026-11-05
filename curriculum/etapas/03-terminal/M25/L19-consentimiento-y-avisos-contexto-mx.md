---
id: L19
materia: M25
orden: 19
titulo: Consentimiento y avisos (contexto MX)
horas: 5
semana: 5
lectura: OWASP Privacy / LFPDPPP notas (contexto)
evidencia: projects/m25-ciber/privacidad/aviso-borrador.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Aviso privacidad en landing o panel; enlaces en repo
      marketing.


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
      git add projects/
      git status
      git commit -m "docs(m25): l19 consentimiento-y-avisos-contexto-mx"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Consentimiento y avisos (contexto MX)" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m25-ciber/privacidad/aviso-borrador.md
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Aviso privacidad en landing o panel; enlaces en repo marketing.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Localiza avisos actuales
    xp: 10
    cuerpo: >-
      En `projects/m25-ciber/privacidad/aviso-borrador.md`: URLs de
      landing/panel donde debería vivir aviso/privacidad.
  - id: s7
    tipo: explicacion
    titulo: 3. Borrador técnico-operativo
    xp: 10
    cuerpo: >-
      Redacta aviso **corto** (no copies plantilla legal genérica): qué datos,
      para qué, con quién (Stripe), retención, contacto.


      Marca claramente: *borrador técnico del plan — no es asesoría legal*.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/privacidad/aviso-borrador.md`.'
      - Documento en ruta indicada.
      - ≥2 hallazgos aislamiento cerrados acumulado.
      - 'Commit `docs(m25): l19 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L19 — Consentimiento y avisos (contexto MX)

**~5 h · Semana 5**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/privacidad/aviso-borrador.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Aviso privacidad en landing o panel; enlaces en repo marketing.

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

### 2. Localiza avisos actuales (20–30 min)

En `projects/m25-ciber/privacidad/aviso-borrador.md`: URLs de landing/panel donde debería vivir aviso/privacidad.

### 3. Borrador técnico-operativo (100–120 min)

Redacta aviso **corto** (no copies plantilla legal genérica): qué datos, para qué, con quién (Stripe), retención, contacto.

Marca claramente: *borrador técnico del plan — no es asesoría legal*.

### 4. Enlaces en producto (25–35 min)

Issue/PR para linkear aviso desde footer o signup. Bitácora semana-05.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l19 consentimiento-y-avisos-contexto-mx"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Privacy / LFPDPPP notas (contexto) | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/privacidad/aviso-borrador.md`.
2. Documento en ruta indicada.
3. ≥2 hallazgos aislamiento cerrados acumulado.
4. Commit `docs(m25): l19 …` en el historial.

## Errores comunes

- Política genérica sin tu producto.
- Un solo hallazgo en todo M25.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L20 — Segundo hallazgo aislamiento cerrado](L20-segundo-hallazgo-aislamiento-cerrado.md)
