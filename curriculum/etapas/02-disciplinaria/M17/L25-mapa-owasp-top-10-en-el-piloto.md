---
id: L25
materia: M17
orden: 25
titulo: Mapa OWASP Top 10 en el piloto
horas: 5.0
semana: 7
lectura: OWASP Top 10 overview
evidencia: projects/m17-vitrina/docs/owasp-mapa.md
---

# L25 — Mapa OWASP Top 10 en el piloto

**~5.0 h · Semana 7**

M18 profundiza; hoy ubicas huecos.

## Objetivo

Tabla: cada riesgo → mitigación actual o gap hacia M18.

## Conceptos clave

- OWASP
- gap
- mitigación

## Pasos (hazlos en orden)

### 1. Mapa OWASP Top 10 (80–100 min)

```bash
cat > projects/m17-vitrina/docs/owasp-mapa.md << 'EOF'
# OWASP Top 10 → Vitrina
| Riesgo | ¿Aplica? | Control en piloto | Gap |
|--------|----------|-------------------|-----|
| A01 Broken Access Control | sí | authorize()+tests 403 | |
| A02 Cryptographic Failures | sí | bcrypt + HTTPS | |
EOF
```

Cubre al menos A01–A05 con evidencia (ruta de test o doc).

### 2. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/owasp-mapa.md
git commit -m "docs(m17): L25 mapa owasp top10"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP Top 10 overview | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/owasp-mapa.md` cubre ≥A01–A05 con control o gap.
2. Commit `docs(m17): L25 mapa-owasp-top-10-en-el-piloto`.

## Errores comunes

- Tabla OWASP vacía o copy-paste sin controles del repo.
- Ignorar Broken Access Control.

## Siguiente

[L26 — Headers de seguridad y CORS prod](L26-headers-de-seguridad-y-cors-prod.md)
