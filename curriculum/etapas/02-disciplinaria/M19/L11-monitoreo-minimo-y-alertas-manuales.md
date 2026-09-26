---
id: L11
materia: M19
orden: 11
titulo: Monitoreo mínimo y alertas manuales
horas: 5
semana: 3
lectura: "Uptime básico"
evidencia: "projects/m19-ops/monitoring.md"
---

# L11 — Monitoreo mínimo y alertas manuales

**~5 h · Semana 3**

## Objetivo

Configurar healthcheck externo o calendario de revisión manual; definir qué hacer si cae.

## Por qué importa

No necesitas Datadog para el piloto; sí necesitas saber si está caído.

## Conceptos

- uptime
- on-call manual

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

monitoring.md: herramienta o ritual calendario + contacto. Enlaza /health prod.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l11 monitoreo-minimo-y-alertas-manuales"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M19 | — |

## Hecho cuando

1. Monitoreo definido.
2. Contacto.
3. health prod

## Errores comunes

- Asumir siempre up
- Alertas sin acción

## Siguiente

[L12 — Revisión seguridad: puertos, SSH y firewall](L12-revision-seguridad-puertos-ssh-y-firewall.md)
