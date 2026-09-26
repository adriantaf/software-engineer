---
id: L07
materia: M10
orden: 7
titulo: Status codes y cabeceras de respuesta
horas: 5
semana: 2
lectura: "MDN HTTP response status + lista IANA selecta"
evidencia: "labs/status-codes.md"
---

# L07 — Status codes y cabeceras de respuesta

**~5 h · Semana 2**

## Objetivo

Clasificar códigos 2xx/3xx/4xx/5xx y leer cabeceras `Cache-Control`, `Content-Type`, `Server` con ojo crítico.

## Por qué importa

Un 401 mal interpretado como 500 envía horas de debug al lugar equivocado.

## Conceptos

- Semántica 401 vs 403.
- Redirects 301/302.
- Caching en APIs (cuándo no cachear).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://httpbin.org/status/404
curl -sI https://httpbin.org/response-headers?freeform=%22X-Test:1%22 | head -25
```

Mapea códigos que usará Agenda Ops: login fallido, cita no encontrada, conflicto de horario.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l07 status-codes-y-cabeceras-de-respuesta"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | HTTP status codes | httpbin.org/status |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Lista ≥8 códigos con ejemplo Agenda Ops.
2. Captura de cabeceras anotada.
3. Diferencia 401/403 escrita.

## Errores comunes

- Devolver siempre 200 con `{error:true}`.
- Exponer `Server` con versión vulnerable.

## Siguiente

[L08 — HTTP/2 intuición y curl avanzado](L08-http-2-intuicion-y-curl-avanzado.md)
