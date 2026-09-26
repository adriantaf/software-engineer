---
id: L13
materia: M22
orden: 13
titulo: Métricas accionables — tablero de trials
horas: 5
semana: 4
lectura: "Lean — medir lo que importa"
evidencia: "projects/m22-bektor/metricas-trials.md datos"
---

# L13 — Métricas accionables — tablero de trials

**~5 h · Semana 4**

## Objetivo

Llenar tablero con trials iniciados, activación 7d y notas; rechazar vanity metrics.

## Por qué importa

MRR ficticio sin pagos está prohibido en la ficha; mide activación y conversación.

## Conceptos

- Trial iniciado.
- Activación 7d.
- Vanity vs accionable.
- Seguimiento.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Actualiza `projects/m22-bektor/metricas-trials.md` con filas reales (≥6 negocios contactados).

Define fórmula activación en el archivo. Gráfico ASCII o tabla semanal suficiente.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l13 metricas-accionables-tablero-de-trials"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M23 | métricas por tenant | ../../../producto-saas.md |
| Catálogo | Entrada M22 | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

1. Tablero con datos.
2. Fórmula activación.
3. Sin MRR inventado.

## Errores comunes

- Contar WhatsApp enviado como trial.
- Métricas sin definición.

## Siguiente

[L14 — Demos 7–8 — seguimiento y lotes pequeños](L14-demos-7-8-seguimiento-y-lotes-pequenos.md)
