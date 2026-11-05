---
id: L01
materia: M02
orden: 1
titulo: Entorno TS strict y primer programa
horas: 2.5
semana: 1
lectura: 'EJ cap. 1 (valores, tipos, estructura) + TS Handbook Everyday Types (intro)'
evidencia: 'projects/m02-katas/ con tsconfig strict, src/hola.ts ejecutable, README mínimo'
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin `strict` y sin hábito de leer errores del compilador, M02 se convierte
      en “JavaScript con archivos `.ts`”. Hoy instalas el suelo donde vivirán
      katas, el script P2 y la CLI.


      **Objetivo de esta lección:** Crear `projects/m02-katas/`, activar
      `strict: true`, ejecutar un programa tipado y documentar el setup en git.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Carpeta de evidencia
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m02-katas/src

      ```


      Desde la raíz del plan: Revisa `projects/m02-programacion/README.md` y
      enlaza esta carpeta si aún no está.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Inicializar Node + TypeScript
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m02-katas

      npm init -y

      npm install -D typescript tsx vitest @types/node

      npx tsc --init

      ```


      En `tsconfig.json` asegura: **No desactives `strict`** “para avanzar”. Ese
      atajo te cobra intereses en la semana 4.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Entorno TS strict y primer programa», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          Existe `projects/m02-katas/` con `strict: true` y `src/hola.ts` que
          corre.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Entorno TS strict y
          primer programa
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `mkdir -p projects/m02-katas/src`
    comandoEsperado:
      - mkdir -p projects/m02-katas/src
      - cd projects/m02-katas
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m02-katas/src'
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
          Crear `projects/m02-katas/`, activar `strict: true`, ejecutar un
          programa tipado y documentar el setup en git.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Primer programa tipado
    xp: 10
    cuerpo: >-
      `src/hola.ts`: Ejecuta: Rompe el tipo a propósito: `saludar(42)` y luego
      `npx tsc --noEmit`. **Lee el mensaje completo** (archivo, línea, tipo
      esperado). Corrige antes de seguir.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        Existe `projects/m02-katas/` con `strict: true` y `src/hola.ts` que
        corre.
      - Probaste un error de tipos con `tsc` y lo resumiste en una frase.
      - Commit en git con el proyecto katas.
      - Dos ejercicios del cap. 1 de EJ en TS bajo `src/`.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Entorno TS strict y primer programa

**~2.5 h · Semana 1**

Arrancas M02 con un proyecto TypeScript real: compilador en modo estricto, ejecución con `tsx` y tu primer error de tipos leído con calma.

## Objetivo

Crear `projects/m02-katas/`, activar `strict: true`, ejecutar un programa tipado y documentar el setup en git.

## Por qué empieza así

Sin `strict` y sin hábito de leer errores del compilador, M02 se convierte en “JavaScript con archivos `.ts`”. Hoy instalas el suelo donde vivirán katas, el script P2 y la CLI.

## Pasos (hazlos en orden)

### 1. Carpeta de evidencia (10 min)

Desde la raíz del plan:

```bash
mkdir -p projects/m02-katas/src
```

Revisa `projects/m02-programacion/README.md` y enlaza esta carpeta si aún no está.

### 2. Inicializar Node + TypeScript (25–35 min)

```bash
cd projects/m02-katas
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init
```

En `tsconfig.json` asegura:

```json
{
  "compilerOptions": {
    "strict": true,
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "target": "ES2022",
    "outDir": "dist",
    "rootDir": "src",
    "skipLibCheck": true
  },
  "include": ["src"]
}
```

**No desactives `strict`** “para avanzar”. Ese atajo te cobra intereses en la semana 4.

### 3. Primer programa tipado (30–40 min)

`src/hola.ts`:

```ts
function saludar(nombre: string): string {
  return `Hola, ${nombre}`;
}

console.log(saludar("Adrian"));
```

Ejecuta:

```bash
npx tsx src/hola.ts
```

Rompe el tipo a propósito: `saludar(42)` y luego `npx tsc --noEmit`. **Lee el mensaje completo** (archivo, línea, tipo esperado). Corrige antes de seguir.

### 4. README del repo de katas (20 min)

`projects/m02-katas/README.md` con Node, confirmación de strict, y comandos `tsx` / `npm test` (cuando exista).

### 5. Commit atómico (15 min)

```bash
git add projects/m02-katas
git commit -m "feat(m02): proyecto katas con TypeScript strict"
```

### 6. Lectura + 2 ejercicios EJ (40–50 min)

Lee *Eloquent JavaScript* **capítulo 1**. Resuelve **2 ejercicios** en `src/ej-cap01-<nombre>.ts` y ejecútalos con `tsx`.

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| *Eloquent JavaScript* | Cap. 1 | https://eloquentjavascript.net/ |
| TS Handbook | [Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) (intro) | Misma URL EN |
| Catálogo | Entrada M02 | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. Existe `projects/m02-katas/` con `strict: true` y `src/hola.ts` que corre.
2. Probaste un error de tipos con `tsc` y lo resumiste en una frase.
3. Commit en git con el proyecto katas.
4. Dos ejercicios del cap. 1 de EJ en TS bajo `src/`.

## Errores comunes

- Poner `"strict": false` sin leer las opciones.
- Solo ejecutar en el editor y no usar `tsx`/`tsc`.
- Instalar dependencias y no commitear.

## Siguiente

[L02 — Valores, primitivos y variables](L02-valores-primitivos-y-variables.md)
