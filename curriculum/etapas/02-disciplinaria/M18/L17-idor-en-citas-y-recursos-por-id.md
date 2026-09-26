---
id: L17
materia: M18
orden: 17
titulo: IDOR en citas y recursos por ID
horas: 5
semana: 5
lectura: "OWASP A01 Broken Access Control"
evidencia: "projects/m18-appsec/findings/003-idor.md"
---

# L17 — IDOR en citas y recursos por ID

**~5 h · Semana 5**

## Objetivo

Demostrar acceso cross-user a `GET/PUT /api/citas/:id` (u otro recurso) con dos cuentas de prueba.

## Por qué importa

El ejemplo de la ficha M18: ocultar botones no basta.

## Conceptos

- Autorización server-side.
- ID predecible.
- UUID no es autorización.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea usuario A y B. A crea cita. B intenta leer/editar ID de A. Documenta en `003-idor.md`.

Si ya está protegido, muestra test automatizado que falla si quitas el check.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l17 idor-en-citas-y-recursos-por-id"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | A01 | Ejemplo IDOR ficha M18 |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. PoC con dos usuarios.
2. Impacto descrito.
3. Ruta exacta.

## Errores comunes

- Probar en datos de design partner real.
- Autorización solo en front.

## Siguiente

[L18 — Autorización por rol owner vs staff](L18-autorizacion-por-rol-owner-vs-staff.md)
