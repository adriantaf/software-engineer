---
id: L13
materia: M14
orden: 13
titulo: Repository — interfaz Cita sin SQL
horas: 5
semana: 4
lectura: "Patrón Repository + diseño M13"
evidencia: "projects/m14-patrones/src/cita-repository.ts"
---

# L13 — Repository — interfaz Cita sin SQL

**~5 h · Semana 4**

## Objetivo

Definir `CitaRepository` en dominio e implementación en memoria para tests.

## Por qué importa

M17 usará Postgres; hoy fijas el puerto.

## Conceptos

- Repository.
- puerto.
- infra separada.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Interfaz async `findById`, `save`. Impl memoria + test roundtrip.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l13 repository-interfaz-cita-sin-sql"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m13-diseno | persistencia ADR | M09 esquema |

## Hecho cuando

1. Interfaz en dominio.
2. Impl memoria testeada.
3. Sin SQL en dominio.

## Errores comunes

- Repository que devuelve rows SQL.
- Mezclar con Service aún.

## Siguiente

[L14 — Service — capa aplicación de citas](L14-service-capa-aplicacion-de-citas.md)
