---
id: L15
materia: M20
orden: 15
titulo: Timeout, 5xx y mensajes humanos
horas: 5
semana: 4
lectura: "HTTP timeouts"
evidencia: "nota en demo doc"
---

# L15 — Timeout, 5xx y mensajes humanos

**~5 h · Semana 4**

## Objetivo

Configurar timeout cliente; distinguir 5xx de error usuario.

## Por qué importa

No todo es ‘algo salió mal’.

## Conceptos

- timeout
- 5xx

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Prueba timeout bajo artificialmente en dev.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l15 timeout-5xx-y-mensajes-humanos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M20 semana 4 | — |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Timeout configurado
2. 5xx mensaje
3. Log dev sin PII

## Errores comunes

- Sin timeout
- Stack al usuario

## Siguiente

[L16 — AppSec móvil: no loguear PII ni tokens](L16-appsec-movil-no-loguear-pii-ni-tokens.md)
