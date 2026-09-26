---
id: L04
materia: M15
orden: 4
titulo: Cierre semana 1 — suite dominio y bitácora
horas: 5
semana: 1
lectura: "Repaso P1 parcial"
evidencia: "projects/m15-calidad/semana-01.md"
---

# L04 — Cierre semana 1 — suite dominio y bitácora

**~5 h · Semana 1**

## Objetivo

Cerrar semana 1 con bitácora y verificación de que cada regla SRS Must tiene al menos un test.

## Por qué importa

Trazabilidad SRS → test es contrato para M17.

## Conceptos

- trazabilidad.
- Must.
- bitácora.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Matriz story/test en `semana-01.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l04 cierre-semana-1-suite-dominio-y-bitacora"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m12-srs | srs-v1 | — |

## Hecho cuando

1. Matriz story→test.
2. Suite verde.
3. Cierre semana 1.

## Errores comunes

- Tests huérfanos.
- Sin enlace a SRS.

## Siguiente

[L05 — Fake repositorio y reloj para tests rápidos](L05-fake-repositorio-y-reloj-para-tests-rapidos.md)
