---
id: L14
materia: M18
orden: 14
titulo: "Mitigar SQLi: queries parametrizadas y permisos DB"
horas: 5
semana: 4
lectura: "SQLi Prevention Cheat Sheet"
evidencia: "commit fix + test en repo producto"
---

# L14 — Mitigar SQLi: queries parametrizadas y permisos DB

**~5 h · Semana 4**

## Objetivo

Corregir el vector SQLi (o endurecer consulta) y añadir test de regresión que falle si vuelve la concatenación.

## Por qué importa

Hallazgo sin fix no cuenta para P2.

## Conceptos

- Prepared statements.
- Validación de entrada en frontera.
- Usuario DB sin DDL.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementa fix en tu API de Agenda Ops (repo M17). Test automatizado: input malicioso → 400 o resultado vacío, nunca error SQL expuesto.

Actualiza `001-sqli.md` con commit hash y captura de test verde.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l14 mitigar-sqli-queries-parametrizadas-y-pe"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | SQLi Prevention | Tests M15 si aplica |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Commit fix.
2. Test de regresión.
3. Finding actualizado a Cerrado.

## Errores comunes

- Escapar manualmente sin parametrizar.
- Silenciar error sin arreglar query.

## Siguiente

[L15 — XSS reflejado en campos de cliente o búsqueda](L15-xss-reflejado-en-campos-de-cliente-o-busqueda.md)
