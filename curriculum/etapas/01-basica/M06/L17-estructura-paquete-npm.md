---
id: L17
materia: M06
orden: 17
titulo: Estructura de paquete npm
horas: 5
semana: 5
lectura: "Docs npm package.json; CC cap. 9 (pruebas) repaso"
evidencia: "package.json con exports, types, files; build dist/"
---

# L17 — Estructura de paquete npm

**~5 h · Semana 5**

Tu código pasa de carpeta de curso a **paquete** consumible.

## Objetivo

Organizar `src/`, `dist/`, entrypoints ESM/CJS según necesites; configurar `exports` y `types` en `package.json`.

## Pasos

### 1. Lectura npm (60 min)

Official docs: `package.json`, `exports`, `files`.

### 2. Layout (45 min)

```
src/
dist/   (gitignore)
tests/
README.md
```

### 3. tsconfig producción (60 min)

`outDir: dist`, `declaration: true`, `rootDir: src`.

### 4. package.json (90 min)

```json
{
  "name": "@tu-usuario/m06-biblioteca",
  "version": "0.1.0",
  "type": "module",
  "exports": { ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" } },
  "files": ["dist"]
}
```

Adapta nombre.

### 5. Verificación (45 min)

```bash
npm run build
npm pack --dry-run
```

## Hecho cuando

1. `npm run build` genera `.js` + `.d.ts`.
2. `npm pack --dry-run` lista solo lo necesario.
3. Tests siguen verdes.

## Errores comunes

- Publicar `src/` sin compilar.
- Olvidar `files` y subir basura.

## Siguiente

[L18 — Semver, scripts y build](L18-semver-scripts-y-build.md)
