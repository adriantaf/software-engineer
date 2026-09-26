---
id: L05
materia: M15
orden: 5
titulo: Fake repositorio y reloj para tests rápidos
horas: 5
semana: 2
lectura: "Test doubles — Fowler / Vitest mocks"
evidencia: "projects/m15-calidad/tests/fakes/"
---

# L05 — Fake repositorio y reloj para tests rápidos

**~5 h · Semana 2**

## Objetivo

Implementar repo en memoria y `RelojFalso` para probar citas en el futuro/pasado.

## Por qué importa

Tests de integración lentos matan CI; fakes bien hechos dan confianza.

## Conceptos

- fake.
- reloj.
- determinismo.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Fakes en carpeta dedicada. Test que avanza reloj y verifica expiración o ventana.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l05 fake-repositorio-y-reloj-para-tests-rapi"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vitest | mocking guide | — |

## Hecho cuando

1. Fakes reutilizables.
2. Test reloj.
3. Sin mock excesivo.

## Errores comunes

- Mock de cada línea.
- Fake que no respeta contrato repo.

## Siguiente

[L06 — Tests de integración con persistencia](L06-tests-de-integracion-con-persistencia.md)
