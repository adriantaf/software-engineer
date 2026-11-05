---
id: L14
materia: M19
orden: 14
titulo: Prueba de restore en entorno aislado
horas: 5
semana: 4
lectura: Restore docs
evidencia: projects/m19-ops/restore-test.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Restaurar dump en DB de prueba, verificar pedidos visibles,
      registrar tiempo y resultado.


      - restore

      - RTO idea

      - vacuum
  - id: s2
    tipo: ejemplo
    titulo: 1. Restore aislado
    xp: 10
    cuerpo: >-
      ```bash

      # entorno scratch — NO prod

      createdb agenda_restore_test || true

      gunzip -c backups/agenda-XXXX.sql.gz | psql
      "postgresql://…/agenda_restore_test"

      psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*) FROM
      pedidos;'

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Prueba de restore en entorno aislado" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/restore-test.md
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

      `git add projects/m19-ops/restore-test.md`
    comandoEsperado:
      - git add projects/m19-ops/restore-test.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m19-ops/restore-test.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Restaurar dump en DB de prueba, verificar pedidos visibles, registrar
          tiempo y resultado.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. restore-test.md
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/restore-test.md << 'EOF'
      Restore test
      Fecha: YYYY-MM-DD
      Dump usado: agenda-….sql.gz
      Destino: DB aislada …
      Resultado: OK — count pedidos = N
      EOF
      git add projects/m19-ops/restore-test.md
      git commit -m "docs(m19): L14 prueba restore aislado"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/restore-test.md` con fecha, dump usado y resultado
        real.
      - 'Commit `docs(m19): L14 prueba-de-restore-en-entorno-aislado`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L14 — Prueba de restore en entorno aislado

**~5.0 h · Semana 4**

Un restore nunca probado no cuenta.

## Objetivo

Restaurar dump en DB de prueba, verificar pedidos visibles, registrar tiempo y resultado.

## Conceptos clave

- restore
- RTO idea
- vacuum

## Pasos (hazlos en orden)

### 1. Restore aislado (80–100 min)

```bash
# entorno scratch — NO prod
createdb agenda_restore_test || true
gunzip -c backups/agenda-XXXX.sql.gz | psql "postgresql://…/agenda_restore_test"
psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*) FROM pedidos;'
```

### 2. restore-test.md (30–40 min)

```bash
cat > projects/m19-ops/restore-test.md << 'EOF'
# Restore test
Fecha: YYYY-MM-DD
Dump usado: agenda-….sql.gz
Destino: DB aislada …
Resultado: OK — count pedidos = N
EOF
git add projects/m19-ops/restore-test.md
git commit -m "docs(m19): L14 prueba restore aislado"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Restore docs | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/restore-test.md` con fecha, dump usado y resultado real.
2. Commit `docs(m19): L14 prueba-de-restore-en-entorno-aislado`.

## Errores comunes

- Restore probado en prod.
- Afirmar OK sin `SELECT count`.

## Siguiente

[L15 — Runbook completo de producción](L15-runbook-completo-de-produccion.md)
