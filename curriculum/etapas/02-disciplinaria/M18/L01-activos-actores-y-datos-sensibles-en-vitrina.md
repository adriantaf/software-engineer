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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin lista de activos, el threat model es decoración. Hoy arrancas P1 y el
      hilo OWASP.


      **Objetivo de esta lección:** Completar tablas Actores y ≥5 Activos en
      `projects/m18-appsec/threat-model-v0.md` (PII, credenciales, pedidos,
      tokens, Postgres).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Carpeta de evidencia
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}
      ls projects/m18-appsec
      ```

      Crea la estructura si aún no existe:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Actores y activos
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}
      ls projects/m18-appsec
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Activos, actores y datos sensibles en Vitrina», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Activos, actores y
          datos sensibles en V…
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

      `mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}`
    comandoEsperado:
      - 'mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}'
      - ls projects/m18-appsec
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}'
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
          Completar tablas Actores y ≥5 Activos en
          `projects/m18-appsec/threat-model-v0.md` (PII, credenciales, pedidos,
          tokens, Postgres).
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

      `ls projects/m18-appsec`
    comandoEsperado:
      - ls projects/m18-appsec
    explicacionError: 'Esperado: ls projects/m18-appsec'
  - id: s8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
