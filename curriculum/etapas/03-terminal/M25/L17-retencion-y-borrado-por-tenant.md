---
id: L17
materia: M25
orden: 17
titulo: Retención y borrado por tenant
horas: 5.0
semana: 5
lectura: OWASP Privacy / LFPDPPP notas (contexto)
evidencia: projects/m25-ciber/privacidad/retencion.md
---

# L17 — Retención y borrado por tenant

**~5 h · Semana 5**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/privacidad/retencion.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Política corta: cuánto guardas pedidos/logs; cómo borrar tenant demo.

## Por qué empieza así

Multi-tenant amplifica impacto de una fuga; privacidad es feature de confianza.

Conceptos que debes poder explicar al cerrar:

- Retención
- Derecho de cancelación
- Datos por negocio

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Privacy / LFPDPPP notas (contexto)_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Política de retención (30–40 min)

En `projects/m25-ciber/privacidad/retencion.md`:

| Dato | Retención | Base | Cómo se borra |
|------|-----------|------|---------------|

Pedidos, logs, backups, tenants demo, exports temporales.

### 3. Borrado de tenant demo (90–110 min)

Describe (o ejecuta en staging) borrado de un tenant de prueba: tablas afectadas, orden, qué queda en backups.

```sql
-- ejemplo de inventario — adapta schemas
-- SELECT count(*) FROM pedidos WHERE tenant_id = $1;
```

**No** borres prod real de un cliente.

### 4. Gaps legales vs técnicos (25–35 min)

3 bullets: qué es decisión técnica hoy vs qué requiere abogado. Bitácora semana-05.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l17 retenci-n-y-borrado-por-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Privacy / LFPDPPP notas (contexto) | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/privacidad/retencion.md`.
2. Documento en ruta indicada.
3. ≥2 hallazgos aislamiento cerrados acumulado.
4. Commit `docs(m25): l17 …` en el historial.

## Errores comunes

- Política genérica sin tu producto.
- Un solo hallazgo en todo M25.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L18 — Minimización en exports y soporte](L18-minimizacion-en-exports-y-soporte.md)
