---
id: L09
materia: M13
orden: 9
titulo: Arquitectura en capas
horas: 5
semana: 3
lectura: "Capas + Clean idea"
evidencia: "arquitectura.md borrador"
---

# L09 — Arquitectura en capas

**~5 h · Semana 3**

## Objetivo

Definir capas HTTP → aplicación → dominio → infraestructura.

## Por qué importa

Evita mezclar SQL en controllers.

## Conceptos

- controller.
- service.
- repository.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Diagrama capas + regla: autorización en aplicación/dominio.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l09 arquitectura-en-capas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Larman | capas | Código limpio módulos |

## Hecho cuando

1. arquitectura.md.
2. Regla autorización.
3. Nombres de capas.

## Errores comunes

- Anémico sin comportamiento.
- Lógica en React.

## Siguiente

[L10 — DTOs, validación y frontera HTTP](L10-dtos-validacion-y-frontera-http.md)
