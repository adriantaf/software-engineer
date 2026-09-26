---
id: L08
materia: M18
orden: 8
titulo: Threat model v1 post-autenticación (P1)
horas: 5
semana: 2
lectura: "Repaso STRIDE semanas 1–2"
evidencia: "projects/m18-appsec/threat-model-v1.md"
---

# L08 — Threat model v1 post-autenticación (P1)

**~5 h · Semana 2**

## Objetivo

Actualizar threat model con flujos de auth reales y marcar controles implementados vs pendientes.

## Por qué importa

P1 exige v1 revisado tras entender login; hoy entregas el hito.

## Conceptos

- Control vs amenaza.
- Gap analysis.
- Priorización por explotabilidad.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Copia `threat-model-v0.md` → `threat-model-v1.md`. Añade sección **Controles auth** (hashing, cookies, rate limit planificado).

Tabla: Amenaza | Control | Estado (OK/TODO) | Issue/commit.

Checklist P1 de la ficha: confirma que un revisor podría seguir el doc sin abrir el código.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l08 threat-model-v1-post-autenticacion-p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M18-seguridad.md P1 | — |

## Hecho cuando

1. threat-model-v1.md completo.
2. Tabla amenaza-control.
3. Listo para marcar P1 en UI.

## Errores comunes

- Renombrar v0 sin cambios.
- Omitir auth en el modelo.

## Siguiente

[L09 — Cookies Secure, HttpOnly y SameSite](L09-cookies-secure-httponly-y-samesite.md)
