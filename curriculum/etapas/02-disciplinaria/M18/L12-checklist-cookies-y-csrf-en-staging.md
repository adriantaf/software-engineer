---
id: L12
materia: M18
orden: 12
titulo: Checklist cookies y CSRF en staging
horas: 5
semana: 3
lectura: "Repaso semana 3"
evidencia: "projects/m18-appsec/checklist-cookies-csrf.md"
---

# L12 — Checklist cookies y CSRF en staging

**~5 h · Semana 3**

## Objetivo

Checklist binario ejecutable antes de cada deploy: cookies, CSRF, HTTPS, logout.

## Por qué importa

Operacionalizas controles para M19 deploy y trials M22.

## Conceptos

- Checklist reproducible.
- Evidencia en staging.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m18-appsec/checklist-cookies-csrf.md` con ≥10 ítems Sí/No. Ejecútalo contra staging y pega resultado (fecha, URL).

Enlaza issues/commits de la semana. Cierra con riesgo residual CSRF.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l12 checklist-cookies-y-csrf-en-staging"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M18 semana 3 | M19 ambientes futuro |

## Hecho cuando

1. Checklist ejecutado.
2. Fecha y URL.
3. ≥1 ítem corregido esta semana.

## Errores comunes

- Checklist nunca ejecutado.
- Marcar todo Sí sin prueba.

## Siguiente

[L13 — SQLi: reproducir en tu propia API](L13-sqli-reproducir-en-tu-propia-api.md)
