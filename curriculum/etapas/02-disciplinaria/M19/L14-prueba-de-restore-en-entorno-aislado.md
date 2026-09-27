---
id: L14
materia: M19
orden: 14
titulo: Prueba de restore en entorno aislado
horas: 5.0
semana: 4
lectura: Restore docs
evidencia: projects/m19-ops/restore-test.md
---

# L14 — Prueba de restore en entorno aislado

**~5.0 h · Semana 4**

Un restore nunca probado no cuenta.

## Objetivo

Restaurar dump en DB de prueba, verificar pedidos visibles, registrar tiempo y resultado.

## Conceptos clave

- restore
- RTO idea
- vacuum

## Pasos (hazlos en orden)

### 1. Restore aislado (80–100 min)

```bash
# entorno scratch — NO prod
createdb agenda_restore_test || true
gunzip -c backups/agenda-XXXX.sql.gz | psql "postgresql://…/agenda_restore_test"
psql "postgresql://…/agenda_restore_test" -c 'SELECT count(*) FROM pedidos;'
```

### 2. restore-test.md (30–40 min)

```bash
cat > projects/m19-ops/restore-test.md << 'EOF'
# Restore test
Fecha: YYYY-MM-DD
Dump usado: agenda-….sql.gz
Destino: DB aislada …
Resultado: OK — count pedidos = N
EOF
git add projects/m19-ops/restore-test.md
git commit -m "docs(m19): L14 prueba restore aislado"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Restore docs | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/restore-test.md` con fecha, dump usado y resultado real.
2. Commit `docs(m19): L14 prueba-de-restore-en-entorno-aislado`.

## Errores comunes

- Restore probado en prod.
- Afirmar OK sin `SELECT count`.

## Siguiente

[L15 — Runbook completo de producción](L15-runbook-completo-de-produccion.md)
