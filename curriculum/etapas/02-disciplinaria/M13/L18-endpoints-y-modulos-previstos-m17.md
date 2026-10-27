---
id: L18
materia: M13
orden: 18
titulo: Endpoints y módulos previstos M17
horas: 5.0
semana: 5
lectura: Lista de rutas API y módulos de código previstos
evidencia: projects/m13-diseno/endpoints-m17.md
---

# L18 — Endpoints y módulos previstos M17

**~5.0 h · Semana 5**

Puente explícito al scaffold: qué rutas y carpetas nacerán en M17.

## Objetivo

`endpoints-m17.md` breve y accionable.

## Pasos (hazlos en orden)

### 1. Tabla de endpoints (70–90 min)

| Método | Ruta | Auth | Éxito | Errores |
|--------|------|------|-------|---------|
| POST | /auth/login | no | 200 | 401 |
| POST | /pedidos | sí | 201 | 400/401/403/409 |
| GET | /pedidos | sí | 200 | 401 |
| … | … | … | … | … |

### 2. Módulos (40 min)

```text
auth/  clientes/  servicios/  pedidos/
```

Relación con capas de L09.

### 3. Enlaza desde README (20 min)

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): endpoints y modulos previstos M17"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Contrato tentativo de API y módulos para el scaffold M17 | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `endpoints-m17.md` lista métodos/rutas Must con DTO/status resumidos.
2. Mapa módulo → carpeta (`auth`, `orders`, `clientes`).
3. Commit `docs(m13): endpoints y modulos previstos M17`.

## Errores comunes

- OpenAPI de 80 rutas para el MVP.
- Endpoints sin auth marcada.
- Módulos que no coinciden con arquitectura.md.

## Siguiente

[L19 — Checklist listo para scaffold](L19-checklist-listo-para-scaffold.md)
