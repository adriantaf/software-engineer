---
id: L01
materia: M18
orden: 1
titulo: 'Activos, actores y datos sensibles en Vitrina'
horas: 5
semana: 1
lectura: OWASP Threat Modeling (overview) + notas STRIDE
evidencia: projects/m18-appsec/threat-model-v0.md sección Activos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar tablas Actores y ≥5 Activos en
      `projects/m18-appsec/threat-model-v0.md` (PII, credenciales, pedidos,
      tokens, Postgres).


      Sin lista de activos, el threat model es decoración. Hoy arrancas P1 y el
      hilo OWASP.
  - id: s2
    tipo: ejemplo
    titulo: 1. Carpeta de evidencia
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}
      ls projects/m18-appsec
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Activos, actores y datos sensibles en Vitrina" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/threat-model-v0.md sección Activos
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

      `mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}`
    comandoEsperado:
      - 'mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar tablas Actores y ≥5 Activos en
          `projects/m18-appsec/threat-model-v0.md` (PII, credenciales, pedidos,
          tokens, Postgres).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Actores y activos
    xp: 10
    cuerpo: >-
      Abre `projects/m18-appsec/threat-model-v0.md`. Completa **Actores**
      (dueño, staff, cliente final, atacante anónimo) y **Activos** (≥5) con
      confidencialidad. Diagrama: navegador → API → Postgres.


      ```markdown
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m18-appsec/threat-model-v0.md` con actores y ≥5
        activos.
      - >-
        Diagrama ASCII o Mermaid del piloto (artefacto:
        `projects/m18-appsec/threat-model-v0.md sección Activos`).
      - 'Commit `docs(m18): L01 activos-actores-y-datos-sensibles-en-vitrina`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Activos, actores y datos sensibles en Vitrina

**~5.0 h · Semana 1**

Sin lista de activos, el threat model es decoración. Hoy arrancas P1 y el hilo OWASP.

## Objetivo

Completar tablas Actores y ≥5 Activos en `projects/m18-appsec/threat-model-v0.md` (PII, credenciales, pedidos, tokens, Postgres).

## Pasos

### 1. Carpeta de evidencia (15 min)

Crea la estructura si aún no existe:

```bash
mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}
ls projects/m18-appsec
```
### 2. Actores y activos (80–100 min)

Abre `projects/m18-appsec/threat-model-v0.md`. Completa **Actores** (dueño, staff, cliente final, atacante anónimo) y **Activos** (≥5) con confidencialidad. Diagrama: navegador → API → Postgres.

```markdown
## Actores
| Actor | Objetivos | Capacidades |
|-------|-----------|-------------|
| Dueño (owner) | Gestionar negocio | CRUD total |
| Staff | Operar pedidos | CRUD limitado |
| Cliente final | Pedir pedido | Solo sus datos |
| Atacante anónimo | Robar PII / sesión | Sin credenciales |

## Activos (≥5)
| Activo | Confidencialidad | Dónde vive |
|--------|------------------|------------|
| Teléfono cliente | Alta | `clientes.telefono` |
| Hash password | Crítica | `users.password_hash` |
| Notas de pedido | Alta | `pedidos.notas` |
| Cookie de sesión | Crítica | `Set-Cookie` |
| Postgres | Crítica | volumen / hosting |
```
### 3. Superficie JSON + anti-secretos (30–40 min)

Marca qué campos salen en `GET /api/pedidos`. Ejecuta el barrido y anota rutas (sin pegar secretos):

```bash
git ls-files | rg -i 'env|secret|credential|\.pem' || true
```
### 4. Commit (10–15 min)

```bash
git add projects/m18-appsec/threat-model-v0.md
git status   # sin .env
git commit -m "docs(m18): l01 activos actores agenda ops"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Threat Modeling (overview) + notas STRIDE | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m18-appsec/threat-model-v0.md` con actores y ≥5 activos.
2. Diagrama ASCII o Mermaid del piloto (artefacto: `projects/m18-appsec/threat-model-v0.md sección Activos`).
3. Commit `docs(m18): L01 activos-actores-y-datos-sensibles-en-vitrina`.

## Errores comunes

- Activos genéricos (“la DB”) sin tablas/campos.
- Omitir al cliente final como fuente de datos.

## Siguiente

[L02 — Trust boundaries y flujos de confianza](L02-trust-boundaries-y-flujos-de-confianza.md)
