---
id: L19
materia: M13
orden: 19
titulo: Checklist listo para scaffold
horas: 5
semana: 5
lectura: Checklist de salida hacia M17
evidencia: checklist-scaffold.md marcado con evidencia enlazada
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Definition of Ready: si falta algo Must, hoy se arregla o se documenta el
      riesgo.


      **Objetivo de esta lección:** `checklist-scaffold.md` que un yo futuro use
      el día 1 de M17.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Escribe el checklist
    xp: 10
    cuerpo: |-
      ```markdown
      # Checklist — listo para scaffold M17

      - [ ] SRS enlazado
      - [ ] casos-de-uso.md (P1)
      - [ ] clases + secuencia (P2)
      - [ ] trust-boundaries (P3)
      - [ ] arquitectura.md + DTOs
      - [ ] ADR 001–003
      - [ ] endpoints-m17.md
      - [ ] nota tenant_id
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Marca con enlaces
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/checklist-scaffold.md
      git commit -m "docs(m13): checklist listo para scaffold"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Checklist listo para scaffold», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Checklist listo para
          scaffold
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Checklist todo ✓ sin enlaces."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: '`checklist-scaffold.md` que un yo futuro use el día 1 de M17.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Deuda consciente
    xp: 10
    cuerpo: Sección “Aceptamos no tener X porque…”.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `checklist-scaffold.md` con ítems marcados y enlaces a archivos del
        paquete.
      - Cero ítems Must en “TBD” sin justificación.
      - 'Commit `docs(m13): checklist listo para scaffold`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — Checklist listo para scaffold

**~5.0 h · Semana 5**

Definition of Ready: si falta algo Must, hoy se arregla o se documenta el riesgo.

## Objetivo

`checklist-scaffold.md` que un yo futuro use el día 1 de M17.

## Pasos (hazlos en orden)

### 1. Escribe el checklist (60–70 min)

```markdown
# Checklist — listo para scaffold M17

- [ ] SRS enlazado
- [ ] casos-de-uso.md (P1)
- [ ] clases + secuencia (P2)
- [ ] trust-boundaries (P3)
- [ ] arquitectura.md + DTOs
- [ ] ADR 001–003
- [ ] endpoints-m17.md
- [ ] nota tenant_id
```

### 2. Marca con enlaces (50–60 min)

Cada ítem: ruta relativa al archivo.

### 3. Deuda consciente (30 min)

Sección “Aceptamos no tener X porque…”.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/checklist-scaffold.md
git commit -m "docs(m13): checklist listo para scaffold"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Definition of Ready del paquete de diseño | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `checklist-scaffold.md` con ítems marcados y enlaces a archivos del paquete.
2. Cero ítems Must en “TBD” sin justificación.
3. Commit `docs(m13): checklist listo para scaffold`.

## Errores comunes

- Checklist todo ✓ sin enlaces.
- Dejar P2/P3 incompletos y seguir igual.
- Incluir nice-to-have como bloqueantes.

## Siguiente

[L20 — Cierre M13 — trazabilidad y dominio](L20-cierre-m13-trazabilidad-y-dominio.md)
