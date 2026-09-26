---
id: L16
materia: M20
orden: 16
titulo: "AppSec móvil: no loguear PII ni tokens"
horas: 5
semana: 4
lectura: "OWASP MASVS logging"
evidencia: "projects/m20-movil/logging-policy.md"
---

# L16 — AppSec móvil: no loguear PII ni tokens

**~5 h · Semana 4**

## Objetivo

Revisar print/debug; política de logs en dev vs release.

## Por qué importa

Un logcat filtrado filtra tokens.

## Conceptos

- PII
- tokens
- crash reports

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

logging-policy.md + grep prints de token en repo app.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l16 appsec-movil-no-loguear-pii-ni-tokens"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M18 | informe | MASVS |

## Hecho cuando

1. Política escrita
2. Sin token en logs
3. Commit limpieza si hubo

## Errores comunes

- console.log(token)
- Sentry con PII

## Siguiente

[L17 — Firma Android y keystore fuera del repo](L17-firma-android-y-keystore-fuera-del-repo.md)
