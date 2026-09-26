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
  titulo: Aplicar ≥5 patrones en el CRM con justificación
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

## Cómo estudiar esta materia

- Un patrón por día: leer → implementar en TypeScript → test → párrafo “por qué aquí”.
- Prioriza el dominio Agenda Ops: precios, recordatorios, estados de cita, parsing de horarios.
- Si aún no tienes repo de producto, usa `projects/m14-patrones/src/` y enlaza desde el README cómo migrarás a M17.
- Cada patrón sin justificación en markdown **no cuenta** para evidencia.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura patrones | 6–8 | GoF selecto / Refactoring.Guru |
| Implementar | 6–8 | Código + tests |
| ADR / fichas | 4–6 | Por qué cada patrón |
| Retro | 1 | Un anti-patrón que cometiste |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Prepara el espacio de trabajo:
   ```bash
   mkdir -p projects/m14-patrones/src projects/m14-patrones/adr
   ```
2. Implementa **Strategy** para calcular precio de servicio (tarifa base vs promoción) en `projects/m14-patrones/src/precio-strategy.ts`.
3. Escribe al menos 2 tests (caso normal y promoción) con Vitest o el runner que uses en el plan.
4. Crea `projects/m14-patrones/adr/001-strategy-precio.md` con contexto, decisión y **cuándo NO** usar Strategy aquí.
5. Commit: `feat(m14): strategy de precios con tests`.

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

## Lecturas

Canon: *Patrones de diseño* — GoF (ed. ES si hay). Alternativa: [Refactoring.Guru ES](https://refactoring.guru/es/design-patterns). Ver [bibliografía](../../bibliografia.md).

| Semana | Patrones / capítulos | Alternativa gratis |
|--------|---------------------|--------------------|
| 1 | **Creacionales** selectos: Factory, Singleton (cuándo NO) | Refactoring.Guru — Factory / Singleton |
| 2 | **Estructurales**: Adapter, Decorator, Facade | Refactoring.Guru equivalentes |
| 3 | **Comportamiento**: Strategy, Observer, Command (selecto) | Refactoring.Guru equivalentes |
| 4 | **Repository / Service** en tu backend + ADR de 5 patrones | Código en `projects/m14-patrones/` + ADRs |

**Regla:** patrón sin justificación escrita = no cuenta.

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
