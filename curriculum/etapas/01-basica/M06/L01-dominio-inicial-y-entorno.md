---
id: L01
materia: M06
orden: 1
titulo: Dominio inicial y entorno del proyecto
horas: 5
semana: 1
lectura: >-
  Código limpio caps. 1–2 (limpieza, significado de nombres intro) + Pragmático
  DRY
evidencia: >-
  projects/m06-programacion-ii/ con package.json, tsconfig strict, src/dominio
  inicial
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M06 es ingeniería de software aplicada: modelas un dominio real sin
      frameworks web y con tipos estrictos.


      **Objetivo de esta lección:** Crear el proyecto TypeScript en
      `projects/m06-programacion-ii/`, elegir dominio (biblioteca o inventario)
      y definir interfaces nucleares con tests mínimos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Entorno
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m06-programacion-ii/src
      cd projects/m06-programacion-ii
      npm init -y
      npm install -D typescript tsx vitest @types/node
      npx tsc --init
      ```

      `strict: true`. Scripts: `"test": "vitest run"`, `"build": "tsc"`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Elige dominio
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m06-programacion-ii/src
      cd projects/m06-programacion-ii
      npm init -y
      npm install -D typescript tsx vitest @types/node
      npx tsc --init
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dominio inicial y entorno del proyecto», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Repo TS strict con ≥3 tests verdes.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dominio inicial y
          entorno del proyecto
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

      `mkdir -p projects/m06-programacion-ii/src`
    comandoEsperado:
      - mkdir -p projects/m06-programacion-ii/src
      - cd projects/m06-programacion-ii
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m06-programacion-ii/src'
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
          Crear el proyecto TypeScript en `projects/m06-programacion-ii/`,
          elegir dominio (biblioteca o inventario) y definir interfaces
          nucleares con tests mínimos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Interfaces
    xp: 10
    cuerpo: |-
      ```ts
      // src/model.ts — adapta nombres a tu dominio
      export interface Libro {
        id: string;
        titulo: string;
        prestado: boolean;
      }

      export interface RepositorioLibros {
        guardar(libro: Libro): void;
        obtener(id: string): Libro | undefined;
      }
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Repo TS strict con ≥3 tests verdes.
      - '`DOMINIO.md` describe el dominio elegido.'
      - Hay al menos una interfaz + implementación en memoria.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Dominio inicial y entorno del proyecto

**~5 h · Semana 1**

M06 es ingeniería de software aplicada: modelas un dominio real sin frameworks web y con tipos estrictos.

## Objetivo

Crear el proyecto TypeScript en `projects/m06-programacion-ii/`, elegir dominio (biblioteca o inventario) y definir interfaces nucleares con tests mínimos.

## Pasos

### 1. Entorno (45 min)

```bash
mkdir -p projects/m06-programacion-ii/src
cd projects/m06-programacion-ii
npm init -y
npm install -D typescript tsx vitest @types/node
npx tsc --init
```

`strict: true`. Scripts: `"test": "vitest run"`, `"build": "tsc"`.

### 2. Elige dominio (30 min)

Documenta en `DOMINIO.md`: actores, reglas de negocio, 5 operaciones core. Ejemplo biblioteca: agregar, prestar, devolver, buscar, listar disponibles.

### 3. Interfaces (90 min)

```ts
// src/model.ts — adapta nombres a tu dominio
export interface Libro {
  id: string;
  titulo: string;
  prestado: boolean;
}

export interface RepositorioLibros {
  guardar(libro: Libro): void;
  obtener(id: string): Libro | undefined;
}
```

### 4. Implementación en memoria (90 min)

Clase `BibliotecaMemoria` (o equivalente) con array o `Map`. Comportamiento real, no solo getters.

### 5. Tres tests (60 min)

Vitest: agregar, operación feliz, caso que debe fallar (libro inexistente). Deja el fallo **claro** (throw o Result; Result llega en L14).

### 6. Lectura CC (45 min)

Caps. 1–2: anota 5 reglas que aplicarás esta semana en comentarios al final de `DOMINIO.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Código limpio* | Caps. 1–2 |
| *Pragmático* | DRY (sección equivalente) |
| Catálogo | [Bibliografía · M06](../../../bibliografia.md#m06-programacion-ii) |


## Hecho cuando

1. Repo TS strict con ≥3 tests verdes.
2. `DOMINIO.md` describe el dominio elegido.
3. Hay al menos una interfaz + implementación en memoria.

## Errores comunes

- Elegir dominio enorme (ERP completo).
- Clase `Libro` con 20 propiedades irrelevantes.

## Siguiente

[L02 — Objetos con comportamiento real](L02-objetos-con-comportamiento-real.md)
