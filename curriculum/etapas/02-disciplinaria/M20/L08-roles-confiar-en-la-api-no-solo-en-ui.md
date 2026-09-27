---
id: L08
materia: M20
orden: 8
titulo: "Roles: confiar en la API, no solo en UI"
horas: 5.0
semana: 2
lectura: RBAC móvil
evidencia: nota rbac en demo-login-lista.md
---

# L08 — Roles: confiar en la API, no solo en UI

**~5.0 h · Semana 2**

Doble fuente de verdad mata proyectos.

## Objetivo

Probar cuenta staff vs owner; ocultar acciones que API niega con 403.

## Conceptos clave

- 403 handling
- roles

## Pasos (hazlos en orden)

### 1. Confía en API para RBAC (50–60 min)

```bash
# staff token → acción owner debe fallar 403 aunque el botón exista
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" "$API_BASE/admin/staff"
```

### 2. Nota rbac (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## RBAC
UI puede ocultar; autorización real = API 403. Probado: …
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "docs(m20): L08 roles confiar en api"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | RBAC móvil | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Nota RBAC: UI puede ocultar; 403 de API verificado (staff vs owner).
2. Commit `docs(m20): L08 roles-confiar-en-la-api-no-solo-en-ui`.

## Errores comunes

- Ocultar botón y creer que es seguridad.
- Ignorar 403 de la API.

## Siguiente

[L09 — Pantalla detalle de cita](L09-pantalla-detalle-de-cita.md)
