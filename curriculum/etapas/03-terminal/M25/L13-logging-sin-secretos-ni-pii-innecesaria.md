---
id: L13
materia: M25
orden: 13
titulo: Logging sin secretos ni PII innecesaria
horas: 5.0
semana: 4
lectura: OWASP Error handling / logging
evidencia: projects/m25-ciber/logging/politica-logs.md
---

# L13 — Logging sin secretos ni PII innecesaria

**~5 h · Semana 4**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/logging/politica-logs.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Auditar logs recientes; redactar campos; política breve.

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

### 2. Audita logs recientes (30–40 min)

En `projects/m25-ciber/logging/politica-logs.md` pega **2** ejemplos redactados: uno inseguro (PII/token) y uno seguro.

```text
# INSEGURO (ejemplo a capturar y redactar)
{"msg":"login","authorization":"Bearer eyJ…","email":"ana@…"}
# SEGURO
{"msg":"login_ok","request_id":"req_…","tenant_id":"t_…","user_id":"u_…"}
```

Fuentes: app logs, access logs, errores.

### 3. Escribe la política (80–100 min)

Secciones: **Qué se loguea**, **Qué nunca** (Authorization, passwords, bodies de pago), **Retención**, **Quién accede**, **correlation id**.

≥8 reglas concretas ligadas a tu stack.

### 4. Ejemplo de cambio (30–40 min)

Si encontraste fuga: PR o issue. Si no: checklist de revisión trimestral. Bitácora `semana-04.md`.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l13 logging-sin-secretos-ni-pii-innecesaria"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Error handling / logging | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/logging/politica-logs.md`.
2. Política o config documentada.
3. Ejemplo de log seguro vs inseguro.
4. Commit `docs(m25): l13 …` en el historial.

## Errores comunes

- Loguear Authorization header.
- Alertas imposibles de actuar.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L14 — Rate limit login y abuso básico](L14-rate-limit-login-y-abuso-basico.md)
