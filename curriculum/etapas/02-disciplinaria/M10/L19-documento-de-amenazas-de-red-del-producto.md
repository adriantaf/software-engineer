---
id: L19
materia: M10
orden: 19
titulo: Documento de amenazas de red del producto
horas: 5
semana: 5
lectura: "Proyecto M10 README + STRIDE lite (red)"
evidencia: "projects/m10-redes/amenazas-red.md actualizado"
---

# L19 — Documento de amenazas de red del producto

**~5 h · Semana 5**

## Objetivo

Redactar amenazas de red (eavesdropping, session theft, DNS spoofing) con mitigaciones enlazadas a M18/M19.

## Por qué importa

Es el entregable proyecto de la materia y debe ser usable por tu yo de M17.

## Conceptos

- STRIDE a nivel red.
- Mitigación vs aceptación de riesgo.
- Dependencias (CDN, hosting).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Estructura: activo, amenaza, impacto, mitigación, estado. Mínimo 8 entradas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l19 documento-de-amenazas-de-red-del-product"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | Proyecto m10-redes README | Hilo seguridad |

## Hecho cuando

1. `amenazas-red.md` ≥8 entradas.
2. Mitigaciones realistas.
3. README enlaza doc.

## Errores comunes

- Mitigación “usar HTTPS” sin detalle.
- No priorizar por impacto.

## Siguiente

[L20 — Cierre M10 — evidencias y dominio](L20-cierre-m10-evidencias-y-dominio.md)
