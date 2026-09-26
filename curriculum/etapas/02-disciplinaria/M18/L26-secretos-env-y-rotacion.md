---
id: L26
materia: M18
orden: 26
titulo: Secretos, .env y rotación
horas: 5
semana: 7
lectura: "Secrets Management Cheat Sheet"
evidencia: "projects/m18-appsec/secrets-rotation.md"
---

# L26 — Secretos, .env y rotación

**~5 h · Semana 7**

## Objetivo

Verificar que secretos viven fuera de git; plan de rotación para JWT/session secret y DB.

## Por qué importa

Un commit con `.env` es incidente permanente (historial).

## Conceptos

- `.gitignore`.
- Rotación sin downtime (idea).
- Pre-commit hooks.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
git log -p --all -S 'DATABASE_URL' | head -20
```

`projects/m18-appsec/secrets-rotation.md`: inventario (sin valores), dónde viven en local/staging, pasos rotar session secret.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l26 secretos-env-y-rotacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Secrets | M19 secrets-inventory |

## Hecho cuando

1. Inventario sin valores.
2. grep historial ejecutado.
3. Plan rotación.

## Errores comunes

- Pegar secretos en issue.
- Rotar sin probar logout.

## Siguiente

[L27 — Cabeceras de seguridad con Helmet o equivalente](L27-cabeceras-de-seguridad-con-helmet-o-equivalente.md)
