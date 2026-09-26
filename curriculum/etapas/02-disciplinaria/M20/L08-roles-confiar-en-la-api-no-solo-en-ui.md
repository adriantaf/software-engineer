---
id: L08
materia: M20
orden: 8
titulo: Roles: confiar en la API, no solo en UI
horas: 5
semana: 2
lectura: "RBAC móvil"
evidencia: "nota rbac en demo-login-lista.md"
---

# L08 — Roles: confiar en la API, no solo en UI

**~5 h · Semana 2**

## Objetivo

Probar cuenta staff vs owner; ocultar acciones que API niega con 403.

## Por qué importa

Doble fuente de verdad mata proyectos.

## Conceptos

- 403 handling
- roles

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Prueba endpoint prohibido; muestra mensaje adecuado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l08 roles-confiar-en-la-api-no-solo-en-ui"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M18 | rbac-matrix | M12 roles |

## Hecho cuando

1. Prueba rol documentada
2. 403 UX
3. Sin lógica secreta solo UI

## Errores comunes

- Admin hardcoded en app
- Ignorar 403

## Siguiente

[L09 — Pantalla detalle de cita](L09-pantalla-detalle-de-cita.md)
