---
id: L07
materia: M14
orden: 7
titulo: Facade para el flujo agendar cita
horas: 5
semana: 2
lectura: "Refactoring.Guru Facade"
evidencia: "projects/m14-patrones/src/agendar-cita-facade.ts"
---

# L07 — Facade para el flujo agendar cita

**~5 h · Semana 2**

## Objetivo

Crear Facade `agendarCita` que coordine validación, persistencia (fake) y evento.

## Por qué importa

El panel y la API de M17 necesitan un punto de entrada claro, no seis llamadas sueltas.

## Conceptos

- Facade.
- orquestación.
- caso de uso.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Facade con dependencias inyectadas (repos fake). Test happy path y error de solapamiento.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l07 facade-para-el-flujo-agendar-cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m13-diseno | secuencia crear cita | — |

## Hecho cuando

1. Facade + 2 tests.
2. Alineado a caso de uso M13.
3. Nota en README.

## Errores comunes

- Facade con SQL dentro.
- Sin test de error.

## Siguiente

[L08 — Tests de regresión en API pública del módulo](L08-tests-de-regresion-en-api-publica-del-modulo.md)
