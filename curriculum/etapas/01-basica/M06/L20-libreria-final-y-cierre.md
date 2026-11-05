---
id: L20
materia: M06
orden: 20
titulo: Librería final y cierre de etapa básica
horas: 5
semana: 5
lectura: Ficha M06 criterios; repaso M02 código para 5 mejoras
evidencia: npm pack final + cierre-etapa.md con 5 mejoras M02
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras M06 y la **Etapa Básica**: librería empaquetada, evidencias
      completas, reflexión sobre M02.


      **Objetivo de esta lección:** Entregar paquete local (`npm pack` o GitHub
      package si tienes remoto); completar checklist; redactar `cierre-etapa.md`
      con 5 mejoras concretas al código M02.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría final
    xp: 10
    cuerpo: |-
      ```bash
      npm run test
      npm run build
      npm pack
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Build y pack
    xp: 10
    cuerpo: |-
      ```bash
      npm run test
      npm run build
      npm pack
      ```

      Guarda nombre del `.tgz` en bitácora.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Librería final y cierre de etapa básica», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Tarball generado y probado.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Librería final y cierre
          de etapa básica
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

      `npm run test`
    comandoEsperado:
      - npm run test
      - npm run build
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm run test'
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
          Entregar paquete local (`npm pack` o GitHub package si tienes remoto);
          completar checklist; redactar `cierre-etapa.md` con 5 mejoras
          concretas al código M02.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M06
    xp: 25
    enunciado: >-
      Cierra **Programación II (OO, tipos y errores)** con evidencia real en el
      repo. Marca la rúbrica solo si puedes demostrar cada criterio (si no está
      en git, no cuenta).
    entregables:
      - 'P1: Modelar un dominio con clases/interfaces (sin framework)'
      - 'P2: Refactor a Código limpio (nombres, funciones pequeñas)'
      - 'P3: Manejo de errores tipado + tests de borde'
      - 'Proyecto: Librería reutilizable publicada (npm local o GitHub package)'
      - npm pack final + cierre-etapa.md con 5 mejoras M02
    rubrica:
      - id: r1
        criterio: Tarball generado y probado.
      - id: r2
        criterio: '`cierre-etapa.md` con 5 mejoras M02 accionables.'
      - id: r3
        criterio: Evidencia proyecto completa; puedes enseñar la librería en 3 minutos.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Tarball generado y probado.
      - '`cierre-etapa.md` con 5 mejoras M02 accionables.'
      - Evidencia proyecto completa; puedes enseñar la librería en 3 minutos.
    siguiente: Materia M06 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Librería final y cierre de etapa básica

**~5 h · Semana 5**

Cierras M06 y la **Etapa Básica**: librería empaquetada, evidencias completas, reflexión sobre M02.

## Objetivo

Entregar paquete local (`npm pack` o GitHub package si tienes remoto); completar checklist; redactar `cierre-etapa.md` con 5 mejoras concretas al código M02.

## Pasos

### 1. Auditoría final (60 min)

| Ítem | OK |
|------|-----|
| P1 dominio TS | |
| P2 refactor | |
| P3 bordes | |
| Proyecto README/semver/tests | |

### 2. Build y pack (45 min)

```bash
npm run test
npm run build
npm pack
```

Guarda nombre del `.tgz` en bitácora.

### 3. Prueba de consumo (60 min)

Proyecto vacío temporal importa tu paquete; ejecuta ejemplo.

### 4. Revisión M02 (90 min)

Abre `projects/m02-habits/` (o tu CLI M02). Escribe `cierre-etapa.md`:

```markdown
# Cierre etapa básica — M06

## Librería
- Paquete:
- Versión:

## Cinco mejoras concretas para M02
1. (archivo:línea — qué cambiar — principio)
...
```

Debe ser específico, no “usar mejores nombres”.

### 5. Criterios de dominio (30 min)

Autoevalúa checkboxes de la ficha M06. Graba commit final:

```bash
git add .
git commit -m "feat(m06): libreria final y cierre etapa basica"
```

### 6. Retro (15 min)

¿Cuándo no usar herencia? Respuesta escrita en `cierre-etapa.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Ficha M06 | Criterios de dominio |
| Tu M02 | Código real a mejorar |
| Catálogo | [Bibliografía · M06](../../../bibliografia.md#m06-programacion-ii) |


## Hecho cuando

1. Tarball generado y probado.
2. `cierre-etapa.md` con 5 mejoras M02 accionables.
3. Evidencia proyecto completa; puedes enseñar la librería en 3 minutos.

## Errores comunes

- Marcar proyecto sin tarball.
- Mejoras M02 vagas.

## Siguiente

Siguiente etapa del plan: **Etapa Disciplinaria** (M07 en adelante). Revisa [README etapa básica](../README.md).
