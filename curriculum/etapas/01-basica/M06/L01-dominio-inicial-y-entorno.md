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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear el proyecto TypeScript en
      `projects/m06-programacion-ii/`, elegir dominio (biblioteca o inventario)
      y definir interfaces nucleares con tests mínimos.


      M06 es ingeniería de software aplicada: modelas un dominio real sin
      frameworks web y con tipos estrictos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Entorno
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Dominio inicial y entorno del proyecto" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: >-
          projects/m06-programacion-ii/ con package.json, tsconfig strict,
          src/dominio inicial
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `mkdir -p projects/m06-programacion-ii/src`
    comandoEsperado:
      - mkdir -p projects/m06-programacion-ii/src
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m06-programacion-ii/src'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Crear el proyecto TypeScript en `projects/m06-programacion-ii/`,
          elegir dominio (biblioteca o inventario) y definir interfaces
          nucleares co…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Elige dominio
    xp: 10
    cuerpo: >-
      Documenta en `DOMINIO.md`: actores, reglas de negocio, 5 operaciones core.
      Ejemplo biblioteca: agregar, prestar, devolver, buscar, listar
      disponibles.
  - id: s7
    tipo: ejemplo
    titulo: 3. Interfaces
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
