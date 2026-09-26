---
id: L03
materia: M16
orden: 3
titulo: Estados vacío, carga y error en agenda
horas: 5
semana: 1
lectura: "Krug formularios + estados UI"
evidencia: "projects/m16-ihc/heuristicas/estados-ui.md"
---

# L03 — Estados vacío, carga y error en agenda

**~5 h · Semana 1**

## Objetivo

Diseñar o auditar estados vacío/carga/error en lista de citas y formulario.

## Por qué importa

Agenda vacía el primer día es normal; error de red no debe ser pantalla blanca.

## Conceptos

- empty state.
- loading.
- error recovery.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Mockups o capturas en `estados-ui.md`. Propuesta de copy en español claro.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m16): l03 estados-vacio-carga-y-error-en-agenda"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m17 | ui-estados futuro | m12 stories |

## Hecho cuando

1. 3 estados documentados.
2. Copy propuesto.
3. Commit.

## Errores comunes

- Spinner infinito.
- Error técnico crudo.

## Siguiente

[L04 — auditoria-v1 y cierre P1 heurísticas](L04-auditoria-v1-y-cierre-p1-heuristicas.md)
