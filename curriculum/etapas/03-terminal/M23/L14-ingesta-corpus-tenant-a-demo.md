---
id: L14
materia: M23
orden: 14
titulo: Ingesta corpus tenant A (demo)
horas: 5
semana: 4
lectura: "Docs markdown políticas negocio"
evidencia: "projects/m23-ia/rag/corpus/tenant-a/"
---

# L14 — Ingesta corpus tenant A (demo)

**~5 h · Semana 4**

## Objetivo

Ingestar ≥3 documentos markdown de políticas ficticias del tenant A demo.

## Por qué importa

Necesitas corpus separado antes de probar cross-tenant.

## Conceptos

- Corpus.
- Markdown.
- Metadatos.
- Sin PII real.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m23-ia/rag/corpus/tenant-a/*.md` (horarios, cancelación, servicios). Script ingesta documentado o manual con hashes.

Registra versión corpus en `projects/m23-ia/rag/corpus/README.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l14 ingesta-corpus-tenant-a-demo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M12 | SRS políticas | ../../../producto-saas.md |

## Hecho cuando

1. ≥3 docs tenant A.
2. README corpus.
3. Sin PII real.

## Errores comunes

- PDF escaneado sin OCR plan.
- Mezclar A y B en carpeta.

## Siguiente

[L15 — Ingesta corpus tenant B y contraste](L15-ingesta-corpus-tenant-b-y-contraste.md)
