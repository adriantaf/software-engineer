---
id: L05
materia: M20
orden: 5
titulo: Lista de citas autenticada
horas: 5
semana: 2
lectura: "ListView / FlatList patterns"
evidencia: "projects/m20-movil/demo-login-lista.md"
---

# L05 — Lista de citas autenticada

**~5 h · Semana 2**

## Objetivo

GET citas con token; mostrar fecha, cliente, servicio, estado.

## Por qué importa

P1 M20: login + lista evidenciada.

## Conceptos

- Authorization header
- JSON parse
- orden

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Captura lista + commit hash en demo-login-lista.md.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l05 lista-de-citas-autenticada"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| API | GET citas | SRS |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Lista con datos reales API
2. commit hash en doc
3. token adjunto

## Errores comunes

- Mock JSON
- Datos inventados

## Siguiente

[L06 — Pull-to-refresh y paginación simple](L06-pull-to-refresh-y-paginacion-simple.md)
