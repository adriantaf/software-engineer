---
id: L27
materia: M18
orden: 27
titulo: Cabeceras de seguridad con Helmet o equivalente
horas: 5
semana: 7
lectura: "Security Headers Cheat Sheet"
evidencia: "commit headers + captura curl"
---

# L27 — Cabeceras de seguridad con Helmet o equivalente

**~5 h · Semana 7**

## Objetivo

Configurar HSTS (si HTTPS), X-Frame-Options/ frame-ancestors, X-Content-Type-Options, Referrer-Policy.

## Por qué importa

M10 L16 en tu código de producción.

## Conceptos

- Helmet middleware.
- HSTS solo con HTTPS estable.
- Clickjacking.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -sI https://<tu-staging>/ | rg -i 'strict|frame|content-type|referrer'
```

Documenta antes/después en bitácora. No rompas el front (prueba login).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l27 cabeceras-de-seguridad-con-helmet-o-equi"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Secure Headers | M10 L16 |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Headers visibles en staging.
2. Login sigue funcionando.
3. Commit.

## Errores comunes

- HSTS en localhost sin TLS.
- CSP rota todo sin reporte.

## Siguiente

[L28 — CSP básica sin romper Agenda Ops](L28-csp-basica-sin-romper-agenda-ops.md)
