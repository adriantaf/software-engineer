---
id: L12
materia: M11
orden: 12
titulo: Rotación de logs y restore de prueba
horas: 5
semana: 3
lectura: "logrotate concept + tu script"
evidencia: "restore-prueba.md + rotación"
---

# L12 — Rotación de logs y restore de prueba

**~5 h · Semana 3**

## Objetivo

Añadir rotación por tamaño/fecha y documentar **un** restore de prueba.

## Por qué importa

P2 no cuenta sin restore documentado.

## Conceptos

- rotación.
- restore.
- RPO/RTO (intro).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Rotación en script o logrotate config. Restore a carpeta/DB vacía; fecha en `restore-prueba.md`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l12 rotacion-de-logs-y-restore-de-prueba"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M11 P2 | — |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. `restore-prueba.md` con fecha.
2. Rotación funciona.
3. P2 lista para auditoría.

## Errores comunes

- Restore nunca probado.
- Sobrescribir único backup.

## Siguiente

[L13 — Imágenes, contenedores y volúmenes](L13-imagenes-contenedores-y-volumenes.md)
