# M20 — Aplicaciones móviles (Vitrina)

Carpeta de **evidencia** de la app móvil del dueño. Si no está en git (aquí o con enlace claro), no cuenta.

## En resumen

El dueño vive en el teléfono: misma auth que la web, sesión segura, build instalable.

## Arranque

1. Elige Flutter **o** React Native → `stack-movil.md`.
2. Apunta la app al API staging de M17/M19 (no mocks eternos).
3. Deja el código en submódulo/repo hermano y enlázalo desde este README.

## Estructura esperada

```
projects/m20-movil/
├── README.md                 # enlace al código + paridad auth
├── stack-movil.md
├── auth-storage.md           # P2
├── demo-login-lista.md       # P1
├── build-evidence.md         # P3
├── docs/
│   ├── logging-policy.md
│   └── release-notes.md
└── (opcional) app/           # monorepo del cliente móvil
```

## Lecciones → artefactos

| Semana | Foco | Artefacto |
|--------|------|-----------|
| 1 | Scaffold + login + secure storage + 401 | storage doc |
| 2 | Lista pedidos, refresh, roles | demo-login-lista (P1) |
| 3 | Detalle, nav, acciones, deep link | |
| 4 | Vacío/offline/timeouts/logging | auth-storage + estados (P2) |
| 5 | Firma, release, demo cruzada | build-evidence (P3) |

## Checklist (Evidencia de hecho)

- **P1 — Login+lista:** App contra API real; `demo-login-lista.md`.
- **P2 — Estados:** `auth-storage.md` + vacío/error/401.
- **P3 — Build:** APK/artefacto en `build-evidence.md` en dispositivo real.
- **Proyecto — App CRM:** README con enlace al código y paridad auth web.

## Enlaces

- Ficha: `curriculum/etapas/02-disciplinaria/M20-aplicaciones-moviles.md`
- API: `projects/m17-vitrina/`
- Ops: `projects/m19-ops/`
- Plan: `/materia/M20/`
