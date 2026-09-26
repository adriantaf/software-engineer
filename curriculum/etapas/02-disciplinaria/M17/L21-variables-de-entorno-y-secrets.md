---
id: L21
materia: M17
orden: 21
titulo: Variables de entorno y secrets
horas: 5
semana: 6
lectura: "12-factor config"
evidencia: "projects/m17-agenda-ops/.env.example"
---

# L21 — Variables de entorno y secrets

**~5 h · Semana 6**

## Objetivo

Separar config: DATABASE_URL, SESSION_SECRET, etc. `.env.example` sin valores reales.

## Por qué importa

Deploy seguro empieza por no commitear secrets.

## Conceptos

- env.
- secrets.
- example.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Validar arranque si falta variable crítica. Documentar en README.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l21 variables-de-entorno-y-secrets"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Secrets management | — |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. .env.example.
2. Validación arranque.
3. Commit.

## Errores comunes

- .env en git.
- Secrets en front.

## Siguiente

[L22 — Deploy staging en PaaS](L22-deploy-staging-en-paas.md)
