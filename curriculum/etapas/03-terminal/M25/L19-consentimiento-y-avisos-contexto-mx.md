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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Multi-tenant amplifica impacto de una fuga; privacidad es feature de
      confianza.


      Conceptos que debes poder explicar al cerrar:


      - Retención

      - Derecho de cancelación

      - Datos por negocio


      **Objetivo de esta lección:** Aviso privacidad en landing o panel; enlaces
      en repo marketing.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l19 consentimiento-y-avisos-contexto-mx"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Localiza avisos actuales
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l19 consentimiento-y-avisos-contexto-mx"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Consentimiento y avisos (contexto MX)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Consentimiento y avisos
          (contexto MX)
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

      `git add projects/`
    comandoEsperado:
      - git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/'
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
        texto: Aviso privacidad en landing o panel; enlaces en repo marketing.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Borrador técnico-operativo
    xp: 10
    cuerpo: >-
      Redacta aviso **corto** (no copies plantilla legal genérica): qué datos,
      para qué, con quién (Stripe), retención, contacto. Marca claramente:
      *borrador técnico del plan — no es asesoría legal*.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
