---
id: L32
materia: M18
orden: 32
titulo: Cierre M18 — dominio y riesgo residual
horas: 5
semana: 8
lectura: "Repaso completo M18"
evidencia: "projects/m18-appsec/informe-appsec.md final + README"
---

# L32 — Cierre M18 — dominio y riesgo residual

**~5 h · Semana 8**

## Objetivo

Finalizar informe, verificar P1–P3, criterios de dominio y handoff a M19 (deploy seguro).

## Por qué importa

Cierras la capa B de seguridad antes de exponer el piloto en internet.

## Conceptos

- Checklist pre-deploy.
- Handoff M19.
- Dominio M18 checklist.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Actualiza `projects/m18-appsec/README.md` con índice de artefactos. Checklist ficha **Criterios de dominio** en `cierre-m18.md` con evidencia por ítem.

Escribe 5 bullets **qué NO cubriste** (ej. pentest externo, WAF) como residual risk.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l32 cierre-m18-dominio-y-riesgo-residual"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M18-seguridad.md | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Informe final.
2. P1–P3 verificables.
3. README índice.
4. Residual risk escrito.

## Errores comunes

- Marcar dominio sin tests.
- Deploy público sin headers.
