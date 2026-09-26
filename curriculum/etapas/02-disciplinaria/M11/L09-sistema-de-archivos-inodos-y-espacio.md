---
id: L09
materia: M11
orden: 9
titulo: Sistema de archivos: inodos y espacio
horas: 5
semana: 3
lectura: "Silberschatz sistema de archivos"
evidencia: "labs/semana-03-fs.md"
---

# L09 — Sistema de archivos: inodos y espacio

**~5 h · Semana 3**

## Objetivo

Usar `df` y `du` para localizar consumo; explicar inodo y nombre.

## Por qué importa

Logs de API y backups llenan disco antes que CPU.

## Conceptos

- inodo.
- df vs du.
- Enlaces duros/simbólicos (idea).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
df -h
du -sh projects/* 2>/dev/null | sort -h | tail
```

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l09 sistema-de-archivos-inodos-y-espacio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Sistema de archivos | man df/du |

## Hecho cuando

1. Salida df/du comentada.
2. Riesgo logs Agenda Ops.
3. Plan rotación (L11).

## Errores comunes

- Borrar datos sin backup.
- Ignorar inodos agotados.

## Siguiente

[L10 — Permisos, usuarios y mínimo privilegio](L10-permisos-usuarios-y-minimo-privilegio.md)
