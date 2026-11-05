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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Organizar `src/funciones/`, terminar ejercicios de EJ cap. 3
      en TS y acumular **≥7 katas** (camino a P1).


      La CLI será una capa fina sobre funciones de dominio testeables. Practica
      sin acoplar todo a `console.log`.
  - id: s2
    tipo: ejemplo
    titulo: 1. Funciones puras
    xp: 10
    cuerpo: |-
      ```ts
      export type Comparador<T> = (a: T, b: T) => number;

      export function ordenarPor<T>(items: T[], cmp: Comparador<T>): T[] {
        return [...items].sort(cmp);
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Funciones tipadas" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/funciones/ con 4+ funciones puras; ≥7 katas acumuladas en repo
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Funciones gigantes que mezclan I/O y
      lógica."
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
          Organizar `src/funciones/`, terminar ejercicios de EJ cap. 3 en TS y
          acumular **≥7 katas** (camino a P1).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Funciones como valores
    xp: 10
    cuerpo: |-
      `src/funciones/ordenar.ts`:

      ```ts
      export type Comparador<T> = (a: T, b: T) => number;

      export function ordenarPor<T>(items: T[], cmp: Comparador<T>): T[] {
        return [...items].sort(cmp);
      }
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. EJ cap. 3
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
