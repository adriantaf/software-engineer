---
id: L20
materia: M10
orden: 20
titulo: Cierre M10 — evidencias y dominio
horas: 5.0
semana: 5
lectura: Ficha M10 completa
evidencia: checklist P1–P3 + proyecto verificados
---

# L20 — Cierre M10 — evidencias y dominio

**~5.0 h · Semana 5**

Cierras la materia como ingeniero: evidencia en git + dominio oral.

## Objetivo

Auditar P1–P3/proyecto y dejar el README listo para revisión.

## Pasos

### 1. Auditoría (60 min)

```bash
find projects/m10-redes -type f | sort
```

Verifica: labs semana 1–4, tls/certs, cookies/cors/headers, `tcp-echo/`, `superficie/`, `amenazas-red.md`.

### 2. Criterios de dominio (60 min)

Escribe en `projects/m10-redes/dominio-oral.md` respuestas a:

1. Depurar un timeout (red vs app)
2. Explicar TLS sin “magia”
3. Defender tu mapa de superficie

### 3. README final (40 min)

Checklist con casillas marcadas y rutas exactas.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): cierre materia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Auditoría de evidencia y criterios de dominio de la ficha | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist P1 labs, P2 tcp-echo, P3 superficie, proyecto amenazas — todo enlazado en README.
2. Auto-respuesta escrita a los 3 criterios de dominio de la ficha M10.
3. Commit `docs(m10): cierre materia`.

## Errores comunes

- Marcar dominio sin poder explicar TLS en voz alta.
- Evidencia solo en la cabeza / Discord.
- Dejar `tcp-echo` sin README de uso.

## Siguiente

Cierra la [ficha M10](../M10-redes.md). Siguiente: [M11 — Sistemas operativos](../M11-sistemas-operativos.md).
