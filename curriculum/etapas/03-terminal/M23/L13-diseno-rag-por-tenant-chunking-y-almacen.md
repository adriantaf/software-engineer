---
id: L13
materia: M23
orden: 13
titulo: Diseño RAG por tenant — chunking y almacén
horas: 5
semana: 4
lectura: "Vendor RAG docs + pgvector/sqlite-vss"
evidencia: "projects/m23-ia/rag/diseno.md"
---

# L13 — Diseño RAG por tenant — chunking y almacén

**~5 h · Semana 4**

## Objetivo

Documentar arquitectura RAG: ingesta, chunking, embeddings, store, filtro tenant_id **antes** de retrieval.

## Por qué importa

RAG global con filtro ‘después’ en prompt es vulnerabilidad explícita del plan.

## Conceptos

- Chunking.
- Embeddings.
- tenant_id en WHERE.
- Amenaza injection.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/rag/diseno.md`: diagrama, elección store, tamaño chunk, metadata obligatoria tenant_id.

Sección amenazas: prompt injection en PDF del dueño, metadatos mal filtrados.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l13 diseno-rag-por-tenant-chunking-y-almacen"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | RAG guide | ../../hilos/seguridad.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. diseno.md completo.
2. Filtro tenant antes retrieval.
3. Amenazas listadas.

## Errores comunes

- Filtro solo en prompt.
- Store sin tenant_id.

## Siguiente

[L14 — Ingesta corpus tenant A (demo)](L14-ingesta-corpus-tenant-a-demo.md)
