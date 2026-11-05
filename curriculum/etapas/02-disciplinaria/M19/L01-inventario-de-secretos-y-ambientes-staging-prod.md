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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear inventario de secretos sin valores y definir
      URLs/objetivo de staging y prod para Vitrina.


      - DATABASE_URL

      - SESSION_SECRET

      - Stripe test futuro
  - id: s2
    tipo: ejemplo
    titulo: 1. Carpetas de evidencia
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m19-ops/{scripts,logs,docs}
      ls projects/m19-ops
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Inventario de secretos y ambientes staging/prod" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/secrets-inventory.md + ambientes.md
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

      `mkdir -p projects/m19-ops/{scripts,logs,docs}`
    comandoEsperado:
      - 'mkdir -p projects/m19-ops/{scripts,logs,docs}'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m19-ops/{scripts,logs,docs}'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Crear inventario de secretos sin valores y definir URLs/objetivo de
          staging y prod para Vitrina.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario de secretos sin valores
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/secrets-inventory.md << 'EOF'
      Inventario de secretos (SIN valores)
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
  - id: s7
    tipo: ejemplo
    titulo: 3. ambientes.md staging vs prod
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
