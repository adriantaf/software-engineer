---
id: L01
materia: M02
orden: 1
titulo: Entorno TS strict y primer programa
horas: 2.5
semana: 1
lectura: "EJ cap. 1 (valores, tipos, estructura) + TS Handbook Everyday Types (intro)"
evidencia: "projects/m02-katas/ con tsconfig strict, src/hola.ts ejecutable, README mínimo"
---

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
