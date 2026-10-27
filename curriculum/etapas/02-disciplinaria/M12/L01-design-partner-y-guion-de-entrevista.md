---
id: L01
materia: M12
orden: 1
titulo: Design partner y guion de entrevista
horas: 5.0
semana: 1
lectura: plantilla.md + producto-saas.md
evidencia: entrevistas/guion-v1.md
---

# L01 — Design partner y guion de entrevista

**~5.0 h · Semana 1**

Vitrina empieza con un problema real, no con Figma. Hoy eliges partner y guion.

## Objetivo

Fijar sub-vertical + `guion-v1.md` listo para una entrevista real o simulada seria.

## Pasos (hazlos en orden)

### 1. Scaffold (15 min)

```bash
mkdir -p projects/m12-srs/entrevistas
cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
cat projects/m12-srs/README.md
```

### 2. Producto e ICP (45–60 min)

Lee [producto-saas.md](../../../producto-saas.md). En `entrevistas/guion-v1.md` escribe:

- Sub-vertical (ej. barbería / consultorio / taller) — **uno**
- Ciudad/contexto
- Nombre o rol del design partner (puede ser anónimo)
- Qué herramientas usa hoy (WhatsApp, libreta, Excel…)

### 3. Guion ≥10 preguntas (75–90 min)

Categorías obligatorias:

1. Flujo de una pedido de punta a punta
2. No-shows y recordatorios
3. Datos de clientes que guardan (PII)
4. Quién agenda (dueño vs staff)
5. Dolores de cobro / adelantos (sin diseñar pagos aún)
6. Qué **no** quieren automatizar

Regla: preguntas abiertas (“cuéntame…”, “¿qué pasa cuando…?”).

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l01 guion entrevista"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | ICP, design partner, alcance piloto single-tenant Vitrina | [producto-saas.md](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Sub-vertical elegido y escrito (no se cambia en M12).
2. `entrevistas/guion-v1.md` con ≥10 preguntas abiertas (flujo pedidos, pedido abandonados, datos sensibles).
3. Commit `docs(m12): l01 guion entrevista`.

## Errores comunes

- Empezar por pantallas UI.
- Preguntas cerradas tipo “¿te gustaría una app?”.
- Cambiar de barbería a clínica a mitad de semana.

## Siguiente

[L02 — Entrevista y notas timestamp](L02-entrevista-y-notas-timestamp.md)
