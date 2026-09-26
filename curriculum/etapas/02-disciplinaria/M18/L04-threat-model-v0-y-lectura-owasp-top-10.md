---
id: L04
materia: M18
orden: 4
titulo: Threat model v0 y lectura OWASP Top 10
horas: 5
semana: 1
lectura: "OWASP Top 10 (2021) — lectura completa en español"
evidencia: "projects/m18-appsec/owasp-top10-map.md"
---

# L04 — Threat model v0 y lectura OWASP Top 10

**~5 h · Semana 1**

## Objetivo

Mapear cada categoría del OWASP Top 10 a un endpoint o pantalla concreta de Agenda Ops (aunque aún no tengas el bug).

## Por qué importa

Cierras la semana 1 con backlog de riesgo alineado al estándar de la industria.

## Conceptos

- A01 Broken Access Control.
- A03 Injection.
- A07 Identification and Authentication Failures.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

En `projects/m18-appsec/owasp-top10-map.md` tabla: **OWASP id**, **Ejemplo en Agenda Ops**, **Mitigación prevista**, **Semana M18**.

Añade en `threat-model-v0.md` sección **Riesgo residual semana 1** (3 bullets).

Relee la ficha M18: confirma que P1 (threat model v1) llegará tras semana 2 auth.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l04 threat-model-v0-y-lectura-owasp-top-10"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Top 10 ES | Cheat Sheets índice |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Mapa 10 filas mínimo.
2. threat-model-v0 actualizado.
3. Commit semana 1.

## Errores comunes

- Marcar ‘no aplica’ en todo.
- Atacar sitios que no controlas.

## Siguiente

[L05 — Inventario de autenticación actual](L05-inventario-de-autenticacion-actual.md)
