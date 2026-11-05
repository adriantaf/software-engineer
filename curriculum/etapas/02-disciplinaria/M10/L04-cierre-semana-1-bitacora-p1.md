---
id: L04
materia: M10
orden: 4
titulo: Cierre semana 1 — bitácora P1
horas: 5
semana: 1
lectura: Repaso semana 1 Tanenbaum + ficha M10
evidencia: projects/m10-redes/labs/semana-01.md consolidado (P1)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Consolidar evidencia de capas/IP/TCP y actualizar el README
      del proyecto.


      P1 es bitácora reproducible. Hoy la dejas legible para tu yo de la semana
      5.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría de archivos
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m10-redes -type f | sort
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre semana 1 — bitácora P1" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m10-redes/labs/semana-01.md consolidado (P1)
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

      `find projects/m10-redes -type f | sort`
    comandoEsperado:
      - find projects/m10-redes -type f | sort
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: find projects/m10-redes -type f | sort'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Consolidar evidencia de capas/IP/TCP y actualizar el README del
          proyecto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Consolida `semana-01.md`
    xp: 10
    cuerpo: |-
      Estructura mínima:

      ```markdown
      Semana 1 — Capas, IP, TCP/UDP
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/semana-01.md` unifica L01–L03 con índice y enlaces a logs.'
      - README de m10 marca “Semana 1 / P1 parcial” con checklist.
      - 'Commit `docs(m10): l04 cierre semana 1 bitacora`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre semana 1 — bitácora P1

**~5.0 h · Semana 1**

P1 es bitácora reproducible. Hoy la dejas legible para tu yo de la semana 5.

## Objetivo

Consolidar evidencia de capas/IP/TCP y actualizar el README del proyecto.

## Pasos

### 1. Auditoría de archivos (30 min)

```bash
find projects/m10-redes -type f | sort
```

Mueve notas sueltas a `labs/` si hace falta.

### 2. Consolida `semana-01.md` (90–120 min)

Estructura mínima:

```markdown
# Semana 1 — Capas, IP, TCP/UDP
## Índice
## Capas + curl (L01)
## IP / ruta (L02)
## Puertos Vitrina (L03)
## Pendientes
```

Copia fragmentos **anotados** (no dumps enteros).

### 3. README (45 min)

En `projects/m10-redes/README.md`, sección “Semana 1”:

- [x] dia1 + curl log
- [x] IP/gateway/traceroute
- [x] tabla puertos

### 4. Auto-quiz (30 min)

Responde por escrito (5–8 líneas c/u): (a) qué protege TLS vs qué no; (b) por qué 5432 no va a internet; (c) triage timeout.

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l04 cierre semana 1 bitacora"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Síntesis capas + IP + transporte; checklist P1 parcial | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-01.md` unifica L01–L03 con índice y enlaces a logs.
2. README de m10 marca “Semana 1 / P1 parcial” con checklist.
3. Commit `docs(m10): l04 cierre semana 1 bitacora`.

## Errores comunes

- Tres archivos sueltos sin índice.
- Checklist vacía (“luego documento”).
- Commit sin `labs/`.

## Siguiente

[L05 — DNS: resolución, registros y fallos](L05-dns-resolucion-registros-y-fallos.md)
