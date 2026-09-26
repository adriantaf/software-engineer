---
id: L01
materia: M15
orden: 1
titulo: Entorno M15 y pirámide de tests
horas: 5
semana: 1
lectura: "Código limpio cap. 9 + Vitest"
evidencia: "projects/m15-calidad/piramide.md + tests iniciales"
---

# L01 — Entorno M15 y pirámide de tests

**~5 h · Semana 1**

## Objetivo

Crear `projects/m15-calidad/`, documentar pirámide objetivo para Agenda Ops y 5 tests iniciales de dominio.

## Por qué importa

Sin pirámide escrita, acabarás con E2E lentos o cero tests de auth.

## Conceptos

- pirámide.
- unit.
- regla negocio.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m15-calidad/tests
```
Elige función dominio (crear cita, solapamiento). 5 tests: feliz, regla rota, y placeholders auth si aplica.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l01 entorno-m15-y-piramide-de-tests"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vitest | getting started | Código limpio cap. 9 |

## Hecho cuando

1. piramide.md.
2. 5 tests.
3. Commit test(m15).

## Errores comunes

- Solo tests felices.
- Pirámide genérica sin capas.

## Siguiente

[L02 — Tests unitarios puros de reglas de cita](L02-tests-unitarios-puros-de-reglas-de-cita.md)
