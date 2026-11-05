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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar paquete local (`npm pack` o GitHub package si
      tienes remoto); completar checklist; redactar `cierre-etapa.md` con 5
      mejoras concretas al código M02.


      Cierras M06 y la **Etapa Básica**: librería empaquetada, evidencias
      completas, reflexión sobre M02.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría final
    xp: 10
    cuerpo: |-
      ```bash
      npm run test
      npm run build
      npm pack
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Librería final y cierre de etapa básica" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: npm pack final + cierre-etapa.md con 5 mejoras M02
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

      `npm run test`
    comandoEsperado:
      - npm run test
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm run test'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Entregar paquete local (`npm pack` o GitHub package si tienes remoto);
          completar checklist; redactar `cierre-etapa.md` con 5 mejoras concre…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Build y pack
    xp: 10
    cuerpo: |-
      ```bash
      npm run test
      npm run build
      npm pack
      ```

      Guarda nombre del `.tgz` en bitácora.
  - id: s7
    tipo: explicacion
    titulo: 3. Prueba de consumo
    xp: 10
    cuerpo: Proyecto vacío temporal importa tu paquete; ejecuta ejemplo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Tarball generado y probado.
      - '`cierre-etapa.md` con 5 mejoras M02 accionables.'
      - Evidencia proyecto completa; puedes enseñar la librería en 3 minutos.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
