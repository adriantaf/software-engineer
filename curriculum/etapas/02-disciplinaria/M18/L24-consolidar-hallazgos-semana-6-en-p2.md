---
id: L24
materia: M18
orden: 24
titulo: Consolidar hallazgos semana 6 en P2
horas: 5
semana: 6
lectura: "Repaso findings"
evidencia: "projects/m18-appsec/findings-table.md actualizado"
---

# L24 — Consolidar hallazgos semana 6 en P2

**~5 h · Semana 6**

## Objetivo

Asegurar ≥5 hallazgos con PoC, fix y test o verificación repetible; priorizar los de mayor impacto.

## Por qué importa

Mitad del módulo: P2 debe ser visible en git.

## Conceptos

- Severidad.
- Estado.
- Regresión.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Revisa tabla P2. Cada fila: ID, OWASP, PoC resumen, commit fix, test/link.

Abre issues para hallazgos abiertos con fecha objetivo semana 7–8.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l24 consolidar-hallazgos-semana-6-en-p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M18 P2 | — |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. ≥5 filas completas o plan con 5.
2. Commits enlazados.
3. Ningún secreto en tabla.

## Errores comunes

- Hallazgos duplicados.
- PoC sin fix planificado.

## Siguiente

[L25 — npm audit y cadena de dependencias](L25-npm-audit-y-cadena-de-dependencias.md)
