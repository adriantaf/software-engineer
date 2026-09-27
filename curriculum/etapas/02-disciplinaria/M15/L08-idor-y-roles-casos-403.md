---
id: L08
materia: M15
orden: 8
titulo: IDOR y roles — casos 403
horas: 5.0
semana: 2
lectura: IDOR; autorización por dueño/rol
evidencia: tests HTTP 403 IDOR + rol insuficiente
---

# L08 — IDOR y roles — casos 403

**~5.0 h · Semana 2**

Hilo seguridad: el piloto single-tenant aún puede tener IDOR entre usuarios/roles.

## Objetivo

Automatizar 403 (P1 capa API completa).

## Pasos (hazlos en orden)

### 1. Fixtures de dos usuarios (40 min)

### 2. Tests IDOR + rol (80–100 min)

### 3. Actualiza piramide.md (20 min)

### 4. Commit

`test(m15): idor y roles 403`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | 403: IDOR de pedido ajena y rol staff vs owner | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Test: usuario A no lee/modifica pedido de B → 403 (o 404 documentado).
2. Test: rol insuficiente → 403.
3. Commit `test(m15): idor y roles 403`.

## Errores comunes

- Devolver 200 con body vacío (silencio peligroso sin política).
- Mensajes que revelan existencia de recurso ajeno sin decisión consciente.
- Solo test de UI ocultando botón.

## Siguiente

[L09 — Workflow GitHub Actions — esqueleto](L09-workflow-github-actions-esqueleto.md)
