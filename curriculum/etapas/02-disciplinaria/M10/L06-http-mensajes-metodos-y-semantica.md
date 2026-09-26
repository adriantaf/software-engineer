---
id: L06
materia: M10
orden: 6
titulo: HTTP mensajes, métodos y semántica
horas: 5
semana: 2
lectura: "MDN HTTP methods + Tanenbaum capa aplicación"
evidencia: "labs/http-metodos.md"
---

# L06 — HTTP mensajes, métodos y semántica

**~5 h · Semana 2**

## Objetivo

Construir requests GET/HEAD/OPTIONS con `curl` y explicar idempotencia y seguridad de métodos comunes.

## Por qué importa

REST mal diseñado mezcla verbos; hoy fijas criterio antes de modelar `/citas` en Agenda Ops.

## Conceptos

- Línea de petición y cabeceras.
- Cuerpo y `Content-Type`.
- Idempotencia (GET, PUT, DELETE).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -sI https://httpbin.org/get
curl -s -X OPTIONS -I https://httpbin.org/ 2>/dev/null | head -20
```

Escribe qué método usarías para listar citas vs cancelar una (borrador conceptual).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l06 http-mensajes-metodos-y-semantica"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | HTTP request methods | httpbin.org para pruebas |

## Hecho cuando

1. Tabla método/uso/riesgo.
2. Al menos tres requests documentados.
3. Nota sobre idempotencia en cancelación de citas.

## Errores comunes

- Usar POST para todo.
- Olvidar que HEAD no lleva cuerpo.

## Siguiente

[L07 — Status codes y cabeceras de respuesta](L07-status-codes-y-cabeceras-de-respuesta.md)
