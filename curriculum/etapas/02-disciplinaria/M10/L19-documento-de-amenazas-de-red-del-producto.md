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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Publicar `amenazas-red.md` completo y enlazado.


      El entregable del proyecto: un doc que M18 pueda consumir sin redescubrir
      la red.
  - id: s2
    tipo: ejemplo
    titulo: 1. Fusiona fuentes
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes
      git commit -m "docs(m10): l19 amenazas red producto"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Documento de amenazas de red del producto" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m10-redes/amenazas-red.md actualizado
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
        texto: Publicar `amenazas-red.md` completo y enlazado.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. STRIDE lite
    xp: 10
    cuerpo: >-
      Al menos una fila por: Spoofing, Tampering, Repudiation (logs),
      Information disclosure, DoS, Elevation (si aplica a red/admin).
  - id: s7
    tipo: explicacion
    titulo: 3. README
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
