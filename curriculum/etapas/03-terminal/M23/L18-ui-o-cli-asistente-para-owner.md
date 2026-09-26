---
id: L18
materia: M23
orden: 18
titulo: UI o CLI asistente para owner
horas: 5
semana: 5
lectura: "UX mínima FAQ"
evidencia: "projects/m23-ia/faq-asistente/README.md borrador"
---

# L18 — UI o CLI asistente para owner

**~5 h · Semana 5**

## Objetivo

Exponer asistente mínimo: owner pregunta política cancelación → respuesta grounded.

## Por qué importa

Proyecto materia: asistente scoped por tenant en staging.

## Conceptos

- UI mínima.
- CLI alternativa.
- Citas fuente.
- Fallback sin alucinar.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Amplía `projects/m23-ia/faq-asistente/README.md`: cómo probar, credenciales test, ejemplo pregunta/respuesta.

Captura o log de sesión **redactado**.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m23): l18 ui-o-cli-asistente-para-owner"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../../producto-saas.md | ../M16-ihc.md estados UI |

## Hecho cuando

1. README uso.
2. Ejemplo Q&A.
3. Staging URL.

## Errores comunes

- Prometer auto-agenda.
- Respuesta sin fuente.

## Siguiente

[L19 — Casos tests-cross-tenant manuales](L19-casos-tests-cross-tenant-manuales.md)
