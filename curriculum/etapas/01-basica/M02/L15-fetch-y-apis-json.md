---
id: L15
materia: M02
orden: 15
titulo: fetch y APIs JSON
horas: 2.5
semana: 4
lectura: "MDN fetch + API pública JSON (ej. GitHub o JSONPlaceholder)"
evidencia: "src/async/fetch-ejemplo.ts con tipado de respuesta"
---

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
