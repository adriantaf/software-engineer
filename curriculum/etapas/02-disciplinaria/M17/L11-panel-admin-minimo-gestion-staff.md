---
id: L11
materia: M17
orden: 11
titulo: Panel admin mínimo — gestión staff
horas: 5
semana: 3
lectura: "UI admin sin adornos"
evidencia: "ruta /admin o equivalente"
---

# L11 — Panel admin mínimo — gestión staff

**~5 h · Semana 3**

## Objetivo

Pantalla admin: listar staff, invitar o crear staff (según SRS), solo owner.

## Por qué importa

El dueño del negocio administra su equipo aquí.

## Conceptos

- admin.
- invitación.
- UX claro.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

UI fea pero clara. Errores 403 visibles. Notas en `docs/ui-admin.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l11 panel-admin-minimo-gestion-staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m16 | handoff UX | — |

## Hecho cuando

1. Admin usable.
2. Owner-only verificado.
3. ui-admin.md.

## Errores comunes

- Admin sin auth.
- Confundir roles.

## Siguiente

[L12 — Demo roles y inicio P3 WhatsApp](L12-demo-roles-y-inicio-p3-whatsapp.md)
