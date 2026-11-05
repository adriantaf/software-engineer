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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Consolidar semana 1 y actualizar el README.

      P1 es bitácora de procesos/señales/permisos. Hoy la dejas revisable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m11-so -type f | sort
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre semana 1 — práctica P1" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: labs/semana-01-procesos.md consolidado (P1)
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

      `find projects/m11-so -type f | sort`
    comandoEsperado:
      - find projects/m11-so -type f | sort
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: find projects/m11-so -type f | sort'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Consolidar semana 1 y actualizar el README.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Consolida
    xp: 10
    cuerpo: >-
      `semana-01-procesos.md` con secciones: dia1, proceso vs hilo, SIGTERM
      (enlace al código). Incluye 3 comandos “runbook” de diagnóstico.
  - id: s7
    tipo: explicacion
    titulo: 3. README
    xp: 10
    cuerpo: |-
      Checklist:

      - [x] labs dia1
      - [x] notas hilos/event loop
      - [x] graceful-server + prueba
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/semana-01-procesos.md` unifica L01–L03 con comandos reproducibles.'
      - README marca P1 parcial (procesos/señales).
      - 'Commit `docs(m11): l04 cierre semana 1 p1`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
