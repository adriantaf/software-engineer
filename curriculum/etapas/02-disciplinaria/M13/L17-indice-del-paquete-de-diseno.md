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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Reescribir `projects/m13-diseno/README.md` como índice
      navegable.


      El proyecto de M13 es el paquete. Hoy el README se vuelve el mapa.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario
    xp: 10
    cuerpo: |-
      ```bash
      find projects/m13-diseno -type f -name '*.md' | sort
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Índice del paquete de diseño" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m13-diseno/README.md índice enlazando SRS/diagramas/ADRs
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

      `find projects/m13-diseno -type f -name '*.md' | sort`
    comandoEsperado:
      - find projects/m13-diseno -type f -name '*.md' | sort
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: find projects/m13-diseno -type f -name ''*.md'' | sort'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Reescribir `projects/m13-diseno/README.md` como índice navegable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. README índice
    xp: 10
    cuerpo: >-
      Secciones: En resumen · Enlace SRS · Flujos · Diagramas · Arquitectura ·
      ADRs · Checklist evidencias P1–P3 · Cómo empezar M17.
  - id: s7
    tipo: explicacion
    titulo: 3. Rompe enlaces
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
