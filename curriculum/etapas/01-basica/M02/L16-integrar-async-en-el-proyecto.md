---
id: L16
materia: M02
orden: 16
titulo: Integrar async en el proyecto
horas: 3
semana: 4
lectura: "Repaso cap. 11 EJ + revisión load/save CLI"
evidencia: "m02-habits estable async + nota semana 4 en bitácora"
---

# L16 — Integrar async en el proyecto

**~3 h · Semana 4**

Cierras la semana 4 consolidando async en la CLI, corrigiendo race conditions obvias y completando katas hasta **20** (P1).

## Objetivo

CLI estable con flujo async completo; repo katas con **≥20** soluciones P1 listas para marcar.

## Por qué importa

P1 y la CLI comparten semanas 3–4. Hoy cierras el canon de katas y dejas async sin deuda técnica grave.

## Pasos

### 1. Auditoría async CLI (45 min)

Revisa cada comando: ¿siempre `await saveEstado`? ¿`main` captura errores? Añade prueba manual documentada en README habits.

### 2. Completar P1 katas (90 min)

Hasta **20** archivos en `src/katas/` o carpeta `katas/` documentada. README lista títulos y dificultad.

### 3. Refactor menor (30 min)

Extrae cualquier función >40 líneas del cli a `src/servicios/`.

### 4. Retro semana 4 (25 min)

Bitácora: fetch usado, async explicado a un compañero imaginario en 3 frases.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Repaso cap. 11 |

## Hecho cuando

1. ≥20 katas con README (P1 lista para evidencia).
2. CLI habits async sin errores silenciosos en prueba manual.
3. Commits de la semana 4 agrupados con sentido.

## Errores comunes

- Marcar P1 con 12 katas “casi”.
- Duplicar lógica entre katas y CLI en vez de reutilizar ideas.
- Ignorar JSON corrupto (lo atacas en L17).

## Siguiente

[L17 — Errores, throw y mensajes](L17-errores-throw-y-mensajes.md)
