---
id: L06
materia: M14
orden: 6
titulo: Decorator para logging de operaciones de cita
horas: 5
semana: 2
lectura: "Refactoring.Guru Decorator"
evidencia: "projects/m14-patrones/src/cita-logging-decorator.ts"
---

# L06 — Decorator para logging de operaciones de cita

**~5 h · Semana 2**

## Objetivo

Envolver un servicio de citas con Decorator que registre operaciones sin modificar la clase core.

## Por qué importa

Observabilidad sin ensuciar reglas de negocio.

## Conceptos

- Decorator.
- composición.
- logging estructurado.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementa decorador que loguea `crear`/`cancelar` (sin PII en prod — documenta qué omites). Test: core se invoca.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l06 decorator-para-logging-de-operaciones-de"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Decorator | — |
| Catálogo | Entrada M14 | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

1. Decorator con test.
2. PII no en logs de ejemplo.
3. Commit.

## Errores comunes

- Decorator que cambia comportamiento.
- Logs con teléfono completo.

## Siguiente

[L07 — Facade para el flujo agendar cita](L07-facade-para-el-flujo-agendar-cita.md)
