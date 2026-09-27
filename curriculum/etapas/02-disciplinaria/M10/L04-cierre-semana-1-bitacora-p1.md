---
id: L04
materia: M10
orden: 4
titulo: Cierre semana 1 — bitácora P1
horas: 5.0
semana: 1
lectura: Repaso semana 1 Tanenbaum + ficha M10
evidencia: projects/m10-redes/labs/semana-01.md consolidado (P1)
---

# L04 — Cierre semana 1 — bitácora P1

**~5.0 h · Semana 1**

P1 es bitácora reproducible. Hoy la dejas legible para tu yo de la semana 5.

## Objetivo

Consolidar evidencia de capas/IP/TCP y actualizar el README del proyecto.

## Pasos

### 1. Auditoría de archivos (30 min)

```bash
find projects/m10-redes -type f | sort
```

Mueve notas sueltas a `labs/` si hace falta.

### 2. Consolida `semana-01.md` (90–120 min)

Estructura mínima:

```markdown
# Semana 1 — Capas, IP, TCP/UDP
## Índice
## Capas + curl (L01)
## IP / ruta (L02)
## Puertos Vitrina (L03)
## Pendientes
```

Copia fragmentos **anotados** (no dumps enteros).

### 3. README (45 min)

En `projects/m10-redes/README.md`, sección “Semana 1”:

- [x] dia1 + curl log
- [x] IP/gateway/traceroute
- [x] tabla puertos

### 4. Auto-quiz (30 min)

Responde por escrito (5–8 líneas c/u): (a) qué protege TLS vs qué no; (b) por qué 5432 no va a internet; (c) triage timeout.

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l04 cierre semana 1 bitacora"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Síntesis capas + IP + transporte; checklist P1 parcial | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-01.md` unifica L01–L03 con índice y enlaces a logs.
2. README de m10 marca “Semana 1 / P1 parcial” con checklist.
3. Commit `docs(m10): l04 cierre semana 1 bitacora`.

## Errores comunes

- Tres archivos sueltos sin índice.
- Checklist vacía (“luego documento”).
- Commit sin `labs/`.

## Siguiente

[L05 — DNS: resolución, registros y fallos](L05-dns-resolucion-registros-y-fallos.md)
