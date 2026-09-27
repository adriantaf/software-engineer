---
id: L01
materia: M20
orden: 1
titulo: Stack móvil y scaffold Agenda Ops
horas: 5.0
semana: 1
lectura: Flutter o RN — get started
evidencia: projects/m20-movil/stack.md + repo-url.md
---

# L01 — Stack móvil y scaffold Agenda Ops

**~5.0 h · Semana 1**

Un framework, un camino hasta M20 cierre.

## Objetivo

Elegir Flutter o RN, documentar SDK, crear scaffold y enlazar repo.

## Conceptos clave

- Flutter vs RN
- staging URL
- lint

## Pasos (hazlos en orden)

### 1. Decide Flutter o RN (25–35 min)

```bash
mkdir -p projects/m20-movil/docs
cat > projects/m20-movil/stack-movil.md << 'EOF'
# Stack móvil Agenda Ops
- Elección: Flutter X.Y  **o** React Native X.Y
- Por qué: …
- SDK / JDK: …
- No cambiar sin ADR
EOF
```

### 2. Scaffold app (90–110 min)

```bash
# Flutter:
# flutter create agenda_ops_app
# React Native:
# npx @react-native-community/cli init AgendaOpsApp
```

App corre en emulador/dispositivo. Deja el código en submódulo o `projects/m20-movil/app/` y enlázalo en README.

### 3. Evidencia + commit (30 min)

```bash
cat > projects/m20-movil/repo-url.md << 'EOF'
# Código móvil
Repo / ruta: …
Commit scaffold: …
EOF
# README m20 apunta a repo-url.md y stack-movil.md
git add projects/m20-movil
git commit -m "docs(m20): L01 scaffold stack movil"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Flutter o RN — get started | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existen `projects/m20-movil/stack-movil.md` y `projects/m20-movil/repo-url.md`.
2. Scaffold corre en emulador/dispositivo; README enlaza el código.
3. Commit `docs(m20): L01 stack-movil-y-scaffold-agenda-ops`.

## Errores comunes

- Cambiar Flutter↔RN en semana 3 sin ADR.
- Scaffold sin versión de SDK.

## Siguiente

[L02 — Pantalla login contra API staging](L02-pantalla-login-contra-api-staging.md)
