---
id: L02
materia: M13
orden: 2
titulo: Actores y casos de uso prioritarios
horas: 5
semana: 1
lectura: 'Larman: actores y casos de uso; SRS Vitrina Must'
evidencia: projects/m13-diseno/casos-de-uso.md (actores + UC prioritarios)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M17 implementará login, CRUD de pedidos/clientes y roles. Si hoy no
      priorizas, mañana codificas features que el design partner no usa.


      **Objetivo de esta lección:** Borrador sólido de
      `projects/m13-diseno/casos-de-uso.md`: actores + casos Must del piloto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Extrae actores del SRS
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/casos-de-uso.md
      git commit -m "docs(m13): actores y casos de uso prioritarios"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Lista casos Must
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/casos-de-uso.md
      git commit -m "docs(m13): actores y casos de uso prioritarios"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Actores y casos de uso prioritarios», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Actores y casos de uso
          prioritarios
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

      `git add projects/m13-diseno/casos-de-uso.md`
    comandoEsperado:
      - git add projects/m13-diseno/casos-de-uso.md
      - 'git commit -m "docs(m13): actores y casos de uso prioritarios"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m13-diseno/casos-de-uso.md'
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
          Borrador sólido de `projects/m13-diseno/casos-de-uso.md`: actores +
          casos Must del piloto.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Diagrama ligero opcional
    xp: 10
    cuerpo: >-
      Si ayuda, añade Mermaid use-case (máx. 8 elipses). Si el diagrama no
      cambia una decisión, bórralo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `casos-de-uso.md` lista actores (owner, staff, sistema) con 1 frase de
        responsabilidad cada uno.
      - >-
        ≥5 casos de uso Must con id (UC-xx), actor primario y traza a
        historia/requisito del SRS.
      - 'Commit `docs(m13): actores y casos de uso prioritarios`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Actores y casos de uso prioritarios

**~5.0 h · Semana 1**

Sin actores claros, los diagramas de la semana 2 no saben *quién* habla con la API.

## Objetivo

Borrador sólido de `projects/m13-diseno/casos-de-uso.md`: actores + casos Must del piloto.

## Por qué importa

M17 implementará login, CRUD de pedidos/clientes y roles. Si hoy no priorizas, mañana codificas features que el design partner no usa.

## Pasos (hazlos en orden)

### 1. Extrae actores del SRS (40–50 min)

Abre `projects/m12-srs/srs-v1.md` (o plantilla) y marca quién inicia cada historia Must.

Actores mínimos esperados:

| Actor | Responsabilidad |
|-------|-----------------|
| Owner | Admin del negocio: roles, servicios, clientes |
| Staff | Opera agenda del día: crear/cancelar pedidos |
| Sistema | Recordatorios futuros / jobs (aunque sea stub) |

### 2. Lista casos Must (70–90 min)

Crea o amplía `projects/m13-diseno/casos-de-uso.md` con secciones **Actores** y **Casos prioritarios (Must)**.

Tabla mínima esperada:

| ID | Nombre | Actor | Traza SRS | Notas |
|----|--------|-------|-----------|-------|
| UC-01 | Iniciar sesión | Owner/Staff | H-auth-01 | cookie/sesión |
| UC-02 | Crear cliente | Owner/Staff | H-cli-01 | |
| UC-03 | Crear pedido | Staff | H-pedido-01 | slot + servicio |
| UC-04 | Cancelar pedido | Staff | H-pedido-02 | |
| UC-05 | Listar agenda del día | Staff | H-pedido-03 | |

Ajusta IDs a tu SRS; no copies ciegos.

### 3. Diagrama ligero opcional (30–40 min)

Si ayuda, añade Mermaid use-case (máx. 8 elipses). Si el diagrama no cambia una decisión, bórralo.

### 4. Párrafo de alcance (20 min)

Al final del archivo: qué **queda fuera** del piloto (pagos Stripe, multi-sucursal, WhatsApp bot completo).

### 5. Commit (15 min)

```bash
git add projects/m13-diseno/casos-de-uso.md
git commit -m "docs(m13): actores y casos de uso prioritarios"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Actores, casos de uso y priorización Must del SRS | [UML — Use Case Diagram (resumen)](https://www.uml-diagrams.org/use-case-diagrams.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `casos-de-uso.md` lista actores (owner, staff, sistema) con 1 frase de responsabilidad cada uno.
2. ≥5 casos de uso Must con id (UC-xx), actor primario y traza a historia/requisito del SRS.
3. Commit `docs(m13): actores y casos de uso prioritarios`.

## Errores comunes

- 30 casos de uso “por si acaso”; quédate en el MVP Must.
- Actor “Usuario” genérico sin distinguir owner vs staff.
- Casos sin traza al SRS (imposible saber si son inventados).

## Siguiente

[L03 — Escenarios alternos y errores](L03-escenarios-alternos-y-errores.md)
