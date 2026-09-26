---
id: L10
materia: M17
orden: 10
titulo: Middleware de autorización en API
horas: 5
semana: 3
lectura: "Middleware pattern"
evidencia: "authorize(role) middleware"
---

# L10 — Middleware de autorización en API

**~5 h · Semana 3**

## Objetivo

Middleware que verifica rol y negocio en cada handler sensible.

## Por qué importa

403 debe ser imposible de evitar desde el front.

## Conceptos

- middleware.
- 403.
- contexto usuario.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tests staff bloqueado en acción owner. Test 403 IDOR entre recursos.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l10 middleware-de-autorizacion-en-api"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m15 | tests seguridad | — |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. Middleware activo.
2. 403 tests.
3. Sin lógica duplicada.

## Errores comunes

- Check solo en UI.
- Hardcode user id.

## Siguiente

[L11 — Panel admin mínimo — gestión staff](L11-panel-admin-minimo-gestion-staff.md)
