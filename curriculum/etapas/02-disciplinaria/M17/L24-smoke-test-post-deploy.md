---
id: L24
materia: M17
orden: 24
titulo: Smoke test post-deploy
horas: 5
semana: 6
lectura: "Checklist smoke"
evidencia: "projects/m17-agenda-ops/docs/smoke-test.md"
---

# L24 — Smoke test post-deploy

**~5 h · Semana 6**

## Objetivo

Script o checklist: register/login/crear cita en staging.

## Por qué importa

Detecta config rota antes de la demo.

## Conceptos

- smoke.
- staging.
- regresión manual.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

smoke-test.md con resultado fechado de última corrida.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l24 smoke-test-post-deploy"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m15 | regresión | — |

## Hecho cuando

1. smoke-test.md.
2. Corrida fechada.
3. Cierre semana 6.

## Errores comunes

- Smoke solo health.
- Olvidar auth.

## Siguiente

[L25 — Mapa OWASP Top 10 en el piloto](L25-mapa-owasp-top-10-en-el-piloto.md)
