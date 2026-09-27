# Threat model v0 — Vitrina

## Actores

| Actor | Objetivos | Capacidades |
|-------|-----------|-------------|
| Dueño (owner) | | |
| Staff | | |
| Cliente final | | |
| Atacante anónimo | | |

## Activos (≥5)

| Activo | Confidencialidad | Dónde vive |
|--------|------------------|------------|
| | | |

## Boundaries

```
[Browser] --HTTPS--> [API] --> [Postgres]
                \-> [WhatsApp deep-link]
```

## STRIDE (L03)

| Letra | Amenaza en Vitrina | Mitigación / gap |
|-------|----------------------|------------------|
