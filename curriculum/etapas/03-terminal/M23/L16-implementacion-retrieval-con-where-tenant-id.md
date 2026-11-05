---
id: L16
materia: M23
orden: 16
titulo: Implementación retrieval con WHERE tenant_id
horas: 5
semana: 4
lectura: Pseudocódigo SQL/ORM del plan
evidencia: projects/m23-ia/rag/implementacion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Describir o implementar retrieval donde tenant_id viene de
      sesión autenticada, no del cliente.


      Confiar en parámetro `tenantId` del JSON es IDOR waiting to happen.


      Conceptos que debes poder explicar al cerrar:


      - Sesión server-side.

      - WHERE obligatorio.

      - Tests unit retrieval.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l16 implementaci-n-retrieval-con-where-tenan"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Implementación retrieval con WHERE tenant_id" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m23-ia/rag/implementacion.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Describir o implementar retrieval donde tenant_id viene de sesión
          autenticada, no del cliente.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m23-ia/rag`.


      `projects/m23-ia/rag/implementacion.md`: código en repo producto **o**
      pseudocódigo con enlaces commit.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: Incluye snippet SQL estilo ficha (ORDER BY dist LIMIT 5 **con tenant**).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/rag/implementacion.md`.'
      - implementacion.md.
      - tenant de sesión.
      - Snippet SQL correcto.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Implementación retrieval con WHERE tenant_id

**~5 h · Semana 4**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/rag/implementacion.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Describir o implementar retrieval donde tenant_id viene de sesión autenticada, no del cliente.

## Por qué empieza así

Confiar en parámetro `tenantId` del JSON es IDOR waiting to happen.

Conceptos que debes poder explicar al cerrar:

- Sesión server-side.
- WHERE obligatorio.
- Tests unit retrieval.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Pseudocódigo SQL/ORM del plan_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/rag`.

`projects/m23-ia/rag/implementacion.md`: código en repo producto **o** pseudocódigo con enlaces commit.

### 3. Laboratorio principal (90–120 min)

Incluye snippet SQL estilo ficha (ORDER BY dist LIMIT 5 **con tenant**).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l16 implementaci-n-retrieval-con-where-tenan"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Pseudocódigo SQL/ORM del plan | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/rag/implementacion.md`.
2. implementacion.md.
3. tenant de sesión.
4. Snippet SQL correcto.
5. Commit `docs(m23): l16 …` en el historial.

## Errores comunes

- tenant_id query param.
- Búsqueda global k-NN.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L17 — Endpoint faq-preview protegido](L17-endpoint-faq-preview-protegido.md)
