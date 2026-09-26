---
id: L02
materia: M15
orden: 2
titulo: Tests unitarios puros de reglas de cita
horas: 5
semana: 1
lectura: "Dominio sin I/O"
evidencia: "projects/m15-calidad/tests/dominio-citas.test.ts"
---

# L02 — Tests unitarios puros de reglas de cita

**~5 h · Semana 1**

## Objetivo

Ampliar tests unitarios: pasado, duración, solapamiento, zona horaria documentada.

## Por qué importa

La lógica de citas es donde más duele un bug en producción.

## Conceptos

- unit puro.
- fast feedback.
- tabla casos.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥8 casos en tabla markdown + tests. Sin DB ni HTTP en esta lección.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l02 tests-unitarios-puros-de-reglas-de-cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m12-srs | stories Must | — |

## Hecho cuando

1. ≥8 tests dominio.
2. Tabla casos.
3. Verde local.

## Errores comunes

- Tests que levantan servidor.
- Datos hardcode sin nombre.

## Siguiente

[L03 — Qué no testear y carpetas de coverage](L03-que-no-testear-y-carpetas-de-coverage.md)
