---
id: M24
titulo: Tecnologías emergentes
etapa: terminal
orden: 24
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Research notes de 3 tecnologías candidatas
  - id: p2
    titulo: Criterios de adopción (costo, riesgo, valor, seguridad)
  - id: p3
    titulo: Spike de 1 semana
proyecto:
  id: proj
  titulo: PoC justificado (IoT, edge, realtime, etc.)
---

# M24 — Tecnologías emergentes (electiva dirigida)

## Por qué existe

Agenda Ops no necesita adoptar cada moda (blockchain, “serverless por moda”, IoT sin caso de uso). Un ingeniero senior **evalúa** antes de meter una dependencia en producción: costo, riesgo operativo, superficie de ataque y encaje con el producto. M24 es esa disciplina aplicada a **tres candidatos** y un **spike** de una semana con decisión go/no-go escrita — por ejemplo recordatorios por WhatsApp Business API, cola realtime para disponibilidad de citas, o edge para latencia en Baja California.

No es obligatorio llevar el spike a M26; es obligatorio **pensar** antes de acumular deuda.

**En resumen:** separas hype de utilidad: research, criterios (incluye seguridad) y un spike go/no-go.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Investigar tres tecnologías con **fuentes primarias** (docs oficiales) y al menos una crítica o limitación conocida.
2. Construir una matriz de adopción con costo, riesgo, valor para Agenda Ops, fit y **seguridad**.
3. Ejecutar un spike acotado (≤1 semana de esfuerzo documentado) con alcance explícito.
4. Redactar go/no-go con criterios medibles, no intuición.
5. Descartar candidatos con argumentos sólidos (tanto vale un “no” bien fundado).
6. Relacionar el spike con el backlog M21 sin prometer features no validadas.

## Cómo estudiar esta materia (lecciones)

M24 es **evaluación disciplinada** de tecnologías emergentes para Agenda Ops: L01–L12 (formato M01), evidencia en `projects/m24-emergentes/`.

1. Orden **L01 → L12**; marca solo con “Hecho cuando” cumplido.
2. **Fuentes primarias** (docs oficiales) antes de puntuar la matriz.
3. El spike vive aislado; no merges a prod sin go explícito en `go-no-go.md`.
4. Un “no” bien argumentado vale igual que un “go” si el spike midió costo/riesgo.
5. [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lecciones research/spike | 10–12 | 4× ~5 h (lectura + `projects/m24-emergentes/`) |
| Matriz / PoC (P2–P3) | 6–8 | Criterios + spike acotado |
| Retro | 1 | Qué descartaste y por qué |

Si un día solo tienes 2 h: **una lección** con archivo en git. No saltes la lectura del vendor.

## Lecciones

### Semana 1 — Research de tres candidatos (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Estructura M24 y tres candidatos al producto](M24/L01-estructura-m24-y-tres-candidatos-al-producto.md) | 5 |
| L02 | [Research candidato 1 — fuentes primarias](M24/L02-research-candidato-1-fuentes-primarias.md) | 5 |
| L03 | [Research candidatos 2 y 3](M24/L03-research-candidatos-2-y-3.md) | 5 |
| L04 | [Cierre research semana 1 y backlog M21](M24/L04-cierre-research-semana-1-y-backlog-m21.md) | 5 |

### Semana 2 — Matriz, costo y plan de spike (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Matriz de adopción y pesos](M24/L05-matriz-de-adopcion-y-pesos.md) | 5 |
| L06 | [Costo, operación y vendor lock-in](M24/L06-costo-operacion-y-vendor-lock-in.md) | 5 |
| L07 | [Threat sketch del candidato para spike](M24/L07-threat-sketch-del-candidato-para-spike.md) | 5 |
| L08 | [Plan del spike — hipótesis, alcance y éxito](M24/L08-plan-del-spike-hipotesis-alcance-y-exito.md) | 5 |

### Semana 3 — Spike, medición y go/no-go (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Scaffold del spike y entorno aislado](M24/L09-scaffold-del-spike-y-entorno-aislado.md) | 5 |
| L10 | [Flujo mínimo demostrable](M24/L10-flujo-minimo-demostrable.md) | 5 |
| L11 | [Medición contra la hipótesis](M24/L11-medicion-contra-la-hipotesis.md) | 5 |
| L12 | [Go/no-go, cierre M24 y handoff](M24/L12-go-no-go-cierre-m24-y-handoff.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: **docs oficiales** de los tres candidatos + notas de la matriz. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura | Entrega |
|--------|-----------|---------|---------|
| 1 | L01–L04 | 3× docs vendor + 1 crítica/candidato | `research/candidato-*.md` (P1) |
| 2 | L05–L08 | Pricing, webhooks, threat sketch | `matriz-adopcion.md` + `spike/plan.md` (P2) |
| 3 | L09–L12 | Quickstart spike + changelog seguridad | `spike/` + `go-no-go.md` (P3) |

**Regla:** sin fuente primaria no entra a la matriz; spike con hipótesis medible.



## Ejemplo — filas de matriz (extracto)

| Criterio | Candidato A (WhatsApp API) | Candidato B (SSE) | Candidato C (…) |
|----------|---------------------------|-------------------|-----------------|
| Valor ICP | Recordatorios donde ya están | Calendario vivo en panel | … |
| Costo mensual est. | Por conversación + dev time | Hosting + conexiones | … |
| Riesgo seguridad | Tokens Meta, webhooks firmados | Auth en canal largo | … |
| Fit M26 | Alto si trial pide WhatsApp | Medio | … |
| Decisión spike | **Go** | No esta fase | Descartado: … |



## Prácticas

1. **P1 — Research:** tres archivos en `projects/m24-emergentes/research/` con enlaces y resumen honesto.
2. **P2 — Matriz:** `projects/m24-emergentes/matriz-adopcion.md` con costo, riesgo, valor, seguridad y fit.
3. **P3 — Spike:** código o script en `projects/m24-emergentes/spike/` + nota de cómo ejecutar la demo.

## Proyecto útil

**PoC justificado** documentado en `projects/m24-emergentes/go-no-go.md`, enlazando al spike. Un “no” bien argumentado cumple el proyecto si el spike demostró que el costo o riesgo supera el valor.

## Errores comunes

- Elegir tecnología por Twitter sin leer límites de la API.
- Spike sin hipótesis medible (“jugué con X” no basta).
- Meter el PoC directo en prod de Agenda Ops.
- Ignorar seguridad de webhooks (firma, replay) en integraciones messaging.
- Adoptar tres cosas a la vez en lugar de un spike enfocado.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Notes:** `projects/m24-emergentes/research/candidato-1.md`, `candidato-2.md`, `candidato-3.md`.
- **P2 — Matriz:** `projects/m24-emergentes/matriz-adopcion.md`.
- **P3 — Spike:** `projects/m24-emergentes/spike/` (README con comando demo) + commits o tag.
- **Proyecto — Go/no-go:** `projects/m24-emergentes/go-no-go.md`.

## Criterios de dominio

- [ ] PoC con decisión go/no-go argumentada y criterios explícitos.
- [ ] Matriz incluye columna de seguridad no vacía.
- [ ] Puedes explicar por qué descartaste al menos un candidato.
- [ ] Spike acotado en tiempo; alcance documentado.
- [ ] Fuentes primarias citadas en cada research note.
