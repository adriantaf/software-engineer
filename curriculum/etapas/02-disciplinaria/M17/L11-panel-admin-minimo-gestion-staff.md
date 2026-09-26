---
id: L11
materia: M17
orden: 11
titulo: Panel admin mínimo — gestión staff
horas: 5.0
semana: 3
lectura: UI admin sin adornos
evidencia: ruta /admin o equivalente
---

# L11 — Panel admin mínimo — gestión staff

**~5.0 h · Semana 3**

El dueño administra su equipo aquí — feo pero claro.

## Objetivo

Ruta admin: listar/crear staff solo owner; `docs/ui-admin.md`.

## Pasos (hazlos en orden)

### 1. API admin si falta (40–50 min)

Endpoints alineados a matriz.

### 2. UI mínima (80–100 min)

Lista + formulario. Errores 403 visibles. Sin CSS hero.

### 3. Doc (20 min)

`docs/ui-admin.md` con pasos de demo.

### 4. Commit

`feat(m17): l11 panel admin staff`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | UI admin sin adornos | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Admin usable (artefacto: `ruta /admin o equivalente`).
2. Owner-only verificado (artefacto: `ruta /admin o equivalente`).
3. ui-admin.md (artefacto: `ruta /admin o equivalente`).
4. Commit `docs(m17): L11 panel-admin-minimo-gestion-staff`.

## Errores comunes

- Admin sin auth.
- Confundir roles.

## Siguiente

[L12 — Demo roles y inicio P3 WhatsApp](L12-demo-roles-y-inicio-p3-whatsapp.md)
