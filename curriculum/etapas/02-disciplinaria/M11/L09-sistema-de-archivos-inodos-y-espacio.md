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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Backups y logs viven en disco. Hoy mides espacio e inodos.


      **Objetivo de esta lección:** Diagnosticar uso de disco como operador del
      piloto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Medición
    xp: 10
    cuerpo: |-
      ```bash
      df -h
      df -i
      du -sh projects/* 2>/dev/null | sort -h
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Conceptos
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so/labs/semana-03-fs.md
      git commit -m "docs(m11): l09 filesystem inodos"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Sistema de archivos: inodos y espacio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Sistema de archivos:
          inodos y espacio
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

      `git add projects/m11-so/labs/semana-03-fs.md`
    comandoEsperado:
      - git add projects/m11-so/labs/semana-03-fs.md
      - 'git commit -m "docs(m11): l09 filesystem inodos"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m11-so/labs/semana-03-fs.md'
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
        texto: Diagnosticar uso de disco como operador del piloto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Política
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
