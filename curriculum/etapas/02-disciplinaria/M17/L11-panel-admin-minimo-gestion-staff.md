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

El dueño del negocio administra su equipo aquí.

## Objetivo

Pantalla admin: listar staff, invitar o crear staff (según SRS), solo owner.

## Conceptos clave

- admin
- invitación
- UX claro

## Pasos (hazlos en orden)

### 1. Ruta /admin mínima (70–90 min)

UI o API: listar staff, invitar/desactivar. Solo owner.

```bash
curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" http://localhost:3000/admin/staff
# 403
```

### 2. Evidencia + commit (40 min)

Anota URL/ruta en `docs/permisos.md` o captura redactada en `docs/`.

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L11 panel admin staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | UI admin sin adornos | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Ruta `/admin` (o equiv.) lista/gestiona staff; staff recibe 403.
2. Commit `docs(m17): L11 panel-admin-minimo-gestion-staff`.

## Errores comunes

- Admin usable por staff.
- Invitar staff sin audit/nota.

## Siguiente

[L12 — Demo roles y inicio P3 WhatsApp](L12-demo-roles-y-inicio-p3-whatsapp.md)
