---
id: L17
materia: M13
orden: 17
titulo: Índice del paquete de diseño
horas: 5.0
semana: 5
lectura: Empaquetar evidencias; README como mapa M17
evidencia: projects/m13-diseno/README.md índice enlazando SRS/diagramas/ADRs
---

# L17 — Índice del paquete de diseño

**~5.0 h · Semana 5**

El proyecto de M13 es el paquete. Hoy el README se vuelve el mapa.

## Objetivo

Reescribir `projects/m13-diseno/README.md` como índice navegable.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

```bash
find projects/m13-diseno -type f -name '*.md' | sort
```

### 2. README índice (80–100 min)

Secciones: En resumen · Enlace SRS · Flujos · Diagramas · Arquitectura · ADRs · Checklist evidencias P1–P3 · Cómo empezar M17.

### 3. Rompe enlaces (20 min)

Haz clic mental: cada ruta relativa debe existir.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/README.md
git commit -m "docs(m13): indice del paquete de diseno"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | README índice del paquete de diseño Agenda Ops | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. README M13 enlaza SRS, casos-de-uso, diagramas, arquitectura y ADRs.
2. Un extraño puede navegar el paquete en ≤10 minutos.
3. Commit `docs(m13): indice del paquete de diseno`.

## Errores comunes

- README genérico de la plantilla sin enlaces.
- Enlaces rotos a archivos que no existen.
- Diagramas huérfanos fuera del índice.

## Siguiente

[L18 — Endpoints y módulos previstos M17](L18-endpoints-y-modulos-previstos-m17.md)
