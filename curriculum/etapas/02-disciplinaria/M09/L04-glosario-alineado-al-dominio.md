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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar `glosario.md` usable por alguien que no leyó Elmasri,
      alineado a Vitrina y a tu ER.


      Si el equipo dice “cliente” y uno piensa en el tenant SaaS, el esquema se
      rompe en M17. Hoy cierras vocabulario.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lee producto
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos
      git commit -m "docs(m09): glosario dominio agenda ops"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Glosario alineado al dominio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: glosario.md completo + README enlaza P1 parcial
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m09-bases-datos`
    comandoEsperado:
      - git add projects/m09-bases-datos
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m09-bases-datos'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar `glosario.md` usable por alguien que no leyó Elmasri, alineado a
          Vitrina y a tu ER.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Completa el glosario
    xp: 10
    cuerpo: >-
      Abre `projects/m09-bases-datos/glosario.md`. Amplía a ≥8 filas.
      Obligatorio cubrir: Cliente, Servicio, Pedido, Tenant, No-show, Migración,
      Seed, Least privilege.
  - id: s7
    tipo: explicacion
    titulo: 3. Cruza con el ER
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
