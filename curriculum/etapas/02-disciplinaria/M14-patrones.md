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
Patrones son vocabulario compartido. Mal usados = cargo cult.

**En cristiano:** aplicas pocos patrones con justificación (no nombres de adorno) en el código del CRM.

## Día 1 (2–3 h)
Implementa Strategy para “calcular precio” (base vs con descuento) con tests. Escribe cuándo NO usar el patrón.

## Ejemplo
```ts
type Precio = { calcular(base: number): number };
const normal: Precio = { calcular: (b) => b };
const promo: Precio = { calcular: (b) => b * 0.9 };
```

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura patrones | 6–8 | GoF / Refactoring.Guru |
| Implementar | 6–8 | Strategy/Factory/etc. |
| ADR | 4–6 | Por qué cada patrón |
| Retro | 1 | Un anti-patrón que cometiste |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Temario
GoF selectos → Repository/Service → refactor CRM → justificación en ADR.

## Lecturas

Canon: *Patrones de diseño* — GoF (ed. ES si hay). Alternativa: [Refactoring.Guru ES](https://refactoring.guru/es/design-patterns). Ver [bibliografía](../../bibliografia.md).

| Semana | Patrones / capítulos | Alternativa gratis |
|--------|---------------------|--------------------|
| 1 | **Creacionales** selectos: Factory, Singleton (cuándo NO) | Refactoring.Guru — Factory / Singleton |
| 2 | **Estructurales**: Adapter, Decorator, Facade | Refactoring.Guru equivalentes |
| 3 | **Comportamiento**: Strategy, Observer, Command | Refactoring.Guru equivalentes |
| 4 | **Repository / Service** en tu CRM + ADR justificando 5 patrones aplicados | Código + ADR |

**Regla:** patrón sin justificación escrita = no cuenta.

## Errores comunes
Nombrar “Factory” sin factory; over-engineering.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — 3 patrones:** Strategy, Observer, Factory con tests.
- **P2 — Repo/Service:** Capa backend del CRM.
- **P3 — Refactor:** Módulo legacy refactorizado + diff.
- **Proyecto — ≥5 patrones:** ADR justificando cada uno en contexto.

## Criterios de dominio
- [ ] 5 patrones aplicados con justificación escrita.
