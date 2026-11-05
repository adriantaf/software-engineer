---
id: L01
materia: M19
orden: 1
titulo: Inventario de secretos y ambientes staging/prod
horas: 5
semana: 1
lectura: Docker docs — env vars + 12-factor
evidencia: projects/m19-ops/secrets-inventory.md + ambientes.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - DATABASE_URL

      - SESSION_SECRET

      - Stripe test futuro


      **Objetivo de esta lección:** Crear inventario de secretos sin valores y
      definir URLs/objetivo de staging y prod para Vitrina.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Carpetas de evidencia
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m19-ops/{scripts,logs,docs}
      ls projects/m19-ops
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Inventario de secretos sin valores
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/secrets-inventory.md << 'EOF'
      # Inventario de secretos (SIN valores)
      | Variable | Staging | Prod | Quién inyecta | Rotación |
      |----------|---------|------|---------------|----------|
      | DATABASE_URL | sí | sí | PaaS/VPS secrets | 90d |
      | SESSION_SECRET | sí | sí | secrets manager | 90d |
      EOF
      ```

      Cruza con M17:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Inventario de secretos y ambientes staging/prod», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Inventario de secretos
          y ambientes stag…
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

      `mkdir -p projects/m19-ops/{scripts,logs,docs}`
    comandoEsperado:
      - 'mkdir -p projects/m19-ops/{scripts,logs,docs}'
      - ls projects/m19-ops
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m19-ops/{scripts,logs,docs}'
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
          Crear inventario de secretos sin valores y definir URLs/objetivo de
          staging y prod para Vitrina.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: ambientes.md staging vs prod
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/ambientes.md << 'EOF'
      # Ambientes
      | Env | URL API | URL Front | Notas |
      |-----|---------|-----------|-------|
      | local | http://localhost:3000 | http://localhost:5173 | |
      | staging | https://… | https://… | |
      | prod | TBD | TBD | |
      EOF
      git add projects/m19-ops
      git commit -m "docs(m19): L01 inventario secretos ambientes"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existen `projects/m19-ops/secrets-inventory.md` y
        `projects/m19-ops/ambientes.md`.
      - Inventario sin valores secretos; URLs staging/prod anotadas.
      - 'Commit `docs(m19): L01 inventario-de-secretos-y-ambientes-staging-prod`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Inventario de secretos y ambientes staging/prod

**~5.0 h · Semana 1**

M19 empieza donde M18 dejó: nada de secretos en git antes de empaquetar.

## Objetivo

Crear inventario de secretos sin valores y definir URLs/objetivo de staging y prod para Vitrina.

## Conceptos clave

- DATABASE_URL
- SESSION_SECRET
- Stripe test futuro

## Pasos (hazlos en orden)

### 1. Carpetas de evidencia (15 min)

```bash
mkdir -p projects/m19-ops/{scripts,logs,docs}
ls projects/m19-ops
```

### 2. Inventario de secretos sin valores (80–100 min)

```bash
cat > projects/m19-ops/secrets-inventory.md << 'EOF'
# Inventario de secretos (SIN valores)
| Variable | Staging | Prod | Quién inyecta | Rotación |
|----------|---------|------|---------------|----------|
| DATABASE_URL | sí | sí | PaaS/VPS secrets | 90d |
| SESSION_SECRET | sí | sí | secrets manager | 90d |
EOF
```

Cruza con M17:

```bash
cat projects/m17-vitrina/.env.example
```

### 3. ambientes.md staging vs prod (30–40 min)

```bash
cat > projects/m19-ops/ambientes.md << 'EOF'
# Ambientes
| Env | URL API | URL Front | Notas |
|-----|---------|-----------|-------|
| local | http://localhost:3000 | http://localhost:5173 | |
| staging | https://… | https://… | |
| prod | TBD | TBD | |
EOF
git add projects/m19-ops
git commit -m "docs(m19): L01 inventario secretos ambientes"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Docker docs — env vars + 12-factor | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existen `projects/m19-ops/secrets-inventory.md` y `projects/m19-ops/ambientes.md`.
2. Inventario **sin** valores secretos; URLs staging/prod anotadas.
3. Commit `docs(m19): L01 inventario-de-secretos-y-ambientes-staging-prod`.

## Errores comunes

- Pegar JWT/passwords en markdown.
- Un solo ambiente llamado ‘prod’.

## Siguiente

[L02 — Dockerfile multi-stage para la API](L02-dockerfile-multi-stage-para-la-api.md)
