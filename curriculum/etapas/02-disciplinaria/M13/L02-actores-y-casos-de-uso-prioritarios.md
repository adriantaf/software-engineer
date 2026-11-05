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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Borrador sólido de `projects/m13-diseno/casos-de-uso.md`:
      actores + casos Must del piloto.


      M17 implementará login, CRUD de pedidos/clientes y roles. Si hoy no
      priorizas, mañana codificas features que el design partner no usa.
  - id: s2
    tipo: ejemplo
    titulo: 1. Extrae actores del SRS
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/casos-de-uso.md
      git commit -m "docs(m13): actores y casos de uso prioritarios"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Actores y casos de uso prioritarios" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m13-diseno/casos-de-uso.md (actores + UC prioritarios)
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

      `git add projects/m13-diseno/casos-de-uso.md`
    comandoEsperado:
      - git add projects/m13-diseno/casos-de-uso.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m13-diseno/casos-de-uso.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Borrador sólido de `projects/m13-diseno/casos-de-uso.md`: actores +
          casos Must del piloto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Lista casos Must
    xp: 10
    cuerpo: >-
      Crea o amplía `projects/m13-diseno/casos-de-uso.md` con secciones
      **Actores** y **Casos prioritarios (Must)**.


      Tabla mínima esperada:


      | ID | Nombre | Actor | Traza SRS | Notas |

      |----|--------|-------|-----------|-------|

      | UC-01 | Iniciar sesión | Owner/Staff | H-auth-01 | cookie/sesión |

      | UC-02 | Crear cliente | Owner/Staff | H-cli-01 | |

      | UC-03 | Crear pedido | Staff | H-pedido-01 | slot + servicio |

      | UC-04 | Cancelar pedido | Staff | H-pedido-02 | |

      | UC-05 | Listar agenda del día | Staff | H-pedido-03 | |


      Ajusta IDs a tu SRS; no copies ciegos.
  - id: s7
    tipo: explicacion
    titulo: 3. Diagrama ligero opcional
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
