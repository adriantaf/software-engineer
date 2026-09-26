---
id: L07
materia: M15
orden: 7
titulo: Tests HTTP de API — auth y validación
horas: 5
semana: 2
lectura: "supertest o fetch contra app test"
evidencia: "projects/m15-calidad/tests/api/"
---

# L07 — Tests HTTP de API — auth y validación

**~5 h · Semana 2**

## Objetivo

Tests HTTP: 401 sin sesión, 400 payload inválido, 201 feliz en ruta de citas (spike o m17).

## Por qué importa

La autorización se prueba en servidor, no ocultando botones.

## Conceptos

- HTTP.
- 401.
- 400.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥4 tests API. Tabla entrada/esperado como en ficha M15.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l07 tests-http-de-api-auth-y-validacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Auth cheat sheet | m13 endpoints |
| Catálogo | Entrada M15 | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

1. 401 automatizado.
2. 400 validación.
3. 201 feliz.

## Errores comunes

- Solo test unitario.
- Olvidar 403.

## Siguiente

[L08 — IDOR y roles — casos 403](L08-idor-y-roles-casos-403.md)
