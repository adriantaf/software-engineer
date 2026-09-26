---
id: L13
materia: M10
orden: 13
titulo: "Cookies: atributos y modelo de almacenamiento"
horas: 5
semana: 4
lectura: "MDN Cookies (ES)"
evidencia: "labs/cookies.md"
---

# L13 — Cookies: atributos y modelo de almacenamiento

**~5 h · Semana 4**

## Objetivo

Documentar `Set-Cookie` con `Secure`, `HttpOnly`, `SameSite` y cuándo usar cookie vs header Authorization.

## Por qué importa

La sesión del dueño de Agenda Ops no puede robarse por XSS ni enviarse en HTTP plano.

## Conceptos

- Cookie de sesión vs token en memoria.
- SameSite=Lax/Strict.
- Path y Domain.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -sI https://httpbin.org/cookies/set/session/abc | rg -i set-cookie || true
```

Diseña (en texto) la cookie de sesión del piloto: atributos obligatorios.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l13 cookies-atributos-y-modelo-de-almacenami"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | HTTP cookies | OWASP Session Management cheat sheet (selecto) |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Diseño de cookie de sesión escrito.
2. Tabla atributo/propósito.
3. Riesgo XSS ligado a HttpOnly.

## Errores comunes

- SameSite=None sin Secure.
- Guardar JWT enorme en cookie sin necesidad.

## Siguiente

[L14 — Sesiones, tokens y estado en APIs](L14-sesiones-tokens-y-estado-en-apis.md)
