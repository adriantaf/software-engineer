---
id: L17
materia: M13
orden: 17
titulo: Índice del paquete de diseño
horas: 5
semana: 5
lectura: Empaquetar evidencias; README como mapa M17
evidencia: projects/m13-diseno/README.md índice enlazando SRS/diagramas/ADRs
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El proyecto de M13 es el paquete. Hoy el README se vuelve el mapa.


      **Objetivo de esta lección:** Reescribir `projects/m13-diseno/README.md`
      como índice navegable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m13-diseno -type f -name '*.md' | sort
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: README índice
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m13-diseno/README.md
      git commit -m "docs(m13): indice del paquete de diseno"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Índice del paquete de diseño», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Índice del paquete de
          diseño
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

      `find projects/m13-diseno -type f -name '*.md' | sort`
    comandoEsperado:
      - find projects/m13-diseno -type f -name '*.md' | sort
      - git add projects/m13-diseno/README.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: find projects/m13-diseno -type f -name ''*.md'' | sort'
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
        texto: Reescribir `projects/m13-diseno/README.md` como índice navegable.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Rompe enlaces
    xp: 10
    cuerpo: 'Haz clic mental: cada ruta relativa debe existir.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'README M13 enlaza SRS, casos-de-uso, diagramas, arquitectura y ADRs.'
      - Un extraño puede navegar el paquete en ≤10 minutos.
      - 'Commit `docs(m13): indice del paquete de diseno`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L17 — Índice del paquete de diseño

**~5.0 h · Semana 5**

El proyecto de M13 es el paquete. Hoy el README se vuelve el mapa.

## Objetivo

Reescribir `projects/m13-diseno/README.md` como índice navegable.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

```bash
find projects/m13-diseno -type f -name '*.md' | sort
```

### 2. README índice (80–100 min)

Secciones: En resumen · Enlace SRS · Flujos · Diagramas · Arquitectura · ADRs · Checklist evidencias P1–P3 · Cómo empezar M17.

### 3. Rompe enlaces (20 min)

Haz clic mental: cada ruta relativa debe existir.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/README.md
git commit -m "docs(m13): indice del paquete de diseno"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | README índice del paquete de diseño Vitrina | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. README M13 enlaza SRS, casos-de-uso, diagramas, arquitectura y ADRs.
2. Un extraño puede navegar el paquete en ≤10 minutos.
3. Commit `docs(m13): indice del paquete de diseno`.

## Errores comunes

- README genérico de la plantilla sin enlaces.
- Enlaces rotos a archivos que no existen.
- Diagramas huérfanos fuera del índice.

## Siguiente

[L18 — Endpoints y módulos previstos M17](L18-endpoints-y-modulos-previstos-m17.md)
