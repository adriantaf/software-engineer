---
id: L06
materia: M15
orden: 6
titulo: Tests de integración con persistencia
horas: 5
semana: 2
lectura: "Testcontainers o DB test (documentado)"
evidencia: "projects/m15-calidad/tests/integration/"
---

# L06 — Tests de integración con persistencia

**~5 h · Semana 2**

## Objetivo

Un test de integración que persista y lea una cita (sqlite test o docker postgres).

## Por qué importa

M17 usará Postgres; hoy validas el puerto Repository real.

## Conceptos

- integración.
- migración.
- fixture.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Documenta cómo levantar DB test en README. ≥1 test integración verde.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l06 tests-de-integracion-con-persistencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m09 | esquema citas | m14 Repository |
| Catálogo | Entrada M15 | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

1. Test integración.
2. README comando.
3. Limpieza datos test.

## Errores comunes

- Usar prod DB.
- Tests orden-dependientes.

## Siguiente

[L07 — Tests HTTP de API — auth y validación](L07-tests-http-de-api-auth-y-validacion.md)
