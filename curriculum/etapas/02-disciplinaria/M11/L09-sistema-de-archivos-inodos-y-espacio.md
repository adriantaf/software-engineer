---
id: L09
materia: M11
orden: 9
titulo: 'Sistema de archivos: inodos y espacio'
horas: 5
semana: 3
lectura: Silberschatz sistema de archivos
evidencia: labs/semana-03-fs.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Diagnosticar uso de disco como operador del piloto.

      Backups y logs viven en disco. Hoy mides espacio e inodos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Medición
    xp: 10
    cuerpo: |-
      ```bash
      df -h
      df -i
      du -sh projects/* 2>/dev/null | sort -h
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Sistema de archivos: inodos y espacio" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: labs/semana-03-fs.md
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

      `git add projects/m11-so/labs/semana-03-fs.md`
    comandoEsperado:
      - git add projects/m11-so/labs/semana-03-fs.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m11-so/labs/semana-03-fs.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Diagnosticar uso de disco como operador del piloto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Conceptos
    xp: 10
    cuerpo: >-
      Inodo vs nombre de archivo; hardlink vs symlink (una tabla). Qué pasa con
      muchas fotos/tmp de pedidos.
  - id: s7
    tipo: explicacion
    titulo: 3. Política
    xp: 10
    cuerpo: >-
      Dónde vivirían backups y logs de Vitrina; cuota mínima libre antes de
      alerta.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`labs/semana-03-fs.md` con `df -h`, `df -i`, `du -sh` anotados.'
      - Explicas diferencia “disco lleno” vs “sin inodos”.
      - 'Commit `docs(m11): l09 filesystem inodos`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Sistema de archivos: inodos y espacio

**~5.0 h · Semana 3**

Backups y logs viven en disco. Hoy mides espacio e inodos.

## Objetivo

Diagnosticar uso de disco como operador del piloto.

## Pasos

### 1. Medición (45 min)

```bash
df -h
df -i
du -sh projects/* 2>/dev/null | sort -h
```

### 2. Conceptos (45 min)

Inodo vs nombre de archivo; hardlink vs symlink (una tabla). Qué pasa con muchas fotos/tmp de pedidos.

### 3. Política (30 min)

Dónde vivirían backups y logs de Vitrina; cuota mínima libre antes de alerta.

### 4. Commit (15 min)

```bash
git add projects/m11-so/labs/semana-03-fs.md
git commit -m "docs(m11): l09 filesystem inodos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Inodos, enlaces, df/du; quedarse sin inodos vs sin bloques | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-03-fs.md` con `df -h`, `df -i`, `du -sh` anotados.
2. Explicas diferencia “disco lleno” vs “sin inodos”.
3. Commit `docs(m11): l09 filesystem inodos`.

## Errores comunes

- Borrar logs a ciegas en prod.
- Llenar disco con dumps de BD sin rotación.
- Ignorar tamaño de `node_modules`/imágenes Docker.

## Siguiente

[L10 — Permisos, usuarios y mínimo privilegio](L10-permisos-usuarios-y-minimo-privilegio.md)
