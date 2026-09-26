---
id: L05
materia: M13
orden: 5
titulo: Diagrama de clases del dominio
horas: 5
semana: 2
lectura: "Larman modelo dominio"
evidencia: "diagramas/clases.md"
---

# L05 — Diagrama de clases del dominio

**~5 h · Semana 2**

## Objetivo

Modelar entidades MVP: Usuario, Cliente, Cita, Servicio (ajusta a SRS).

## Por qué importa

Clases deben caber en 4 semanas de build.

## Conceptos

- entidad.
- agregado (idea).
- relación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Mermaid classDiagram en clases.md. Solo Must.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l05 diagrama-de-clases-del-dominio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Larman | modelo conceptual | M09 FK preview |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. clases.md con Mermaid.
2. ≤8 entidades.
3. Nombres alineados SRS.

## Errores comunes

- 40 entidades día 1.
- UML sin atributos útiles.

## Siguiente

[L06 — Cardinalidades y persistencia futura](L06-cardinalidades-y-persistencia-futura.md)
