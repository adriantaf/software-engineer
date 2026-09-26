---
id: L03
materia: M14
orden: 3
titulo: "Singleton: cuándo NO usarlo"
horas: 5
semana: 1
lectura: "GoF Singleton + notas anti-patrón"
evidencia: "projects/m14-patrones/adr/002-singleton-rechazado.md"
---

# L03 — Singleton: cuándo NO usarlo

**~5 h · Semana 1**

## Objetivo

Documentar por qué **no** usar Singleton para DB/logger global en Agenda Ops y qué alternativa (DI) usarás en M17.

## Por qué importa

Singleton en tests y multi-tenant es deuda; mejor inyectar dependencias.

## Conceptos

- Singleton.
- estado global.
- inyección de dependencias.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Escribe ADR 002: caso rechazado (p. ej. conexión DB). Lista 3 problemas (tests, tenant, concurrencia). Sin implementar Singleton productivo.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l03 singleton-cuando-no-usarlo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Singleton | Ficha M14 semana 1 |
| Catálogo | Entrada M14 | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

1. ADR 002 con alternativa DI.
2. Enlazado desde README.
3. Commit docs(m14).

## Errores comunes

- Implementar Singleton “porque GoF”.
- ADR sin consecuencias.

## Siguiente

[L04 — Cierre semana 1 — creacionales y bitácora](L04-cierre-semana-1-creacionales-y-bitacora.md)
