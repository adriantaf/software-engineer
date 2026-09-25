---
id: M13
titulo: Análisis y diseño de software
etapa: disciplinaria
orden: 13
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: Casos de uso / flujos principales
  - id: p2
    titulo: Diagrama de clases y secuencia
  - id: p3
    titulo: Arquitectura en capas + trust boundaries
proyecto:
  id: proj
  titulo: Paquete de diseño del producto (ADR + diagramas)
---

# M13 — Análisis y diseño de software

## Por qué existe
Diseñar límites evita un monolito caótico. Marca **trust boundaries** (qué confías del cliente HTTP).

**En resumen:** traduces el SRS a diseño usable: flujos, diagramas y ADRs que el yo-de-M17 pueda seguir.


## Objetivos
Flujos, diagramas útiles, arquitectura simple defendible, ADRs.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Flujos | 6–8 | Casos de uso |
| Diagramas | 6–8 | Clases / secuencia |
| Arquitectura | 4–6 | Capas + trust boundaries |
| Retro | 1 | Por qué monolito modular |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)
1. Lista módulos del CRM (auth, citas, clientes, admin).
2. Dibuja trust boundary: navegador | API | DB.
3. Escribe ADR: “monolito modular ahora, no microservicios”.

## Ejemplo — capas
```text
HTTP controllers → application services → domain → infrastructure (DB)
Autorización se decide en application/domain, no solo en el front.
```

## Temario
Casos de uso → UML práctico → capas → ADRs → paquete de diseño.

## Lecturas

Canon: *UML y patrones* — Larman (ed. ES) **o** guía UML ES + ADRs. Apoyo: *Código limpio*. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / secciones | Alternativa |
|--------|----------------------|-------------|
| 1 | Casos de uso / escenarios (Larman caps. de requisitos→casos de uso) | Lista de casos Agenda Ops |
| 2 | **UML práctico**: clases, secuencia (solo lo que usarás) | Diagramas en Markdown/Mermaid |
| 3 | Arquitectura en **capas** + trust boundaries | Diagrama de M13 en el repo |
| 4 | **ADRs** (plantilla M01) — 2 decisiones de diseño | — |
| 5 | Paquete de diseño listo para M17 (repaso + pulido) | Relaciona con [producto-saas](../../producto-saas.md) |

**Regla:** cada diagrama debe usarse en una decisión; si no se usa, bórralo.

## Proyecto útil
Diseño del Agenda/CRM listo para M17.

## Errores comunes
Microservicios prematuros; diagramas que nadie usa; confiar en el cliente.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Flujos:** Casos de uso principales del Agenda.
- **P2 — UML:** Diagrama clases + 1 secuencia crítica.
- **P3 — Boundaries:** Diagrama con trust boundaries marcados.
- **Proyecto — Paquete:** ADRs + diagramas enlazados al repo.

## Criterios de dominio
- [ ] Defiendes monolito modular con trade-offs.
- [ ] Trust boundaries están en el diagrama.
