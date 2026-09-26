---
id: L03
materia: M17
orden: 3
titulo: Login, sesión y GET /me protegido
horas: 5
semana: 1
lectura: "MDN cookies + ADR sesión M13"
evidencia: "POST /auth/login + GET /me"
---

# L03 — Login, sesión y GET /me protegido

**~5 h · Semana 1**

## Objetivo

Login con cookie HttpOnly o JWT en cookie; `GET /me` devuelve 401 sin credencial.

## Por qué importa

El panel Agenda Ops necesita identidad servidor-confiable.

## Conceptos

- sesión.
- 401.
- HttpOnly.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tests: login → me 200; sin cookie → 401. Documenta elección en `docs/auth.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l03 login-sesion-y-get-me-protegido"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | HTTP cookies | hilo seguridad |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. Login+me.
2. 401 test.
3. auth.md.

## Errores comunes

- JWT localStorage sin doc.
- Me devuelve todo el row.

## Siguiente

[L04 — Cierre semana 1 — suite auth P1](L04-cierre-semana-1-suite-auth-p1.md)
