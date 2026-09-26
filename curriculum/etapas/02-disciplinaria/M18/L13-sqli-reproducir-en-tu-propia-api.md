---
id: L13
materia: M18
orden: 13
titulo: SQLi: reproducir en tu propia API
horas: 5
semana: 4
lectura: "OWASP A03 Injection + SQLi Prevention"
evidencia: "projects/m18-appsec/findings/001-sqli.md"
---

# L13 — SQLi: reproducir en tu propia API

**~5 h · Semana 4**

## Objetivo

Encontrar al menos un punto susceptible (búsqueda, filtro, orden) y demostrar SQLi controlada en local/staging **sin** dañar datos reales.

## Por qué importa

P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.

## Conceptos

- Consulta concatenada vs parametrizada.
- Error verbose vs genérico.
- Principio de mínimo privilegio DB.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Usa cuenta de prueba. Intenta payloads en query params/body (`' OR '1'='1` etc.) en endpoints de búsqueda de clientes/citas.

Documenta en `projects/m18-appsec/findings/001-sqli.md`: endpoint, payload, respuesta, impacto. **No** pegues datos de clientes reales.

Si no hay SQLi, documenta por qué (ORM parametrizado) y prueba bypass conocido del ORM.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l13 sqli-reproducir-en-tu-propia-api"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | SQL Injection | ORM docs de tu stack |

## Hecho cuando

1. Finding documentado o prueba de mitigación.
2. Solo tu entorno.
3. Sin PII en el reporte.

## Errores comunes

- SQLi en producción de terceros.
- Drop table en staging compartido.

## Siguiente

[L14 — Mitigar SQLi: queries parametrizadas y permisos DB](L14-mitigar-sqli-queries-parametrizadas-y-permisos-db.md)
