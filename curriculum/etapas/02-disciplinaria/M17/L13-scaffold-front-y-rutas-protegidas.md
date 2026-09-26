---
id: L13
materia: M17
orden: 13
titulo: Scaffold front y rutas protegidas
horas: 5
semana: 4
lectura: "React Router / framework docs"
evidencia: "front app + router"
---

# L13 — Scaffold front y rutas protegidas

**~5 h · Semana 4**

## Objetivo

Crear front con login, layout panel, rutas protegidas redirect a login.

## Por qué importa

Agenda Ops se usa desde navegador diario.

## Conceptos

- SPA.
- protected route.
- layout.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Estructura `apps/web` o `client/`. Env API_URL documentado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l13 scaffold-front-y-rutas-protegidas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | fetch | m16 prototipo |

## Hecho cuando

1. Front arranca.
2. Redirect sin sesión.
3. Commit.

## Errores comunes

- CORS `*` sin doc.
- API_URL hardcode prod.

## Siguiente

[L14 — Flujo login/logout en UI](L14-flujo-login-logout-en-ui.md)
