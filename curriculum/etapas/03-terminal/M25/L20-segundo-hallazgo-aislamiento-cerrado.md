---
id: L20
materia: M25
orden: 20
titulo: Segundo hallazgo aislamiento cerrado
horas: 5.0
semana: 5
lectura: OWASP Privacy / LFPDPPP notas (contexto)
evidencia: projects/m25-ciber/hallazgos/hallazgo-02.md
---

# L20 — Segundo hallazgo aislamiento cerrado

**~5 h · Semana 5**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hallazgos/hallazgo-02.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Otro fix cross-tenant con test; tabla hallazgos actualizada.

## Por qué empieza así

Multi-tenant amplifica impacto de una fuga; privacidad es feature de confianza.

Conceptos que debes poder explicar al cerrar:

- Retención
- Derecho de cancelación
- Datos por negocio

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Privacy / LFPDPPP notas (contexto)_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Segundo hallazgo distinto (25–35 min)

En `projects/m25-ciber/hallazgos/hallazgo-02.md`: debe ser **otro** vector (p.ej. listado, update, export) distinto a hallazgo-01.

### 3. Fix + test (100–130 min)

Repro, root cause, PR, test automatizado o curl post-fix.

```bash
# post-fix — mismo vector que el hallazgo-02
curl -s -w "\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \
  "$API/EXPORT_O_UPDATE_DE_B"
```

Actualiza `hallazgos/README.md` con tabla acumulada (≥2 cerrados).

### 4. Regresión (25–35 min)

Confirma que hallazgo-01 sigue cerrado. Bitácora semana-05.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l20 segundo-hallazgo-aislamiento-cerrado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Privacy / LFPDPPP notas (contexto) | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hallazgos/hallazgo-02.md`.
2. Documento en ruta indicada.
3. ≥2 hallazgos aislamiento cerrados acumulado.
4. Commit `docs(m25): l20 …` en el historial.

## Errores comunes

- Política genérica sin tu producto.
- Un solo hallazgo en todo M25.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L21 — Tabletop — fuga de .env](L21-tabletop-fuga-de-env.md)
