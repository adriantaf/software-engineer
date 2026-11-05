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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 es bitácora reproducible. Hoy la dejas legible para tu yo de la semana
      5.


      **Objetivo de esta lección:** Consolidar evidencia de capas/IP/TCP y
      actualizar el README del proyecto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría de archivos
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m10-redes -type f | sort
      ```

      Mueve notas sueltas a `labs/` si hace falta.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Consolida `semana-01.md`
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m10-redes -type f | sort
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre semana 1 — bitácora P1», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre semana 1 —
          bitácora P1
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

      `find projects/m10-redes -type f | sort`
    comandoEsperado:
      - find projects/m10-redes -type f | sort
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: find projects/m10-redes -type f | sort'
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
          Consolidar evidencia de capas/IP/TCP y actualizar el README del
          proyecto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Checklist vacía (“luego documento”)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/semana-01.md` unifica L01–L03 con índice y enlaces a logs.'
      - README de m10 marca “Semana 1 / P1 parcial” con checklist.
      - 'Commit `docs(m10): l04 cierre semana 1 bitacora`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
