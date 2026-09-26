---
id: L14
materia: M18
orden: 14
titulo: "Mitigar SQLi: queries parametrizadas y permisos DB"
horas: 5.0
semana: 4
lectura: SQLi Prevention Cheat Sheet
evidencia: commit fix + test en repo producto
---

# L14 — Mitigar SQLi: queries parametrizadas y permisos DB

**~5.0 h · Semana 4**

Fix + least privilege del rol app en Postgres de Agenda Ops.

## Objetivo

Commit fix (si había) + nota de rol DB sin DDL; test de regresión en búsquedas de clientes/citas.

## Pasos (hazlos en orden)

### 1. Parametriza (60–80 min)

Reemplaza concat en la API del piloto. Test con payload previo → seguro.

### 2. Permisos DB (40 min)

Usuario app de Agenda Ops: DML limitado (sin DDL). Documenta en hallazgos.

### 3. Commit

`fix(m18): l14 sqli parametrizado`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | SQLi Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Commit fix (artefacto: `commit fix`).
2. Test de regresión (artefacto: `commit fix`).
3. Finding actualizado a Cerrado (artefacto: `commit fix`).

## Errores comunes

- Escapar manualmente sin parametrizar.
- Silenciar error sin arreglar query.

## Siguiente

[L15 — XSS reflejado en campos de cliente o búsqueda](L15-xss-reflejado-en-campos-de-cliente-o-busqueda.md)
