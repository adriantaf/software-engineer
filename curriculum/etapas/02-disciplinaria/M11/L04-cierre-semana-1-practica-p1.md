---
id: L04
materia: M11
orden: 4
titulo: Cierre semana 1 — práctica P1
horas: 5
semana: 1
lectura: Repaso Silberschatz procesos
evidencia: labs/semana-01-procesos.md consolidado (P1)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 es bitácora de procesos/señales/permisos. Hoy la dejas revisable.


      **Objetivo de esta lección:** Consolidar semana 1 y actualizar el README.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m11-so -type f | sort
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Consolida
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so
      git commit -m "docs(m11): l04 cierre semana 1 p1"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre semana 1 — práctica P1», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre semana 1 —
          práctica P1
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

      `find projects/m11-so -type f | sort`
    comandoEsperado:
      - find projects/m11-so -type f | sort
      - git add projects/m11-so
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: find projects/m11-so -type f | sort'
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
        texto: Consolidar semana 1 y actualizar el README.
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
    cuerpo: >-
      Checklist: - [x] labs dia1 - [x] notas hilos/event loop - [x]
      graceful-server + prueba
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/semana-01-procesos.md` unifica L01–L03 con comandos reproducibles.'
      - README marca P1 parcial (procesos/señales).
      - 'Commit `docs(m11): l04 cierre semana 1 p1`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Cierre semana 1 — práctica P1

**~5.0 h · Semana 1**

P1 es bitácora de procesos/señales/permisos. Hoy la dejas revisable.

## Objetivo

Consolidar semana 1 y actualizar el README.

## Pasos

### 1. Inventario (25 min)

```bash
find projects/m11-so -type f | sort
```

### 2. Consolida (90–110 min)

`semana-01-procesos.md` con secciones: dia1, proceso vs hilo, SIGTERM (enlace al código). Incluye 3 comandos “runbook” de diagnóstico.

### 3. README (40 min)

Checklist:

- [x] labs dia1
- [x] notas hilos/event loop
- [x] graceful-server + prueba

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): l04 cierre semana 1 p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Síntesis procesos/hilos/señales; checklist P1 parcial | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-01-procesos.md` unifica L01–L03 con comandos reproducibles.
2. README marca P1 parcial (procesos/señales).
3. Commit `docs(m11): l04 cierre semana 1 p1`.

## Errores comunes

- Labs sin comandos copiables.
- Código graceful sin nota de prueba.
- Checklist vacía.

## Siguiente

[L05 — Memoria virtual y paginación (intuición)](L05-memoria-virtual-y-paginacion-intuicion.md)
