---
id: L12
materia: M11
orden: 12
titulo: Rotación de logs y restore de prueba
horas: 5
semana: 3
lectura: logrotate concept + tu script de backup
evidencia: restore-prueba.md + script rotación
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un backup no probado es un cuento. Hoy rotas y restauras.


      **Objetivo de esta lección:** Cerrar P2 con rotación +
      `restore-prueba.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Rotación
    xp: 10
    cuerpo: |-
      ```bash
      # idea; ajusta a tu motor
      # createdb agenda_restore_test
      # gunzip -c backups/db-….sql.gz | psql agenda_restore_test
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Restore de prueba
    xp: 10
    cuerpo: >-
      ```bash

      # idea; ajusta a tu motor

      # createdb agenda_restore_test

      # gunzip -c backups/db-….sql.gz | psql agenda_restore_test

      ```


      Documenta en `restore-prueba.md`: fecha, origen, destino, verificación
      (`SELECT count(*)` o equivalente en fixture).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Rotación de logs y restore de prueba», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Rotación de logs y
          restore de prueba
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

      `git add projects/m11-so`
    comandoEsperado:
      - git add projects/m11-so
      - 'git commit -m "feat(m11): l12 rotacion y restore"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m11-so'
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
        texto: Cerrar P2 con rotación + `restore-prueba.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README P2
    xp: 10
    cuerpo: Marca P2 listo con enlaces a scripts + restore.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Script de rotación de logs (o backups) en `scripts/`.
      - >-
        `restore-prueba.md` con fecha, comandos y resultado (aunque sea
        fixture).
      - 'Commit `feat(m11): l12 rotacion y restore`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Rotación de logs y restore de prueba

**~5.0 h · Semana 3**

Un backup no probado es un cuento. Hoy rotas y restauras.

## Objetivo

Cerrar P2 con rotación + `restore-prueba.md`.

## Pasos

### 1. Rotación (60 min)

`scripts/rotate-logs.sh`: mueve `logs/app.log` a `logs/app-$(date +%F).log` si supera N bytes; comprime; borra >RETENTION.

### 2. Restore de prueba (75–90 min)

```bash
# idea; ajusta a tu motor
# createdb agenda_restore_test
# gunzip -c backups/db-….sql.gz | psql agenda_restore_test
```

Documenta en `restore-prueba.md`: fecha, origen, destino, verificación (`SELECT count(*)` o equivalente en fixture).

### 3. README P2 (20 min)

Marca P2 listo con enlaces a scripts + restore.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "feat(m11): l12 rotacion y restore"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Rotación por tamaño/fecha; restore de backup a destino de prueba | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. Script de rotación de logs (o backups) en `scripts/`.
2. `restore-prueba.md` con fecha, comandos y resultado (aunque sea fixture).
3. Commit `feat(m11): l12 rotacion y restore`.

## Errores comunes

- Backup sin restore de prueba.
- Rotar borrando el único backup bueno.
- Restore sobre prod sin decirlo.

## Siguiente

[L13 — Imágenes, contenedores y volúmenes](L13-imagenes-contenedores-y-volumenes.md)
