---
id: L03
materia: M18
orden: 3
titulo: STRIDE aplicado al CRM de citas
horas: 5
semana: 1
lectura: "STRIDE cheat sheet (una categoría por componente)"
evidencia: "projects/m18-appsec/stride-matrix.md"
---

# L03 — STRIDE aplicado al CRM de citas

**~5 h · Semana 1**

## Objetivo

Completar una matriz STRIDE (Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation) sobre login, citas y panel admin de Agenda Ops.

## Por qué importa

La matriz obliga a nombrar amenazas antes de buscar exploits al azar.

## Conceptos

- Spoofing en login.
- Tampering en `PUT /api/citas`.
- IDOR como Information Disclosure.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m18-appsec/stride-matrix.md` con filas: **Login**, **Lista citas**, **Detalle cita**, **Admin usuarios** (si existe).

Columnas STRIDE: marca S/T/R/I/D/E con una frase concreta (no “hackeo”). Ejemplo fila Login / Spoofing: “fuerza bruta o credenciales robadas”.

Prioriza 3 celdas rojas que atacarás en las próximas semanas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l03 stride-aplicado-al-crm-de-citas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | STRIDE | Top 10 overview ES |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Matriz ≥4 filas × 6 columnas.
2. ≥3 amenazas priorizadas.
3. Lenguaje del dominio Agenda Ops.

## Errores comunes

- Copiar tabla de blog sin adaptar.
- Dejar celdas vacías con ‘N/A’ en todo.

## Siguiente

[L04 — Threat model v0 y lectura OWASP Top 10](L04-threat-model-v0-y-lectura-owasp-top-10.md)
