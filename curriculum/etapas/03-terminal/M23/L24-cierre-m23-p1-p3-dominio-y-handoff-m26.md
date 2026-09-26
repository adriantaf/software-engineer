---
id: L24
materia: M23
orden: 24
titulo: Cierre M23 — P1–P3, dominio y handoff M26
horas: 5
semana: 6
lectura: "Repaso ficha M23"
evidencia: "projects/m23-ia/cierre-m23.md"
---

# L24 — Cierre M23 — P1–P3, dominio y handoff M26

**~5 h · Semana 6**

## Objetivo

Auditar pipeline, eval LLM, RAG aislado, FAQ; commit cierre; README L01–L24.

## Por qué importa

Cierras hilo IA/datos antes de emergentes (M24) y capstone (M26).

## Conceptos

- Checklist.
- Cross-tenant demo.
- Dominio.
- Handoff.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m23-ia/cierre-m23.md` responde criterios dominio. Verifica política LLM respetada en scripts.

Commit `docs(m23): cierre materia`. Actualiza `projects/m23-ia/README.md` índice lecciones.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l24 cierre-m23-p1-p3-dominio-y-handoff-m26"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M23-ia-datos.md | ../M26-proyecto-integrador.md |

## Hecho cuando

1. cierre-m23.md.
2. Commit cierre.
3. README índice.
4. P1–P3 verificados.

## Errores comunes

- Marcar UI sin test cross-tenant.
- PII en logs eval.
