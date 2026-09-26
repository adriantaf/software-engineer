---
id: L07
materia: M18
orden: 7
titulo: Sesiones server-side vs JWT en Agenda Ops
horas: 5
semana: 2
lectura: "Session Management + JWT Cheat Sheets"
evidencia: "projects/m18-appsec/adr-sesion-vs-jwt.md (o enlace ADR M13)"
---

# L07 — Sesiones server-side vs JWT en Agenda Ops

**~5 h · Semana 2**

## Objetivo

Decidir y documentar si Agenda Ops usa sesión en servidor, JWT firmado, o híbrido; consecuencias para XSS, logout y revocación.

## Por qué importa

M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.

## Conceptos

- Revocación inmediata.
- HttpOnly cookie vs Authorization header.
- Refresh token (si aplica).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Redacta `projects/m18-appsec/adr-sesion-vs-jwt.md`: contexto, decisión, alternativas rechazadas, impacto en móvil M20.

Prueba manual: login → copiar token/cookie → logout → reutilizar credencial vieja (debe fallar).

Anota resultado en la ADR.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l07 sesiones-server-side-vs-jwt-en-agenda-op"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M13 | adr/005-auth si existe | M10 L14 sesiones |

## Hecho cuando

1. ADR con alternativas.
2. Prueba logout/reuse documentada.
3. Coherente con móvil futuro.

## Errores comunes

- JWT en localStorage sin plan anti-XSS.
- Sin estrategia de revocación.

## Siguiente

[L08 — Threat model v1 post-autenticación (P1)](L08-threat-model-v1-post-autenticacion-p1.md)
