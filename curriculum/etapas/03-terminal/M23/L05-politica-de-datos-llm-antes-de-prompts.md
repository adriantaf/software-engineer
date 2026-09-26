---
id: L05
materia: M23
orden: 5
titulo: Política de datos LLM antes de prompts
horas: 5
semana: 2
lectura: "Ética/datos + vendor LLM terms"
evidencia: "projects/m23-ia/politica-datos-llm.md"
---

# L05 — Política de datos LLM antes de prompts

**~5 h · Semana 2**

## Objetivo

Redactar política: qué nunca enviar a LLM, retención logs, filtro tenant, incidentes.

## Por qué importa

Regla M23: política **antes** de pegar datos en ChatGPT ‘solo probar’.

## Conceptos

- PII.
- Retención.
- Tenant scope.
- Incident response.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Completa `projects/m23-ia/politica-datos-llm.md` (≥1 página): prohibidos, permitidos anonimizados, logs, borrado, responsable.

Enlaza [hilo seguridad](../../hilos/seguridad.md). Commit antes de cualquier script que llame API.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l05 politica-de-datos-llm-antes-de-prompts"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../hilos/seguridad.md | Términos API LLM elegida |

## Hecho cuando

1. Política completa.
2. Commit previo a scripts.
3. Enlace seguridad.

## Errores comunes

- Política post-hoc.
- Permitir dumps BD.

## Siguiente

[L06 — Set gold de 10 preguntas FAQ del ICP](L06-set-gold-de-10-preguntas-faq-del-icp.md)
