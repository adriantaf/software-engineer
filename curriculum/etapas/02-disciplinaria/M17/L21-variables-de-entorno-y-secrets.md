---
id: L21
materia: M17
orden: 21
titulo: Variables de entorno y secrets
horas: 5
semana: 6
lectura: 12-factor config
evidencia: projects/m17-vitrina/.env.example
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Separar config: DATABASE_URL, SESSION_SECRET, etc.
      `.env.example` sin valores reales.


      - env

      - secrets

      - example
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventaria vars
    xp: 10
    cuerpo: |-
      ```bash
      cat projects/m17-vitrina/.env.example
      rg -n "process\\.env|env\\." projects/m17-vitrina/src | head -40
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Variables de entorno y secrets" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/.env.example
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

      `cat projects/m17-vitrina/.env.example`
    comandoEsperado:
      - cat projects/m17-vitrina/.env.example
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cat projects/m17-vitrina/.env.example'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Separar config: DATABASE_URL, SESSION_SECRET, etc. `.env.example` sin
          valores reales.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Separa secrets de config
    xp: 10
    cuerpo: |-
      ```bash
      ejemplo .env.example
      cat >> projects/m17-vitrina/.env.example << 'EOF'
      DATABASE_URL=postgresql://app:changeme@localhost:5432/vitrina
      SESSION_SECRET=change-me-min-32-chars
      CORS_ORIGIN=http://localhost:5173
      EOF
      ```

      Confirma `.env` en `.gitignore`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/.env.example
      git status | grep -i '\\.env$' && echo 'FAIL: .env tracked' || true
      git commit -m "docs(m17): L21 env example secrets"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/.env.example` lista vars con comentarios; `.env`
        no tracked.
      - 'Commit `docs(m17): L21 variables-de-entorno-y-secrets`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L21 — Variables de entorno y secrets

**~5.0 h · Semana 6**

Deploy seguro empieza por no commitear secrets.

## Objetivo

Separar config: DATABASE_URL, SESSION_SECRET, etc. `.env.example` sin valores reales.

## Conceptos clave

- env
- secrets
- example

## Pasos (hazlos en orden)

### 1. Inventaria vars (40–50 min)

```bash
cat projects/m17-vitrina/.env.example
rg -n "process\\.env|env\\." projects/m17-vitrina/src | head -40
```

Cada var en `.env.example` con comentario; **sin** valores secretos.

### 2. Separa secrets de config (40 min)

```bash
# ejemplo .env.example
cat >> projects/m17-vitrina/.env.example << 'EOF'
# DATABASE_URL=postgresql://app:changeme@localhost:5432/vitrina
# SESSION_SECRET=change-me-min-32-chars
# CORS_ORIGIN=http://localhost:5173
EOF
```

Confirma `.env` en `.gitignore`.

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/.env.example
git status | grep -i '\\.env$' && echo 'FAIL: .env tracked' || true
git commit -m "docs(m17): L21 env example secrets"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | 12-factor config | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/.env.example` lista vars con comentarios; `.env` no tracked.
2. Commit `docs(m17): L21 variables-de-entorno-y-secrets`.

## Errores comunes

- Commitear `.env`.
- Secrets horneados en código.

## Siguiente

[L22 — Deploy staging en PaaS](L22-deploy-staging-en-paas.md)
