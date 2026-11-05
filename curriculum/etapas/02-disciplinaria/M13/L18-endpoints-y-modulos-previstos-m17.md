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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Puente explícito al scaffold: qué rutas y carpetas nacerán en M17.


      **Objetivo de esta lección:** `endpoints-m17.md` breve y accionable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tabla de endpoints
    xp: 10
    cuerpo: |-
      ```text
      auth/  clientes/  servicios/  pedidos/
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Módulos
    xp: 10
    cuerpo: |-
      ```text
      auth/  clientes/  servicios/  pedidos/
      ```

      Relación con capas de L09.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Endpoints y módulos previstos M17», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Endpoints y módulos
          previstos M17
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “OpenAPI de 80 rutas para el MVP."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: '`endpoints-m17.md` breve y accionable.'
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
