---
id: L09
materia: M18
orden: 9
titulo: Cookies Secure, HttpOnly y SameSite
horas: 5
semana: 3
lectura: "OWASP Session Management + cookie flags"
evidencia: "projects/m18-appsec/cookies-lab.md"
---

# L09 — Cookies Secure, HttpOnly y SameSite

**~5 h · Semana 3**

## Objetivo

Inspeccionar cookies de sesión de Agenda Ops en DevTools y verificar flags; corregir configuración en el servidor.

## Por qué importa

M10 estudió cookies; hoy aplicas flags en **tu** stack.

## Conceptos

- SameSite=Lax/Strict.
- Secure en HTTPS.
- HttpOnly vs JS legítimo.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Login en staging/local. En `projects/m18-appsec/cookies-lab.md` tabla: nombre cookie, flags, lifetime, path.

Si falta `Secure` o `HttpOnly` en cookie de sesión, parchea middleware/framework y captura antes/después (sin valor de cookie).

Prueba: ¿JavaScript puede leer la cookie de sesión? Documenta.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l09 cookies-secure-httponly-y-samesite"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | Set-Cookie | M10 L13 |

## Hecho cuando

1. Tabla de cookies real.
2. Parche o justificación documentada.
3. Prueba HttpOnly.

## Errores comunes

- SameSite=None sin Secure.
- Cookie de sesión accesible desde JS.

## Siguiente

[L10 — CSRF en formularios y mutaciones state-changing](L10-csrf-en-formularios-y-mutaciones-state-changing.md)
