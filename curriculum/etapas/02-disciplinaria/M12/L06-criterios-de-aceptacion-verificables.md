---
id: L06
materia: M12
orden: 6
titulo: Criterios de aceptación verificables
horas: 5
semana: 2
lectura: "Given/When/Then intro"
evidencia: "stories.md criterios"
---

# L06 — Criterios de aceptación verificables

**~5 h · Semana 2**

## Objetivo

Añadir criterios numerados o GWT a cada story; incluir 401/403 donde aplique.

## Por qué importa

Seguridad entra aquí, no “luego en M18”.

## Conceptos

- criterio verificable.
- error path.
- permisos.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Al menos 2 stories con criterios de error. Ejemplo notas privadas staff vs owner.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l06 criterios-de-aceptacion-verificables"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | hilo seguridad | ejemplo ficha M12 |

## Hecho cuando

1. Criterios en todas las stories nuevas.
2. ≥2 con error/permiso.
3. Sin “se ve bien”.

## Errores comunes

- Criterios subjetivos.
- Omitir 403 en datos sensibles.

## Siguiente

[L07 — Historias de vacío, duplicados y conflicto](L07-historias-de-vacio-duplicados-y-conflicto.md)
