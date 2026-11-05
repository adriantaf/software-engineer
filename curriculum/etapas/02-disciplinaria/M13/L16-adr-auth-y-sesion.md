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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `adr/003-auth-sesion.md` coherente con `secuencia-auth.md` y
      boundaries.


      Cierras la decisión que L07 dibujó: cómo autenticamos el piloto.
  - id: s2
    tipo: ejemplo
    titulo: 1. Alternativas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): ADR 003 auth y sesion"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "ADR auth y sesión" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: adr/003-auth-sesion.md
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

      `git add projects/m13-diseno`
    comandoEsperado:
      - git add projects/m13-diseno
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m13-diseno'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          `adr/003-auth-sesion.md` coherente con `secuencia-auth.md` y
          boundaries.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. ADR
    xp: 10
    cuerpo: >-
      Incluye: hash de passwords, expiración, logout, roles, rechazo de “rol en
      query string”.
  - id: s7
    tipo: explicacion
    titulo: 3. Sincroniza diagrama
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
