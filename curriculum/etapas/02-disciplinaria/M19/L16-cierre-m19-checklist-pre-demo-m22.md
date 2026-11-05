---
id: L16
materia: M19
orden: 16
titulo: Cierre M19 — checklist pre-demo M22
horas: 5
semana: 4
lectura: Repaso M19
evidencia: projects/m19-ops/cierre-m19.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - checklist

      - dominio


      **Objetivo de esta lección:** Verificar P1–P3, criterios dominio, prod
      estable para trials.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist pre-demo M22
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/cierre-m19.md << 'EOF'
      # Cierre M19
      - [ ] docker.md P1
      - [ ] deploy-log HTTPS P2
      - [ ] restore-test.md P3
      - [ ] runbook.md
      Handoff: URL staging para M20/M22
      EOF
      ls projects/m19-ops
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m19-ops
      git commit -m "docs(m19): L16 cierre checklist pre-demo"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M19 — checklist pre-demo M22», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M19 — checklist
          pre-demo M22
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: 'Verificar P1–P3, criterios dominio, prod estable para trials.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git add projects/m19-ops`
    comandoEsperado:
      - git add projects/m19-ops
    explicacionError: 'Esperado: git add projects/m19-ops'
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M19
    xp: 25
    enunciado: >-
      Cierra **Cómputo en la nube y DevOps** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Docker multi-stage + Compose prod-like'
      - 'P2: Deploy reproducible con secretos en el hosting (staging/prod)'
      - 'P3: Backup automático de BD + restore probado'
      - 'Proyecto: Runbook de producción del SaaS Vitrina'
      - projects/m19-ops/cierre-m19.md
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          `projects/m19-ops/cierre-m19.md` checklist P1–P3 + handoff URL
          staging.
      - id: r3
        criterio: 'Commit `docs(m19): L16 cierre-m19-checklist-pre-demo-m22`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m19-ops/cierre-m19.md` checklist P1–P3 + handoff URL staging.'
      - 'Commit `docs(m19): L16 cierre-m19-checklist-pre-demo-m22`.'
    siguiente: Materia M19 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Cierre M19 — checklist pre-demo M22

**~5.0 h · Semana 4**

Handoff a M20 (API staging HTTPS) y M22.

## Objetivo

Verificar P1–P3, criterios dominio, prod estable para trials.

## Conceptos clave

- checklist
- dominio

## Pasos (hazlos en orden)

### 1. Checklist pre-demo M22 (50–60 min)

```bash
cat > projects/m19-ops/cierre-m19.md << 'EOF'
# Cierre M19
- [ ] docker.md P1
- [ ] deploy-log HTTPS P2
- [ ] restore-test.md P3
- [ ] runbook.md
Handoff: URL staging para M20/M22
EOF
ls projects/m19-ops
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops
git commit -m "docs(m19): L16 cierre checklist pre-demo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Repaso M19 | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/cierre-m19.md` checklist P1–P3 + handoff URL staging.
2. Commit `docs(m19): L16 cierre-m19-checklist-pre-demo-m22`.

## Errores comunes

- Cerrar sin restore-test.
- No dejar URL staging para M20/M22.

## Siguiente

Materia siguiente: [M20 — Aplicaciones móviles](../M20-aplicaciones-moviles.md) (consume tu staging).
