---
id: L20
materia: M17
orden: 20
titulo: Cierre P3 integración WhatsApp
horas: 5.0
semana: 5
lectura: Ficha P3
evidencia: integracion-whatsapp.md completo
---

# L20 — Cierre P3 integración WhatsApp

**~5.0 h · Semana 5**

P3 no sustituye API oficial si no está configurada — documenta gaps.

## Objetivo

Completar doc P3: capturas, límites legales/opt-in, qué no hace la integración.

## Conceptos clave

- P3
- opt-in
- gap

## Pasos (hazlos en orden)

### 1. Cierra doc P3 (50–60 min)

Completa `projects/m17-vitrina/docs/integracion-whatsapp.md`: flujo, límites (manual), riesgos PII en URL, captura demo.

### 2. Checklist README (30 min)

```bash
rg -n "P3|WhatsApp" projects/m17-vitrina/README.md
```

Marca P3 si el botón + doc existen.

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/integracion-whatsapp.md projects/m17-vitrina/README.md
git commit -m "docs(m17): L20 cierre P3 whatsapp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha P3 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/integracion-whatsapp.md` completo; P3 marcado en README.
2. Commit `docs(m17): L20 cierre-p3-integracion-whatsapp`.

## Errores comunes

- Marcar P3 sin botón + doc.
- Doc genérico sin flujo del piloto.

## Siguiente

[L21 — Variables de entorno y secrets](L21-variables-de-entorno-y-secrets.md)
