---
id: L26
materia: M17
orden: 26
titulo: Headers de seguridad y CORS prod
horas: 5
semana: 7
lectura: "MDN security headers"
evidencia: "helmet o equivalente"
---

# L26 — Headers de seguridad y CORS prod

**~5 h · Semana 7**

## Objetivo

Configurar headers básicos y CORS restrictivo a dominio front.

## Por qué importa

Reduce superficie antes de abrir al partner.

## Conceptos

- helmet.
- CORS.
- CSP intro.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Documenta valores en `docs/seguridad-http.md`. Test manual headers.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l26 headers-de-seguridad-y-cors-prod"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | CORS | m10 lecciones |

## Hecho cuando

1. Headers activos prod.
2. CORS no `*`.
3. Doc.

## Errores comunes

- CORS abierto.
- CSP rota sin probar.

## Siguiente

[L27 — Rate limit en login](L27-rate-limit-en-login.md)
