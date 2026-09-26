---
id: L23
materia: M18
orden: 23
titulo: Deserialización y JSON peligroso
horas: 5
semana: 6
lectura: "Deserialization + API hardening"
evidencia: "projects/m18-appsec/json-trust.md"
---

# L23 — Deserialización y JSON peligroso

**~5 h · Semana 6**

## Objetivo

Auditar parsers JSON, `eval`, plantillas dinámicas y tipos inesperados en body de API.

## Por qué importa

Node/TS rara vez hace Java deserialization, pero prototype pollution y lógica sí.

## Conceptos

- Validación schema (zod/joi).
- Prototype pollution (idea).
- Tamaño body limit.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m18-appsec/json-trust.md`: lista endpoints con body JSON; schema sí/no. Añade límite `express.json({ limit: '100kb' })` o equivalente.

Prueba payload enorme o campos extra; documenta comportamiento.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l23 deserializacion-y-json-peligroso"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | API Security Top 10 | Input validation |

## Hecho cuando

1. Lista endpoints + validación.
2. Límite tamaño body.
3. ≥1 mejora commitada.

## Errores comunes

- Aceptar cualquier JSON.
- Confiar en tipos TS solo compile-time.

## Siguiente

[L24 — Consolidar hallazgos semana 6 en P2](L24-consolidar-hallazgos-semana-6-en-p2.md)
