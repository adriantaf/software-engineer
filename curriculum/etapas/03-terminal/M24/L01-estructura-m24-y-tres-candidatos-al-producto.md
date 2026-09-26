---
id: L01
materia: M24
orden: 1
titulo: Estructura M24 y tres candidatos al producto
horas: 5
semana: 1
lectura: "Ficha M24 + producto-saas (recordatorios / realtime)"
evidencia: "projects/m24-emergentes/candidatos.md + bitácora semana-01.md"
---

# L01 — Estructura M24 y tres candidatos al producto

**~5 h · Semana 1**

## Objetivo

Crear carpetas de evidencia y registrar tres tecnologías candidatas alineadas a Agenda Ops (ej. WhatsApp Cloud API, SSE/WebSockets, cola managed).

## Por qué importa

M24 separa hype de utilidad; sin candidatos escritos terminas en tutorial random sin decisión.

## Conceptos

- Spike vs producción
- Fuentes primarias obligatorias
- Hipótesis de producto

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m24-emergentes/research projects/m24-emergentes/spike
```

En `projects/m24-emergentes/candidatos.md` lista **tres** candidatos con una línea de valor para el ICP (barberías, clínicas dentales, etc.).

Abre `projects/m24-emergentes/bitacora/semana-01.md` (crea la carpeta) con objetivo de la semana: research completo antes del spike.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l01 estructura-m24-y-tres-candidatos-al-produc"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | [producto-saas.md](../../producto-saas.md) | M21 backlog |
| Ficha | M24-tecnologias-emergentes.md | — |
| Catálogo | Entrada M24 | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

1. Tres candidatos nombrados con valor ICP.
2. Carpetas research/ y spike/ existen.
3. Bitácora semana 1 iniciada.

## Errores comunes

- Elegir blockchain sin caso de uso en citas.
- Copiar stack de un tutorial sin leer límites.

## Siguiente

[L02 — Research candidato 1 — fuentes primarias](L02-research-candidato-1-fuentes-primarias.md)
