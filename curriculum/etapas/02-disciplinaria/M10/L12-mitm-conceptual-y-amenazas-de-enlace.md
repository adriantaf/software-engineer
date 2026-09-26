---
id: L12
materia: M10
orden: 12
titulo: MITM conceptual y amenazas de enlace
horas: 5
semana: 3
lectura: "Tanenbaum ataques en red (selecto)"
evidencia: "amenazas-enlace.md en m10-redes"
---

# L12 — MITM conceptual y amenazas de enlace

**~5 h · Semana 3**

## Objetivo

Explicar MITM, downgrade y rogue AP a nivel ingeniero y enlazarlos a controles (TLS, HSTS, no HTTP plano).

## Por qué importa

Esta lección alimenta el documento de amenazas del proyecto y M18.

## Conceptos

- MITM.
- Downgrade TLS.
- HSTS (intro).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Redacta tres escenarios: café Wi‑Fi, DNS comprometido, proxy corporativo. Mitigación por escenario.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l12 mitm-conceptual-y-amenazas-de-enlace"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Tanenbaum | Seguridad en redes | MDN HSTS |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Tres escenarios + mitigación.
2. Enlace a hilo seguridad.
3. Cierre semana 3 en bitácora.

## Errores comunes

- Asumir VPN sustituye TLS end-to-end.
- Mezclar contenido activo HTTP en página HTTPS.

## Siguiente

[L13 — Cookies: atributos y modelo de almacenamiento](L13-cookies-atributos-y-modelo-de-almacenamiento.md)
