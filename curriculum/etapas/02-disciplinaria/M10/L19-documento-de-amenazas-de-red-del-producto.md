---
id: L19
materia: M10
orden: 19
titulo: Documento de amenazas de red del producto
horas: 5
semana: 5
lectura: Proyecto M10 README + STRIDE lite (red)
evidencia: projects/m10-redes/amenazas-red.md actualizado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El entregable del proyecto: un doc que M18 pueda consumir sin redescubrir
      la red.


      **Objetivo de esta lección:** Publicar `amenazas-red.md` completo y
      enlazado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Fusiona fuentes
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l19 amenazas red producto"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: STRIDE lite
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l19 amenazas red producto"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Documento de amenazas de red del producto», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Documento de amenazas
          de red del produc…
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
      - 'git commit -m "docs(m10): l19 amenazas red producto"'
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
        texto: Publicar `amenazas-red.md` completo y enlazado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README
    xp: 10
    cuerpo: Índice del proyecto con P1/P2/P3 y proyecto marcados.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `amenazas-red.md` integra enlace + superficie + mitigaciones hacia
        M18/M19.
      - 'README del proyecto enlaza amenazas, superficie y tcp-echo.'
      - 'Commit `docs(m10): l19 amenazas red producto`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — Documento de amenazas de red del producto

**~5.0 h · Semana 5**

El entregable del proyecto: un doc que M18 pueda consumir sin redescubrir la red.

## Objetivo

Publicar `amenazas-red.md` completo y enlazado.

## Pasos

### 1. Fusiona fuentes (60 min)

Parte de `amenazas-enlace.md` + `superficie/endpoints.md` + labs TLS/cookies. Crea `amenazas-red.md` con secciones: activos, amenazas, mitigaciones, residual, follow-ups M18/M19.

### 2. STRIDE lite (60 min)

Al menos una fila por: Spoofing, Tampering, Repudiation (logs), Information disclosure, DoS, Elevation (si aplica a red/admin).

### 3. README (40 min)

Índice del proyecto con P1/P2/P3 y proyecto marcados.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l19 amenazas red producto"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | STRIDE lite sobre red: spoofing, tampering, info disclosure, DoS | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `amenazas-red.md` integra enlace + superficie + mitigaciones hacia M18/M19.
2. README del proyecto enlaza amenazas, superficie y tcp-echo.
3. Commit `docs(m10): l19 amenazas red producto`.

## Errores comunes

- Lista genérica copiada sin Vitrina.
- Amenazas sin mitigación ni dueño (tú / M18).
- Olvidar DNS y cookies.

## Siguiente

[L20 — Cierre M10 — evidencias y dominio](L20-cierre-m10-evidencias-y-dominio.md)
