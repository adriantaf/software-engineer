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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Cerrar P2 con rotación + `restore-prueba.md`.

      Un backup no probado es un cuento. Hoy rotas y restauras.
  - id: s2
    tipo: ejemplo
    titulo: 1. Rotación
    xp: 10
    cuerpo: |-
      ```bash
      # idea; ajusta a tu motor
      # createdb agenda_restore_test
      # gunzip -c backups/db-….sql.gz | psql agenda_restore_test
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Rotación de logs y restore de prueba" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: restore-prueba.md + script rotación
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

      `git add projects/m11-so`
    comandoEsperado:
      - git add projects/m11-so
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m11-so'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Cerrar P2 con rotación + `restore-prueba.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Restore de prueba
    xp: 10
    cuerpo: >-
      ```bash

      idea; ajusta a tu motor

      createdb agenda_restore_test

      gunzip -c backups/db-….sql.gz | psql agenda_restore_test

      ```


      Documenta en `restore-prueba.md`: fecha, origen, destino, verificación
      (`SELECT count(*)` o equivalente en fixture).
  - id: s7
    tipo: explicacion
    titulo: 3. README P2
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
