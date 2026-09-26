---
id: L01
materia: M11
orden: 1
titulo: Procesos, permisos y bitácora día 1
horas: 5
semana: 1
lectura: "Silberschatz — procesos (intro)"
evidencia: "projects/m11-so/labs/dia1-comandos.md"
---

# L01 — Procesos, permisos y bitácora día 1

**~5 h · Semana 1**

## Objetivo

Documentar procesos en ejecución, identidad (`id`, `umask`) y permisos mínimos en un archivo de prueba.

## Por qué importa

El piloto Agenda Ops correrá en un VPS o contenedor; sin lectura de procesos no diagnosticas incidentes.

## Conceptos

- PID, PPID.
- Usuario efectivo vs real.
- Permisos rwx.
- umask.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m11-so/labs
ps aux | head
id; umask
echo secreto > /tmp/m11-test-$USER.txt && chmod 600 /tmp/m11-test-$USER.txt && ls -la /tmp/m11-test-$USER.txt
```
Explica por qué `chmod 777` es mala idea en datos de clientes.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l01 procesos-permisos-y-bitacora-dia-1"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Procesos | man ps, chmod |

## Hecho cuando

1. `dia1-comandos.md` ≥10 líneas con salida.
2. Archivo 600 creado.
3. Párrafo anti-777.

## Errores comunes

- Correr todo como root por comodidad.
- Subir secretos en la bitácora.

## Siguiente

[L02 — Proceso vs hilo y el runtime Node](L02-proceso-vs-hilo-y-el-runtime-node.md)
