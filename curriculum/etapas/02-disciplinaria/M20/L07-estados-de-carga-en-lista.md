---
id: L07
materia: M20
orden: 7
titulo: Estados de carga en lista
horas: 5.0
semana: 2
lectura: UX loading skeletons
evidencia: captura en demo-login-lista.md
---

# L07 — Estados de carga en lista

**~5.0 h · Semana 2**

Red móvil es lenta; la UI debe comunicarlo.

## Objetivo

Skeleton o spinner, deshabilitar doble tap, error con reintento.

## Conceptos clave

- loading
- error retry

## Pasos (hazlos en orden)

### 1. Estados loading/error (60–80 min)

Spinner inicial; banner error con “Reintentar”; no lista fantasma.

### 2. Captura en demo doc (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Estados carga
loading: …  error: … (captura redactada opcional)
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L07 estados carga lista"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | UX loading skeletons | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Estados loading/error documentados en demo-login-lista.md.
2. Commit `docs(m20): L07 estados-de-carga-en-lista`.

## Errores comunes

- Error silencioso (lista vacía falsa).
- Loading eterno.

## Siguiente

[L08 — Roles: confiar en la API, no solo en UI](L08-roles-confiar-en-la-api-no-solo-en-ui.md)
