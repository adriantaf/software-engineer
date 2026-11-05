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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - scaffold

      - Postgres

      - monolito modular


      **Objetivo de esta lección:** Inicializar `projects/m17-vitrina/` con
      TypeScript strict, conexión Postgres y documentar stack fijo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Revisa producto y diseño previo
    xp: 10
    cuerpo: >-
      ```bash

      cd /workspace   # o raíz del monorepo academia

      head -n 80 curriculum/producto-saas.md

      ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null |
      head

      ```


      Anota 5 endpoints Must del piloto: register, login, me, pedidos,
      clientes/servicios.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Scaffold de carpetas y toolchain
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m17-vitrina/{docs,src,tests,scripts,apps}

      cd projects/m17-vitrina

      # Si aún no hay package.json:

      npm init -y

      npm install -D typescript tsx vitest @types/node

      npx tsc --init --strict --rootDir src --outDir dist --module nodenext
      --moduleResolution nodenext --target ES2022

      ```


      Confirma `strict: true` en `tsconfig.json`. Runtime Node LTS + framework
      HTTP alineado a M13 ADR 001.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Scaffold Vitrina — API, DB y stack», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Scaffold Vitrina — API,
          DB y stack
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

      `cd /workspace   # o raíz del monorepo academia`
    comandoEsperado:
      - 'cd /workspace   # o raíz del monorepo academia'
      - >-
        ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null |
        head
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: cd /workspace   # o raíz del monorepo academia'
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
          Inicializar `projects/m17-vitrina/` con TypeScript strict, conexión
          Postgres y documentar stack fijo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Documenta stack.md inmutable
    xp: 10
    cuerpo: >-
      Completa `projects/m17-vitrina/stack.md` (ya hay plantilla). Ejemplo
      mínimo: Cambio de stack = ADR en `docs/`.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
