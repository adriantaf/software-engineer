---
id: L05
materia: M14
orden: 5
titulo: Adapter para API de calendario externo
horas: 5
semana: 2
lectura: "Refactoring.Guru Adapter"
evidencia: "projects/m14-patrones/src/calendario-adapter.ts"
---

# L05 — Adapter para API de calendario externo

**~5 h · Semana 2**

## Objetivo

Adaptar una interfaz ficticia de calendario externo a tu puerto de dominio `CalendarioPuerto`.

## Por qué importa

Integraciones reales (Google Calendar luego) exigen Adapter, no ifs en el servicio de citas.

## Conceptos

- Adapter.
- puerto.
- librería terceros.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Define puerto dominio + adapter que traduce tipos/fechas. Test: el dominio solo ve tu interfaz.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l05 adapter-para-api-de-calendario-externo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Adapter | — |

## Hecho cuando

1. Adapter + test de traducción.
2. Dominio sin import de SDK.
3. ADR o nota en README.

## Errores comunes

- Copiar tipos del SDK al dominio.
- Adapter que re-lanza errores crudos.

## Siguiente

[L06 — Decorator para logging de operaciones de cita](L06-decorator-para-logging-de-operaciones-de-cita.md)
