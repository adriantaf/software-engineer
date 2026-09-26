---
id: L09
materia: M14
orden: 9
titulo: Observer para eventos de dominio
horas: 5
semana: 3
lectura: "Refactoring.Guru Observer"
evidencia: "projects/m14-patrones/src/eventos-cita-observer.ts"
---

# L09 — Observer para eventos de dominio

**~5 h · Semana 3**

## Objetivo

Publicar evento `CitaCreada` y suscriptores (auditoría, recordatorio futuro) con Observer.

## Por qué importa

Desacopla efectos secundarios del agregado cita.

## Conceptos

- Observer.
- evento dominio.
- suscriptor.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementa bus simple o lista de handlers. Test: al crear cita se notifica a N suscriptores.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l09 observer-para-eventos-de-dominio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Observer | — |
| Catálogo | Entrada M14 | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

1. Observer con ≥2 suscriptores en test.
2. ADR 003 o sección README.
3. Commit.

## Errores comunes

- Observer con orden frágil no documentado.
- Lógica de negocio en suscriptor.

## Siguiente

[L10 — Command para acciones admin reversibles](L10-command-para-acciones-admin-reversibles.md)
