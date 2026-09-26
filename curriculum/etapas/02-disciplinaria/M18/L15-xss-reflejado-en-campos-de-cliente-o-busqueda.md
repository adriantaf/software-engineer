---
id: L15
materia: M18
orden: 15
titulo: XSS reflejado en campos de cliente o búsqueda
horas: 5
semana: 4
lectura: "XSS Prevention Cheat Sheet"
evidencia: "projects/m18-appsec/findings/002-xss-reflected.md"
---

# L15 — XSS reflejado en campos de cliente o búsqueda

**~5 h · Semana 4**

## Objetivo

Probar XSS reflejado en un campo que se renderiza (nombre, mensaje de error) y documentar contexto HTML/JS.

## Por qué importa

XSS roba sesiones si las cookies son legibles por JS.

## Conceptos

- Reflejado vs almacenado.
- Contexto de escape.
- Content-Type correcto.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Payloads: `<script>alert(1)</script>`, event handlers. En `projects/m18-appsec/findings/002-xss-reflected.md` indica pantalla y si el navegador ejecutó (en tu cuenta de prueba).

No uses payloads que exfiltruen a dominios externos; solo demuestra impacto local.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l15 xss-reflejado-en-campos-de-cliente-o-bus"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | XSS Prevention | CSP intro semana 7 |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. PoC documentada.
2. Contexto identificado.
3. Sin atacar usuarios reales.

## Errores comunes

- XSS persistente en prod sin aviso.
- Confiar en ‘React escapa todo’.

## Siguiente

[L16 — XSS almacenado y escape en plantillas/API](L16-xss-almacenado-y-escape-en-plantillas-api.md)
