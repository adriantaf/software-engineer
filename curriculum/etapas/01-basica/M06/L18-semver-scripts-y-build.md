---
id: L18
materia: M06
orden: 18
titulo: Semver, scripts y build
horas: 5
semana: 5
lectura: "semver.org; npm version docs"
evidencia: "CHANGELOG o sección Releases; scripts prepublishOnly"
---

# L18 — Semver, scripts y build

**~5 h · Semana 5**

Versionar comunica rupturas. Semver es contrato con consumidores.

## Objetivo

Aplicar semver conscientemente; automatizar test+build antes de empaquetar; documentar cambios.

## Pasos

### 1. Lectura semver (30 min)

MAJOR.MINOR.PATCH con ejemplos de tu API.

### 2. Scripts (60 min)

```json
"scripts": {
  "test": "vitest run",
  "build": "tsc",
  "prepack": "npm run test && npm run build"
}
```

### 3. CHANGELOG (90 min)

Formato Keep a Changelog lite: Unreleased, 0.1.0 inicial.

### 4. Simular release (60 min)

```bash
npm version patch -m "chore(m06): release %s"
npm pack
```

Inspecciona tarball.

### 5. Política API (30 min)

README sección **Estabilidad**: qué es público vs experimental.

## Hecho cuando

1. Versión coherente con changelog.
2. `prepack`/`prepublishOnly` evita pack roto.
3. Tarball local instalable en proyecto de prueba (`npm i ../...tgz`).

## Errores comunes

- 1.0.0 el día uno sin API estable.
- Olvidar bump en package.json.

## Siguiente

[L19 — README, API pública y ejemplos](L19-readme-api-y-ejemplos.md)
