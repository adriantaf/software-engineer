---
id: L18
materia: M18
orden: 18
titulo: Autorización por rol owner vs staff
horas: 5
semana: 5
lectura: "Access Control Cheat Sheet"
evidencia: "projects/m18-appsec/rbac-matrix.md"
---

# L18 — Autorización por rol owner vs staff

**~5 h · Semana 5**

## Objetivo

Matriz rol × recurso × acción para Agenda Ops y gaps entre SRS y código.

## Por qué importa

Agenda Ops distingue dueño y staff; la API debe hacerlo explícito.

## Conceptos

- RBAC vs ABAC (idea).
- 403 vs 404.
- Principio mínimo privilegio.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m18-appsec/rbac-matrix.md`: filas citas, clientes, configuración; columnas owner/staff/anónimo.

Prueba un caso staff que no debe ver citas de otro tenant (futuro) o acción admin. Registra resultado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l18 autorizacion-por-rol-owner-vs-staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| SRS | M12 roles | OWASP A01 |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Matriz completa.
2. ≥1 prueba manual rol.
3. Gaps listados.

## Errores comunes

- Un solo rol ‘admin’.
- 404 para esconder sin authz.

## Siguiente

[L19 — Rate limiting en login y endpoints sensibles](L19-rate-limiting-en-login-y-endpoints-sensibles.md)
