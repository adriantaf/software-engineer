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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `checklist-scaffold.md` que un yo futuro use el día 1 de
      M17.


      Definition of Ready: si falta algo Must, hoy se arregla o se documenta el
      riesgo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Escribe el checklist
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Checklist listo para scaffold" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: checklist-scaffold.md marcado con evidencia enlazada
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Checklist todo ✓ sin enlaces."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: '`checklist-scaffold.md` que un yo futuro use el día 1 de M17.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Marca con enlaces
    xp: 10
    cuerpo: 'Cada ítem: ruta relativa al archivo.'
  - id: s7
    tipo: explicacion
    titulo: 3. Deuda consciente
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
