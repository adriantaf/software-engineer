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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 empieza aquí: inventarias antes de endurecer (M18).


      **Objetivo de esta lección:** Completar el mapa de superficie del piloto
      Vitrina (aunque sea diseño).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Plantilla
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m10-redes/superficie
      ```

      Crea `endpoints.md` con columnas: método, path, auth, roles, datos, notas.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m10-redes/superficie
      git commit -m "docs(m10): l17 superficie endpoints"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Superficie de ataque: endpoints y datos», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Superficie de ataque:
          endpoints y datos
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

      `mkdir -p projects/m10-redes/superficie`
    comandoEsperado:
      - mkdir -p projects/m10-redes/superficie
      - git add projects/m10-redes/superficie
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m10-redes/superficie'
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
          Completar el mapa de superficie del piloto Vitrina (aunque sea
          diseño).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Trust boundaries
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
