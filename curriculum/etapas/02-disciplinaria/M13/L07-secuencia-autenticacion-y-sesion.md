---
id: L07
materia: M13
orden: 7
titulo: Secuencia: autenticación y sesión
horas: 5
semana: 2
lectura: "Mermaid sequence"
evidencia: "diagramas/secuencia-auth.md"
---

# L07 — Secuencia: autenticación y sesión

**~5 h · Semana 2**

## Objetivo

Diagrama de secuencia login + cookie/sesión según SRS.

## Por qué importa

Auth es secuencia crítica para seguridad.

## Conceptos

- secuencia.
- sesión.
- validación API.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Mermaid: browser→API→DB. Marca validación rol en API.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l07 secuencia-autenticacion-y-sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | cookies/sesión | srs auth |

## Hecho cuando

1. secuencia-auth.md.
2. Validación en API.
3. Errores 401.

## Errores comunes

- Auth solo en front.
- Omitir logout.

## Siguiente

[L08 — Secuencia: crear cita (P2)](L08-secuencia-crear-cita-p2.md)
