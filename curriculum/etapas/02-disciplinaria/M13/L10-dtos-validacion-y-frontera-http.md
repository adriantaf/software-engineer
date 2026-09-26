---
id: L10
materia: M13
orden: 10
titulo: DTOs, validación y frontera HTTP
horas: 5
semana: 3
lectura: "Validación entrada"
evidencia: "arquitectura.md DTO"
---

# L10 — DTOs, validación y frontera HTTP

**~5 h · Semana 3**

## Objetivo

Listar DTOs de entrada/salida y dónde validas (no confiar en cliente).

## Por qué importa

Agenda Ops recibe JSON malicioso desde el primer día.

## Conceptos

- DTO.
- validación.
- sanitización (idea).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tabla endpoint→DTO→reglas. Enlaza RNF.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l10 dtos-validacion-y-frontera-http"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | input validation intro | srs |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. Tabla DTOs.
2. Validación server-side.
3. Sin confiar en front.

## Errores comunes

- Tipos TS = validación.
- Omitir límites tamaño.

## Siguiente

[L11 — Componentes y despliegue (C4 ligero)](L11-componentes-y-despliegue-c4-ligero.md)
