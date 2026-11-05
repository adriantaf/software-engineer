---
id: L15
materia: M23
orden: 15
titulo: Ingesta corpus tenant B y contraste
horas: 5
semana: 4
lectura: Aislamiento datos desde diseño
evidencia: projects/m23-ia/rag/corpus/tenant-b/
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Demo obligatoria A no ve B empieza con datos separados.


      Conceptos que debes poder explicar al cerrar:


      - Separación física.

      - IDs distintos.

      - Políticas opuestas (test).


      **Objetivo de esta lección:** Segundo corpus claramente distinto (tenant
      B) para pruebas cross-tenant.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l15 ingesta-corpus-tenant-b-y-contraste"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l15 ingesta-corpus-tenant-b-y-contraste"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Ingesta corpus tenant B y contraste», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Ingesta corpus tenant B
          y contraste
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
          Segundo corpus claramente distinto (tenant B) para pruebas
          cross-tenant.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: Tabla comparación A vs B en `projects/m23-ia/rag/corpus/README.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/rag/corpus/tenant-b/`.'
      - Corpus B ≥3 docs.
      - Política distinta.
      - README comparativo.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Ingesta corpus tenant B y contraste

**~5 h · Semana 4**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/rag/corpus/tenant-b/`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Segundo corpus claramente distinto (tenant B) para pruebas cross-tenant.

## Por qué empieza así

Demo obligatoria A no ve B empieza con datos separados.

Conceptos que debes poder explicar al cerrar:

- Separación física.
- IDs distintos.
- Políticas opuestas (test).

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Aislamiento datos desde diseño_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/rag/corpus`.

Corpus `projects/m23-ia/rag/corpus/tenant-b/` con política cancelación **distinta** a A (facilita detectar fuga).

### 3. Laboratorio principal (90–120 min)

Tabla comparación A vs B en `projects/m23-ia/rag/corpus/README.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l15 ingesta-corpus-tenant-b-y-contraste"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Aislamiento datos desde diseño | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/rag/corpus/tenant-b/`.
2. Corpus B ≥3 docs.
3. Política distinta.
4. README comparativo.
5. Commit `docs(m23): l15 …` en el historial.

## Errores comunes

- Mismo texto A/B.
- tenant_id solo en comentario.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L16 — Implementación retrieval con WHERE tenant_id](L16-implementacion-retrieval-con-where-tenant-id.md)
