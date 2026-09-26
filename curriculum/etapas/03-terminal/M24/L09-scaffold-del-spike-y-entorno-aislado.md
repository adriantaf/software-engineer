---
id: L09
materia: M24
orden: 9
titulo: Scaffold del spike y entorno aislado
horas: 5
semana: 3
lectura: "Quickstart oficial de la tecnología elegida"
evidencia: "projects/m24-emergentes/spike/README.md"
---

# L09 — Scaffold del spike y entorno aislado

**~5 h · Semana 3**

## Objetivo

Bootstrap del PoC en rama/carpeta aislada sin tocar prod de Agenda Ops.

## Por qué importa

M24 prohíbe merge experimental a prod sin go explícito.

## Conceptos

- Rama spike/*
- Secrets locales
- Staging vs prod

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m24-emergentes/spike/README.md`: prerequisitos, variables de entorno (nombres), comando para arrancar.

Código mínimo o script en `spike/`; `.env.example` sin valores reales.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l09 scaffold-del-spike-y-entorno-aislado"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vendor | Quickstart | Sandbox/test mode |
| Catálogo | Entrada M24 | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

1. README con comando reproducible.
2. .env.example sin secretos.

## Errores comunes

- Commit de tokens.
- PoC directo en rama main del SaaS.

## Siguiente

[L10 — Flujo mínimo demostrable](L10-flujo-minimo-demostrable.md)
