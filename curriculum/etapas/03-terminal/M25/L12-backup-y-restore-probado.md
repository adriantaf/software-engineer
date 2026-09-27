---
id: L12
materia: M25
orden: 12
titulo: Backup y restore probado
horas: 5.0
semana: 3
lectura: OWASP Configuration + Stripe webhooks docs
evidencia: projects/m25-ciber/hardening/restore-test.md
---

# L12 — Backup y restore probado

**~5 h · Semana 3**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hardening/restore-test.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Restore en entorno aislado; anotar tiempo y pasos.

## Por qué empieza así

Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.

Conceptos que debes poder explicar al cerrar:

- Stripe signature
- Secrets manager / env
- Restore ≠ backup

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Configuration + Stripe webhooks docs_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Documenta backup actual (20–30 min)

En `projects/m25-ciber/hardening/restore-test.md`: provider, frecuencia, retención, dónde vive el artefacto (sin keys).

### 3. Restore en entorno aislado (100–130 min)

Restaura a DB/temporal **no prod**. Cronometra.

```bash
# ejemplo — adapta a tu provider; no uses prod
# pg_restore -d vitrina_restore_test backup.dump
```

Tabla: paso | comando/UI | minutos | resultado.

### 4. RTO/RPO honestos (25–35 min)

Declara RPO/RTO medidos (no marketing). Gaps + próxima prueba. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l12 backup-y-restore-probado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Configuration + Stripe webhooks docs | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hardening/restore-test.md`.
2. Checklist ítem demostrado.
3. Sin valores de API keys.
4. Commit `docs(m25): l12 …` en el historial.

## Errores comunes

- Solo checklist teórico.
- Restore nunca probado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L13 — Logging sin secretos ni PII innecesaria](L13-logging-sin-secretos-ni-pii-innecesaria.md)
