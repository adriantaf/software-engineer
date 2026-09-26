"""M14 — Patrones: 16 lessons at M01/M09 quality."""
from __future__ import annotations

FILENAMES = {
    1: "L01-entorno-m14-y-strategy-de-precios.md",
    2: "L02-factory-method-para-notificadores-de-canal.md",
    3: "L03-singleton-cuando-no-usarlo.md",
    4: "L04-cierre-semana-1-creacionales-y-bitacora.md",
    5: "L05-adapter-para-api-de-calendario-externo.md",
    6: "L06-decorator-para-logging-de-operaciones-de-cita.md",
    7: "L07-facade-para-el-flujo-agendar-cita.md",
    8: "L08-tests-de-regresion-en-api-publica-del-modulo.md",
    9: "L09-observer-para-eventos-de-dominio.md",
    10: "L10-command-para-acciones-admin-reversibles.md",
    11: "L11-cierre-p1-strategy-observer-y-factory.md",
    12: "L12-repaso-comportamiento-y-anti-patron-propio.md",
    13: "L13-repository-interfaz-cita-sin-sql.md",
    14: "L14-service-capa-aplicacion-de-citas.md",
    15: "L15-refactor-p3-modulo-legacy-antes-y-despues.md",
    16: "L16-cierre-m14-cinco-patrones-e-integracion-m17.md",
}

LESSONS: list[dict] = []

LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Entorno M14 y Strategy de precios",
        horas=5.0,
        semana=1,
        lectura="GoF/Refactoring.Guru Strategy; precios Agenda Ops",
        evidencia="projects/m14-patrones/ con Vitest + Strategy precios + tests",
        _lectura_corta="Strategy: familia de algoritmos intercambiables (tarifas)",
        _enlace_titulo="Refactoring.Guru — Strategy (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/strategy",
        _hecho="""1. `projects/m14-patrones/` tiene `package.json` con script `test` (Vitest) y TypeScript strict.
2. Strategy de precios (p. ej. base / promo −10 %) con ≥3 tests verdes.
3. `adr/strategy-precios.md` justifica el patrón; commit `feat(m14): strategy de precios con tests`.""",
        _errores="""- Un `if` gigante llamado “Strategy” sin interfaz/tipo común.
- Tests que solo verifican mocks.
- Subir `node_modules/`.""",
        siguiente="[L02 — Factory Method para notificadores de canal](L02-factory-method-para-notificadores-de-canal.md)",
        body=r"""
# L01 — Entorno M14 y Strategy de precios

**~5.0 h · Semana 1**

Patrones sin repo ejecutable son vocabulario vacío. Hoy levantas Vitest y cobras tarifas del piloto con Strategy.

## Objetivo

Dejar `projects/m14-patrones/` usable y un Strategy de precios con tests.

## Por qué empieza así

Agenda Ops tendrá promo, tarifa base y (luego) no-show. Strategy evita `switch` esparcidos en el service de citas.

## Pasos (hazlos en orden)

### 1. Revisa scaffold (20 min)

```bash
ls projects/m14-patrones
cat projects/m14-patrones/README.md
```

Si aún no hay `package.json`, créalo en el siguiente paso (el scaffold del repo ya puede traer stubs).

### 2. Init TypeScript + Vitest (50–70 min)

```bash
cd projects/m14-patrones
npm init -y
npm install -D typescript vitest @types/node
npx tsc --init --strict --rootDir src --outDir dist
```

`package.json`:

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

### 3. Implementa Strategy (70–90 min)

`src/pricing/strategy.ts`:

```ts
export type CalculoPrecio = { calcular(base: number): number };

export const tarifaBase: CalculoPrecio = { calcular: (b) => b };
export const tarifaPromoDiez: CalculoPrecio = {
  calcular: (b) => Math.round(b * 0.9 * 100) / 100,
};

export function totalServicio(base: number, s: CalculoPrecio): number {
  return s.calcular(base);
}
```

Tests en `src/pricing/strategy.test.ts` (≥3 casos).

### 4. ADR corto (30–40 min)

`adr/strategy-precios.md`: contexto (promos del salón/clínica), decisión, por qué no `if` en el controller.

### 5. Commit (15 min)

```bash
git add projects/m14-patrones
git commit -m "feat(m14): strategy de precios con tests"
```
""",
    )
)

LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Factory Method para notificadores de canal",
        horas=5.0,
        semana=1,
        lectura="Factory Method; email vs WhatsApp link",
        evidencia="src/notify/ factory + tests + ADR",
        _lectura_corta="Factory Method: crear notificadores sin acoplar al cliente",
        _enlace_titulo="Refactoring.Guru — Factory Method (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/factory-method",
        _hecho="""1. Factory crea al menos 2 notificadores (email / whatsapp-link) detrás de una interfaz.
2. ≥2 tests: el cliente pide canal y recibe el tipo correcto sin `new` concreto.
3. Commit `feat(m14): factory method notificadores`.""",
        _errores="""- Clase `XFactory` que solo hace `return new X()`.
- WhatsApp = enviar mensajes reales (hoy: deep-link o stub).
- Factory que conoce SMTP y HTML a la vez sin interfaz.""",
        siguiente="[L03 — Singleton: cuándo NO usarlo](L03-singleton-cuando-no-usarlo.md)",
        body=r"""
# L02 — Factory Method para notificadores de canal

**~5.0 h · Semana 1**

El piloto avisará por email o link de WhatsApp. El service de citas no debe importar detalles de cada canal.

## Objetivo

Factory Method (o factory function tipada) para notificadores + tests + ADR.

## Pasos (hazlos en orden)

### 1. Interfaz común (30–40 min)

```ts
export type Notifier = { send(to: string, body: string): Promise<void> };
```

Stubs: `EmailNotifier`, `WhatsAppLinkNotifier` (concatena `https://wa.me/...`).

### 2. Factory (50–60 min)

```ts
export function createNotifier(channel: "email" | "whatsapp"): Notifier {
  switch (channel) {
    case "email": return new EmailNotifier();
    case "whatsapp": return new WhatsAppLinkNotifier();
  }
}
```

### 3. Tests (40–50 min)

Assert de comportamiento observable (p. ej. mock de send, o retorno del link).

### 4. ADR (25 min) + commit

`adr/factory-notifiers.md` · `feat(m14): factory method notificadores`
""",
    )
)

LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Singleton: cuándo NO usarlo",
        horas=5.0,
        semana=1,
        lectura="Singleton — abusos; DI como alternativa",
        evidencia="docs/anti-singleton.md + ejemplo DI vs global",
        _lectura_corta="Cuándo Singleton duele (tests, estado global) y qué usar en su lugar",
        _enlace_titulo="Refactoring.Guru — Singleton (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/singleton",
        _hecho="""1. `docs/anti-singleton.md` explica ≥2 razones para no usarlo en DB/config del piloto.
2. Código de contraste: módulo con export de instancia vs factory/DI inyectable en tests.
3. Commit `docs(m14): anti-singleton y alternativa DI`.""",
        _errores="""- “Nunca uses Singleton” sin matiz (a veces un cache read-only está bien).
- Singleton de conexión PG que impide tests paralelos — y aún así lo adoptas.
- Documento sin ejemplo de código.""",
        siguiente="[L04 — Cierre semana 1 — creacionales y bitácora](L04-cierre-semana-1-creacionales-y-bitacora.md)",
        body=r"""
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
""",
    )
)

LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Cierre semana 1 — creacionales y bitácora",
        horas=5.0,
        semana=1,
        lectura="Repaso Factory/Strategy; bitácora",
        evidencia="bitacora-semana-1.md + README índice parcial",
        _lectura_corta="Cierre creacionales: evidencias Strategy + Factory",
        _hecho="""1. Bitácora semana 1 lista Strategy, Factory y rechazo de Singleton.
2. README enlaza `src/pricing`, `src/notify`, ADRs.
3. Commit `docs(m14): cierre semana 1 creacionales`.""",
        _errores="""- Bitácora sin rutas a archivos.
- Tests rotos dejados “para después”.
- ADR sin enlace desde README.""",
        siguiente="[L05 — Adapter para API de calendario externo](L05-adapter-para-api-de-calendario-externo.md)",
        body=r"""
# L04 — Cierre semana 1 — creacionales y bitácora

**~5.0 h · Semana 1**

Consolidas vocabulario creacional antes de estructurales.

## Objetivo

Bitácora + índice parcial; suite verde.

## Pasos (hazlos en orden)

### 1. Corre tests (20 min)

```bash
cd projects/m14-patrones && npm test
```

### 2. Bitácora (50–60 min)

Qué patrón aporta flexibilidad real; qué rechazaste.

### 3. README (40 min)

Tabla patrón → archivo → ADR.

### 4. Commit (15 min)

`docs(m14): cierre semana 1 creacionales`
""",
    )
)

LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Adapter para API de calendario externo",
        horas=5.0,
        semana=2,
        lectura="Adapter; integrar API externa tras interfaz de dominio",
        evidencia="src/calendar/ adapter + fake API + tests",
        _lectura_corta="Adapter: convierte API de terceros a tu puerto de dominio",
        _enlace_titulo="Refactoring.Guru — Adapter (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/adapter",
        _hecho="""1. Puerto de dominio (p. ej. `ExternalCalendar`) + adapter sobre un cliente “feo” simulado.
2. Tests contra el puerto, no contra el JSON crudo del vendor.
3. Commit `feat(m14): adapter calendario externo`.""",
        _errores="""- Filtrar tipos del vendor a toda la app.
- Adapter sin tests.
- Llamar HTTP real obligatorio (usa fake en memoria).""",
        siguiente="[L06 — Decorator para logging de operaciones de cita](L06-decorator-para-logging-de-operaciones-de-cita.md)",
        body=r"""
# L05 — Adapter para API de calendario externo

**~5.0 h · Semana 2**

Algún design partner vivirá en Google Calendar. Hoy aíslas ese JSON raro detrás de tu interfaz.

## Objetivo

Adapter + fake vendor + tests del puerto de dominio.

## Pasos (hazlos en orden)

### 1. Puerto (30 min)

```ts
export interface ExternalCalendar {
  listBusy(from: Date, to: Date): Promise<{ start: Date; end: Date }[]>;
}
```

### 2. Vendor feo + Adapter (70–90 min)

Simula respuesta `{ items: [{ start: { dateTime: string } }] }` y adapta a `Date`.

### 3. Tests + ADR (50 min)

`adr/adapter-calendar.md` · commit `feat(m14): adapter calendario externo`
""",
    )
)

LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Decorator para logging de operaciones de cita",
        horas=5.0,
        semana=2,
        lectura="Decorator; logging sin ensuciar el core",
        evidencia="src/citas/ decorator logger + tests",
        _lectura_corta="Decorator: añade logging cruzando la misma interfaz",
        _enlace_titulo="Refactoring.Guru — Decorator (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/decorator",
        _hecho="""1. Decorador envuelve un `CitaOps` (o similar) y registra llamada sin cambiar el resultado.
2. Test demuestra que el inner se invoca y que el log recibe evento.
3. Commit `feat(m14): decorator logging citas`.""",
        _errores="""- Meter `console.log` dentro de la regla de solape.
- Decorator que cambia reglas de negocio “de paso”.
- Sin interfaz común inner/outer.""",
        siguiente="[L07 — Facade para el flujo agendar cita](L07-facade-para-el-flujo-agendar-cita.md)",
        body=r"""
# L06 — Decorator para logging de operaciones de cita

**~5.0 h · Semana 2**

Quieres auditoría de “quién creó cita” sin contaminar el dominio con Winston.

## Objetivo

Decorator de logging sobre operaciones de cita.

## Pasos (hazlos en orden)

### 1. Interfaz CitaOps (30 min)

`create`, `cancel` mínimos (pueden ser in-memory).

### 2. LoggingCitaOps (60–70 min)

Delega + empuja a un `LogSink` inyectable.

### 3. Tests (40 min) + ADR + commit

`feat(m14): decorator logging citas`
""",
    )
)

LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Facade para el flujo agendar cita",
        horas=5.0,
        semana=2,
        lectura="Facade; orquestar validación + persistencia + notify",
        evidencia="src/citas/agendar-facade.ts + tests",
        _lectura_corta="Facade: API simple sobre subsistema de agendar",
        _enlace_titulo="Refactoring.Guru — Facade (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/facade",
        _hecho="""1. `agendarCita(...)` facade coordina validación + save + notify (stubs ok).
2. Test de flujo feliz y un fallo (p. ej. slot ocupado) sin que el caller toque 3 servicios.
3. Commit `feat(m14): facade agendar cita`.""",
        _errores="""- Facade dios de 20 dependencias.
- Duplicar reglas fuera y dentro del facade.
- Sin test del camino de error.""",
        siguiente="[L08 — Tests de regresión en API pública del módulo](L08-tests-de-regresion-en-api-publica-del-modulo.md)",
        body=r"""
# L07 — Facade para el flujo agendar cita

**~5.0 h · Semana 2**

El caso de uso “agendar” toca varias piezas. Facade ofrece una puerta al application layer.

## Objetivo

Facade `agendarCita` + tests de feliz/error.

## Pasos (hazlos en orden)

### 1. Subsistemas stubs (40 min)

Validador de solape, repo in-memory, notifier no-op.

### 2. Facade (60–70 min)

Orquesta; traduce errores a resultados tipados.

### 3. Tests + ADR + commit

`feat(m14): facade agendar cita`
""",
    )
)

LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="Tests de regresión en API pública del módulo",
        horas=5.0,
        semana=2,
        lectura="Tests de contrato/API pública; no internals",
        evidencia="tests de regresión sobre exports públicos + nota",
        _lectura_corta="Proteger el comportamiento público tras refactors de patrones",
        _hecho="""1. Suite que ejercita exports públicos (pricing, factory, facade) en verde.
2. `docs/regresion-api-publica.md` lista qué es “contrato” vs detalle interno.
3. Commit `test(m14): regresion api publica modulos`.""",
        _errores="""- Tests acoplados a nombres privados.
- Borrar tests “porque cambió el patrón”.
- Cobertura solo de archivos vacíos.""",
        siguiente="[L09 — Observer para eventos de dominio](L09-observer-para-eventos-de-dominio.md)",
        body=r"""
# L08 — Tests de regresión en API pública del módulo

**~5.0 h · Semana 2**

Los patrones van a mover archivos. Los tests deben anclar el *comportamiento* exportado.

## Objetivo

Capa de regresión sobre la API pública de `projects/m14-patrones`.

## Pasos (hazlos en orden)

### 1. Define superficie pública (30 min)

`src/index.ts` reexporta lo estable.

### 2. Tests de contrato (80–100 min)

Casos: precio promo, notifier channel, agendar ok/conflicto.

### 3. Nota + commit

`test(m14): regresion api publica modulos`
""",
    )
)

LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Observer para eventos de dominio",
        horas=5.0,
        semana=3,
        lectura="Observer; cita creada → listeners",
        evidencia="src/events/ observer + tests + ADR",
        _lectura_corta="Observer/eventos de dominio: desacoplar efectos al crear cita",
        _enlace_titulo="Refactoring.Guru — Observer (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/observer",
        _hecho="""1. Emisor de `CitaCreada` con ≥2 listeners (p. ej. audit log + notify stub).
2. Tests: al crear, ambos listeners reciben el evento.
3. Commit `feat(m14): observer eventos de dominio`.""",
        _errores="""- Observer síncrono que rompe el flujo si un listener lanza — documenta política.
- Event bus global Singleton sin necesidad.
- Listeners que mutan la cita a espaldas del aggregate.""",
        siguiente="[L10 — Command para acciones admin reversibles](L10-command-para-acciones-admin-reversibles.md)",
        body=r"""
# L09 — Observer para eventos de dominio

**~5.0 h · Semana 3**

Crear cita no debería conocer todos los side-effects. Observer (o event emitter tipado) desacopla.

## Objetivo

Evento `CitaCreada` + listeners + tests + ADR.

## Pasos (hazlos en orden)

### 1. Tipos de evento (30 min)

### 2. Emitter + subscribe (60–70 min)

### 3. Integra en facade o service mínimo (40 min)

### 4. Tests + ADR + commit

`feat(m14): observer eventos de dominio`
""",
    )
)

LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Command para acciones admin reversibles",
        horas=5.0,
        semana=3,
        lectura="Command; undo de acción admin",
        evidencia="src/admin/ command cancelar/restaurar + tests",
        _lectura_corta="Command: encapsular acción admin con undo",
        _enlace_titulo="Refactoring.Guru — Command (ES)",
        _enlace="https://refactoring.guru/es/design-patterns/command",
        _hecho="""1. Command con `execute`/`undo` para cancelar cita (o cambiar estado).
2. Test: execute → estado cancelada; undo → restaurada.
3. Commit `feat(m14): command admin reversible`.""",
        _errores="""- Command sin undo cuando el enunciado lo pide.
- Guardar UI clicks como commands innecesarios.
- Undo que ignora invariantes (restaurar sobre slot ya ocupado — documenta).""",
        siguiente="[L11 — Cierre P1 — Strategy, Observer y Factory](L11-cierre-p1-strategy-observer-y-factory.md)",
        body=r"""
# L10 — Command para acciones admin reversibles

**~5.0 h · Semana 3**

Owner cancela por error. Command te da vocabulario para execute/undo en el panel admin.

## Objetivo

Command reversible de cancelación + tests.

## Pasos (hazlos en orden)

### 1. Interfaz Command (25 min)

### 2. CancelCitaCommand (70–80 min)

Guarda estado previo para undo.

### 3. Tests + ADR + commit

`feat(m14): command admin reversible`
""",
    )
)

LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Cierre P1 — Strategy, Observer y Factory",
        horas=5.0,
        semana=3,
        lectura="Evidencia P1: 3 patrones con tests y ADRs",
        evidencia="README P1 checklist + suite verde",
        _lectura_corta="Cierre práctica P1: Strategy + Observer + Factory",
        _hecho="""1. Strategy, Observer y Factory tienen código + tests + ADR cada uno.
2. README marca P1 con rutas.
3. Commit `docs(m14): cierre P1 strategy observer factory`.""",
        _errores="""- Marcar P1 con un solo patrón.
- ADRs vacíos.
- Tests fallando en CI local.""",
        siguiente="[L12 — Repaso comportamiento y anti-patrón propio](L12-repaso-comportamiento-y-anti-patron-propio.md)",
        body=r"""
# L11 — Cierre P1 — Strategy, Observer y Factory

**~5.0 h · Semana 3**

P1 de la ficha: tres patrones con justificación. Hoy cierras evidencia.

## Objetivo

Checklist P1 verificable en git.

## Pasos (hazlos en orden)

### 1. `npm test` (20 min)

### 2. Tabla P1 en README (50 min)

### 3. Relee ADRs (40 min) — una frase de “por qué no if/switch”

### 4. Commit

`docs(m14): cierre P1 strategy observer factory`
""",
    )
)

LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Repaso comportamiento y anti-patrón propio",
        horas=5.0,
        semana=3,
        lectura="Anti-patrón detectado en tu código",
        evidencia="docs/anti-patron-propio.md",
        _lectura_corta="Documentar un anti-patrón propio y el refactor mental",
        _hecho="""1. `anti-patron-propio.md` describe código tuyo (plan o spike) con olor y alternativa.
2. Enlaza al patrón de M14 que lo evita.
3. Commit `docs(m14): anti-patron propio`.""",
        _errores="""- Hablar de anti-patrones abstractos sin tu código.
- Inventar un pecado que no cometiste.
- No proponer fix.""",
        siguiente="[L13 — Repository — interfaz Cita sin SQL](L13-repository-interfaz-cita-sin-sql.md)",
        body=r"""
# L12 — Repaso comportamiento y anti-patrón propio

**~5.0 h · Semana 3**

Criterio de dominio: un patrón que **rechazaste** y un olor que sí tuviste.

## Objetivo

Documento honesto `docs/anti-patron-propio.md`.

## Pasos (hazlos en orden)

### 1. Elige un olor (30 min)

God service, SQL en controller, Singleton de config, etc.

### 2. Escribe antes → después (80–100 min)

Fragmentos de código o pseudocódigo.

### 3. Commit

`docs(m14): anti-patron propio`
""",
    )
)

LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="Repository — interfaz Cita sin SQL",
        horas=5.0,
        semana=4,
        lectura="Repository; puerto de persistencia",
        evidencia="src/citas/cita-repository.ts + InMemory + ADR (P2 inicio)",
        _lectura_corta="Repository: interfaz de dominio sin SQL; impl in-memory",
        _hecho="""1. `CitaRepository` con `findById`/`save` (y filtro por dueño/negocio si aplica).
2. `InMemoryCitaRepository` + tests; **cero** SQL en el dominio.
3. Commit `feat(m14): repository cita sin sql`.""",
        _errores="""- Interfaz que expone `query(sql: string)`.
- Repo que es solo un alias del ORM entity.
- Sin tests del in-memory.""",
        siguiente="[L14 — Service — capa aplicación de citas](L14-service-capa-aplicacion-de-citas.md)",
        body=r"""
# L13 — Repository — interfaz Cita sin SQL

**~5.0 h · Semana 4**

P2: capas backend alineadas a M13. Empiezas por el puerto de persistencia.

## Objetivo

`CitaRepository` + impl in-memory + ADR.

## Pasos (hazlos en orden)

### 1. Tipos de dominio Cita (30 min) — alineados a M13

### 2. Interfaz + InMemory (70–90 min)

### 3. Tests + ADR + commit

`feat(m14): repository cita sin sql`
""",
    )
)

LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="Service — capa aplicación de citas",
        horas=5.0,
        semana=4,
        lectura="Application service; orquestación y authz",
        evidencia="src/citas/cita-service.ts + tests (P2)",
        _lectura_corta="Service de aplicación: reglas + repo; sin HTTP ni SQL",
        _hecho="""1. `CitaService` usa `CitaRepository` y valida solape/rol (stub de auth ok).
2. Tests de servicio con repo in-memory (P2 evidenciado).
3. Commit `feat(m14): service capa aplicacion citas`.""",
        _errores="""- Service que importa Express.
- Authz solo “si rol en string del DTO” sin explicación.
- Duplicar facade y service sin roles claros — documenta relación.""",
        siguiente="[L15 — Refactor P3 — módulo legacy antes y después](L15-refactor-p3-modulo-legacy-antes-y-despues.md)",
        body=r"""
# L14 — Service — capa aplicación de citas

**~5.0 h · Semana 4**

El service es lo que M13 llamó application layer: orquesta dominio + puertos.

## Objetivo

`CitaService` testeable sin HTTP.

## Pasos (hazlos en orden)

### 1. API del service (40 min)

`crear`, `cancelar`, `listarDelDia`.

### 2. Implementación (70–90 min)

Inyecta repo (+ clock + notifier opcionales).

### 3. Tests P2 + README + commit

`feat(m14): service capa aplicacion citas`
""",
    )
)

LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="Refactor P3 — módulo legacy antes y después",
        horas=5.0,
        semana=4,
        lectura="Refactor con comportamiento preservado",
        evidencia="refactor-notas.md + diff/commits (P3)",
        _lectura_corta="Refactor de módulo legacy propio con antes/después",
        _hecho="""1. `refactor-notas.md` con módulo antes/después y qué patrón aplicaste.
2. Evidencia git (commits o diff pegado) y tests verdes post-refactor.
3. Commit `refactor(m14): modulo legacy P3` (o docs si el diff está en notas).""",
        _errores="""- Reescribir de cero y llamarlo refactor.
- Cambiar comportamiento observable sin test.
- Notas sin rutas de archivo.""",
        siguiente="[L16 — Cierre M14 — cinco patrones e integración M17](L16-cierre-m14-cinco-patrones-e-integracion-m17.md)",
        body=r"""
# L15 — Refactor P3 — módulo legacy antes y después

**~5.0 h · Semana 4**

P3: tomas código tuyo (spike feo, god function de precios, etc.) y lo refactorizas.

## Objetivo

`refactor-notas.md` + evidencia en git.

## Pasos (hazlos en orden)

### 1. Elige módulo (20 min)

Si no hay legacy, crea `src/legacy/agendar-todo-en-uno.ts` a propósito y luego rompe el monolito.

### 2. Caracteriza con test (40 min)

### 3. Refactor hacia patrones ya vistos (80–100 min)

### 4. Notas + commit

`refactor(m14): modulo legacy P3`
""",
    )
)

LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Cierre M14 — cinco patrones e integración M17",
        horas=5.0,
        semana=4,
        lectura="≥5 patrones justificados; plan handoff M17",
        evidencia="README índice ≥5 + handoff-m17.md",
        _lectura_corta="Proyecto: ≥5 patrones con ADR; integración hacia M17",
        _hecho="""1. README lista ≥5 patrones con enlace a código y ADR.
2. `handoff-m17.md` dice qué módulos copiar/portar al repo web.
3. Commit `docs(m14): cierre cinco patrones e integracion M17`.""",
        _errores="""- Contar Decorator+logging como 5 patrones repetidos sin sustancia.
- Sin patrón rechazado documentado.
- Handoff vacío.""",
        siguiente="Materia siguiente: [M15 — V&V y calidad](../M15-vv-calidad.md) · L01 en `../M15/`.",
        body=r"""
# L16 — Cierre M14 — cinco patrones e integración M17

**~5.0 h · Semana 4**

Proyecto de la materia: ≥5 patrones justificados en Agenda Ops + camino a M17.

## Objetivo

Índice final + handoff; criterios de dominio autoevaluados.

## Pasos (hazlos en orden)

### 1. Cuenta 5 (40 min)

Strategy, Factory, Adapter, Decorator, Facade, Observer, Command, Repository… elige ≥5 reales.

### 2. Handoff (50–60 min)

Qué se queda en `m14-patrones` vs qué nace en M17; enlaces a M13 endpoints.

### 3. Autoevaluación (30 min)

Patrón rechazado; tests de API pública; repo sin SQL en dominio.

### 4. Commit

`docs(m14): cierre cinco patrones e integracion M17`
""",
    )
)
