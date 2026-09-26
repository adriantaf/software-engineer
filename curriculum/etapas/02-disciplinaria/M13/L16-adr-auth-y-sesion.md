---
id: L16
materia: M13
orden: 16
titulo: ADR auth y sesión
horas: 5
semana: 4
lectura: "SRS seguridad"
evidencia: "adr/005-auth.md"
---

# L16 — ADR auth y sesión

**~5 h · Semana 4**

## Objetivo

ADR alineada a RNF: sesión server-side vs JWT según M10/M12.

## Por qué importa

Auth unificada en diseño antes del código.

## Conceptos

- sesión.
- CSRF.
- rotación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ADR 005 con consecuencias operativas (redis/DB sessions).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l16 adr-auth-y-sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M12 | RNF SEC | M10 cookies |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. ADR 005.
2. Alineado SRS.
3. ≥2 ADRs semana 4.

## Errores comunes

- Auth indefinida en M17.
- Omitir CSRF.

## Siguiente

[L17 — Índice del paquete de diseño](L17-indice-del-paquete-de-diseno.md)
