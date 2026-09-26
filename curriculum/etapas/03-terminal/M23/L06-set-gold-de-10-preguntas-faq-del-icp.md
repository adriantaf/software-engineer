---
id: L06
materia: M23
orden: 6
titulo: Set gold de 10 preguntas FAQ del ICP
horas: 5
semana: 2
lectura: "FAQ realistas barbería/clínica/taller"
evidencia: "projects/m23-ia/llm-eval/preguntas-gold.json"
---

# L06 — Set gold de 10 preguntas FAQ del ICP

**~5 h · Semana 2**

## Objetivo

Listar 10 preguntas con respuesta esperada corta basada en docs ficticios de un tenant demo.

## Por qué importa

Evaluación sin gold set es opinión; M22 ICP informa el tono.

## Conceptos

- Gold set.
- JSON.
- Respuesta esperada.
- Tenant demo.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m23-ia/llm-eval/preguntas-gold.json` array de {id, pregunta, respuesta_esperada, tenant_id_demo}.

Preguntas tipo política cancelación, horario, servicios, no-show.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l06 set-gold-de-10-preguntas-faq-del-icp"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M22 | projects/m22-bektor | ../../../producto-saas.md |

## Hecho cuando

1. 10 preguntas.
2. JSON válido.
3. Respuesta esperada cada una.

## Errores comunes

- Preguntas genéricas Wikipedia.
- Sin tenant_id_demo.

## Siguiente

[L07 — Proveedor LLM — auth, modelo y costos](L07-proveedor-llm-auth-modelo-y-costos.md)
