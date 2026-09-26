---
id: L17
materia: M10
orden: 17
titulo: "Superficie de ataque: endpoints y datos"
horas: 5.0
semana: 5
lectura: Hilo seguridad + ficha M10 proyecto
evidencia: superficie/endpoints.md (P3 inicio)
---

# L17 — Superficie de ataque: endpoints y datos

**~5.0 h · Semana 5**

P3 empieza aquí: inventarias antes de endurecer (M18).

## Objetivo

Completar el mapa de superficie del piloto Agenda Ops (aunque sea diseño).

## Pasos

### 1. Plantilla (30 min)

```bash
mkdir -p projects/m10-redes/superficie
```

Crea `endpoints.md` con columnas: método, path, auth, roles, datos, notas.

### 2. Inventario (90 min)

Incluye al menos: login/logout, CRUD clientes, CRUD citas, listados, health `/health`, estáticos del panel. Marca PII (teléfono, notas privadas).

### 3. Trust boundaries (40 min)

Mermaid o ASCII: User Agent → TLS → API → PG; backups; logs. Qué cruza cada frontera.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/superficie
git commit -m "docs(m10): l17 superficie endpoints"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Inventario de endpoints, auth, datos sensibles y trust boundaries | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `superficie/endpoints.md` lista endpoints previstos (citas/clientes/auth) + auth + PII.
2. Diagrama trust boundary: browser / API / DB / backups.
3. Commit `docs(m10): l17 superficie endpoints`.

## Errores comunes

- Inventario vacío “porque aún no hay código”.
- Olvidar admin, healthchecks, webhooks.
- Marcar todo como “público”.

## Siguiente

[L18 — Cliente y servidor TCP mínimo (P2)](L18-cliente-y-servidor-tcp-minimo-p2.md)
