---
id: L17
materia: M23
orden: 17
titulo: Endpoint faq-preview protegido
horas: 5
semana: 5
lectura: "API interna admin"
evidencia: "projects/m23-ia/faq-asistente/endpoint.md"
---

# L17 — Endpoint faq-preview protegido

**~5 h · Semana 5**

## Objetivo

Diseñar o implementar POST interno faq-preview auth owner/staff con rate limit.

## Por qué importa

Semana 5 entrega superficie controlada antes de UI pulida.

## Conceptos

- AuthZ.
- Rate limit.
- Preview vs prod.
- Logging redacted.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Documenta en `projects/m23-ia/faq-asistente/endpoint.md` ruta, roles, body, respuesta, errores.

Enlaza PR repo producto si existe. Sin endpoint público anónimo.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l17 endpoint-faq-preview-protegido"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M18 | authZ | ../M17-aplicaciones-web.md |

## Hecho cuando

1. endpoint.md.
2. Roles definidos.
3. Rate limit mencionado.

## Errores comunes

- Endpoint público.
- Sin auth.

## Siguiente

[L18 — UI o CLI asistente para owner](L18-ui-o-cli-asistente-para-owner.md)
