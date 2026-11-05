---
id: L17
materia: M10
orden: 17
titulo: 'Superficie de ataque: endpoints y datos'
horas: 5
semana: 5
lectura: Hilo seguridad + ficha M10 proyecto
evidencia: superficie/endpoints.md (P3 inicio)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar el mapa de superficie del piloto Vitrina (aunque
      sea diseño).


      P3 empieza aquí: inventarias antes de endurecer (M18).
  - id: s2
    tipo: ejemplo
    titulo: 1. Plantilla
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m10-redes/superficie
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Superficie de ataque: endpoints y datos" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: superficie/endpoints.md (P3 inicio)
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

      `mkdir -p projects/m10-redes/superficie`
    comandoEsperado:
      - mkdir -p projects/m10-redes/superficie
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m10-redes/superficie'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar el mapa de superficie del piloto Vitrina (aunque sea
          diseño).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario
    xp: 10
    cuerpo: >-
      Incluye al menos: login/logout, CRUD clientes, CRUD pedidos, listados,
      health `/health`, estáticos del panel. Marca PII (teléfono, notas
      privadas).
  - id: s7
    tipo: explicacion
    titulo: 3. Trust boundaries
    xp: 10
    cuerpo: >-
      Mermaid o ASCII: User Agent → TLS → API → PG; backups; logs. Qué cruza
      cada frontera.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `superficie/endpoints.md` lista endpoints previstos
        (pedidos/clientes/auth) + auth + PII.
      - 'Diagrama trust boundary: browser / API / DB / backups.'
      - 'Commit `docs(m10): l17 superficie endpoints`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — Superficie de ataque: endpoints y datos

**~5.0 h · Semana 5**

P3 empieza aquí: inventarias antes de endurecer (M18).

## Objetivo

Completar el mapa de superficie del piloto Vitrina (aunque sea diseño).

## Pasos

### 1. Plantilla (30 min)

```bash
mkdir -p projects/m10-redes/superficie
```

Crea `endpoints.md` con columnas: método, path, auth, roles, datos, notas.

### 2. Inventario (90 min)

Incluye al menos: login/logout, CRUD clientes, CRUD pedidos, listados, health `/health`, estáticos del panel. Marca PII (teléfono, notas privadas).

### 3. Trust boundaries (40 min)

Mermaid o ASCII: User Agent → TLS → API → PG; backups; logs. Qué cruza cada frontera.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/superficie
git commit -m "docs(m10): l17 superficie endpoints"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Inventario de endpoints, auth, datos sensibles y trust boundaries | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `superficie/endpoints.md` lista endpoints previstos (pedidos/clientes/auth) + auth + PII.
2. Diagrama trust boundary: browser / API / DB / backups.
3. Commit `docs(m10): l17 superficie endpoints`.

## Errores comunes

- Inventario vacío “porque aún no hay código”.
- Olvidar admin, healthchecks, webhooks.
- Marcar todo como “público”.

## Siguiente

[L18 — Cliente y servidor TCP mínimo (P2)](L18-cliente-y-servidor-tcp-minimo-p2.md)
