---
id: L04
materia: M02
orden: 4
titulo: Funciones tipadas
horas: 2.5
semana: 1
lectura: EJ cap. 3 (funciones) + TS Handbook More on Functions
evidencia: src/funciones/ con 4+ funciones puras; ≥7 katas acumuladas en repo
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La CLI será una capa fina sobre funciones de dominio testeables. Practica
      sin acoplar todo a `console.log`.


      **Objetivo de esta lección:** Organizar `src/funciones/`, terminar
      ejercicios de EJ cap. 3 en TS y acumular **≥7 katas** (camino a P1).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Funciones puras
    xp: 10
    cuerpo: |-
      ```ts
      export type Comparador<T> = (a: T, b: T) => number;

      export function ordenarPor<T>(items: T[], cmp: Comparador<T>): T[] {
        return [...items].sort(cmp);
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Funciones como valores
    xp: 10
    cuerpo: |-
      ```ts
      export type Comparador<T> = (a: T, b: T) => number;

      export function ordenarPor<T>(items: T[], cmp: Comparador<T>): T[] {
        return [...items].sort(cmp);
      }
      ```

      `src/funciones/ordenar.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Funciones tipadas», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: '`src/funciones/` con ≥4 funciones exportadas y usadas.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Funciones tipadas
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Funciones gigantes que mezclan I/O y
      lógica."
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
          Organizar `src/funciones/`, terminar ejercicios de EJ cap. 3 en TS y
          acumular ≥7 katas (camino a P1).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: EJ cap. 3
    xp: 10
    cuerpo: '**≥2 ejercicios** en `src/ej-cap03-*.ts`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`src/funciones/` con ≥4 funciones exportadas y usadas.'
      - ≥7 katas o ejercicios EJ con solución propia.
      - Commit de cierre de semana 1 M02.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
