---
id: L05
materia: M11
orden: 5
titulo: Memoria virtual y paginación (intuición)
horas: 5
semana: 2
lectura: "Silberschatz — memoria virtual"
evidencia: "labs/semana-02-memoria.md"
---

# L05 — Memoria virtual y paginación (intuición)

**~5 h · Semana 2**

## Objetivo

Explicar espacio de direcciones virtual, paginación y por qué un proceso cree tener memoria contigua.

## Por qué importa

OOM y swapping en un VPS pequeño tumbarán el piloto si no observas RSS.

## Conceptos

- MMU.
- Page fault (idea).
- Swap.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Lee capítulo y dibuja proceso → tablas de páginas → RAM. Relaciona con contenedor (L08).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l05 memoria-virtual-y-paginacion-intuicion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Memoria virtual | Artículos OS notes |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Diagrama virtual→físico.
2. Glosario 5 términos.
3. Hipótesis OOM.

## Errores comunes

- Pensar que `free` miente siempre igual.
- Ignorar swap lleno.

## Siguiente

[L06 — Observar RSS y CPU de Node](L06-observar-rss-y-cpu-de-node.md)
