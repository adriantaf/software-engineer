---
id: L03
materia: M24
orden: 3
titulo: Research candidatos 2 y 3
horas: 5
semana: 1
lectura: "Docs oficiales candidatos 2 y 3"
evidencia: "projects/m24-emergentes/research/candidato-2.md y candidato-3.md"
---

# L03 — Research candidatos 2 y 3

**~5 h · Semana 1**

## Objetivo

Mismo estándar que candidato 1 para los otros dos candidatos.

## Por qué importa

Comparar tres opciones evita enamorarte del primer tutorial que viste.

## Conceptos

- Madurez del ecosistema
- Datos fuera del perímetro
- Operación (on-call)

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Completa `candidato-2.md` y `candidato-3.md` con el mismo template que L02.

Tabla comparativa rápida en `projects/m24-emergentes/research/comparacion-v0.md` (valor, complejidad, riesgo).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l03 research-candidatos-2-y-3"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Docs 2 y 3 | Issues conocidos GitHub |
| Catálogo | Entrada M24 | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

1. Dos archivos research completos.
2. comparacion-v0.md con 3 filas.

## Errores comunes

- Tres candidatos idénticos (solo cambia nombre).
- Ignorar si datos de clientes salen a terceros.

## Siguiente

[L04 — Cierre research semana 1 y backlog M21](L04-cierre-research-semana-1-y-backlog-m21.md)
