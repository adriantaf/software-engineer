---
id: L19
materia: M17
orden: 19
titulo: Confirmación de cita y estados
horas: 5
semana: 5
lectura: "Flujo estado cita"
evidencia: "campo estado + UI"
---

# L19 — Confirmación de cita y estados

**~5 h · Semana 5**

## Objetivo

Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.

## Por qué importa

Staff y owner deben ver el mismo estado.

## Conceptos

- estado.
- sincronización.
- cancelación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tests API cambio estado + UI refleja. Mensaje WhatsApp opcional al confirmar.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l19 confirmacion-de-cita-y-estados"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m12-srs | flujos | — |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. Estados en API/UI.
2. Tests.
3. Commit.

## Errores comunes

- Estado solo en front.
- Cancelar sin auth.

## Siguiente

[L20 — Cierre P3 integración WhatsApp](L20-cierre-p3-integracion-whatsapp.md)
