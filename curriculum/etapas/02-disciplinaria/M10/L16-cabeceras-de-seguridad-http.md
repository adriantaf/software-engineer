---
id: L16
materia: M10
orden: 16
titulo: Cabeceras de seguridad HTTP
horas: 5
semana: 4
lectura: "MDN CSP, HSTS, X-Frame-Options"
evidencia: "labs/security-headers.md"
---

# L16 — Cabeceras de seguridad HTTP

**~5 h · Semana 4**

## Objetivo

Inspeccionar un sitio real y redactar lista de cabeceras que aplicarás en Agenda Ops (aunque aún no exista código).

## Por qué importa

P3 y el proyecto M10 piden inventario honesto de superficie.

## Conceptos

- CSP (idea).
- HSTS.
- X-Content-Type-Options.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -sI https://securityheaders.com 2>/dev/null | head -30
# o cualquier sitio de referencia que elijas
```

Lista cabeceras presentes/ausentes y prioridad para MVP.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l16 cabeceras-de-seguridad-http"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | Content-Security-Policy | securityheaders.com como inspiración |

## Hecho cuando

1. Lista priorizada para MVP.
2. Captura curl comentada.
3. Cierre semana 4.

## Errores comunes

- CSP `unsafe-inline` sin plan de quitarlo.
- HSTS sin HTTPS estable.

## Siguiente

[L17 — Superficie de ataque: endpoints y datos](L17-superficie-de-ataque-endpoints-y-datos.md)
