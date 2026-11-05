---
id: L17
materia: M06
orden: 17
titulo: Estructura de paquete npm
horas: 5
semana: 5
lectura: Docs npm package.json; CC cap. 9 (pruebas) repaso
evidencia: 'package.json con exports, types, files; build dist/'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Organizar `src/`, `dist/`, entrypoints ESM/CJS según
      necesites; configurar `exports` y `types` en `package.json`.


      Tu código pasa de carpeta de curso a **paquete** consumible.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura npm
    xp: 10
    cuerpo: |-
      ```text
      src/
      dist/   (gitignore)
      tests/
      README.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Estructura de paquete npm" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: 'package.json con exports, types, files; build dist/'
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Publicar `src/` sin compilar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Organizar `src/`, `dist/`, entrypoints ESM/CJS según necesites;
          configurar `exports` y `types` en `package.json`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Layout
    xp: 10
    cuerpo: |-
      ```
      src/
      dist/   (gitignore)
      tests/
      README.md
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. tsconfig producción
    xp: 10
    cuerpo: '`outDir: dist`, `declaration: true`, `rootDir: src`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`npm run build` genera `.js` + `.d.ts`.'
      - '`npm pack --dry-run` lista solo lo necesario.'
      - Tests siguen verdes.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
