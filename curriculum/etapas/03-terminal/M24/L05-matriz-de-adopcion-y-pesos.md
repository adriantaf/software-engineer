---
id: L05
materia: M24
orden: 5
titulo: Matriz de adopción y pesos
horas: 5
semana: 2
lectura: "Criterios M24 + threat modeling ligero"
evidencia: "projects/m24-emergentes/matriz-adopcion.md"
---

# L05 — Matriz de adopción y pesos

**~5 h · Semana 2**

## Objetivo

Crear matriz con criterios ponderados: valor ICP, costo, riesgo ops, seguridad, fit M26.

## Por qué importa

P2 obliga a explicitar trade-offs antes de escribir código del spike.

## Conceptos

- Peso ≥ hype
- Columna seguridad
- Score transparente

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

En `projects/m24-emergentes/matriz-adopcion.md` define pesos (suma 100%). Filas = candidatos; columnas = criterios.

Documenta **cómo** puntuas (1–5) con ejemplos por celda del candidato más fuerte.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l05 matriz-de-adopcion-y-pesos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Ejemplo matriz M24 | OWASP threat sketch |
| Catálogo | Entrada M24 | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

1. Matriz con pesos y ≥3 candidatos.
2. Columna seguridad no vacía.

## Errores comunes

- Todos 5/5 sin justificación.
- Olvidar costo mensual estimado.

## Siguiente

[L06 — Costo, operación y vendor lock-in](L06-costo-operacion-y-vendor-lock-in.md)
