---
id: L07
materia: M20
orden: 7
titulo: Estados de carga en lista
horas: 5
semana: 2
lectura: "UX loading skeletons"
evidencia: "captura en demo-login-lista.md"
---

# L07 — Estados de carga en lista

**~5 h · Semana 2**

## Objetivo

Skeleton o spinner, deshabilitar doble tap, error con reintento.

## Por qué importa

Red móvil es lenta; la UI debe comunicarlo.

## Conceptos

- loading
- error retry

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tres capturas: loading, éxito, error en demo doc.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l07 estados-de-carga-en-lista"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M20 semana 2 | — |

## Hecho cuando

1. Tres estados UI
2. Reintento
3. Capturas

## Errores comunes

- Pantalla blanca
- Carga infinita

## Siguiente

[L08 — Roles: confiar en la API, no solo en UI](L08-roles-confiar-en-la-api-no-solo-en-ui.md)
