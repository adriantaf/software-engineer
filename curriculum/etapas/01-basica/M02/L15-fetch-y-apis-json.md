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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Script que descarga datos, los resume en consola y falla con
      mensaje si la red o el status fallan.


      No toda la data vive en tu disco. Fetch es el puente hacia servicios
      reales e IA APIs más adelante.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tipos de respuesta
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "fetch y APIs JSON" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/async/fetch-ejemplo.ts con tipado de respuesta
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
      ¿Es buena práctica en esta lección? “`as Tipo` sin validar forma del
      JSON."
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
          Script que descarga datos, los resume en consola y falla con mensaje
          si la red o el status fallan.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. CLI opcional `import`
    xp: 10
    cuerpo: >-
      Comando experimental `npx tsx src/cli.ts quote` que usa
      [JSONPlaceholder](https://jsonplaceholder.typicode.com/) o similar — solo
      si no complica demasiado; si no, deja script aparte.
  - id: s7
    tipo: explicacion
    titulo: 3. MDN fetch
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
