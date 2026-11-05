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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Exportación CSV de hábitos (id, nombre, # completados) y
      documentación que otra persona pueda seguir sin ti.


      CSV es el puente hacia hojas de cálculo y análisis. El README es evidencia
      de comunicación técnica.
  - id: s2
    tipo: ejemplo
    titulo: 1. Generador CSV
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Export CSV y entrega final CLI" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: comando export --csv + README completo m02-habits
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
    pregunta: ¿Es buena práctica en esta lección? “CSV sin escapar comas en nombres."
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
          Exportación CSV de hábitos (id, nombre, # completados) y documentación
          que otra persona pueda seguir sin ti.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Comando export
    xp: 10
    cuerpo: >-
      `export --csv [ruta]` — si no hay ruta, imprime a stdout. Tests del escape
      CSV.
  - id: s7
    tipo: explicacion
    titulo: 3. README final
    xp: 10
    cuerpo: |-
      `projects/m02-habits/README.md`:

      - Instalación
      - Todos los comandos con ejemplos
      - Dónde vive `data/habits.json`
      - `npm test`
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`export --csv` genera archivo válido abrible en Excel/LibreOffice.'
      - README cumple requisitos mínimos de la ficha M02.
      - '`npm test` sigue verde.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
