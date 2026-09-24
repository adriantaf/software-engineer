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

## Análogos
UABC: Ingeniería de requerimientos.

## Objetivos
Elicitar, documentar, priorizar; separar deseo de requisito.

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

## Recursos
Plantilla [`projects/m12-srs/plantilla.md`](../../../projects/m12-srs/plantilla.md).

## Proyecto útil
SRS real del Agenda/CRM (alcance MVP 4 semanas de build).

## Errores comunes
Empezar por pantallas; omitir seguridad; MVP infinito.

## Criterios de dominio
- [ ] Sabes decir “no” con alternativa.
- [ ] SRS incluye al menos 3 RNF de seguridad.
