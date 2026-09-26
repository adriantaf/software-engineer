---
id: L15
materia: M23
orden: 15
titulo: Ingesta corpus tenant B y contraste
horas: 5
semana: 4
lectura: "Aislamiento datos desde diseño"
evidencia: "projects/m23-ia/rag/corpus/tenant-b/"
---

# L15 — Ingesta corpus tenant B y contraste

**~5 h · Semana 4**

## Objetivo

Segundo corpus claramente distinto (tenant B) para pruebas cross-tenant.

## Por qué importa

Demo obligatoria A no ve B empieza con datos separados.

## Conceptos

- Separación física.
- IDs distintos.
- Políticas opuestas (test).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Corpus `projects/m23-ia/rag/corpus/tenant-b/` con política cancelación **distinta** a A (facilita detectar fuga).

Tabla comparación A vs B en `projects/m23-ia/rag/corpus/README.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l15 ingesta-corpus-tenant-b-y-contraste"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M23-ia-datos.md regla demo | ../../hilos/seguridad.md |

## Hecho cuando

1. Corpus B ≥3 docs.
2. Política distinta.
3. README comparativo.

## Errores comunes

- Mismo texto A/B.
- tenant_id solo en comentario.

## Siguiente

[L16 — Implementación retrieval con WHERE tenant_id](L16-implementacion-retrieval-con-where-tenant-id.md)
