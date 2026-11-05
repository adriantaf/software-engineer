---
id: L01
materia: M17
orden: 1
titulo: 'Scaffold Vitrina — API, DB y stack'
horas: 5
semana: 1
lectura: producto-saas.md + m13-diseno + M09 esquema
evidencia: projects/m17-vitrina/stack.md + scaffold API
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Inicializar `projects/m17-vitrina/` con TypeScript strict,
      conexión Postgres y documentar stack fijo.


      - scaffold

      - Postgres

      - monolito modular
  - id: s2
    tipo: ejemplo
    titulo: 1. Revisa producto y diseño previo
    xp: 10
    cuerpo: >-
      ```bash

      cd /workspace   # o raíz del monorepo academia

      head -n 80 curriculum/producto-saas.md

      ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null |
      head

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Scaffold Vitrina — API, DB y stack" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/stack.md + scaffold API
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

      `cd /workspace   # o raíz del monorepo academia`
    comandoEsperado:
      - 'cd /workspace   # o raíz del monorepo academia'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd /workspace   # o raíz del monorepo academia'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Inicializar `projects/m17-vitrina/` con TypeScript strict, conexión
          Postgres y documentar stack fijo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Scaffold de carpetas y toolchain
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m17-vitrina/{docs,src,tests,scripts,apps}

      cd projects/m17-vitrina

      Si aún no hay package.json:

      npm init -y

      npm install -D typescript tsx vitest @types/node

      npx tsc --init --strict --rootDir src --outDir dist --module nodenext
      --moduleResolution nodenext --target ES2022

      ```


      Confirma `strict: true` en `tsconfig.json`. Runtime Node LTS + framework
      HTTP alineado a M13 ADR 001.
  - id: s7
    tipo: ejemplo
    titulo: 3. Documenta stack.md inmutable
    xp: 10
    cuerpo: |-
      ```md
      | Capa | Elección | Notas |
      |------|----------|-------|
      | Runtime | Node 22 LTS | |
      | API | Fastify / Express / Nest | TypeScript strict |
      | ORM | drizzle / prisma / knex | esquema M09 |
      | Front | React / Next | |
      | Tests | Vitest | |
      | Auth | Cookie HttpOnly | docs/auth.md |
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/` con TypeScript strict y carpetas
        `src/`/`tests/`/`docs/`.
      - >-
        `projects/m17-vitrina/stack.md` lista runtime, API, ORM, front, tests y
        auth.
      - '`GET /health` responde 200 con DB up (anotado en README sin secrets).'
      - 'Commit `docs(m17): L01 scaffold-vitrina-api-db-y-stack`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Scaffold Vitrina — API, DB y stack

**~5.0 h · Semana 1**

Cambiar stack a mitad de materia sin ADR destruye velocidad.

## Objetivo

Inicializar `projects/m17-vitrina/` con TypeScript strict, conexión Postgres y documentar stack fijo.

## Conceptos clave

- scaffold
- Postgres
- monolito modular

## Pasos (hazlos en orden)

### 1. Revisa producto y diseño previo (30–40 min)

```bash
cd /workspace   # o raíz del monorepo academia
head -n 80 curriculum/producto-saas.md
ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null | head
```

Anota 5 endpoints Must del piloto: register, login, me, pedidos, clientes/servicios.

### 2. Scaffold de carpetas y toolchain (40–50 min)

```bash
mkdir -p projects/m17-vitrina/{docs,src,tests,scripts,apps}
cd projects/m17-vitrina
# Si aún no hay package.json:
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist --module nodenext --moduleResolution nodenext --target ES2022
```

Confirma `strict: true` en `tsconfig.json`. Runtime Node LTS + framework HTTP alineado a M13 ADR 001.

### 3. Documenta stack.md inmutable (30–40 min)

Completa `projects/m17-vitrina/stack.md` (ya hay plantilla). Ejemplo mínimo:

```md
| Capa | Elección | Notas |
|------|----------|-------|
| Runtime | Node 22 LTS | |
| API | Fastify / Express / Nest | TypeScript strict |
| ORM | drizzle / prisma / knex | esquema M09 |
| Front | React / Next | |
| Tests | Vitest | |
| Auth | Cookie HttpOnly | docs/auth.md |
```

Cambio de stack = ADR en `docs/`.

### 4. Postgres + GET /health (60–80 min)

```bash
cp projects/m17-vitrina/.env.example projects/m17-vitrina/.env
# Edita DATABASE_URL / POSTGRES_* — .env NO va a git
# Reusa Compose M09 o el tuyo; luego arranca la API
curl -sS http://localhost:3000/health
# Esperado JSON tipo {"ok":true,"db":"up"}
```

Si falla DB, anota el error en README **sin** password.

### 5. Commit (10–15 min)

```bash
git add projects/m17-vitrina
git status   # .env NO debe aparecer
git commit -m "docs(m17): L01 scaffold stack health postgres"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | producto-saas.md + m13-diseno + M09 esquema | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/` con TypeScript strict y carpetas `src/`/`tests/`/`docs/`.
2. `projects/m17-vitrina/stack.md` lista runtime, API, ORM, front, tests y auth.
3. `GET /health` responde 200 con DB up (anotado en README sin secrets).
4. Commit `docs(m17): L01 scaffold-vitrina-api-db-y-stack`.

## Errores comunes

- Subir `.env` con passwords.
- Cambiar framework sin ADR.
- Health 200 sin ping a DB documentado.

## Siguiente

[L02 — Registro con hash de contraseña](L02-registro-con-hash-de-contrasena.md)
