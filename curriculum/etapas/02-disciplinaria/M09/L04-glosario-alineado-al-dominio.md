---
id: L04
materia: M09
orden: 4
titulo: Glosario alineado al dominio
horas: 5
semana: 1
lectura: 'Elmasri: diseño conceptual — vocabulario del dominio'
evidencia: glosario.md completo + README enlaza P1 parcial
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Si el equipo dice “cliente” y uno piensa en el tenant SaaS, el esquema se
      rompe en M17. Hoy cierras vocabulario.


      **Objetivo de esta lección:** Dejar `glosario.md` usable por alguien que
      no leyó Elmasri, alineado a Vitrina y a tu ER.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lee producto
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos
      git commit -m "docs(m09): glosario dominio agenda ops"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Completa el glosario
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos
      git commit -m "docs(m09): glosario dominio agenda ops"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Glosario alineado al dominio», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Glosario alineado al
          dominio
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git add projects/m09-bases-datos`
    comandoEsperado:
      - git add projects/m09-bases-datos
      - 'git commit -m "docs(m09): glosario dominio agenda ops"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m09-bases-datos'
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
          Dejar `glosario.md` usable por alguien que no leyó Elmasri, alineado a
          Vitrina y a tu ER.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Cruza con el ER
    xp: 10
    cuerpo: >-
      Cada término de entidad del glosario debe existir en `er-vitrina.md`. Si
      sobra un término huérfano, elimínalo o modela la entidad.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`glosario.md` tiene ≥8 términos con “no confundir con”.'
      - El README de m09 enlaza `er-vitrina.md` y `glosario.md`.
      - Commit de cierre de semana 1.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Glosario alineado al dominio

**~5.0 h · Semana 1**

Si el equipo dice “cliente” y uno piensa en el tenant SaaS, el esquema se rompe en M17. Hoy cierras vocabulario.

## Objetivo

Dejar `glosario.md` usable por alguien que no leyó Elmasri, alineado a Vitrina y a tu ER.

## Pasos

### 1. Lee producto (30 min)

Revisa `curriculum/producto-saas.md` (ICP, pedidos, tenant). Marca 5 palabras que ya usas distinto.

### 2. Completa el glosario (90 min)

Abre `projects/m09-bases-datos/glosario.md`. Amplía a ≥8 filas. Obligatorio cubrir: Cliente, Servicio, Pedido, Tenant, No-show, Migración, Seed, Least privilege.

### 3. Cruza con el ER (45 min)

Cada término de entidad del glosario debe existir en `er-vitrina.md`. Si sobra un término huérfano, elimínalo o modela la entidad.

### 4. README de evidencia (30 min)

En `projects/m09-bases-datos/README.md`, sección corta “Semana 1” con enlaces a `er-vitrina.md` y `glosario.md`.

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): glosario dominio agenda ops"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: diseño conceptual — vocabulario del dominio | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `glosario.md` tiene ≥8 términos con “no confundir con”.
2. El README de m09 enlaza `er-vitrina.md` y `glosario.md`.
3. Commit de cierre de semana 1.

## Errores comunes

- Usar “usuario” para todo (staff, cliente, tenant).
- Glosario copiado de Wikipedia sin el producto.
- Términos que no aparecen en el ER.

## Siguiente

[L05 — Primera forma normal y anomalías](L05-primera-forma-normal-y-anomalias.md)
