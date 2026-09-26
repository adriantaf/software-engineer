---
id: L07
materia: M11
orden: 7
titulo: OOM, ulimit y síntomas
horas: 5
semana: 2
lectura: "Silberschatz OOM + ulimit man"
evidencia: "labs/oom-ulimit.md"
---

# L07 — OOM, ulimit y síntomas

**~5 h · Semana 2**

## Objetivo

Describir qué hace el kernel ante OOM y cómo `ulimit -v` puede limitar (lab opcional controlado).

## Por qué importa

Agenda Ops en VPS 1GB necesita límites y alertas.

## Conceptos

- OOM killer.
- ulimit.
- cgroup memory (preview).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Documenta señales de OOM en logs (sin forzar en prod). Plan: reinicio, límites compose.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l07 oom-ulimit-y-sintomas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Memoria | Docker memory limits doc |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Síntomas OOM listados.
2. Plan mitigación piloto.
3. No ejecutar fork bomb.

## Errores comunes

- Probar fork bomb en máquina compartida.
- Ignorar límites de contenedor.

## Siguiente

[L08 — cgroups y memoria en contenedores](L08-cgroups-y-memoria-en-contenedores.md)
