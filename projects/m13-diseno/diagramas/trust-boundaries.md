# Trust boundaries — Agenda Ops (piloto)

Completa en **L01** (y actualiza en **L12**).

## Diagrama

```mermaid
flowchart LR
  U[Usuario / browser] -->|HTTPS + cookie sesión| API[API Node]
  API -->|SQL parametrizado| DB[(PostgreSQL)]
```

## Qué cruza cada límite

| Límite | Datos / credenciales | Quién valida |
|--------|----------------------|--------------|
| Browser → API | | |
| API → DB | | |

## Nota de amenaza (alto nivel)

- 
