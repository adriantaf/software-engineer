---
id: L08
materia: M14
orden: 8
titulo: Tests de regresión en API pública del módulo
horas: 5
semana: 2
lectura: "Código limpio cap. pruebas (selecto)"
evidencia: "projects/m14-patrones/tests/regresion-publica.test.ts"
---

# L08 — Tests de regresión en API pública del módulo

**~5 h · Semana 2**

## Objetivo

Añadir tests que solo usen la API pública de tus patrones de la semana 2 (sin acoplarse a internals).

## Por qué importa

M15 exigirá lo mismo en el piloto; hoy practicas el hábito.

## Conceptos

- API pública.
- regresión.
- encapsulamiento.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥3 tests que fallen si cambias detalle interno pero mantienes contrato. Documenta qué es público.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l08 tests-de-regresion-en-api-publica-del-mo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M15-vv-calidad.md | Vitest |
| Catálogo | Entrada M14 | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

1. Suite regresión verde.
2. Lista API pública en README.
3. Cierre semana 2.

## Errores comunes

- Tests de campos privados.
- Romper tests al refactor legítimo.

## Siguiente

[L09 — Observer para eventos de dominio](L09-observer-para-eventos-de-dominio.md)
