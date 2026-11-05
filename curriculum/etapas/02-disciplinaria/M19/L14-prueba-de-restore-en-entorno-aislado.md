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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - restore

      - RTO idea

      - vacuum


      **Objetivo de esta lección:** Restaurar dump en DB de prueba, verificar
      pedidos visibles, registrar tiempo y resultado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Restore aislado
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: restore-test.md
    xp: 10
    cuerpo: |-
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Prueba de restore en entorno aislado», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Prueba de restore en
          entorno aislado
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*) FROM
      pedidos;'`
    comandoEsperado:
      - >-
        psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*) FROM
        pedidos;'
      - git add projects/m19-ops/restore-test.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*)
      FROM pedidos;'
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
          Restaurar dump en DB de prueba, verificar pedidos visibles, registrar
          tiempo y resultado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git add projects/m19-ops/restore-test.md`
    comandoEsperado:
      - git add projects/m19-ops/restore-test.md
    explicacionError: 'Esperado: git add projects/m19-ops/restore-test.md'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/restore-test.md` con fecha, dump usado y resultado
        real.
      - 'Commit `docs(m19): L14 prueba-de-restore-en-entorno-aislado`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
