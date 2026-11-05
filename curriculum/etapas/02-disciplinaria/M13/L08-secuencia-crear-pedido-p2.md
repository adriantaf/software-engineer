---
id: L08
materia: M13
orden: 8
titulo: 'Secuencia: crear pedido (P2)'
horas: 5
semana: 2
lectura: Secuencia crear pedido con auth + reglas; cierre P2 UML
evidencia: diagramas/secuencia-crear-pedido.md + clases.md (P2)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 pide clases + secuencia crítica. Hoy cierras con el corazón del piloto:
      **crear pedido**.


      **Objetivo de esta lección:** `diagramas/secuencia-crear-pedido.md`
      alineada a UC-03 y a los errores de L03.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Borrador Mermaid
    xp: 10
    cuerpo: |-
      ```mermaid
      sequenceDiagram
        participant U as Browser
        participant API as API
        participant S as CitaService
        participant DB as PostgreSQL
        U->>API: POST /pedidos (Cookie + JSON)
        API->>API: sesión + rol
        alt sin sesión
          API-->>U: 401
        end
        API->>S: crearCita(dto, userId)
        S->>S: validar rango horario
        S->>DB: ¿slot libre?
        alt conflicto
          S-->>API: Conflict
          API-->>U: 409
        else ok
          S->>DB: INSERT pedido
          S-->>API: Pedido
          API-->>U: 201 + JSON
        end
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Alinea con clases y casos
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/diagramas
      git commit -m "docs(m13): secuencia crear pedido y cierre P2"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Secuencia: crear pedido (P2)», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Secuencia: crear pedido
          (P2)
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
    pregunta: ¿Es recomendable en esta lección? “API inserta sin chequear sesión."
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
        texto: >-
          `diagramas/secuencia-crear-pedido.md` alineada a UC-03 y a los errores
          de L03.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Checklist P2
    xp: 10
    cuerpo: '- [ ] `diagramas/clases.md` - [ ] `diagramas/secuencia-*.md` (≥1 crítica)'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `secuencia-crear-pedido.md` incluye validación de sesión/rol, reglas de
        dominio e INSERT.
      - >-
        P2 completo: `clases.md` + al menos una secuencia crítica en
        `diagramas/`.
      - 'Commit `docs(m13): secuencia crear pedido y cierre P2`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Secuencia: crear pedido (P2)

**~5.0 h · Semana 2**

P2 pide clases + secuencia crítica. Hoy cierras con el corazón del piloto: **crear pedido**.

## Objetivo

`diagramas/secuencia-crear-pedido.md` alineada a UC-03 y a los errores de L03.

## Pasos (hazlos en orden)

### 1. Borrador Mermaid (80–100 min)

```mermaid
sequenceDiagram
  participant U as Browser
  participant API as API
  participant S as CitaService
  participant DB as PostgreSQL
  U->>API: POST /pedidos (Cookie + JSON)
  API->>API: sesión + rol
  alt sin sesión
    API-->>U: 401
  end
  API->>S: crearCita(dto, userId)
  S->>S: validar rango horario
  S->>DB: ¿slot libre?
  alt conflicto
    S-->>API: Conflict
    API-->>U: 409
  else ok
    S->>DB: INSERT pedido
    S-->>API: Pedido
    API-->>U: 201 + JSON
  end
```

### 2. Alinea con clases y casos (40–50 min)

- Nombres de métodos ≈ lo que pondrás en M14/M17 (`CitaService`).
- Actualiza `casos-de-uso.md` si descubriste un alterno nuevo.

### 3. Checklist P2 (20 min)

- [ ] `diagramas/clases.md`
- [ ] `diagramas/secuencia-*.md` (≥1 crítica)

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas
git commit -m "docs(m13): secuencia crear pedido y cierre P2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Secuencia crítica crear pedido; authz en API | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `secuencia-crear-pedido.md` incluye validación de sesión/rol, reglas de dominio e INSERT.
2. P2 completo: `clases.md` + al menos una secuencia crítica en `diagramas/`.
3. Commit `docs(m13): secuencia crear pedido y cierre P2`.

## Errores comunes

- API inserta sin chequear sesión.
- Conflicto de horario ausente en la secuencia.
- Marcar P2 sin archivo de secuencia en git.

## Siguiente

[L09 — Arquitectura en capas](L09-arquitectura-en-capas.md)
