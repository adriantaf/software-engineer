---
id: M26
titulo: Proyecto integrador / titulación interna
etapa: terminal
orden: 26
semanas: 8
horas: 160
practicas:
  - id: p1
    titulo: Alcance congelado + plan de 8 semanas
  - id: p2
    titulo: Memoria técnica v1
  - id: p3
    titulo: Demo pública / video
proyecto:
  id: proj
  titulo: Capstone en producción + egreso
---

# M26 — Proyecto integrador

## Por qué existe

Cierre de la academia. Demuestras que puedes **imaginar → diseñar → construir → asegurar → operar → explicar**.

## Análogos
UABC: Desarrollo de aplicaciones innovadoras. Tec: cierre de ingeniería de software.

## Objetivos

Cumplir la [rúbrica de egreso](../../egreso.md) completa, incluyendo seguridad (M18 + M25).

## Cómo estudiar esta materia

- Congela alcance en la semana 1. El enemigo es el scope creep.
- Cada semana: demo interna + bitácora.
- Seguridad y tests no se “dejan para el final”.

## Día 1 (2–3 h)

1. Escribe `projects/m26-capstone/alcance.md`: in / out / no-go.
2. Copia checklist de [`egreso.md`](../../egreso.md) y marca estado actual.
3. Planifica 8 sprints (aunque seas equipo de 1).
4. Agenda la demo pública (fecha).

## Temario (8 semanas)

| Semana | Foco |
|--------|------|
| 1 | Alcance, arquitectura, riesgos |
| 2–5 | Build del producto (features críticas) |
| 6 | Hardening + tests + CI verdes |
| 7 | Memoria técnica + polish comercial |
| 8 | Demo, video, cierre de egreso |

## Entregables

1. Producto en producción (evolución del CRM u otro aprobado).
2. Memoria técnica.
3. App móvil/desktop conectada (o justificación fuerte si el vertical no la requiere — por defecto **sí**).
4. Security review (M25) aplicado y vigente.
5. Registro comercial (M22).
6. Video demo sin tutorial de fondo.

## Errores comunes

- Empezar features nuevas en la semana 7.
- Demo con credenciales hardcodeadas.
- Memoria que describe el stack pero no las decisiones.

## Criterios de dominio final

Construyes un CRUD con auth + deploy + tests en un fin de semana **sin seguir un curso**. Ese es el examen.
