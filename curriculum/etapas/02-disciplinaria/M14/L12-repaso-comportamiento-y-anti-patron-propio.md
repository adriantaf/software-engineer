---
id: L12
materia: M14
orden: 12
titulo: Repaso comportamiento y anti-patrón propio
horas: 5
semana: 3
lectura: "Retro patrones semana 3"
evidencia: "projects/m14-patrones/semana-03.md"
---

# L12 — Repaso comportamiento y anti-patrón propio

**~5 h · Semana 3**

## Objetivo

Documentar un anti-patrón que cometiste y cómo lo corregiste (cargo cult).

## Por qué importa

La retro alimenta code review en M15.

## Conceptos

- cargo cult.
- retro.
- simplificación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`semana-03.md` + enlace al commit de fix.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l12 repaso-comportamiento-y-anti-patron-prop"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | catálogo | — |

## Hecho cuando

1. Anti-patrón descrito.
2. Fix commiteado.
3. Cierre semana 3.

## Errores comunes

- Retro vacía.
- Añadir patrón sin necesidad.

## Siguiente

[L13 — Repository — interfaz Cita sin SQL](L13-repository-interfaz-cita-sin-sql.md)
