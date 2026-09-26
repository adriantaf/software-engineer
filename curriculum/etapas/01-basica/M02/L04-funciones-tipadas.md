---
id: L04
materia: M02
orden: 4
titulo: Funciones tipadas
horas: 2.5
semana: 1
lectura: "EJ cap. 3 (funciones) + TS Handbook More on Functions"
evidencia: "src/funciones/ con 4+ funciones puras; ≥7 katas acumuladas en repo"
---

# L04 — Funciones tipadas

**~2.5 h · Semana 1**

Cierras la semana 1 con funciones como contratos: parámetros, retornos, pureza y valores por defecto.

## Objetivo

Organizar `src/funciones/`, terminar ejercicios de EJ cap. 3 en TS y acumular **≥7 katas** (camino a P1).

## Por qué importa

La CLI será una capa fina sobre funciones de dominio testeables. Practica sin acoplar todo a `console.log`.

## Pasos

### 1. Funciones puras (50 min)

`src/funciones/texto.ts` — `truncar`, `normalizarEspacios`.  
`src/funciones/numeros.ts` — `clamp(valor, min, max)`.

### 2. Funciones como valores (30 min)

`src/funciones/ordenar.ts`:

```ts
export type Comparador<T> = (a: T, b: T) => number;

export function ordenarPor<T>(items: T[], cmp: Comparador<T>): T[] {
  return [...items].sort(cmp);
}
```

### 3. EJ cap. 3 (45 min)

**≥2 ejercicios** en `src/ej-cap03-*.ts`.

### 4. Katas hasta 7 (30 min)

Cuenta L02–L03; completa hasta **7** soluciones en `src/katas/`.

### 5. Retro semana 1 (15 min)

Nota en bitácora: horas, katas, un error de tipos que te costó.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 3 |
| TS Handbook | [More on Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html) |

## Hecho cuando

1. `src/funciones/` con ≥4 funciones exportadas y usadas.
2. ≥7 katas o ejercicios EJ con solución propia.
3. Commit de cierre de semana 1 M02.

## Errores comunes

- Funciones gigantes que mezclan I/O y lógica.
- Opcionales sin default documentado.
- Copiar katas sin reescribir.

## Siguiente

[L05 — Arrays y métodos esenciales](L05-arrays-y-metodos-esenciales.md)
