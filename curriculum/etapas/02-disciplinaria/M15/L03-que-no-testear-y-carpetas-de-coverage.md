---
id: L03
materia: M15
orden: 3
titulo: Qué no testear y carpetas de coverage
horas: 5
semana: 1
lectura: "Vitest coverage v8"
evidencia: "projects/m15-calidad/coverage-objetivo.md"
---

# L03 — Qué no testear y carpetas de coverage

**~5 h · Semana 1**

## Objetivo

Definir carpetas donde coverage **sí** importa (`domain/`) y dónde no (DTOs boilerplate).

## Por qué importa

100 % en mappers no salva un IDOR.

## Conceptos

- coverage útil.
- exclusiones.
- umbral.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`coverage-objetivo.md` + script `npm test -- --coverage` si aplica al spike.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l03 que-no-testear-y-carpetas-de-coverage"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Vitest | coverage | Ficha M15 |

## Hecho cuando

1. Documento coverage.
2. Umbral solo dominio.
3. Commit.

## Errores comunes

- Perseguir 100 % global.
- Ignorar dominio.

## Siguiente

[L04 — Cierre semana 1 — suite dominio y bitácora](L04-cierre-semana-1-suite-dominio-y-bitacora.md)
