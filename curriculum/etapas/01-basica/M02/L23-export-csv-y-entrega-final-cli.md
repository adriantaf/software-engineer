---
id: L23
materia: M02
orden: 23
titulo: Export CSV y entrega final CLI
horas: 2.5
semana: 6
lectura: — (foco proyecto + README)
evidencia: comando export --csv + README completo m02-habits
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      CSV es el puente hacia hojas de cálculo y análisis. El README es evidencia
      de comunicación técnica.


      **Objetivo de esta lección:** Exportación CSV de hábitos (id, nombre, #
      completados) y documentación que otra persona pueda seguir sin ti.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Generador CSV
    xp: 10
    cuerpo: |-
      ```ts
      import type { Habito } from "../modelo/habito.js";

      export function habitosACsv(habitos: Habito[]): string {
        const header = "id,nombre,marcados";
        const rows = habitos.map(
          (h) => `${h.id},${escapeCsv(h.nombre)},${h.completados.length}`
        );
        return [header, ...rows].join("\n");
      }

      function escapeCsv(s: string): string {
        if (/[",\n]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
        return s;
      }
      ```

      `src/dominio/exportar-csv.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Comando export
    xp: 10
    cuerpo: |-
      ```ts
      import type { Habito } from "../modelo/habito.js";

      export function habitosACsv(habitos: Habito[]): string {
        const header = "id,nombre,marcados";
        const rows = habitos.map(
          (h) => `${h.id},${escapeCsv(h.nombre)},${h.completados.length}`
        );
        return [header, ...rows].join("\n");
      }

      function escapeCsv(s: string): string {
        if (/[",\n]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
        return s;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Export CSV y entrega final CLI», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: '`export --csv` genera archivo válido abrible en Excel/LibreOffice.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Export CSV y entrega
          final CLI
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
    pregunta: ¿Es recomendable en esta lección? “CSV sin escapar comas en nombres."
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
          Exportación CSV de hábitos (id, nombre, # completados) y documentación
          que otra persona pueda seguir sin ti.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README final
    xp: 10
    cuerpo: >-
      `projects/m02-habits/README.md`: - Instalación - Todos los comandos con
      ejemplos - Dónde vive `data/habits.json` - `npm test`
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`export --csv` genera archivo válido abrible en Excel/LibreOffice.'
      - README cumple requisitos mínimos de la ficha M02.
      - '`npm test` sigue verde.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L23 — Export CSV y entrega final CLI

**~2.5 h · Semana 6**

Cierras funcionalidad: `export --csv` a archivo o stdout, README con ejemplos copy-paste, checklist de requisitos del proyecto.

## Objetivo

Exportación CSV de hábitos (id, nombre, # completados) y documentación que otra persona pueda seguir sin ti.

## Por qué importa

CSV es el puente hacia hojas de cálculo y análisis. El README es evidencia de comunicación técnica.

## Pasos

### 1. Generador CSV (50 min)

`src/dominio/exportar-csv.ts`:

```ts
import type { Habito } from "../modelo/habito.js";

export function habitosACsv(habitos: Habito[]): string {
  const header = "id,nombre,marcados";
  const rows = habitos.map(
    (h) => `${h.id},${escapeCsv(h.nombre)},${h.completados.length}`
  );
  return [header, ...rows].join("\n");
}

function escapeCsv(s: string): string {
  if (/[",\n]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
  return s;
}
```

### 2. Comando export (40 min)

`export --csv [ruta]` — si no hay ruta, imprime a stdout. Tests del escape CSV.

### 3. README final (50 min)

`projects/m02-habits/README.md`:

- Instalación
- Todos los comandos con ejemplos
- Dónde vive `data/habits.json`
- `npm test`

### 4. Verificación requisitos (20 min)

Tabla en README: add/list/done/stats/export ✓

## Lectura de esta lección

Opcional: EJ cap. 7 si buscas ideas de proyecto integrador.

## Hecho cuando

1. `export --csv` genera archivo válido abrible en Excel/LibreOffice.
2. README cumple requisitos mínimos de la ficha M02.
3. `npm test` sigue verde.

## Errores comunes

- CSV sin escapar comas en nombres.
- README sin comandos reales probados.
- Commitear CSV con datos personales.

## Siguiente

[L24 — Cierre M02 y evidencias](L24-cierre-m02-y-evidencias.md)
