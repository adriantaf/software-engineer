---
id: L13
materia: M13
orden: 13
titulo: Plantilla ADR y decisiones de diseño
horas: 5.0
semana: 4
lectura: Plantilla ADR M01; índice de decisiones pendientes
evidencia: adr/README.md índice + plantilla reutilizable
---

# L13 — Plantilla ADR y decisiones de diseño

**~5.0 h · Semana 4**

Semana de decisiones. Hoy ordenas el proceso para no improvisar en M17.

## Objetivo

Índice de ADRs + plantilla; lista de decisiones que faltan (persistencia, auth, tenant).

## Pasos (hazlos en orden)

### 1. Plantilla (30–40 min)

`projects/m13-diseno/adr/PLANTILLA.md` con secciones Contexto / Decisión / Consecuencias / Alternativas rechazadas.

### 2. Índice (40–50 min)

`adr/README.md`:

| ADR | Título | Estado |
|-----|--------|--------|
| 001 | Monolito modular | Aceptado |
| 002 | Persistencia | Borrador L14 |
| 003 | Auth/sesión | Borrador L16 |
| 004 | Extensibilidad tenant | Nota L15 |

### 3. Backlog de decisiones (50–60 min)

Lista 5 preguntas abiertas (¿ORM?, ¿calcula fin el server?, ¿soft-delete pedidos?).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/adr
git commit -m "docs(m13): indice ADR y plantilla"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | ADR: contexto, decisión, consecuencias; índice vivo | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `adr/README.md` lista ADR 001 y placeholders 002–004 con estado.
2. Existe `adr/PLANTILLA.md` (o equivalente) copiable.
3. Commit `docs(m13): indice ADR y plantilla`.

## Errores comunes

- ADRs de 3 líneas sin consecuencias.
- Decisiones en chats/Discord sin archivo.
- Índice que no enlaza archivos reales.

## Siguiente

[L14 — ADR persistencia y modelo de datos](L14-adr-persistencia-y-modelo-de-datos.md)
