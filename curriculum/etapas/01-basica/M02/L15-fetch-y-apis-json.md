---
id: L15
materia: M02
orden: 15
titulo: fetch y APIs JSON
horas: 2.5
semana: 4
lectura: MDN fetch + API pública JSON (ej. GitHub o JSONPlaceholder)
evidencia: src/async/fetch-ejemplo.ts con tipado de respuesta
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      No toda la data vive en tu disco. Fetch es el puente hacia servicios
      reales e IA APIs más adelante.


      **Objetivo de esta lección:** Script que descarga datos, los resume en
      consola y falla con mensaje si la red o el status fallan.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Tipos de respuesta
    xp: 10
    cuerpo: >-
      ```ts

      export interface GithubUser {
        login: string;
        id: number;
        public_repos: number;
      }


      export async function fetchGithubUser(login: string): Promise<GithubUser>
      {
        const res = await fetch(`https://api.github.com/users/${login}`);
        if (!res.ok) {
          throw new Error(`GitHub respondió ${res.status}`);
        }
        return (await res.json()) as GithubUser;
      }

      ```


      `src/async/github-user.ts` (ejemplo):
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: CLI opcional `import`
    xp: 10
    cuerpo: >-
      ```ts

      export interface GithubUser {
        login: string;
        id: number;
        public_repos: number;
      }


      export async function fetchGithubUser(login: string): Promise<GithubUser>
      {
        const res = await fetch(`https://api.github.com/users/${login}`);
        if (!res.ok) {
          throw new Error(`GitHub respondió ${res.status}`);
        }
        return (await res.json()) as GithubUser;
      }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «fetch y APIs JSON», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: Script async descarga y muestra datos tipados.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de fetch y APIs JSON
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
    pregunta: ¿Es recomendable en esta lección? “`as Tipo` sin validar forma del JSON."
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
          Script que descarga datos, los resume en consola y falla con mensaje
          si la red o el status fallan.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: MDN fetch
    xp: 10
    cuerpo: Lee MDN *Using fetch* (ES o EN).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Script async descarga y muestra datos tipados.
      - Status 404/500 manejado con mensaje.
      - >-
        Commit con evidencia de ejecución (salida pegada en bitácora, no
        secretos).
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — fetch y APIs JSON

**~2.5 h · Semana 4**

Consumes un endpoint HTTP con `fetch`, compruebas `response.ok` y tipas el JSON con cuidado (sin confiar ciegamente).

## Objetivo

Script que descarga datos, los resume en consola y falla con mensaje si la red o el status fallan.

## Por qué importa

No toda la data vive en tu disco. Fetch es el puente hacia servicios reales e IA APIs más adelante.

## Pasos

### 1. Tipos de respuesta (30 min)

`src/async/github-user.ts` (ejemplo):

```ts
export interface GithubUser {
  login: string;
  id: number;
  public_repos: number;
}

export async function fetchGithubUser(login: string): Promise<GithubUser> {
  const res = await fetch(`https://api.github.com/users/${login}`);
  if (!res.ok) {
    throw new Error(`GitHub respondió ${res.status}`);
  }
  return (await res.json()) as GithubUser;
}
```

### 2. CLI opcional `import` (50 min)

Comando experimental `npx tsx src/cli.ts quote` que usa [JSONPlaceholder](https://jsonplaceholder.typicode.com/) o similar — solo si no complica demasiado; si no, deja script aparte.

### 3. MDN fetch (40 min)

Lee MDN *Using fetch* (ES o EN).

### 4. Rate limits y ética (15 min)

Anota en README: no abusar de APIs públicas en bucles.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| MDN | [fetch](https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. Script async descarga y muestra datos tipados.
2. Status 404/500 manejado con mensaje.
3. Commit con evidencia de ejecución (salida pegada en bitácora, no secretos).

## Errores comunes

- `as Tipo` sin validar forma del JSON.
- No timeout (opcional: menciona `AbortSignal` para más adelante).
- Commitear tokens en URLs.

## Siguiente

[L16 — Integrar async en el proyecto](L16-integrar-async-en-el-proyecto.md)
