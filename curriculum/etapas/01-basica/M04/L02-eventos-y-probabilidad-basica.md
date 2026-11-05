---
id: L02
materia: M04
orden: 2
titulo: 'Eventos, reglas y frecuentismo'
horas: 5
semana: 1
lectura: 'Walpole cap. 2 (reglas, conteo básico) · OpenStax Ch. 3'
evidencia: projects/m04-stats/src/eventos-dado.ts + notas/eventos-dado.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      **Espacio muestral** = todos los resultados posibles. **Evento** =
      subconjunto que te interesa (“par”, “≥ 5”, “error 5xx”). En analytics,
      casi siempre trabajas con eventos discretos contables.


      **Objetivo de esta lección:** Implementar reglas P(Aᶜ), P(A ∪ B) en un
      ejemplo concreto (dado) y escribir qué evento responde una métrica de
      producto que elijas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dado en TS
    xp: 10
    cuerpo: >-
      ```ts

      export function lanzarDado(): number {
        return 1 + Math.floor(Math.random() * 6);
      }


      export function simularEvento(
        n: number,
        pred: (x: number) => boolean,
      ): { cuenta: number; frecuencia: number } {
        let cuenta = 0;
        for (let i = 0; i < n; i++) if (pred(lanzarDado())) cuenta++;
        return { cuenta, frecuencia: cuenta / n };
      }

      ```


      Crea `src/eventos-dado.ts`: Simula con n = 60_000: - A = “sale par” →
      teoría 3/6 - B = “sale 6” → teoría 1/6 - A ∩ B = “par y 6” → solo {6}
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Reglas en la nota
    xp: 10
    cuerpo: |-
      ```ts
      export function lanzarDado(): number {
        return 1 + Math.floor(Math.random() * 6);
      }

      export function simularEvento(
        n: number,
        pred: (x: number) => boolean,
      ): { cuenta: number; frecuencia: number } {
        let cuenta = 0;
        for (let i = 0; i < n; i++) if (pred(lanzarDado())) cuenta++;
        return { cuenta, frecuencia: cuenta / n };
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Eventos, reglas y frecuentismo», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `eventos-dado.ts` corre y reporta frecuencias cercanas a 0.5 y 1/6 con
          n grande.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Eventos, reglas y
          frecuentismo
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Tratar “OR” en lenguaje natural como
      unión inclusiva sin ver solapamiento."
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
          Implementar reglas P(Aᶜ), P(A ∪ B) en un ejemplo concreto (dado) y
          escribir qué evento responde una métrica de producto que elijas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Simular con n = 100 y concluir que la teoría “falla”."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `eventos-dado.ts` corre y reporta frecuencias cercanas a 0.5 y 1/6 con n
        grande.
      - La nota incluye tabla teórico vs simulado y un párrafo métrica→evento.
      - Commit en git.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Eventos, reglas y frecuentismo

**~5 h · Semana 1**

Defines eventos, complemento y unión; simulas un dado y contrastas frecuencias con probabilidades clásicas 1/6.

## Objetivo

Implementar reglas P(Aᶜ), P(A ∪ B) en un ejemplo concreto (dado) y escribir qué evento responde una métrica de producto que elijas.

## Idea clave

**Espacio muestral** = todos los resultados posibles. **Evento** = subconjunto que te interesa (“par”, “≥ 5”, “error 5xx”). En analytics, casi siempre trabajas con eventos discretos contables.

## Pasos

### 1. Dado en TS (40–50 min)

Crea `src/eventos-dado.ts`:

```ts
export function lanzarDado(): number {
  return 1 + Math.floor(Math.random() * 6);
}

export function simularEvento(
  n: number,
  pred: (x: number) => boolean,
): { cuenta: number; frecuencia: number } {
  let cuenta = 0;
  for (let i = 0; i < n; i++) if (pred(lanzarDado())) cuenta++;
  return { cuenta, frecuencia: cuenta / n };
}
```

Simula con n = 60_000:

- A = “sale par” → teoría 3/6
- B = “sale 6” → teoría 1/6
- A ∩ B = “par y 6” → solo {6}

### 2. Reglas en la nota (40 min)

En `notas/eventos-dado.md` escribe:

```markdown
# Dado — eventos

| Evento | Teórico | Simulado (n=…) |
|--------|---------|----------------|
| Par | 0.5 | |
| Seis | 1/6 | |
| Par ∩ Seis | 1/6 | |

## P(A ∪ B) en un ejemplo con dos eventos de producto
Ejemplo: usuario hace clic en banner (A) o en menú (B). ¿Qué pasa si cuentas doble a quien hace ambos?
```

Relaciona **unión** con métricas que no deben sumarse sin cuidado (usuarios únicos vs eventos).

### 3. Métrica → evento (30 min)

Elige una métrica real o ficticia (retención D7, crash, compra). Escribe:

- Espacio muestral (¿qué puede pasar por usuario/día?)
- Evento que mide el dashboard
- Un error de interpretación si confundes evento con usuario

### 4. Lectura (60 min)

Walpole cap. 2: reglas de probabilidad, complemento, suma para eventos mutuamente excluyentes.

### 5. Commit

```bash
git add projects/m04-stats/src/eventos-dado.ts projects/m04-stats/notas/eventos-dado.md
git commit -m "feat(m04): eventos y dado simulado L02"
```

## Lectura de esta lección

| Fuente | Foco |
|--------|------|
| Walpole | Cap. 2 — axiomas y reglas |
| OpenStax | Ch. 3 — sets y probability rules |
| Catálogo | [Bibliografía · M04](../../../bibliografia.md#m04-probabilidad-y-estadistica) |


## Hecho cuando

1. `eventos-dado.ts` corre y reporta frecuencias cercanas a 0.5 y 1/6 con n grande.
2. La nota incluye tabla teórico vs simulado y un párrafo métrica→evento.
3. Commit en git.

## Errores comunes

- Tratar “OR” en lenguaje natural como unión inclusiva sin ver solapamiento.
- Simular con n = 100 y concluir que la teoría “falla”.

## Siguiente

[L03 — Independencia y probabilidad condicional](L03-independencia-y-condicional.md)
