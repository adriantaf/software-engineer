---
id: M12
titulo: Ingeniería de requerimientos
etapa: disciplinaria
orden: 12
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Entrevista a un negocio real (o simulado serio)
  - id: p2
    titulo: User stories + criterios de aceptación
  - id: p3
    titulo: SRS v1 con requisitos de seguridad
proyecto:
  id: proj
  titulo: SRS del Agenda/CRM Ensenada
---

# M12 — Ingeniería de requerimientos

## Por qué existe
Construir sin requisitos es adivinar. Incluye **requisitos no funcionales de seguridad** desde el SRS ([hilo](../../hilos/seguridad.md)).

**En cristiano:** congelas qué construir: entrevistas, stories y un SRS con seguridad, no pantallas bonitas primero.

## Análogos
UABC: Ingeniería de requerimientos.

## Objetivos
Elicitar, documentar, priorizar; separar deseo de requisito.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Entrevistas | 6–8 | Guion + notas |
| Stories + RNF | 6–8 | Aceptación + seguridad |
| SRS v1 | 4–6 | Plantilla llenada |
| Retro | 1 | Un “no” dicho con alternativa |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)
1. Elige vertical (peluquería, taller, consultorio…).
2. Escribe 10 preguntas de entrevista.
3. Habla con alguien real o simula con guion serio y graba notas.
4. Lista 5 problemas observados (no soluciones todavía).

## Ejemplo — historia con seguridad
```text
Como dueño, quiero que solo yo vea notas privadas de clientes
para proteger su información.
Criterio: usuario empleado no puede GET /notas de otro local (403).
```

## Temario
Entrevistas → stories/aceptación → SRS + RNF seguridad/privacidad → priorización MVP.

## Lecturas

Canon: plantilla IEEE 830 adaptada en el repo. Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura obligatoria | Entrega ligada |
|--------|--------------------|----------------|
| 1 | [`projects/m12-srs/plantilla.md`](../../../projects/m12-srs/plantilla.md) completa + notas de entrevista | Guion de entrevista / stories |
| 2 | Misma plantilla: secciones **funcionales** + **RNF** (seguridad, privacidad, performance) | Borrador SRS Agenda Ops |
| 3 | Priorización MVP (MoSCoW o equivalente) + freeze de alcance 4 semanas de build | SRS v1 firmado por ti |

**Regla:** no hay novela de libro: la “lectura” es la plantilla + rellenar con evidencia de entrevistas.

## Proyecto útil
SRS real del Agenda/CRM (alcance MVP 4 semanas de build).

## Errores comunes
Empezar por pantallas; omitir seguridad; MVP infinito.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Entrevista:** Notas de negocio real/simulado serio.
- **P2 — Stories:** ≥8 stories con criterios de aceptación.
- **P3 — SRS:** SRS con ≥3 RNF de seguridad/privacidad.
- **Proyecto — SRS Agenda:** `projects/m12-srs/` listo para M13/M17.

## Criterios de dominio
- [ ] Sabes decir “no” con alternativa.
- [ ] SRS incluye al menos 3 RNF de seguridad.
