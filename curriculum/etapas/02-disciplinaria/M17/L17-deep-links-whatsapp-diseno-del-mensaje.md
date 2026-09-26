---
id: L17
materia: M17
orden: 17
titulo: Deep links WhatsApp — diseño del mensaje
horas: 5
semana: 5
lectura: "Docs proveedor WhatsApp"
evidencia: "projects/m17-agenda-ops/docs/integracion-whatsapp.md"
---

# L17 — Deep links WhatsApp — diseño del mensaje

**~5 h · Semana 5**

## Objetivo

Definir plantilla mensaje recordatorio/confirmación con placeholders y enlace wa.me.

## Por qué importa

Canal que el design partner ya usa.

## Conceptos

- deep link.
- plantilla.
- PII mínima.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

integracion-whatsapp.md: ejemplo URL encoded, qué datos van (nombre cita, hora).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l17 deep-links-whatsapp-diseno-del-mensaje"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Oficial | WhatsApp Business | — |

## Hecho cuando

1. Doc plantilla.
2. Sin secrets.
3. Commit.

## Errores comunes

- API keys en front.
- Teléfono en logs.

## Siguiente

[L18 — Botón enviar recordatorio desde ficha cita](L18-boton-enviar-recordatorio-desde-ficha-cita.md)
