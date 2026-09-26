---
id: L17
materia: M10
orden: 17
titulo: "Superficie de ataque: endpoints y datos"
horas: 5
semana: 5
lectura: "Hilo seguridad + ficha M10 proyecto"
evidencia: "superficie/endpoints.md (P3 inicio)"
---

# L17 — Superficie de ataque: endpoints y datos

**~5 h · Semana 5**

## Objetivo

Inventariar endpoints previstos, datos sensibles y vectores de red para el piloto web.

## Por qué importa

El mapa de superficie es entregable P3 y entrada a M18.

## Conceptos

- Superficie de ataque.
- PII en tránsito y en reposo (intro).
- Trust boundary navegador/API.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tabla: endpoint, auth, datos, riesgo red (robo sesión, sniffing, CSRF). Incluye admin y staff.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l17 superficie-de-ataque-endpoints-y-datos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | [Hilo seguridad](../../../hilos/seguridad.md) | Ficha M10 |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Tabla ≥10 filas (borrador API).
2. Datos PII marcados.
3. Riesgos numerados.

## Errores comunes

- Inventario solo del happy path.
- Olvidar webhooks o health checks.

## Siguiente

[L18 — Cliente y servidor TCP mínimo (P2)](L18-cliente-y-servidor-tcp-minimo-p2.md)
