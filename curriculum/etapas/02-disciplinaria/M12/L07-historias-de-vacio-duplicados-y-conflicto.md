---
id: L07
materia: M12
orden: 7
titulo: Historias de vacío, duplicados y conflicto
horas: 5
semana: 2
lectura: "Casos borde negocio citas"
evidencia: "stories.md ampliado"
---

# L07 — Historias de vacío, duplicados y conflicto

**~5 h · Semana 2**

## Objetivo

Cubrir sin citas, cliente duplicado, horario inválido, doble reserva.

## Por qué importa

El MVP falla en borde si solo happy path.

## Conceptos

- caso borde.
- idempotencia.
- mensaje usuario.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥4 stories adicionales (total acumulado ≥8). Prioriza Must.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l07 historias-de-vacio-duplicados-y-conflict"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plantilla | reglas negocio | — |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. ≥8 stories total.
2. Bordes cubiertos.
3. Mapa story→SRS.

## Errores comunes

- Duplicar stories sin criterio.
- Ignorar zona horaria.

## Siguiente

[L08 — RNF seguridad, privacidad y P2](L08-rnf-seguridad-privacidad-y-p2.md)
