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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Tu código pasa de carpeta de curso a **paquete** consumible.


      **Objetivo de esta lección:** Organizar `src/`, `dist/`, entrypoints
      ESM/CJS según necesites; configurar `exports` y `types` en `package.json`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura npm
    xp: 10
    cuerpo: |-
      ```json
      {
        "name": "@tu-usuario/m06-biblioteca",
        "version": "0.1.0",
        "type": "module",
        "exports": { ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" } },
        "files": ["dist"]
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Layout
    xp: 10
    cuerpo: |-
      ```text
      src/
      dist/   (gitignore)
      tests/
      README.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Estructura de paquete npm», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`npm run build` genera `.js` + `.d.ts`.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Estructura de paquete
          npm
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Publicar `src/` sin compilar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Organizar `src/`, `dist/`, entrypoints ESM/CJS según necesites;
          configurar `exports` y `types` en `package.json`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: tsconfig producción
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
