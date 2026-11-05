---
id: L16
materia: M13
orden: 16
titulo: ADR auth y sesión
horas: 5
semana: 4
lectura: Sesión vs JWT; cookie HttpOnly; roles owner/staff
evidencia: adr/003-auth-sesion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la decisión que L07 dibujó: cómo autenticamos el piloto.


      **Objetivo de esta lección:** `adr/003-auth-sesion.md` coherente con
      `secuencia-auth.md` y boundaries.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Alternativas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): ADR 003 auth y sesion"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: ADR
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): ADR 003 auth y sesion"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «ADR auth y sesión», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de ADR auth y sesión
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

      `git add projects/m13-diseno`
    comandoEsperado:
      - git add projects/m13-diseno
      - 'git commit -m "docs(m13): ADR 003 auth y sesion"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m13-diseno'
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
          `adr/003-auth-sesion.md` coherente con `secuencia-auth.md` y
          boundaries.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Sincroniza diagrama
    xp: 10
    cuerpo: 'Si cambió el mecanismo, actualiza `secuencia-auth.md`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - ADR 003 elige mecanismo (p. ej. cookie de sesión) con consecuencias.
      - Roles owner/staff y dónde se autorizan (API) quedan escritos.
      - 'Commit `docs(m13): ADR 003 auth y sesion`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — ADR auth y sesión

**~5.0 h · Semana 4**

Cierras la decisión que L07 dibujó: cómo autenticamos el piloto.

## Objetivo

`adr/003-auth-sesion.md` coherente con `secuencia-auth.md` y boundaries.

## Pasos (hazlos en orden)

### 1. Alternativas (40 min)

Tabla: sesión servidor / JWT cookie / JWT bearer. Elige una para el piloto.

### 2. ADR (70–90 min)

Incluye: hash de passwords, expiración, logout, roles, rechazo de “rol en query string”.

### 3. Sincroniza diagrama (30 min)

Si cambió el mecanismo, actualiza `secuencia-auth.md`.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): ADR 003 auth y sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Decisión de autenticación/sesión y roles del piloto | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR 003 elige mecanismo (p. ej. cookie de sesión) con consecuencias.
2. Roles owner/staff y dónde se autorizan (API) quedan escritos.
3. Commit `docs(m13): ADR 003 auth y sesion`.

## Errores comunes

- JWT en localStorage “porque tutorial” sin amenazas.
- Roles solo en el front.
- ADR que contradice secuencia-auth sin actualizarla.

## Siguiente

[L17 — Índice del paquete de diseño](L17-indice-del-paquete-de-diseno.md)
