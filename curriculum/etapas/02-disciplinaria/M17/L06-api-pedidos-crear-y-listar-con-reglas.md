---
id: L06
materia: M17
orden: 6
titulo: API pedidos — crear y listar con reglas
horas: 5.0
semana: 2
lectura: REST + validación horarios
evidencia: POST/GET /pedidos
---

# L06 — API pedidos — crear y listar con reglas

**~5.0 h · Semana 2**

Core del piloto Vitrina.

## Objetivo

Endpoints crear/listar pedidos con auth, validación fin>inicio, no pasado sin override documentado.

## Conceptos clave

- REST
- 409 solapamiento
- paginación

## Pasos (hazlos en orden)

### 1. POST /pedidos autenticado (70–90 min)

```bash
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/pedidos \
  -H 'content-type: application/json' \
  -d '{"clienteId":"...","servicioId":"...","inicio":"2026-10-01T15:00:00Z","fin":"2026-10-01T15:30:00Z"}'
# 201
curl -sS -b /tmp/ao.ck -X POST http://localhost:3000/pedidos \
  -H 'content-type: application/json' \
  -d '{"clienteId":"...","servicioId":"...","inicio":"2026-10-01T16:00:00Z","fin":"2026-10-01T15:00:00Z"}'
# 400 horario
```

### 2. GET /pedidos + reglas (50–60 min)

Listar con filtro fecha; 401 sin auth; 409 si documentas solapamiento.

```bash
curl -sS -b /tmp/ao.ck "http://localhost:3000/pedidos?desde=2026-10-01&hasta=2026-10-02"
curl -sS -o /dev/null -w "%{http_code}\n" http://localhost:3000/pedidos
# 401
```

### 3. Tests + commit (40 min)

```bash
npm test -- pedidos
git add projects/m17-vitrina
git commit -m "feat(m17): L06 api pedidos crear y listar"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | REST + validación horarios | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /pedidos` y `GET /pedidos` con auth; 401 sin sesión.
2. Tests 201, 400 horario y (si aplica) 409 solapamiento (artefacto: `POST/GET /pedidos`).
3. Commit `docs(m17): L06 api-pedidos-crear-y-listar-con-reglas`.

## Errores comunes

- Listar pedidos sin autenticación.
- Ignorar timezone / guardar strings locales ambiguos.

## Siguiente

[L07 — CRUD clientes y servicios](L07-crud-clientes-y-servicios.md)
