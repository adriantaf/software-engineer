---
id: L20
materia: M25
orden: 20
titulo: Segundo hallazgo aislamiento cerrado
horas: 5
semana: 5
lectura: "OWASP Privacy / LFPDPPP notas (contexto)"
evidencia: "projects/m25-ciber/hallazgos/README.md"
---

# L20 — Segundo hallazgo aislamiento cerrado

**~5 h · Semana 5**

## Objetivo

Otro fix cross-tenant con test; tabla hallazgos actualizada.

## Por qué importa

Multi-tenant amplifica impacto de una fuga; privacidad es feature de confianza.

## Conceptos

- Retención
- Derecho de cancelación
- Datos por negocio

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

No copies plantillas legales sin revisión; borrador técnico-operativo basta para el plan.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m25): l20 segundo-hallazgo-aislamiento-cerrado"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | producto-saas privacidad | M23 política LLM |

## Hecho cuando

1. Documento en ruta indicada.
2. ≥2 hallazgos aislamiento cerrados acumulado.

## Errores comunes

- Política genérica sin tu producto.
- Un solo hallazgo en todo M25.

## Siguiente

[L21 — Tabletop — fuga de .env](L21-tabletop-fuga-de-env.md)
