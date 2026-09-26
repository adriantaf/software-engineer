---
id: L20
materia: M18
orden: 20
titulo: Tests automatizados cross-user (P2 avance)
horas: 5
semana: 5
lectura: "Testing access control"
evidencia: "tests en repo producto + projects/m18-appsec/findings-table.md"
---

# L20 — Tests automatizados cross-user (P2 avance)

**~5 h · Semana 5**

## Objetivo

Escribir ≥2 tests: usuario A no lee/edita recurso de B; rol staff no ejecuta acción de owner.

## Por qué importa

P2 pide tabla hallazgo→fix→test; hoy consolidas access control.

## Conceptos

- Fixture dos usuarios.
- Arrange-Act-Assert.
- 401 vs 403 semántica.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
# ejemplo nombre
npm test -- --testPathPattern=authz
```

Actualiza findings-table con IDOR y RBAC. Mínimo 5 hallazgos totales en P2 al cerrar M18 — planifica los que faltan.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l20 tests-automatizados-cross-user-p2-avance"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M18 P2 | M15 testing |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. ≥2 tests authz verdes.
2. findings-table ≥3 filas.
3. Commits referenciados.

## Errores comunes

- Tests que mockean auth siempre true.
- Un solo usuario en tests.

## Siguiente

[L21 — SSRF: superficie en webhooks e integraciones](L21-ssrf-superficie-en-webhooks-e-integraciones.md)
