---
id: L01
materia: M23
orden: 1
titulo: Tres métricas SaaS por tenant — definiciones
horas: 5
semana: 1
lectura: "producto-saas + notas métricas M23"
evidencia: "projects/m23-ia/metricas/definiciones.md"
---

# L01 — Tres métricas SaaS por tenant — definiciones

**~5 h · Semana 1**

## Objetivo

Definir activación 7d, citas creadas/semana y trials activos con fórmula y fuente de datos.

## Por qué importa

M23 y M22 comparten métricas accionables; sin definición clara los CSV mienten.

## Conceptos

- Activación.
- tenant_id.
- Vanity vs accionable.
- Ventana temporal.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
```

En `projects/m23-ia/metricas/definiciones.md` documenta ≥3 métricas con fórmula, numerador/denominador, frecuencia, anti-PII.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l01 tres-metricas-saas-por-tenant-definicion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../../producto-saas.md | ../M22-emprendimiento.md metricas |

## Hecho cuando

1. definiciones.md ≥3 métricas.
2. Fórmulas explícitas.
3. Anti-PII.

## Errores comunes

- Métrica sin fórmula.
- Mezclar tenants en definición.

## Siguiente

[L02 — Consulta agregada por tenant_id sin PII](L02-consulta-agregada-por-tenant-id-sin-pii.md)
