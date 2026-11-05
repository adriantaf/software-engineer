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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir permisos para datos sensibles del piloto.


      Least privilege en host es parte del [hilo de
      seguridad](../../../hilos/seguridad.md).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lab
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Permisos, usuarios y mínimo privilegio" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: labs/permisos.md
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

      `mkdir -p projects/m11-so/samples/permisos-demo`
    comandoEsperado:
      - mkdir -p projects/m11-so/samples/permisos-demo
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m11-so/samples/permisos-demo'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Definir permisos para datos sensibles del piloto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Política
    xp: 10
    cuerpo: >-
      En `labs/permisos.md`: owner del proceso API, grupo, modo de
      `backups/*.sql`, logs, claves TLS.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
