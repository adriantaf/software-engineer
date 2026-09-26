---
id: L18
materia: M17
orden: 18
titulo: Botón enviar recordatorio desde ficha cita
horas: 5
semana: 5
lectura: "UI + API log"
evidencia: "acción recordatorio"
---

# L18 — Botón enviar recordatorio desde ficha cita

**~5 h · Semana 5**

## Objetivo

En UI de cita, acción que abre WhatsApp o registra intento según diseño.

## Por qué importa

Cierra loop operativo del negocio.

## Conceptos

- acción usuario.
- auditoría ligera.
- opt-in.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementación + test manual documentado. Log sin PII completa.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l18 boton-enviar-recordatorio-desde-ficha-ci"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m14 | notificador | — |

## Hecho cuando

1. Acción en UI.
2. Log sanitizado.
3. Test manual pasos.

## Errores comunes

- Spam sin confirmación.
- Log con teléfono.

## Siguiente

[L19 — Confirmación de cita y estados](L19-confirmacion-de-cita-y-estados.md)
