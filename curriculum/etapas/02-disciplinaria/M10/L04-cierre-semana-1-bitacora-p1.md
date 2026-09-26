---
id: L04
materia: M10
orden: 4
titulo: Cierre semana 1 — bitácora P1
horas: 5
semana: 1
lectura: "Repaso semana 1 Tanenbaum + ficha M10"
evidencia: "projects/m10-redes/labs/semana-01.md consolidado"
---

# L04 — Cierre semana 1 — bitácora P1

**~5 h · Semana 1**

## Objetivo

Consolidar la bitácora de labs de la semana 1 y enlazar cada experimento a una hipótesis de fallo en producción.

## Por qué importa

P1 exige evidencia continua; hoy cierras la semana con criterio de auditoría, no con notas sueltas.

## Conceptos

- Trazabilidad comando → observación → implicación.
- Hipótesis red vs aplicación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Revisa L01–L03. Une logs en `semana-01.md` con secciones: **Comando**, **Salida clave**, **Qué aprendí**, **Riesgo Agenda Ops**. Añade un mini diagrama DNS→TCP→TLS→HTTP.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l04 cierre-semana-1-bitacora-p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M10-redes.md | — |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. `semana-01.md` ≥4 experimentos documentados.
2. Un riesgo concreto para API futura.
3. Commit de cierre semana 1.

## Errores comunes

- Marcar P1 sin carpeta `labs/`.
- Diagrama copiado sin explicación propia.

## Siguiente

[L05 — DNS: resolución, registros y fallos](L05-dns-resolucion-registros-y-fallos.md)
