---
id: L01
materia: M14
orden: 1
titulo: Entorno M14 y Strategy de precios
horas: 5
semana: 1
lectura: "Refactoring.Guru Factory + Strategy (ES)"
evidencia: "projects/m14-patrones/src/precio-strategy.ts + adr/001"
---

# L01 — Entorno M14 y Strategy de precios

**~5 h · Semana 1**

## Objetivo

Preparar `projects/m14-patrones/` e implementar **Strategy** para precio de servicio (base vs promoción) con tests.

## Por qué importa

Los precios en Agenda Ops cambiarán; Strategy evita `if (promo)` esparcidos.

## Conceptos

- Strategy.
- interfaz pequeña.
- tests de comportamiento.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m14-patrones/src projects/m14-patrones/adr
```
Implementa `CalculoPrecio` y al menos dos estrategias (tarifa base, promo 10%). Vitest: caso normal y promo.
ADR `001-strategy-precio.md`: contexto, decisión, **cuándo NO** usar Strategy aquí.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l01 entorno-m14-y-strategy-de-precios"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Strategy | GoF creacionales intro |

## Hecho cuando

1. Strategy con ≥2 tests verdes.
2. ADR 001 commiteado.
3. README enlaza archivo.

## Errores comunes

- Clase Strategy vacía.
- Tests que mockean todo.

## Siguiente

[L02 — Factory Method para notificadores de canal](L02-factory-method-para-notificadores-de-canal.md)
