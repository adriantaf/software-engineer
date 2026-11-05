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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Vitrina correrá en un VPS o contenedor. Hoy lees procesos e identidad como
      lo harás en un incidente.


      **Objetivo de esta lección:** Levantar `projects/m11-so/` y documentar
      procesos, `id`/`umask` y permisos mínimos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Scaffold
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m11-so/{labs,scripts,app,samples}
      cat projects/m11-so/README.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Procesos
    xp: 10
    cuerpo: >-
      ```bash

      ps aux | head -20

      ps -o pid,ppid,user,stat,cmd --forest | head -40

      ```


      En `labs/dia1-comandos.md`: define PID, PPID, STAT común (R/S/Z a alto
      nivel).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Procesos, permisos y bitácora día 1», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Procesos, permisos y
          bitácora día 1
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

      `mkdir -p projects/m11-so/{labs,scripts,app,samples}`
    comandoEsperado:
      - 'mkdir -p projects/m11-so/{labs,scripts,app,samples}'
      - cat projects/m11-so/README.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m11-so/{labs,scripts,app,samples}'
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
          Levantar `projects/m11-so/` y documentar procesos, `id`/`umask` y
          permisos mínimos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Identidad y umask
    xp: 10
    cuerpo: Explica owner/group/other.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
