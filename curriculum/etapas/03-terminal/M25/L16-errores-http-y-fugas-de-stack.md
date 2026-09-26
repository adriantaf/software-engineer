---
id: L16
materia: M25
orden: 16
titulo: Errores HTTP y fugas de stack
horas: 5.0
semana: 4
lectura: OWASP Error handling / logging
evidencia: projects/m25-ciber/logging/errores.md
---

# L16 — Errores HTTP y fugas de stack

**~5 h · Semana 4**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/logging/errores.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Revisar 500 en staging; mensajes al cliente sin stack trace.

## Por qué empieza así

Un atacante lee tus logs si exfiltras tokens; un cliente lee tus stack traces.

Conceptos que debes poder explicar al cerrar:

- Structured logging
- Correlation id
- Fail closed

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Error handling / logging_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Prepara carpetas (15–25 min)

```bash
mkdir -p projects/m25-ciber/logging
```

Confirma que escribirás `projects/m25-ciber/logging/errores.md`.

### 3. Laboratorio principal (100–130 min)

Bitácora semana 4 en `projects/m25-ciber/bitacora/semana-04.md`.

### 4. Criterio de calidad (30–45 min)

Relee `projects/m25-ciber/logging/errores.md`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l16 errores-http-y-fugas-de-stack"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Error handling / logging | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/logging/errores.md`.
2. Política o config documentada.
3. Ejemplo de log seguro vs inseguro.
4. Commit `docs(m25): l16 …` en el historial.

## Errores comunes

- Loguear Authorization header.
- Alertas imposibles de actuar.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L17 — Retención y borrado por tenant](L17-retencion-y-borrado-por-tenant.md)
