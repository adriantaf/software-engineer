---
id: L09
materia: M13
orden: 9
titulo: Arquitectura en capas
horas: 5
semana: 3
lectura: Capas HTTP → application → domain → infrastructure
evidencia: projects/m13-diseno/arquitectura.md (capas + responsabilidades)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `projects/m13-diseno/arquitectura.md` con capas que M14/M17
      puedan respetar.


      El monolito modular de ADR 001 necesita fronteras internas. Hoy las
      escribes.
  - id: s2
    tipo: ejemplo
    titulo: 1. Define capas
    xp: 10
    cuerpo: |-
      ```text
      HTTP (controllers/routes)
        → Application (services / use cases)
          → Domain (reglas: solape, estados)
            → Infrastructure (Postgres, mail, reloj)
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Arquitectura en capas" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m13-diseno/arquitectura.md (capas + responsabilidades)
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? ““Arquitectura” = lista de librerías
      sin fronteras."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          `projects/m13-diseno/arquitectura.md` con capas que M14/M17 puedan
          respetar.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Mapa de carpetas previstas
    xp: 10
    cuerpo: |-
      ```text
      src/
        http/
        application/
        domain/
        infrastructure/
      ```

      Enlaza a módulos: `orders`, `clientes`, `auth`.
  - id: s7
    tipo: explicacion
    titulo: 3. Dibuja dependencias
    xp: 10
    cuerpo: Mermaid `flowchart TB` de capas; flechas solo hacia abajo (o inward).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `arquitectura.md` describe ≥4 capas con responsabilidad y ejemplo de
        archivo futuro.
      - >-
        Queda explícito que autorización/reglas de pedido no viven solo en
        React.
      - 'Commit `docs(m13): arquitectura en capas Vitrina`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Arquitectura en capas

**~5.0 h · Semana 3**

El monolito modular de ADR 001 necesita fronteras internas. Hoy las escribes.

## Objetivo

`projects/m13-diseno/arquitectura.md` con capas que M14/M17 puedan respetar.

## Pasos (hazlos en orden)

### 1. Define capas (60–70 min)

```text
HTTP (controllers/routes)
  → Application (services / use cases)
    → Domain (reglas: solape, estados)
      → Infrastructure (Postgres, mail, reloj)
```

Tabla:

| Capa | Puede | No puede |
|------|-------|----------|
| HTTP | parsear DTO, status codes | reglas de solape |
| Application | orquestar | SQL crudo (mejor vía repo) |
| Domain | invariantes | conocer Express |
| Infra | SQL, SMTP | decidir autorización de negocio a solas |

### 2. Mapa de carpetas previstas (40–50 min)

```text
src/
  http/
  application/
  domain/
  infrastructure/
```

Enlaza a módulos: `orders`, `clientes`, `auth`.

### 3. Dibuja dependencias (40 min)

Mermaid `flowchart TB` de capas; flechas solo hacia abajo (o inward).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/arquitectura.md
git commit -m "docs(m13): arquitectura en capas Vitrina"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Arquitectura en capas; dónde viven reglas vs I/O | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `arquitectura.md` describe ≥4 capas con responsabilidad y ejemplo de archivo futuro.
2. Queda explícito que autorización/reglas de pedido no viven solo en React.
3. Commit `docs(m13): arquitectura en capas Vitrina`.

## Errores comunes

- “Arquitectura” = lista de librerías sin fronteras.
- Domain que importa SQL o Express.
- Capas de adorno (8 capas para un CRUD).

## Siguiente

[L10 — DTOs, validación y frontera HTTP](L10-dtos-validacion-y-frontera-http.md)
