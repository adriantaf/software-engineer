---
id: L30
materia: M18
orden: 30
titulo: Estructura del informe AppSec
horas: 5.0
semana: 8
lectura: Reporting + risk rating
evidencia: projects/m18-appsec/informe-appsec.md (borrador)
---

# L30 — Estructura del informe AppSec

**~5.0 h · Semana 8**

El entregable del proyecto es el informe: ejecutivo, alcance, hallazgos, mitigaciones, residual.

## Objetivo

Borrador `projects/m18-appsec/informe-appsec.md` enlazando PoCs y commits (sin PII de partner).

## Pasos

### 1. Plantilla (25–35 min)

```bash
cat > projects/m18-appsec/informe-appsec.md <<'EOF'
# Informe AppSec — Vitrina

## 1. Ejecutivo
- …

## 2. Alcance y supuestos
- Solo staging/local propio
- Fuera de alcance: …

## 3. Metodología
STRIDE + OWASP Top 10 + PoC en API propia

## 4. Hallazgos
Tabla → ver findings-table.md (severidad, estado)

## 5. Mitigaciones
Commits / PRs: …

## 6. Riesgo residual
Top 3 con dueño/fecha

## 7. Anexos
- threat-model-v1.md
- docs/auth-inventario.md
- ci/
EOF
```
### 2. Redacción con enlaces (90–110 min)

Rellena §§1–6 con datos reales de tu P2/P3. Verifica que no hay secretos ni teléfonos reales.

```bash
rg -n 'password|Bearer |postgresql://|@gmail' projects/m18-appsec/informe-appsec.md || echo "sin secretos obvios"
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/informe-appsec.md
git commit -m "docs(m18): l30 informe appsec"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Reporting + risk rating | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Borrador ≥4 secciones (artefacto: `projects/m18-appsec/informe-appsec.md (borrador)`).
2. Enlaces internos (artefacto: `projects/m18-appsec/informe-appsec.md (borrador)`).
3. Commit `docs(m18): L30 estructura-del-informe-appsec`.

## Errores comunes

- Informe sin hallazgos reales.
- Copiar OWASP sin contexto.

## Siguiente

[L31 — Tests de regresión de seguridad (≥3)](L31-tests-de-regresion-de-seguridad-3.md)
