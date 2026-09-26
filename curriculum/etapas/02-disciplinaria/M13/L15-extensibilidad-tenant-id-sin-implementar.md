---
id: L15
materia: M13
orden: 15
titulo: Extensibilidad tenant_id sin implementar
horas: 5
semana: 4
lectura: "producto-saas evolución"
evidencia: "adr/004-tenant-future.md"
---

# L15 — Extensibilidad tenant_id sin implementar

**~5 h · Semana 4**

## Objetivo

Documentar dónde vivirá `tenant_id` en modelo y API sin implementarlo en piloto.

## Por qué importa

Camino a SaaS sin reescribir todo en M21.

## Conceptos

- single-tenant ahora.
- tenant_id futuro.
- riesgo mezcla datos.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ADR 004: supuestos, columnas futuras, no exponer multi-tenant en MVP.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l15 extensibilidad-tenant-id-sin-implementar"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | producto-saas.md | srs supuestos |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. ADR 004.
2. Riesgo cross-tenant nombrado.
3. No implementar aún.

## Errores comunes

- Implementar multi-tenant en piloto.
- Ignorar extensión.

## Siguiente

[L16 — ADR auth y sesión](L16-adr-auth-y-sesion.md)
