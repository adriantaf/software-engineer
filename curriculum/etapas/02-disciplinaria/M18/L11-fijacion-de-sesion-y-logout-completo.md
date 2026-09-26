---
id: L11
materia: M18
orden: 11
titulo: Fijación de sesión y logout completo
horas: 5
semana: 3
lectura: "Session fixation + logout best practices"
evidencia: "projects/m18-appsec/session-lifecycle.md"
---

# L11 — Fijación de sesión y logout completo

**~5 h · Semana 3**

## Objetivo

Asegurar rotación de ID de sesión tras login y destrucción server-side en logout.

## Por qué importa

Robar sesión fija es un clásico en apps que reutilizan el mismo session id.

## Conceptos

- Regenerar session id post-auth.
- Invalidar en logout.
- Timeout por inactividad (idea).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Traza el ciclo en código. Documenta en `projects/m18-appsec/session-lifecycle.md`.

Pruebas: login dos veces ¿cambia id? logout ¿cookie inválida en siguiente request?

Si usas JWT stateless, documenta blacklist/short TTL en su lugar.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l11 fijacion-de-sesion-y-logout-completo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Session Management | Auth cheat sheet |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Doc ciclo de vida.
2. Pruebas login/logout documentadas.
3. Commit si hubo fix.

## Errores comunes

- Logout solo borra cookie cliente.
- Session id pre-login reutilizado.

## Siguiente

[L12 — Checklist cookies y CSRF en staging](L12-checklist-cookies-y-csrf-en-staging.md)
