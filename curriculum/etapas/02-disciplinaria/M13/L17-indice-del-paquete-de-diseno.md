---
id: L17
materia: M13
orden: 17
titulo: Índice del paquete de diseño
horas: 5
semana: 5
lectura: "README proyecto"
evidencia: "projects/m13-diseno/README.md"
---

# L17 — Índice del paquete de diseño

**~5 h · Semana 5**

## Objetivo

Crear índice enlazando SRS, diagramas, ADRs, arquitectura.

## Por qué importa

El paquete debe ser navegable en 2 minutos.

## Conceptos

- índice.
- trazabilidad.
- onboarding.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

README con checklist enlaces. Verifica rutas relativas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l17 indice-del-paquete-de-diseno"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | proyecto M13 | srs-v1 |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. README índice.
2. Todos los artefactos enlazados.
3. Sin enlaces rotos.

## Errores comunes

- README vacío.
- Diagramas huérfanos.

## Siguiente

[L18 — Endpoints y módulos previstos M17](L18-endpoints-y-modulos-previstos-m17.md)
