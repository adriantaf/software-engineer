---
id: L18
materia: M13
orden: 18
titulo: Endpoints y módulos previstos M17
horas: 5
semana: 5
lectura: Lista de rutas API y módulos de código previstos
evidencia: projects/m13-diseno/endpoints-m17.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `endpoints-m17.md` breve y accionable.

      Puente explícito al scaffold: qué rutas y carpetas nacerán en M17.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tabla de endpoints
    xp: 10
    cuerpo: |-
      ```text
      auth/  clientes/  servicios/  pedidos/
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Endpoints y módulos previstos M17" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m13-diseno/endpoints-m17.md
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
    pregunta: ¿Es buena práctica en esta lección? “OpenAPI de 80 rutas para el MVP."
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
        texto: '`endpoints-m17.md` breve y accionable.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Módulos
    xp: 10
    cuerpo: |-
      ```text
      auth/  clientes/  servicios/  pedidos/
      ```

      Relación con capas de L09.
  - id: s7
    tipo: ejemplo
    titulo: 4. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno
      git commit -m "docs(m13): endpoints y modulos previstos M17"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`endpoints-m17.md` lista métodos/rutas Must con DTO/status resumidos.'
      - 'Mapa módulo → carpeta (`auth`, `orders`, `clientes`).'
      - 'Commit `docs(m13): endpoints y modulos previstos M17`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L18 — Endpoints y módulos previstos M17

**~5.0 h · Semana 5**

Puente explícito al scaffold: qué rutas y carpetas nacerán en M17.

## Objetivo

`endpoints-m17.md` breve y accionable.

## Pasos (hazlos en orden)

### 1. Tabla de endpoints (70–90 min)

| Método | Ruta | Auth | Éxito | Errores |
|--------|------|------|-------|---------|
| POST | /auth/login | no | 200 | 401 |
| POST | /pedidos | sí | 201 | 400/401/403/409 |
| GET | /pedidos | sí | 200 | 401 |
| … | … | … | … | … |

### 2. Módulos (40 min)

```text
auth/  clientes/  servicios/  pedidos/
```

Relación con capas de L09.

### 3. Enlaza desde README (20 min)

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): endpoints y modulos previstos M17"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Contrato tentativo de API y módulos para el scaffold M17 | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `endpoints-m17.md` lista métodos/rutas Must con DTO/status resumidos.
2. Mapa módulo → carpeta (`auth`, `orders`, `clientes`).
3. Commit `docs(m13): endpoints y modulos previstos M17`.

## Errores comunes

- OpenAPI de 80 rutas para el MVP.
- Endpoints sin auth marcada.
- Módulos que no coinciden con arquitectura.md.

## Siguiente

[L19 — Checklist listo para scaffold](L19-checklist-listo-para-scaffold.md)
