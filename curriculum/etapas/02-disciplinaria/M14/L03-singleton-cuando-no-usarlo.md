---
id: L03
materia: M14
orden: 3
titulo: "Singleton: cuándo NO usarlo"
horas: 5.0
semana: 1
lectura: Singleton — abusos; DI como alternativa
evidencia: docs/anti-singleton.md + ejemplo DI vs global
---

# L03 — Singleton: cuándo NO usarlo

**~5.0 h · Semana 1**

Aprender patrones incluye rechazarlos. Hoy documentas por qué Agenda Ops no necesita Singleton de “AppContext”.

## Objetivo

Anti-patrón documentado + alternativa con inyección de dependencias simple.

## Pasos (hazlos en orden)

### 1. Lee Singleton (40–50 min)

Enfócate en problemas: estado global, orden de init, tests acoplados.

### 2. Escribe anti-singleton.md (60–70 min)

Incluye: “conexión DB como Singleton” vs “pasar `pool` al Repository”; “Config.getInstance()” vs `loadConfig()` en main.

### 3. Mini demo (50–60 min)

`src/examples/di-clock.ts`: reloj inyectable para tests (servirá en M15). Sin `getInstance()`.

### 4. Commit (15 min)

`docs(m14): anti-singleton y alternativa DI`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Cuándo Singleton duele (tests, estado global) y qué usar en su lugar | [Refactoring.Guru — Singleton (ES)](https://refactoring.guru/es/design-patterns/singleton) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. `docs/anti-singleton.md` explica ≥2 razones para no usarlo en DB/config del piloto.
2. Código de contraste: módulo con export de instancia vs factory/DI inyectable en tests.
3. Commit `docs(m14): anti-singleton y alternativa DI`.

## Errores comunes

- “Nunca uses Singleton” sin matiz (a veces un cache read-only está bien).
- Singleton de conexión PG que impide tests paralelos — y aún así lo adoptas.
- Documento sin ejemplo de código.

## Siguiente

[L04 — Cierre semana 1 — creacionales y bitácora](L04-cierre-semana-1-creacionales-y-bitacora.md)
