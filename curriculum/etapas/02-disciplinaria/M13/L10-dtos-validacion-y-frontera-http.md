---
id: L10
materia: M13
orden: 10
titulo: 'DTOs, validación y frontera HTTP'
horas: 5
semana: 3
lectura: DTO vs entidad; validación de entrada en frontera
evidencia: arquitectura.md sección DTOs + ejemplo CreateCitaDto
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Ampliar `arquitectura.md` (o `diagramas/dtos.md`) con
      contratos de entrada/salida del piloto.


      La frontera HTTP es el primer filtro: basura in → 400. El dominio recibe
      datos ya saneados.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario de endpoints que ya prevés
    xp: 10
    cuerpo: >-
      ```ts

      // contrato documental (aún sin código M17)

      type CreateCitaDto = {
        clienteId: string;   // uuid
        servicioId: string;
        inicio: string;      // ISO-8601
      };

      // fin se calcula con duracionMin del servicio (o viene explícito — decide
      y documenta)

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "DTOs, validación y frontera HTTP" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: arquitectura.md sección DTOs + ejemplo CreateCitaDto
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Aceptar el body entero y pasarlo al
      INSERT."
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
        texto: >-
          Ampliar `arquitectura.md` (o `diagramas/dtos.md`) con contratos de
          entrada/salida del piloto.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Especifica CreateCitaDto
    xp: 10
    cuerpo: >-
      ```ts

      // contrato documental (aún sin código M17)

      type CreateCitaDto = {
        clienteId: string;   // uuid
        servicioId: string;
        inicio: string;      // ISO-8601
      };

      // fin se calcula con duracionMin del servicio (o viene explícito — decide
      y documenta)

      ```


      Validaciones: uuid formato, `inicio` futuro (o ≥ ahora−slack), servicio
      existe.
  - id: s7
    tipo: explicacion
    titulo: 3. Respuesta pública
    xp: 10
    cuerpo: >-
      Lista campos del 201: `id`, `inicio`, `fin`, `estado`, `clienteId` —
      **sin** datos de otros módulos sensibles.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Documentas al menos `CreateCitaDto` / respuesta con campos y
        validaciones (tipos, rangos).
      - 'Dejas claro: entidad de dominio ≠ JSON crudo del request.'
      - 'Commit `docs(m13): DTOs y validacion en frontera HTTP`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — DTOs, validación y frontera HTTP

**~5.0 h · Semana 3**

La frontera HTTP es el primer filtro: basura in → 400. El dominio recibe datos ya saneados.

## Objetivo

Ampliar `arquitectura.md` (o `diagramas/dtos.md`) con contratos de entrada/salida del piloto.

## Pasos (hazlos en orden)

### 1. Inventario de endpoints que ya prevés (30 min)

De L02/L08: `POST /auth/login`, `POST /pedidos`, `GET /pedidos`, `POST /clientes`, …

### 2. Especifica CreateCitaDto (60–70 min)

```ts
// contrato documental (aún sin código M17)
type CreateCitaDto = {
  clienteId: string;   // uuid
  servicioId: string;
  inicio: string;      // ISO-8601
};
// fin se calcula con duracionMin del servicio (o viene explícito — decide y documenta)
```

Validaciones: uuid formato, `inicio` futuro (o ≥ ahora−slack), servicio existe.

### 3. Respuesta pública (40 min)

Lista campos del 201: `id`, `inicio`, `fin`, `estado`, `clienteId` — **sin** datos de otros módulos sensibles.

### 4. Regla de oro (20 min)

Un párrafo: “El controller valida forma; el service/domain valida negocio (solape, rol).”

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): DTOs y validacion en frontera HTTP"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | DTOs de entrada/salida; validar en HTTP antes del dominio | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas al menos `CreateCitaDto` / respuesta con campos y validaciones (tipos, rangos).
2. Dejas claro: entidad de dominio ≠ JSON crudo del request.
3. Commit `docs(m13): DTOs y validacion en frontera HTTP`.

## Errores comunes

- Aceptar el body entero y pasarlo al INSERT.
- Validar solo en el front.
- Mezclar campos internos (`passwordHash`) en DTO de respuesta.

## Siguiente

[L11 — Componentes y despliegue (C4 ligero)](L11-componentes-y-despliegue-c4-ligero.md)
