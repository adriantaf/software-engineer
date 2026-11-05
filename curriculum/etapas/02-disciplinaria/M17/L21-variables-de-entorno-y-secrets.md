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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - env

      - secrets

      - example


      **Objetivo de esta lección:** Separar config: DATABASE_URL,
      SESSION_SECRET, etc. `.env.example` sin valores reales.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventaria vars
    xp: 10
    cuerpo: |-
      ```bash
      cat projects/m17-vitrina/.env.example
      rg -n "process\\.env|env\\." projects/m17-vitrina/src | head -40
      ```

      Cada var en `.env.example` con comentario; **sin** valores secretos.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Separa secrets de config
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo .env.example
      cat >> projects/m17-vitrina/.env.example << 'EOF'
      # DATABASE_URL=postgresql://app:changeme@localhost:5432/vitrina
      # SESSION_SECRET=change-me-min-32-chars
      # CORS_ORIGIN=http://localhost:5173
      EOF
      ```

      Confirma `.env` en `.gitignore`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Variables de entorno y secrets», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Variables de entorno y
          secrets
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

      `cat projects/m17-vitrina/.env.example`
    comandoEsperado:
      - cat projects/m17-vitrina/.env.example
      - git add projects/m17-vitrina/.env.example
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cat projects/m17-vitrina/.env.example'
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
          Separar config: DATABASE_URL, SESSION_SECRET, etc. `.env.example` sin
          valores reales.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
