---
id: L21
materia: M18
orden: 21
titulo: "SSRF: superficie en webhooks e integraciones"
horas: 5
semana: 6
lectura: "SSRF Prevention Cheat Sheet"
evidencia: "projects/m18-appsec/findings/004-ssrf.md"
---

# L21 — SSRF: superficie en webhooks e integraciones

**~5 h · Semana 6**

## Objetivo

Identificar si Agenda Ops (o roadmap) acepta URLs server-side (webhook, import, avatar remoto) y evaluar riesgo SSRF.

## Por qué importa

Aun sin feature, documentar el control evita sorpresas en M26 integraciones.

## Conceptos

- Allowlist de hosts.
- Bloquear metadata IP.
- No reutilizar cliente HTTP sin validar.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Si no hay feature URL, simula diseño en `004-ssrf.md`: qué pasaría con `http://169.254.169.254`. Define allowlist propuesta.

Si hay fetch server-side, prueba URL interna en staging aislado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l21 ssrf-superficie-en-webhooks-e-integracio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | SSRF | — |

## Hecho cuando

1. Doc SSRF con allowlist.
2. Riesgo nombrado.
3. Sin escanear terceros.

## Errores comunes

- curl a metadata cloud en prod.
- SSRF ‘para probar AWS’ en cuenta ajena.

## Siguiente

[L22 — Subida de archivos segura](L22-subida-de-archivos-segura.md)
