---
id: M14
titulo: Patrones de software
etapa: disciplinaria
orden: 14
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Implementar Strategy, Observer, Factory
  - id: p2
    titulo: Repository + Service en el backend
  - id: p3
    titulo: Refactor de un módulo legacy tuyo
proyecto:
  id: proj
  titulo: Aplicar ≥5 patrones en Agenda Ops con justificación
---

# M14 — Patrones de software

## Por qué existe

Los patrones son vocabulario compartido entre ingenieros: aceleran revisiones y ADRs. Mal usados se convierten en **cargo cult** (clases llamadas `Factory` que solo hacen `new`). En esta materia aplicas patrones **en el código del piloto Agenda Ops** (o en un módulo de práctica que luego integrarás en M17), siempre con justificación escrita en `projects/m14-patrones/`.

**En resumen:** aplicas pocos patrones con justificación (no nombres de adorno) en el dominio de citas, precios o notificaciones.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Reconocer cuándo un patrón GoF aporta flexibilidad real vs complejidad innecesaria.
2. Implementar Strategy, Observer y Factory con tests unitarios mínimos.
3. Estructurar backend con Repository + Service acorde a M13.
4. Refactorizar un módulo “legacy” propio (código previo del plan o spike) sin cambiar comportamiento observable.
5. Documentar ≥5 patrones aplicados con ADR o ficha en `projects/m14-patrones/`.
6. Articular cuándo **no** usar Singleton u otros patrones sobrevalorados.

## Cómo estudiar esta materia (lecciones)

M14 aplica patrones con justificación en el dominio **Agenda Ops**: L01–L16 en orden.

