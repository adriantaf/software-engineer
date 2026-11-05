---
id: L01
materia: M04
orden: 1
titulo: Proyecto M04 y simulación de moneda
horas: 5
semana: 1
lectura: Walpole cap. 2 (intro probabilidad) · OpenStax Ch. 3 (inicio)
evidencia: >-
  projects/m04-stats/src/sim-moneda.ts + notas/ley-grandes-numeros.md
  commiteados
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      En producto y en SRE ves **muestras** (clics, errores, latencias). Sin
      simular primero, las fórmulas del libro suenan abstractas. Hoy conectas
      `Math.random()` con una pregunta real: “¿qué tan seguro estoy de esta
      proporción?”.


      **Objetivo de esta lección:** Crear `projects/m04-stats/`, simular 10_000
      lanzamientos de moneda en TypeScript y documentar en tus palabras la ley
      de los grandes números.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Carpeta de evidencia
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m04-stats/src projects/m04-stats/notas

      ```


      Desde la raíz del repo: Lee el checklist en
      [`projects/m04-stats/README.md`](../../../../projects/m04-stats/README.md).
      Es tu mapa de P1–P3 y del informe.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Proyecto TS mínimo
    xp: 10
    cuerpo: >-
      ```bash

      cd projects/m04-stats

      npm init -y

      npm install -D typescript tsx @types/node

      npx tsc --init

      ```


      Si aún no tienes `package.json` en `m04-stats`: En `src/sim-moneda.ts`:
      Ejecuta con `npx tsx src/sim-moneda.ts` (añade un `console.log` temporal o
      un pequeño `main`).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Proyecto M04 y simulación de moneda», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Proyecto M04 y
          simulación de moneda
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

      `mkdir -p projects/m04-stats/src projects/m04-stats/notas`
    comandoEsperado:
      - mkdir -p projects/m04-stats/src projects/m04-stats/notas
      - cd projects/m04-stats
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m04-stats/src projects/m04-stats/notas'
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
          Crear `projects/m04-stats/`, simular 10_000 lanzamientos de moneda en
          TypeScript y documentar en tus palabras la ley de los grandes números.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Experimento 100 vs 10_000
    xp: 10
    cuerpo: >-
      Compara `estimarP(100)` y `estimarP(10_000)` varias veces (bucle o
      script). Anota en una tabla: | n | p̂ (cara) | |p̂ − 0.5| |
      |---|----------|-----------| | 100 | | | | 10_000 | | | **Pregunta de
      producto:** si un feature tiene 52% de conversión con 80 usuarios, ¿es
      “mejor” que 50%? (Aún no hagas inferencia formal; solo intuición.)
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m04-stats/src/sim-moneda.ts` con `lanzar` y `estimarP`.
      - >-
        Corriste el experimento con al menos n = 100 y n = 10_000 y guardaste
        resultados en la nota o en comentarios del script.
      - >-
        Existe `notas/ley-grandes-numeros.md` con al menos un párrafo aplicado a
        producto.
      - Hay commit en git con esos archivos.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Proyecto M04 y simulación de moneda

**~5 h · Semana 1**

Arrancas la carpeta de evidencia de la materia y compruebas con código que la frecuencia relativa se acerca a la probabilidad teórica cuando aumentas el tamaño de muestra.

## Objetivo

Crear `projects/m04-stats/`, simular 10_000 lanzamientos de moneda en TypeScript y documentar en tus palabras la ley de los grandes números.

## Por qué empieza así

En producto y en SRE ves **muestras** (clics, errores, latencias). Sin simular primero, las fórmulas del libro suenan abstractas. Hoy conectas `Math.random()` con una pregunta real: “¿qué tan seguro estoy de esta proporción?”.

## Pasos (hazlos en orden)

### 1. Carpeta de evidencia (15–20 min)

Desde la raíz del repo:

```bash
mkdir -p projects/m04-stats/src projects/m04-stats/notas
```

Lee el checklist en [`projects/m04-stats/README.md`](../../../../projects/m04-stats/README.md). Es tu mapa de P1–P3 y del informe.

### 2. Proyecto TS mínimo (30–40 min)

Si aún no tienes `package.json` en `m04-stats`:

```bash
cd projects/m04-stats
npm init -y
npm install -D typescript tsx @types/node
npx tsc --init
```

En `src/sim-moneda.ts`:

```ts
export type CaraCruz = "cara" | "cruz";

export function lanzar(): CaraCruz {
  return Math.random() < 0.5 ? "cara" : "cruz";
}

export function estimarP(n: number): { caras: number; p: number } {
  let caras = 0;
  for (let i = 0; i < n; i++) if (lanzar() === "cara") caras++;
  return { caras, p: caras / n };
}
```

Ejecuta con `npx tsx src/sim-moneda.ts` (añade un `console.log` temporal o un pequeño `main`).

### 3. Experimento 100 vs 10_000 (45–60 min)

Compara `estimarP(100)` y `estimarP(10_000)` varias veces (bucle o script). Anota en una tabla:

| n | p̂ (cara) | |p̂ − 0.5| |
|---|----------|-----------|
| 100 | | |
| 10_000 | | |

**Pregunta de producto:** si un feature tiene 52% de conversión con 80 usuarios, ¿es “mejor” que 50%? (Aún no hagas inferencia formal; solo intuición.)

### 4. Nota escrita (30–40 min)

Crea `projects/m04-stats/notas/ley-grandes-numeros.md`:

```markdown
# Ley de los grandes números — mis palabras

## Qué observé en la simulación
-

## Qué significa para métricas de producto (1 párrafo)
-

## Qué NO significa (error común)
-
```

### 5. Commit (15 min)

```bash
git add projects/m04-stats/
git commit -m "feat(m04): simulación moneda y nota LGN"
```

### 6. Lectura (45–60 min)

Walpole **cap. 2** (eventos, probabilidad) hasta reglas básicas, o OpenStax **Ch. 3** (inicio). Subraya solo definiciones que usarás en L02.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Walpole | Cap. 2 — introducción y frecuencia relativa |
| OpenStax | Ch. 3 — Probability Topics (primeras secciones) |
| Plan | [Ficha M04](../M04-probabilidad-estadistica.md) — objetivos |
| Catálogo | [Bibliografía · M04](../../../bibliografia.md#m04-probabilidad-y-estadistica) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m04-stats/src/sim-moneda.ts` con `lanzar` y `estimarP`.
2. Corriste el experimento con al menos n = 100 y n = 10_000 y guardaste resultados en la nota o en comentarios del script.
3. Existe `notas/ley-grandes-numeros.md` con al menos un párrafo aplicado a producto.
4. Hay commit en git con esos archivos.

Esto avanza la **P1** de la materia.

## Errores comunes

- Simular una vez y creer que “ya probaste la teoría”.
- Olvidar commitear: sin evidencia en git no cuenta para la UI.
- Confundir “la media de muchas muestras” con “una muestra grande” (lo profundizas en L13).

## Siguiente

[L02 — Eventos, reglas y frecuentismo](L02-eventos-y-probabilidad-basica.md)
