---
id: L06
materia: M11
orden: 6
titulo: Observar RSS y CPU de Node
horas: 5
semana: 2
lectura: "man ps, top/htop"
evidencia: "labs/rss-node.md"
---

# L06 — Observar RSS y CPU de Node

**~5 h · Semana 2**

## Objetivo

Medir RSS/CPU de un proceso Node bajo carga ligera (script bucle + servidor).

## Por qué importa

Sin baseline no sabes si un leak es real.

## Conceptos

- RSS vs VSZ.
- %CPU.
- Carga sintética.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
node -e "setInterval(()=>{},1000)"
# en otra terminal: ps -o pid,rss,cmd -p <pid>
```

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l06 observar-rss-y-cpu-de-node"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Memoria | htop tutorial |

## Hecho cuando

1. Captura antes/después carga.
2. Números con unidades.
3. Interpretación honesta.

## Errores comunes

- Un solo snapshot.
- Confundir heap JS con RSS total.

## Siguiente

[L07 — OOM, ulimit y síntomas](L07-oom-ulimit-y-sintomas.md)
