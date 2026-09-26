---
id: L02
materia: M18
orden: 2
titulo: Trust boundaries y flujos de confianza
horas: 5
semana: 1
lectura: "STRIDE por boundary + M13 `trust-boundaries`"
evidencia: "projects/m18-appsec/trust-boundaries-appsec.md"
---

# L02 — Trust boundaries y flujos de confianza

**~5 h · Semana 1**

## Objetivo

Dibujar límites de confianza (browser, API, DB, integraciones futuras) y etiquetar protocolo + datos que cruzan cada límite.

## Por qué importa

M10 y M13 ya nombraron boundaries; hoy los operacionalizas para amenazas AppSec.

## Conceptos

- Zona de confianza vs desconfianza.
- Datos en tránsito vs en reposo.
- Admin vs tenant (futuro).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Abre `projects/m13-diseno/trust-boundaries.md` si existe. Copia o enlaza y extiende en `projects/m18-appsec/trust-boundaries-appsec.md`.

Por cada límite documenta: **origen**, **destino**, **protocolo**, **autenticación**, **datos**. Mínimo 4 límites (ej. browser→API, API→Postgres, API→SMTP futuro, operador→hosting).

Para cada límite escribe una pregunta “¿qué pasa si el atacante controla este lado?”

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l02 trust-boundaries-y-flujos-de-confianza"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M13 | trust-boundaries | M10 amenazas de red |
| OWASP | STRIDE en boundaries | — |

## Hecho cuando

1. ≥4 boundaries documentados.
2. Pregunta de abuso por límite.
3. Enlace a diseño M13 si aplica.

## Errores comunes

- Un solo boundary “internet”.
- Ignorar Postgres como activo interno.

## Siguiente

[L03 — STRIDE aplicado al CRM de citas](L03-stride-aplicado-al-crm-de-citas.md)
