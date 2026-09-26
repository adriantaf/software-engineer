---
id: L03
materia: M13
orden: 3
titulo: Escenarios alternos y errores
horas: 5
semana: 1
lectura: "Escenarios excepción"
evidencia: "casos-de-uso.md escenarios"
---

# L03 — Escenarios alternos y errores

**~5 h · Semana 1**

## Objetivo

Documentar alternos 401/403, conflicto horario, validación.

## Por qué importa

M17 implementará estos caminos; hoy los nombras.

## Conceptos

- flujo alterno.
- postcondición error.
- mensaje.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Cada caso Must tiene ≥1 alterno de error.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l03 escenarios-alternos-y-errores"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Larman | escenarios | stories errores |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. Alternos documentados.
2. Códigos HTTP previstos.
3. Sin happy path único.

## Errores comunes

- Errores genéricos 500.
- Ignorar 403 en notas privadas.

## Siguiente

[L04 — Cierre P1 flujos principales](L04-cierre-p1-flujos-principales.md)
