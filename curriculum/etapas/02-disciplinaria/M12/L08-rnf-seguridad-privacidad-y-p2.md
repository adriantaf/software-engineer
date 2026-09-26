---
id: L08
materia: M12
orden: 8
titulo: RNF seguridad, privacidad y P2
horas: 5
semana: 2
lectura: "Plantilla RNF + hilo seguridad"
evidencia: "stories.md + srs-borrador RNF"
---

# L08 — RNF seguridad, privacidad y P2

**~5 h · Semana 2**

## Objetivo

Definir ≥3 RNF numerados (SEC/PRIV) trazables a stories.

## Por qué importa

P2 y P3 dependen de RNF explícitos.

## Conceptos

- RNF.
- PII mínimo.
- auditoría.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

RNF-SEC/PRIV en borrador SRS. Cada RNF enlaza a ≥1 story.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l08 rnf-seguridad-privacidad-y-p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Hilo | seguridad.md | plantilla |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. ≥3 RNF seguridad/privacidad.
2. Trazabilidad.
3. P2 listo.

## Errores comunes

- RNF genéricos.
- Sin criterio de prueba futuro.

## Siguiente

[L09 — Alcance MVP y MoSCoW](L09-alcance-mvp-y-moscow.md)
