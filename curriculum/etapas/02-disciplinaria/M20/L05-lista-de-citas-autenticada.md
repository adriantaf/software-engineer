---
id: L05
materia: M20
orden: 5
titulo: Lista de citas autenticada
horas: 5.0
semana: 2
lectura: ListView / FlatList patterns
evidencia: projects/m20-movil/demo-login-lista.md
---

# L05 — Lista de citas autenticada

**~5.0 h · Semana 2**

P1 M20: login + lista evidenciada.

## Objetivo

GET citas con token; mostrar fecha, cliente, servicio, estado.

## Conceptos clave

- Authorization header
- JSON parse
- orden

## Pasos (hazlos en orden)

### 1. GET /citas autenticado (80–100 min)

```bash
# Misma cookie/Bearer que web — documenta el esquema en stack-movil.md
curl -sS -b /tmp/st.ck "$API_BASE/citas"
```

Lista en UI con fecha/cliente/servicio.

### 2. Evidencia P1 (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Lista citas
Fecha demo: …  API: staging …  Resultado: OK
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L05 lista citas autenticada"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | ListView / FlatList patterns | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/demo-login-lista.md` registra lista de citas contra API real (P1).
2. Commit `docs(m20): L05 lista-de-citas-autenticada`.

## Errores comunes

- Lista desde JSON local fingiendo API.
- Sin auth header/cookie.

## Siguiente

[L06 — Pull-to-refresh y paginación simple](L06-pull-to-refresh-y-paginacion-simple.md)