1. Un patrón por lección: leer → implementar en TypeScript → test → ADR o nota.
2. Marca la lección solo si cumples “Hecho cuando”.
3. Evidencia en `projects/m14-patrones/` (o repo producto enlazado en README).
4. Cada patrón sin justificación escrita **no cuenta** para el proyecto.
5. [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura patrones | 6–8 | Lecciones de la semana (4× ~5 h) |
| Implementar + tests | 6–8 | Código en `src/` |
| ADR / fichas | 4–6 | Por qué cada patrón |
| Retro | 1 | Anti-patrón que evitaste |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la lectura de esa lección.

## Lecciones

### Semana 1 — Patrones creacionales y Strategy (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Entorno M14 y Strategy de precios](M14/L01-entorno-m14-y-strategy-de-precios.md) | 5 |
| L02 | [Factory Method para notificadores de canal](M14/L02-factory-method-para-notificadores-de-canal.md) | 5 |
| L03 | [Singleton: cuándo NO usarlo](M14/L03-singleton-cuando-no-usarlo.md) | 5 |
| L04 | [Cierre semana 1 — creacionales y bitácora](M14/L04-cierre-semana-1-creacionales-y-bitacora.md) | 5 |

### Semana 2 — Patrones estructurales y regresión (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Adapter para API de calendario externo](M14/L05-adapter-para-api-de-calendario-externo.md) | 5 |
| L06 | [Decorator para logging de operaciones de cita](M14/L06-decorator-para-logging-de-operaciones-de-cita.md) | 5 |
| L07 | [Facade para el flujo agendar cita](M14/L07-facade-para-el-flujo-agendar-cita.md) | 5 |
| L08 | [Tests de regresión en API pública del módulo](M14/L08-tests-de-regresion-en-api-publica-del-modulo.md) | 5 |

### Semana 3 — Patrones de comportamiento y P1 (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Observer para eventos de dominio](M14/L09-observer-para-eventos-de-dominio.md) | 5 |
| L10 | [Command para acciones admin reversibles](M14/L10-command-para-acciones-admin-reversibles.md) | 5 |
| L11 | [Cierre P1 — Strategy, Observer y Factory](M14/L11-cierre-p1-strategy-observer-y-factory.md) | 5 |
| L12 | [Repaso comportamiento y anti-patrón propio](M14/L12-repaso-comportamiento-y-anti-patron-propio.md) | 5 |

### Semana 4 — Repository, Service y proyecto (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Repository — interfaz Cita sin SQL](M14/L13-repository-interfaz-cita-sin-sql.md) | 5 |
| L14 | [Service — capa aplicación de citas](M14/L14-service-capa-aplicacion-de-citas.md) | 5 |
| L15 | [Refactor P3 — módulo legacy antes y después](M14/L15-refactor-p3-modulo-legacy-antes-y-despues.md) | 5 |
| L16 | [Cierre M14 — cinco patrones e integración M17](M14/L16-cierre-m14-cinco-patrones-e-integracion-m17.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Patrones de diseño* — GoF (ed. ES si hay). Alternativa: [Refactoring.Guru ES](https://refactoring.guru/es/design-patterns). Ver [bibliografía](../../bibliografia.md#m14-patrones).

| Semana | Lecciones | Patrones / capítulos | Alternativa |
|--------|-----------|----------------------|-------------|
| 1 | L01–L04 | **Creacionales** + Strategy precios | Refactoring.Guru Factory / Singleton (cuándo NO) |
| 2 | L05–L08 | **Estructurales**: Adapter, Decorator, Facade | Tests de regresión en API pública |
| 3 | L09–L12 | **Comportamiento**: Observer, Command; cierre P1 | Strategy + Observer + Factory documentados |
| 4 | L13–L16 | **Repository / Service** + refactor P3 + ≥5 patrones | `projects/m14-patrones/README.md` |

**Regla:** patrón sin justificación escrita = no cuenta.



## Ejemplo — Strategy (TypeScript)

```ts
export type CalculoPrecio = { calcular(base: number): number };

export const tarifaBase: CalculoPrecio = {
  calcular: (base) => base,
};

export const tarifaPromoDiez: CalculoPrecio = {
  calcular: (base) => Math.round(base * 0.9 * 100) / 100,
};

export function totalServicio(base: number, estrategia: CalculoPrecio): number {
  return estrategia.calcular(base);
}
```

## Ejemplo — Repository (interfaz)

```ts
export interface CitaRepository {
  findById(id: string, negocioId: string): Promise<Cita | null>;
  save(cita: Cita): Promise<void>;
}
// La implementación Postgres vive en infrastructure; el dominio no importa SQL.
```

## Temario semanal

### Semana 1 — Patrones creacionales (~20 h)

- Factory Method / Abstract Factory (solo si hay varias familias de objetos).
- Singleton: cuándo evitarlo (estado global, tests difíciles).
- Implementación práctica: Factory para crear notificadores o parsers de canal (email vs WhatsApp link).
- Ficha ADR por patrón creacional usado.

### Semana 2 — Patrones estructurales (~20 h)

- Adapter para integrar librería de terceros con tu interfaz de dominio.
- Decorator para añadir logging o métricas sin ensuciar el core.
- Facade para simplificar un subsistema (p. ej. “agendar cita” que coordina validación + persistencia).
- Tests de regresión en comportamiento público.

### Semana 3 — Patrones de comportamiento (~20 h)

- Strategy (precios, políticas de no-show).
- Observer (eventos de dominio: cita creada → auditoría o recordatorio futuro).
- Command (opcional: cola de acciones admin reversibles).
- Cierre P1: Strategy + Observer + Factory documentados con tests.

### Semana 4 — Capas Repository/Service + proyecto (~20 h)

- Repository + Service en backend alineado a M13.
- Refactor P3: módulo legacy propio (antes/después + diff en notas).
- ADR resumen: ≥5 patrones con contexto Agenda Ops.
- Plan de integración en repo M17 si el código vive en `projects/m14-patrones/`.


## Prácticas

1. **P1 — 3 patrones:** Strategy, Observer y Factory con tests en `projects/m14-patrones/src/` (o repo producto con ruta documentada).
2. **P2 — Repo/Service:** Capa backend (aunque sea spike) con interfaces de dominio separadas de Postgres.
3. **P3 — Refactor:** `projects/m14-patrones/refactor-notas.md` con módulo antes/después y commits o diff.

## Proyecto útil

**≥5 patrones justificados en Agenda Ops:** entrega en `projects/m14-patrones/`:

- Índice `README.md` listando patrón → archivo → ADR.
- Código ejecutable y tests verdes.
- ADRs cortos (uno por patrón o uno consolidado con 5 subsecciones).

## Errores comunes

- Nombrar clases `XFactory` sin encapsular creación variable.
- Singleton para “conexión DB” sin entender inyección de dependencias.
- Over-engineering: 12 patrones en un CRUD de 200 líneas.
- Copiar ejemplos de Java sin adaptar al estilo TypeScript del plan.
- Patrones en el front que duplican reglas de negocio que deben vivir en la API.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — 3 patrones:** código + tests en `projects/m14-patrones/src/` y ADRs en `projects/m14-patrones/adr/`.
- **P2 — Repo/Service:** archivos `*Repository*` / `*Service*` (o rutas equivalentes documentadas en README).
- **P3 — Refactor:** `projects/m14-patrones/refactor-notas.md` + evidencia en git (commits o diff).
- **Proyecto — ≥5 patrones:** `projects/m14-patrones/README.md` índice + ADRs justificando cada uno.

## Criterios de dominio

- [ ] 5 patrones aplicados con justificación escrita y enlace al código.
- [ ] Explicas un patrón que **rechazaste** para Agenda Ops y por qué.
- [ ] Los tests cubren el comportamiento público, no detalles internos frágiles.
- [ ] Repository no filtra SQL al dominio.
