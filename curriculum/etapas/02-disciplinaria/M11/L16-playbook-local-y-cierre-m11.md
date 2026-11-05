---
id: L16
materia: M11
orden: 16
titulo: Playbook local y cierre M11
horas: 5
semana: 4
lectura: Ficha M11 completa
evidencia: playbook.md + cierre P1–P3
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Publicar `playbook.md` y cerrar evidencias P1–P3.

      Otro desarrollador debe levantar el stack solo con tu playbook.
  - id: s2
    tipo: ejemplo
    titulo: 1. Redacta playbook
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m11-so
      git commit -m "docs(m11): cierre playbook"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Playbook local y cierre M11" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: playbook.md + cierre P1–P3
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
        texto: Publicar `playbook.md` y cerrar evidencias P1–P3.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Dry-run
    xp: 10
    cuerpo: >-
      Sigue el playbook desde cero (borra contenedores) y anota fricciones;
      corrígelas.
  - id: s7
    tipo: explicacion
    titulo: 3. Checklist dominio
    xp: 10
    cuerpo: >-
      Responde en `dominio-oral.md`: SIGTERM, backup+restore, non-root, playbook
      ajeno.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `playbook.md` con prerequisitos, up/down, backup, restore,
        troubleshooting.
      - 'README enlaza P1 labs, P2 scripts, P3 Docker, playbook.'
      - 'Commit `docs(m11): cierre playbook`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Playbook local y cierre M11

**~5.0 h · Semana 4**

Otro desarrollador debe levantar el stack solo con tu playbook.

## Objetivo

Publicar `playbook.md` y cerrar evidencias P1–P3.

## Pasos

### 1. Redacta playbook (90–110 min)

`projects/m11-so/playbook.md`:

- Prerequisitos (Docker, puertos)
- `cp .env.example .env` + editar
- `docker compose up -d --build`
- Healthcheck curl
- Backup (`scripts/backup.sh`)
- Restore de prueba (enlace)
- `docker compose down`
- Diagrama Mermaid host → api/db → volume

### 2. Dry-run (50 min)

Sigue el playbook desde cero (borra contenedores) y anota fricciones; corrígelas.

### 3. Checklist dominio (30 min)

Responde en `dominio-oral.md`: SIGTERM, backup+restore, non-root, playbook ajeno.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): cierre playbook"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Playbook reproducible: up/down/backup/restore | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `playbook.md` con prerequisitos, up/down, backup, restore, troubleshooting.
2. README enlaza P1 labs, P2 scripts, P3 Docker, playbook.
3. Commit `docs(m11): cierre playbook`.

## Errores comunes

- Playbook que solo funciona en tu cabeza.
- Secretos en el playbook.
- Marcar dominio sin restore documentado.

## Siguiente

Cierra la [ficha M11](../M11-sistemas-operativos.md). Recomendado: [M27](../M27-sistemas-bajo-nivel.md) o sigue a [M12](../M12-requerimientos.md).
