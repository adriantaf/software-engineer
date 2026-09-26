---
id: L08
materia: M12
orden: 8
titulo: RNF seguridad, privacidad y P2
horas: 5.0
semana: 2
lectura: Plantilla RNF + hilo seguridad
evidencia: stories.md + srs-borrador RNF (≥8 stories)
---

# L08 — RNF seguridad, privacidad y P2

**~5.0 h · Semana 2**

Cierras P2 y metes seguridad en el SRS desde ya ([hilo](../../../hilos/seguridad.md)).

## Objetivo

≥8 stories + ≥3 RNF de seguridad/privacidad trazables.

## Pasos

### 1. Completa stories (45 min)

Llega a ≥8 con criterios. Índice al inicio de `stories.md`.

### 2. RNF (75 min)

En `srs-borrador.md` §3.2, ejemplos:

| ID | Tipo | Descripción |
|----|------|-------------|
| RNF-SEC-01 | Seguridad | Toda ruta de negocio exige sesión; sin token → 401 |
| RNF-SEC-02 | Autorización | Staff no lee notas privadas → 403 + log |
| RNF-PRIV-01 | Privacidad | PII mínimo; single-tenant documentado |

Enlaza cada RNF a US-xx.

### 3. README P2 (20 min)

Marca P2 listo.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l08 rnf seguridad p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | RNF seguridad/privacidad trazables; single-tenant; 401/403 | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `stories.md` tiene ≥8 stories con criterios (P2).
2. `srs-borrador.md` incluye ≥3 RNF-SEC/PRIV numerados y enlazados a stories.
3. Commit `docs(m12): l08 rnf seguridad p2`.

## Errores comunes

- “Seguridad luego en M18” sin RNF.
- RNF no medibles (“máxima seguridad”).
- Stories sin permisos.

## Siguiente

[L09 — Alcance MVP y MoSCoW](L09-alcance-mvp-y-moscow.md)
