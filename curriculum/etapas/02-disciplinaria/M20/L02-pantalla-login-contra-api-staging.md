---
id: L02
materia: M20
orden: 2
titulo: Pantalla login contra API staging
horas: 5
semana: 1
lectura: "HTTP client + auth API"
evidencia: "projects/m20-movil/demo-login-lista.md (inicio)"
---

# L02 — Pantalla login contra API staging

**~5 h · Semana 1**

## Objetivo

Implementar login email/password contra HTTPS M19; errores claros sin stack trace.

## Por qué importa

Misma API que web M17.

## Conceptos

- POST login
- 401 UX
- timeout

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Probar contra staging. Anota URL base en stack.md. Commit feat(m20): login.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l02 pantalla-login-contra-api-staging"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M17 | auth endpoints | M19 staging |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Login feliz
2. 401 mensaje humano
3. HTTPS

## Errores comunes

- localhost en release
- Password en logs

## Siguiente

[L03 — Secure storage de token o sesión](L03-secure-storage-de-token-o-sesion.md)
