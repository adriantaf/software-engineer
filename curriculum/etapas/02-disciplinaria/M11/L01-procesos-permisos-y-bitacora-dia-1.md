---
id: L01
materia: M11
orden: 1
titulo: 'Procesos, permisos y bitácora día 1'
horas: 5
semana: 1
lectura: Silberschatz — procesos (intro) + permisos básicos
evidencia: projects/m11-so/labs/dia1-comandos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Levantar `projects/m11-so/` y documentar procesos,
      `id`/`umask` y permisos mínimos.


      Vitrina correrá en un VPS o contenedor. Hoy lees procesos e identidad como
      lo harás en un incidente.
  - id: s2
    tipo: ejemplo
    titulo: 1. Scaffold
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m11-so/{labs,scripts,app,samples}
      cat projects/m11-so/README.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Procesos, permisos y bitácora día 1" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m11-so/labs/dia1-comandos.md
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

      `mkdir -p projects/m11-so/{labs,scripts,app,samples}`
    comandoEsperado:
      - 'mkdir -p projects/m11-so/{labs,scripts,app,samples}'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m11-so/{labs,scripts,app,samples}'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Levantar `projects/m11-so/` y documentar procesos, `id`/`umask` y
          permisos mínimos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Procesos
    xp: 10
    cuerpo: >-
      ```bash

      ps aux | head -20

      ps -o pid,ppid,user,stat,cmd --forest | head -40

      ```


      En `labs/dia1-comandos.md`: define PID, PPID, STAT común (R/S/Z a alto
      nivel).
  - id: s7
    tipo: ejemplo
    titulo: 3. Identidad y umask
    xp: 10
    cuerpo: |-
      ```bash
      id
      umask
      echo "dato-piloto" > "/tmp/m11-test-$USER.txt"
      chmod 600 "/tmp/m11-test-$USER.txt"
      ls -la "/tmp/m11-test-$USER.txt"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/dia1-comandos.md` con salidas anotadas de `ps`, `id`, `umask` y un
        archivo `chmod 600`.
      - >-
        Párrafo: por qué `chmod 777` es inaceptable para datos de clientes
        Vitrina.
      - 'Commit `docs(m11): l01 procesos y permisos dia1`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Procesos, permisos y bitácora día 1

**~5.0 h · Semana 1**

Vitrina correrá en un VPS o contenedor. Hoy lees procesos e identidad como lo harás en un incidente.

## Objetivo

Levantar `projects/m11-so/` y documentar procesos, `id`/`umask` y permisos mínimos.

## Pasos (hazlos en orden)

### 1. Scaffold (15 min)

```bash
mkdir -p projects/m11-so/{labs,scripts,app,samples}
cat projects/m11-so/README.md
```

### 2. Procesos (45 min)

```bash
ps aux | head -20
ps -o pid,ppid,user,stat,cmd --forest | head -40
```

En `labs/dia1-comandos.md`: define PID, PPID, STAT común (R/S/Z a alto nivel).

### 3. Identidad y umask (40 min)

```bash
id
umask
echo "dato-piloto" > "/tmp/m11-test-$USER.txt"
chmod 600 "/tmp/m11-test-$USER.txt"
ls -la "/tmp/m11-test-$USER.txt"
```

Explica owner/group/other.

### 4. Anti-patrón (30 min)

Escribe por qué `chmod 777` en un directorio de backups/logs rompe confidencialidad de clientes.

### 5. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): l01 procesos y permisos dia1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | PID/PPID, usuario efectivo, permisos rwx, umask | [man ps (conceptos)](https://man7.org/linux/man-pages/man1/ps.1.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/dia1-comandos.md` con salidas anotadas de `ps`, `id`, `umask` y un archivo `chmod 600`.
2. Párrafo: por qué `chmod 777` es inaceptable para datos de clientes Vitrina.
3. Commit `docs(m11): l01 procesos y permisos dia1`.

## Errores comunes

- Pegar `ps aux` completo sin marcar tu shell/node.
- Correr labs como root “porque sí”.
- Dejar el archivo de prueba world-readable.

## Siguiente

[L02 — Proceso vs hilo y el runtime Node](L02-proceso-vs-hilo-y-el-runtime-node.md)
