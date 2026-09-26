---
id: L19
materia: M18
orden: 19
titulo: Rate limiting en login y endpoints sensibles
horas: 5
semana: 5
lectura: "Brute Force + Rate Limiting Cheat Sheets"
evidencia: "commit middleware + nota en findings"
---

# L19 — Rate limiting en login y endpoints sensibles

**~5 h · Semana 5**

## Objetivo

Implementar límite de intentos (IP o cuenta) en login y al menos un endpoint costoso.

## Por qué importa

Sin rate limit, A07 y A04 (DoS ligero) son triviales.

## Conceptos

- Ventana fija vs token bucket (idea).
- 429 Too Many Requests.
- No bloquear legítimos sin UX.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Añade rate limit (lib o reverse proxy local). Prueba 20 intentos fallidos login → bloqueo temporal.

Documenta configuración y cómo resetear en dev.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l19 rate-limiting-en-login-y-endpoints-sensi"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Brute Force | M11 recursos |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Rate limit activo.
2. Prueba documentada.
3. Mensaje usuario claro.

## Errores comunes

- Rate limit solo en front.
- Bloqueo permanente sin unlock.

## Siguiente

[L20 — Tests automatizados cross-user (P2 avance)](L20-tests-automatizados-cross-user-p2-avance.md)
