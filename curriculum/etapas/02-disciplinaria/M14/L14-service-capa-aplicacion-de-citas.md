---
id: L14
materia: M14
orden: 14
titulo: Service — capa aplicación de citas
horas: 5
semana: 4
lectura: "Service layer + casos de uso"
evidencia: "projects/m14-patrones/src/cita-service.ts"
---

# L14 — Service — capa aplicación de citas

**~5 h · Semana 4**

## Objetivo

Implementar `CitaService` que use Repository y publique eventos (Observer de L09).

## Por qué importa

Orquesta reglas sin conocer HTTP ni SQL.

## Conceptos

- Service.
- caso de uso.
- transacción futura.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Service crea cita con validación de horario. Test con repo memoria + fake event bus.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l14 service-capa-aplicacion-de-citas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m13-diseno | capas | — |

## Hecho cuando

1. Service con tests.
2. Reglas no en controller.
3. Enlace a Repository.

## Errores comunes

- God service.
- Validación solo en front.

## Siguiente

[L15 — Refactor P3 — módulo legacy antes y después](L15-refactor-p3-modulo-legacy-antes-y-despues.md)
