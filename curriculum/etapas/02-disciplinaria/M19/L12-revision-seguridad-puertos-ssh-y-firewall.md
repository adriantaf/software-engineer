---
id: L12
materia: M19
orden: 12
titulo: "Revisión seguridad: puertos, SSH y firewall"
horas: 5
semana: 3
lectura: "M18 + M11 seguridad host"
evidencia: "projects/m19-ops/security-host.md"
---

# L12 — Revisión seguridad: puertos, SSH y firewall

**~5 h · Semana 3**

## Objetivo

Checklist puertos expuestos, SSH (clave, no password), firewall si VPS.

## Por qué importa

Deploy sin postura de host revierte M18.

## Conceptos

- firewall
- SSH
- least privilege

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

security-host.md checklist. Si PaaS, documenta qué gestiona el proveedor vs tú.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l12 revision-seguridad-puertos-ssh-y-firewal"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Hilo | seguridad | M18 |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. Checklist completo.
2. SSH seguro o N/A PaaS.
3. Sin Postgres público.

## Errores comunes

- SSH password root
- 22 abierto al mundo sin necesidad

## Siguiente

[L13 — Backup automático PostgreSQL](L13-backup-automatico-postgresql.md)
