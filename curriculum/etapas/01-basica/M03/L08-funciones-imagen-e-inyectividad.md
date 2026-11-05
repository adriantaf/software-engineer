---
id: L08
materia: M03
orden: 8
titulo: 'Funciones — imagen, inyectividad y biyección'
horas: 3
semana: 2
lectura: 'Rosen Cap. 2.3 — funciones, imagen, inyectiva, sobreyectiva, biyectiva'
evidencia: apuntes/funciones.md + src/functions.ts (predicados) + 1 demo inyectividad
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana 2 relacionando conjuntos con **funciones** (la base de
      map/filter y de cardinalidad).


      **Objetivo de esta lección:** Definir función como relación funcional;
      clasificar inyectiva / sobreyectiva / biyectiva; implementar predicados
      sobre funciones finitas `f: A → B`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Apuntes
    xp: 10
    cuerpo: |-
      ```ts
      export function esInyectiva<A>(f: Map<A, unknown>): boolean {
        const vistos = new Set<unknown>();
        for (const v of f.values()) {
          if (vistos.has(v)) return false;
          vistos.add(v);
        }
        return true;
      }

      export function esSobreyectiva<A, B>(
        f: Map<A, B>,
        codominio: Set<B>,
      ): boolean {
        const imagen = new Set(f.values());
        for (const y of codominio) if (!imagen.has(y)) return false;
        return true;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Demostración corta
    xp: 10
    cuerpo: |-
      ```ts
      export function esInyectiva<A>(f: Map<A, unknown>): boolean {
        const vistos = new Set<unknown>();
        for (const v of f.values()) {
          if (vistos.has(v)) return false;
          vistos.add(v);
        }
        return true;
      }

      export function esSobreyectiva<A, B>(
        f: Map<A, B>,
        codominio: Set<B>,
      ): boolean {
        const imagen = new Set(f.values());
        for (const y of codominio) if (!imagen.has(y)) return false;
        return true;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Funciones — imagen, inyectividad y biyección», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `funciones.md` con definiciones y al menos un ejemplo de cada tipo de
          función.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Funciones — imagen,
          inyectividad y biye…
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
    pregunta: ¿Es recomendable en esta lección? “Confundir codominio con imagen."
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
          Definir función como relación funcional; clasificar inyectiva /
          sobreyectiva / biyectiva; implementar predicados sobre funciones
          finitas `f: A → B`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Implementación finita
    xp: 10
    cuerpo: >-
      Modela `f` como `Map<A,B>` o `Record` con dominio listado.
      `src/functions.ts`: Importa `esSubconjunto` solo si lo reutilizas; la
      versión con bucle deja claro el cuantificador ∀y ∈ codominio. Tests con
      funciones en dominios de 3–4 elementos.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `funciones.md` con definiciones y al menos un ejemplo de cada tipo de
        función.
      - Predicados inyectiva/sobreyectiva con tests en dominio finito.
      - Demo 6 en `demos.md` commiteada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Funciones: imagen, inyectividad y biyección

**~3 h · Semana 2**

Cierras la semana 2 relacionando conjuntos con **funciones** (la base de map/filter y de cardinalidad).

## Objetivo

Definir función como relación funcional; clasificar inyectiva / sobreyectiva / biyectiva; implementar predicados sobre funciones finitas `f: A → B`.

## Pasos

### 1. Apuntes (40–50 min)

`projects/m03-discretas/apuntes/funciones.md`:

- `f: A → B`, dominio, codominio, imagen `f(S)`.
- Definiciones formales de inyectiva, sobreyectiva, biyectiva.
- Ejemplo: `f: ℤ → ℤ`, `f(n)=2n` (inyectiva, no sobreyectiva) — ajusta si usas ℕ.

### 2. Demostración corta (40 min)

**Demo 6** en `demos.md`: prueba de que la composición de dos funciones inyectivas es inyectiva (o ejercicio equivalente del Rosen).

### 3. Implementación finita (60–70 min)

Modela `f` como `Map<A,B>` o `Record` con dominio listado.

`src/functions.ts`:

```ts
export function esInyectiva<A>(f: Map<A, unknown>): boolean {
  const vistos = new Set<unknown>();
  for (const v of f.values()) {
    if (vistos.has(v)) return false;
    vistos.add(v);
  }
  return true;
}

export function esSobreyectiva<A, B>(
  f: Map<A, B>,
  codominio: Set<B>,
): boolean {
  const imagen = new Set(f.values());
  for (const y of codominio) if (!imagen.has(y)) return false;
  return true;
}
```

Importa `esSubconjunto` solo si lo reutilizas; la versión con bucle deja claro el cuantificador ∀y ∈ codominio.

Tests con funciones en dominios de 3–4 elementos.

### 4. Retro semana 2 (15 min)

Nota en `conjuntos.md` o bitácora: qué operación de `sets.ts` usarás en relaciones (semana 3).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 2.3 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `funciones.md` con definiciones y al menos un ejemplo de cada tipo de función.
2. Predicados inyectiva/sobreyectiva con tests en dominio finito.
3. **Demo 6** en `demos.md` commiteada.

## Errores comunes

- Confundir codominio con imagen.
- Probar inyectividad solo con 2 valores.
- Sobreyectiva: olvidar un elemento del codominio.

## Siguiente

[L09 — Relaciones y propiedades](L09-relaciones-y-propiedades.md)
