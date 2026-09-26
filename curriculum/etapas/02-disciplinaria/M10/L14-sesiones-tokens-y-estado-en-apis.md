---
id: L14
materia: M10
orden: 14
titulo: Sesiones, tokens y estado en APIs
horas: 5
semana: 4
lectura: "MDN Web Storage vs cookies + notas OAuth2 (vista alta)"
evidencia: "labs/sesiones.md"
---

# L14 — Sesiones, tokens y estado en APIs

**~5 h · Semana 4**

## Objetivo

Comparar sesión server-side, JWT stateless y refresh tokens; elegir borrador para piloto single-tenant.

## Por qué importa

M12/M13 fijarán auth; hoy entiendes trade-offs de red y superficie.

## Conceptos

- Stateful session store.
- JWT en header vs cookie.
- Rotación de refresh.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tabla comparativa con columnas: revocación, tamaño, CSRF, XSS. Recomendación provisional para Agenda Ops.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l14 sesiones-tokens-y-estado-en-apis"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | Web Storage API | OAuth 2.0 overview (no implementar aún) |

## Hecho cuando

1. Tabla comparativa completa.
2. Recomendación con justificación.
3. Riesgos CSRF mencionados.

## Errores comunes

- JWT en localStorage “porque es fácil”.
- Sesiones sin expiración.

## Siguiente

[L15 — CORS, preflight y errores típicos](L15-cors-preflight-y-errores-tipicos.md)
