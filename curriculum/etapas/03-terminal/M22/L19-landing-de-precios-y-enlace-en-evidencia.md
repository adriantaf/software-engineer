---
id: L19
materia: M22
orden: 19
titulo: Landing de precios y enlace en evidencia
horas: 5
semana: 5
lectura: "producto-saas — página precios"
evidencia: "projects/m22-bektor/landing-precios.md"
---

# L19 — Landing de precios y enlace en evidencia

**~5 h · Semana 5**

## Objetivo

Publicar o enlazar landing estática de precios (repo producto o página) y documentar URL en evidencia.

## Por qué importa

M26 conectará Stripe; hoy el dueño debe **ver** números fuera de un MD privado.

## Conceptos

- Landing.
- URL pública.
- Coherencia pricing.md.
- CTA trial.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m22-bektor/landing-precios.md` con URL HTTPS, captura o commit del HTML/ruta.

Debe coincidir con `projects/m22-bektor/pricing.md`. Anota fecha verificación.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m22): l19 landing-de-precios-y-enlace-en-evidencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M19 | deploy estático | ../../../producto-saas.md |
| Catálogo | Entrada M22 | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

1. URL pública.
2. Coherencia pricing.
3. Fecha verificación.

## Errores comunes

- Solo MD privado.
- Precios distintos web vs doc.

## Siguiente

[L20 — Pivote Bektor → Agenda Ops — narrativa completa](L20-pivote-bektor-agenda-ops-narrativa-completa.md)
