---
id: L01
materia: M13
orden: 1
titulo: Trust boundaries y ADR 001
horas: 5
semana: 1
lectura: "Larman + ADR M01"
evidencia: "diagramas/trust-boundaries.md + adr/001"
---

# L01 — Trust boundaries y ADR 001

**~5 h · Semana 1**

## Objetivo

Marcar límites navegador|API|DB y registrar ADR monolito modular.

## Por qué importa

Autorización no vive solo en el front del panel de citas.

## Conceptos

- trust boundary.
- ADR.
- monolito modular.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m13-diseno/diagramas projects/m13-diseno/adr
```
Lee `projects/m12-srs/srs-v1.md` (o borrador) y dibuja tres zonas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l01 trust-boundaries-y-adr-001"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | hilo seguridad | plantilla ADR M01 |

## Hecho cuando

1. trust-boundaries.md.
2. ADR 001.
3. Commit docs(m13).

## Errores comunes

- Microservicios día 1.
- Boundary sin datos que cruzan.

## Siguiente

[L02 — Actores y casos de uso prioritarios](L02-actores-y-casos-de-uso-prioritarios.md)
