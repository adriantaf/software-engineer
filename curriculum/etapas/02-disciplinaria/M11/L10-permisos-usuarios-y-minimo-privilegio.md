---
id: L10
materia: M11
orden: 10
titulo: 'Permisos, usuarios y mínimo privilegio'
horas: 5
semana: 3
lectura: Silberschatz protección
evidencia: labs/permisos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Least privilege en host es parte del [hilo de
      seguridad](../../../hilos/seguridad.md).


      **Objetivo de esta lección:** Definir permisos para datos sensibles del
      piloto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lab
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m11-so/samples/permisos-demo

      echo 'fake-secret' > projects/m11-so/samples/permisos-demo/secret.env

      chmod 600 projects/m11-so/samples/permisos-demo/secret.env

      ls -la projects/m11-so/samples/permisos-demo

      # secret.env es demo: no pongas secretos reales; añade samples/ al
      criterio de no-commit si hace falta

      ```


      Asegura que `secret.env` **no** se commitea si contiene algo real — usa
      placeholder y `.gitignore` si es necesario. Mejor: documenta solo `ls -la`
      y borra el secreto.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Política
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so/labs/permisos.md
      git commit -m "docs(m11): l10 permisos least privilege"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Permisos, usuarios y mínimo privilegio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Permisos, usuarios y
          mínimo privilegio
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

      `mkdir -p projects/m11-so/samples/permisos-demo`
    comandoEsperado:
      - mkdir -p projects/m11-so/samples/permisos-demo
      - echo 'fake-secret' > projects/m11-so/samples/permisos-demo/secret.env
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m11-so/samples/permisos-demo'
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
        texto: Definir permisos para datos sensibles del piloto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so/labs/permisos.md
      git commit -m "docs(m11): l10 permisos least privilege"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/permisos.md` con árbol de permisos propuesto para `backups/`,
        `logs/`, `.env`.
      - >-
        Demostración local de archivo 600 vs intento de lectura con otro usuario
        (o explicación equivalente).
      - 'Commit `docs(m11): l10 permisos least privilege`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Permisos, usuarios y mínimo privilegio

**~5.0 h · Semana 3**

Least privilege en host es parte del [hilo de seguridad](../../../hilos/seguridad.md).

## Objetivo

Definir permisos para datos sensibles del piloto.

## Pasos

### 1. Lab (50 min)

```bash
mkdir -p projects/m11-so/samples/permisos-demo
echo 'fake-secret' > projects/m11-so/samples/permisos-demo/secret.env
chmod 600 projects/m11-so/samples/permisos-demo/secret.env
ls -la projects/m11-so/samples/permisos-demo
# secret.env es demo: no pongas secretos reales; añade samples/ al criterio de no-commit si hace falta
```

Asegura que `secret.env` **no** se commitea si contiene algo real — usa placeholder y `.gitignore` si es necesario. Mejor: documenta solo `ls -la` y borra el secreto.

### 2. Política (60 min)

En `labs/permisos.md`: owner del proceso API, grupo, modo de `backups/*.sql`, logs, claves TLS.

### 3. Commit (15 min)

```bash
git add projects/m11-so/labs/permisos.md
git commit -m "docs(m11): l10 permisos least privilege"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | chmod/chown, usuarios/grupos, least privilege en datos y logs | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/permisos.md` con árbol de permisos propuesto para `backups/`, `logs/`, `.env`.
2. Demostración local de archivo 600 vs intento de lectura con otro usuario (o explicación equivalente).
3. Commit `docs(m11): l10 permisos least privilege`.

## Errores comunes

- `chmod 777` otra vez.
- Meter el usuario de la app en grupo docker sin necesidad.
- Secretos con ACL abierta en el repo.

## Siguiente

[L11 — Script de backup automatizado (P2)](L11-script-de-backup-automatizado-p2.md)
