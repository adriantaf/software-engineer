---
id: L25
materia: M18
orden: 25
titulo: npm audit y cadena de dependencias
horas: 5
semana: 7
lectura: "OWASP A06 Vulnerable Components"
evidencia: "projects/m18-appsec/deps-audit.md"
---

# L25 — npm audit y cadena de dependencias

**~5 h · Semana 7**

## Objetivo

Ejecutar auditoría de dependencias, triagear findings (prod vs dev), actualizar o documentar riesgo aceptado.

## Por qué importa

Tu app hereda CVEs de `node_modules`.

## Conceptos

- Semver y lockfile.
- DevDependency vs runtime.
- Riesgo aceptado con fecha.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
cd <repo Agenda Ops>
npm audit --omit=dev 2>/dev/null || npm audit
```

Guarda salida en `projects/m18-appsec/deps-audit.md`. Arregla al menos 1 high/critical o documenta por qué no aplica.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l25 npm-audit-y-cadena-de-dependencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | A06 | npm audit docs |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Audit guardado.
2. ≥1 acción tomada.
3. Fecha en doc.

## Errores comunes

- `npm audit fix --force` sin leer.
- Ignorar todo.

## Siguiente

[L26 — Secretos, .env y rotación](L26-secretos-env-y-rotacion.md)
