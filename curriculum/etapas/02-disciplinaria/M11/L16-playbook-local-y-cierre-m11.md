---
id: L16
materia: M11
orden: 16
titulo: Playbook local y cierre M11
horas: 5.0
semana: 4
lectura: Ficha M11 completa
evidencia: playbook.md + cierre P1–P3
---

# L16 — Playbook local y cierre M11

**~5.0 h · Semana 4**

Otro desarrollador debe levantar el stack solo con tu playbook.

## Objetivo

Publicar `playbook.md` y cerrar evidencias P1–P3.

## Pasos

### 1. Redacta playbook (90–110 min)

`projects/m11-so/playbook.md`:

- Prerequisitos (Docker, puertos)
- `cp .env.example .env` + editar
- `docker compose up -d --build`
- Healthcheck curl
- Backup (`scripts/backup.sh`)
- Restore de prueba (enlace)
- `docker compose down`
- Diagrama Mermaid host → api/db → volume

### 2. Dry-run (50 min)

Sigue el playbook desde cero (borra contenedores) y anota fricciones; corrígelas.

### 3. Checklist dominio (30 min)

Responde en `dominio-oral.md`: SIGTERM, backup+restore, non-root, playbook ajeno.

### 4. Commit (15 min)

```bash
git add projects/m11-so
git commit -m "docs(m11): cierre playbook"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES) | Playbook reproducible: up/down/backup/restore | [Node.js process](https://nodejs.org/api/process.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

Marca la lección **solo si**:

1. `playbook.md` con prerequisitos, up/down, backup, restore, troubleshooting.
2. README enlaza P1 labs, P2 scripts, P3 Docker, playbook.
3. Commit `docs(m11): cierre playbook`.

## Errores comunes

- Playbook que solo funciona en tu cabeza.
- Secretos en el playbook.
- Marcar dominio sin restore documentado.

## Siguiente

Cierra la [ficha M11](../M11-sistemas-operativos.md). Recomendado: [M27](../M27-sistemas-bajo-nivel.md) o sigue a [M12](../M12-requerimientos.md).
