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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar `amenazas-enlace.md` usable como input de M18.


      Cierras la semana TLS con un documento de amenazas **defensivo**: qué
      temes y qué mitigación aplica.
  - id: s2
    tipo: ejemplo
    titulo: 1. Modelo
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l12 amenazas enlace"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "MITM conceptual y amenazas de enlace" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: amenazas-enlace.md en m10-redes
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

      `git add projects/m10-redes`
    comandoEsperado:
      - git add projects/m10-redes
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m10-redes'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Redactar `amenazas-enlace.md` usable como input de M18.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Catálogo
    xp: 10
    cuerpo: >-
      Para cada amenaza (eavesdropping HTTP, MITM con cert falso si el cliente
      no valida, DNS spoofing, session theft en tránsito):


      - Impacto en pedidos/PII

      - Mitigación (TLS bien validado, HSTS, no mixed content, DNS provider
      serio…)

      - Residual risk
  - id: s7
    tipo: explicacion
    titulo: 3. Checklist P1
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
