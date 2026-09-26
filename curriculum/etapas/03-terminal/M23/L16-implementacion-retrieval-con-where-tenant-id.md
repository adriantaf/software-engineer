---
id: L16
materia: M23
orden: 16
titulo: Implementación retrieval con WHERE tenant_id
horas: 5
semana: 4
lectura: "Pseudocódigo SQL/ORM del plan"
evidencia: "projects/m23-ia/rag/implementacion.md"
---

# L16 — Implementación retrieval con WHERE tenant_id

**~5 h · Semana 4**

## Objetivo

Describir o implementar retrieval donde tenant_id viene de sesión autenticada, no del cliente.

## Por qué importa

Confiar en parámetro `tenantId` del JSON es IDOR waiting to happen.

## Conceptos

- Sesión server-side.
- WHERE obligatorio.
- Tests unit retrieval.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/rag/implementacion.md`: código en repo producto **o** pseudocódigo con enlaces commit.

Incluye snippet SQL estilo ficha (ORDER BY dist LIMIT 5 **con tenant**).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l16 implementacion-retrieval-con-where-tenan"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M18 | IDOR | ../../hilos/seguridad.md |
| Catálogo | Entrada M23 | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

1. implementacion.md.
2. tenant de sesión.
3. Snippet SQL correcto.

## Errores comunes

- tenant_id query param.
- Búsqueda global k-NN.

## Siguiente

[L17 — Endpoint faq-preview protegido](L17-endpoint-faq-preview-protegido.md)
