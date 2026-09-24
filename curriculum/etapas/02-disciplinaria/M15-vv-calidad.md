---
id: M15
titulo: Verificación, validación y calidad
etapa: disciplinaria
orden: 15
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Pirámide de tests en el CRM
  - id: p2
    titulo: CI en GitHub Actions (lint + test + audit)
  - id: p3
    titulo: Checklist de code review (incluye seguridad)
proyecto:
  id: proj
  titulo: Pipeline CI verde + coverage en lógica de negocio
---

# M15 — V&V y calidad

## Por qué existe
Sin tests, cada cambio es miedo. Incluye tests de **auth/autorización** ([hilo seguridad](../../hilos/seguridad.md)).

## Día 1 (2–3 h)
Elige una función de dominio (crear cita). Escribe 5 tests: feliz, duplicado, sin auth, IDOR, validación.

## Temario
Pirámide → mocks/fakes → CI → coverage útil → review checklist.

## Libros (ES)
*Código limpio*; *El programador pragmático*; guías testing ES.

## Proyecto útil
CI verde + changelog + semver.

## Errores comunes
Tests que solo prueban mocks; CI que puedes saltarte; 0 tests de seguridad.

## Criterios de dominio
- [ ] Un bug en prod tiene test de regresión al día siguiente.
- [ ] CI corre `audit` o equivalente.
