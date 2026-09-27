---
id: L03
materia: M13
orden: 3
titulo: Escenarios alternos y errores
horas: 5.0
semana: 1
lectura: "Larman: escenarios alternos; códigos HTTP de auth/validación"
evidencia: casos-de-uso.md con escenarios 401/403/409 por UC críticos
---

# L03 — Escenarios alternos y errores

**~5.0 h · Semana 1**

El flujo feliz de “crear pedido” es el 20 %. Hoy diseñas el 80 %: sin sesión, sin permiso, slot ocupado, input inválido.

## Objetivo

Extender `casos-de-uso.md` con escenarios alternos y de error alineados a códigos HTTP.

## Por qué importa

M15 pedirá tests 401/403/409. Si el diseño no nombra esos caminos, los tests inventarán comportamiento.

## Pasos (hazlos en orden)

### 1. Elige 3 UC críticos (15 min)

Típico: `UC-01` login, `UC-03` crear pedido, `UC-04` cancelar (o listar agenda).

### 2. Plantilla por UC (90–110 min)

Para cada uno, añade bajo el caso:

```markdown
### UC-03 Crear pedido

**Feliz:** Staff autenticado, slot libre, cliente existente → 201 + pedido.

**A1 — Sin autenticación:** sin cookie → **401**. No revelar si el slot existe.

**A2 — Rol insuficiente:** si defines “solo owner cancela”, staff → **403**.

**A3 — Conflicto de horario:** mismo slot → **409** con mensaje genérico.

**A4 — Input inválido:** `fin < inicio` o servicio inexistente → **400** + campos.

**Datos que NUNCA van en el mensaje:** emails de otros clientes, IDs internos de otro negocio.
```

### 3. Tabla resumen de errores (40–50 min)

Al final de `casos-de-uso.md`:

| UC | Condición | HTTP | Mensaje (idea) |
|----|-----------|------|----------------|
| UC-03 | sin sesión | 401 | “Inicia sesión” |
| UC-03 | slot ocupado | 409 | “Horario no disponible” |

### 4. Revisa contra trust boundaries (20 min)

Abre `diagramas/trust-boundaries.md`: ¿cada error se decide en la **API**, no solo en el front?

### 5. Commit (15 min)

```bash
git add projects/m13-diseno/casos-de-uso.md
git commit -m "docs(m13): escenarios alternos y errores en casos de uso"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Flujos alternos y de error; 401 vs 403 vs 409 en APIs | [MDN — HTTP status codes](https://developer.mozilla.org/es/docs/Web/HTTP/Status) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Al menos 3 UC críticos tienen escenario feliz + ≥2 alternos/error documentados.
2. Cada error nombra código HTTP esperado (401/403/400/409) y mensaje *sin* filtrar datos ajenos.
3. Commit `docs(m13): escenarios alternos y errores en casos de uso`.

## Errores comunes

- Mezclar 401 (no autenticado) con 403 (autenticado sin permiso).
- Mensajes tipo “el cliente X de otro negocio no existe” (filtración).
- Solo escenario feliz: el diseño de M17 fallará en conflictos de horario.

## Siguiente

[L04 — Cierre P1 flujos principales](L04-cierre-p1-flujos-principales.md)
