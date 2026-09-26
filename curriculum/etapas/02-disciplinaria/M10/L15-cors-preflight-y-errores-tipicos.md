---
id: L15
materia: M10
orden: 15
titulo: CORS, preflight y errores típicos
horas: 5
semana: 4
lectura: "MDN CORS"
evidencia: "labs/cors.md"
---

# L15 — CORS, preflight y errores típicos

**~5 h · Semana 4**

## Objetivo

Explicar por qué el navegador aplica CORS y qué cabeceras configura el servidor API para un front en otro origen.

## Por qué importa

En M17 separarás front y API; hoy evitas “arreglar CORS con `*`”.

## Conceptos

- Same-origin policy.
- Preflight OPTIONS.
- Credentials y `Access-Control-Allow-Credentials`.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Esboza política CORS para piloto: orígenes permitidos, métodos, headers. Prohíbe `*` con credenciales.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l15 cors-preflight-y-errores-tipicos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | CORS | Fetch API |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Política CORS borrador.
2. Explicas preflight en 5 frases.
3. Error común documentado.

## Errores comunes

- `Access-Control-Allow-Origin: *` con cookies.
- Confundir CORS con autorización en API.

## Siguiente

[L16 — Cabeceras de seguridad HTTP](L16-cabeceras-de-seguridad-http.md)
