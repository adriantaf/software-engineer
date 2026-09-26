---
id: L11
materia: M20
orden: 11
titulo: "Acciones permitidas: cancelar / atendida"
horas: 5
semana: 3
lectura: "Mutations HTTP"
evidencia: "commit si API expone"
---

# L11 — Acciones permitidas: cancelar / atendida

**~5 h · Semana 3**

## Objetivo

Llamar PATCH/POST que la API expone; deshabilitar si 403.

## Por qué importa

Solo acciones que el backend autoriza.

## Conceptos

- mutation
- optimistic UI opcional

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Si API no tiene acción, documenta en nota y enlaza issue M17.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l11 acciones-permitidas-cancelar-atendida"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| SRS | historias citas | — |

## Hecho cuando

1. Acción o gap documentado
2. 403 manejado
3. Commit

## Errores comunes

- Reglas negocio solo en app
- Silenciar errores

## Siguiente

[L12 — Deep link opcional a una cita](L12-deep-link-opcional-a-una-cita.md)
