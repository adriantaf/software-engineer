---
id: L10
materia: M11
orden: 10
titulo: Permisos, usuarios y mínimo privilegio
horas: 5
semana: 3
lectura: "Silberschatz protección"
evidencia: "labs/permisos.md"
---

# L10 — Permisos, usuarios y mínimo privilegio

**~5 h · Semana 3**

## Objetivo

Practicar `chmod`/`chown` en directorio de datos simulado con roles owner/staff (carpetas).

## Por qué importa

Datos de clientes no deben ser legibles por cualquier usuario del host.

## Conceptos

- rwx para user/group/other.
- 750 vs 700.
- Principio least privilege.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea árbol `data/owner` y `data/staff` con permisos distintos; documenta matriz.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l10 permisos-usuarios-y-minimo-privilegio"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Silberschatz | Protección | Ficha M11 |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Matriz rol/carpeta/permiso.
2. Experimento reproducido.
3. Sin 777.

## Errores comunes

- chmod 777 en volumen Docker.
- Correr Postgres como root innecesario.

## Siguiente

[L11 — Script de backup automatizado (P2)](L11-script-de-backup-automatizado-p2.md)
