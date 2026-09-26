---
id: L06
materia: M17
orden: 6
titulo: API citas — crear y listar con reglas
horas: 5.0
semana: 2
lectura: REST + validación horarios
evidencia: POST/GET /citas
---

# L06 — API citas — crear y listar con reglas

**~5.0 h · Semana 2**

Core del piloto Agenda Ops.

## Objetivo

Endpoints crear/listar citas con auth, validación fin>inicio, no pasado sin override documentado.

## Conceptos clave

- REST
- 409 solapamiento
- paginación

## Pasos (hazlos en orden)

### 1. POST /citas autenticado (70–90 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/citas \
  -H 'content-type: application/json' \
  -d '{"clienteId":"...","servicioId":"...","inicio":"2026-10-01T15:00:00Z","fin":"2026-10-01T15:30:00Z"}'
# 201
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/citas \
  -H 'content-type: application/json' \
  -d '{"clienteId":"...","servicioId":"...","inicio":"2026-10-01T16:00:00Z","fin":"2026-10-01T15:00:00Z"}'
# 400 horario
```

### 2. GET /citas + reglas (50–60 min)

Listar con filtro fecha; 401 sin auth; 409 si documentas solapamiento.

```bash
curl -sS -b /tmp/ao.ck "http://localhost:3000/citas?desde=2026-10-01&hasta=2026-10-02"
curl -sS -o /dev/null -w "%{http_code}\n" http://localhost:3000/citas
# 401
```

### 3. Tests + commit (40 min)

```bash
npm test -- citas
git add projects/m17-agenda-ops
git commit -m "feat(m17): L06 api citas crear y listar"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | REST + validación horarios | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /citas` y `GET /citas` con auth; 401 sin sesión.
2. Tests 201, 400 horario y (si aplica) 409 solapamiento (artefacto: `POST/GET /citas`).
3. Commit `docs(m17): L06 api-citas-crear-y-listar-con-reglas`.

## Errores comunes

- Listar citas sin autenticación.
- Ignorar timezone / guardar strings locales ambiguos.

## Siguiente

[L07 — CRUD clientes y servicios](L07-crud-clientes-y-servicios.md)
