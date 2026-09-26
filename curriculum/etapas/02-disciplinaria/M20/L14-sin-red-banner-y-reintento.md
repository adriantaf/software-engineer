---
id: L14
materia: M20
orden: 14
titulo: Sin red: banner y reintento
horas: 5
semana: 4
lectura: "Connectivity plugins"
evidencia: "captura offline"
---

# L14 — Sin red: banner y reintento

**~5 h · Semana 4**

## Objetivo

Detectar offline o fallo DNS; banner y botón reintentar.

## Por qué importa

Dueño en campo pierde señal a menudo.

## Conceptos

- offline
- retry

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Simula modo avión; documenta comportamiento.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l14 sin-red-banner-y-reintento"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docs | connectivity | — |

## Hecho cuando

1. Modo avión probado
2. Reintento
3. Captura

## Errores comunes

- Crash sin red
- Loop infinito retry

## Siguiente

[L15 — Timeout, 5xx y mensajes humanos](L15-timeout-5xx-y-mensajes-humanos.md)
