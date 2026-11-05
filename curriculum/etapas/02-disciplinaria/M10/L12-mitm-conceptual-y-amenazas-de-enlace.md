---
id: L12
materia: M10
orden: 12
titulo: MITM conceptual y amenazas de enlace
horas: 5
semana: 3
lectura: Tanenbaum ataques en red (selecto) + hilo seguridad
evidencia: amenazas-enlace.md en m10-redes
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana TLS con un documento de amenazas **defensivo**: qué
      temes y qué mitigación aplica.


      **Objetivo de esta lección:** Redactar `amenazas-enlace.md` usable como
      input de M18.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Modelo
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l12 amenazas enlace"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Catálogo
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l12 amenazas enlace"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «MITM conceptual y amenazas de enlace», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de MITM conceptual y
          amenazas de enlace
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

      `git add projects/m10-redes`
    comandoEsperado:
      - git add projects/m10-redes
      - 'git commit -m "docs(m10): l12 amenazas enlace"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m10-redes'
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
        texto: Redactar `amenazas-enlace.md` usable como input de M18.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Checklist P1
    xp: 10
    cuerpo: 'README: labs semana 1–3 listos. Enlace a `amenazas-enlace.md`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m10-redes/amenazas-enlace.md` con ≥4 amenazas y mitigaciones
        (TLS, HSTS, DNS confiable…).
      - Semana 3 enlazada en README; P1 labs TLS cerrados.
      - 'Commit `docs(m10): l12 amenazas enlace`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — MITM conceptual y amenazas de enlace

**~5.0 h · Semana 3**

Cierras la semana TLS con un documento de amenazas **defensivo**: qué temes y qué mitigación aplica.

## Objetivo

Redactar `amenazas-enlace.md` usable como input de M18.

## Pasos

### 1. Modelo (45 min)

Actores: usuario del panel, red del café, ISP, DNS resolver, tu API. Dibuja trust boundaries.

### 2. Catálogo (75 min)

Para cada amenaza (eavesdropping HTTP, MITM con cert falso si el cliente no valida, DNS spoofing, session theft en tránsito):

- Impacto en pedidos/PII
- Mitigación (TLS bien validado, HSTS, no mixed content, DNS provider serio…)
- Residual risk

### 3. Checklist P1 (40 min)

README: labs semana 1–3 listos. Enlace a `amenazas-enlace.md`.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l12 amenazas enlace"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Amenazas en tránsito: eavesdropping, MITM, DNS spoofing (alto nivel) | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m10-redes/amenazas-enlace.md` con ≥4 amenazas y mitigaciones (TLS, HSTS, DNS confiable…).
2. Semana 3 enlazada en README; P1 labs TLS cerrados.
3. Commit `docs(m10): l12 amenazas enlace`.

## Errores comunes

- Tutorial ofensivo de MITM — aquí solo modelo de amenaza y defensa.
- Pensar que HTTP “solo en la LAN” es inocuo.
- Olvidar captive portals / Wi‑Fi públicas en el modelo.

## Siguiente

[L13 — Cookies: atributos y modelo de almacenamiento](L13-cookies-atributos-y-modelo-de-almacenamiento.md)
