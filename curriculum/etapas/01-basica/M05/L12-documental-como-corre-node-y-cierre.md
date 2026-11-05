---
id: L12
materia: M05
orden: 12
titulo: Documental “cómo corre node” y cierre
horas: 5
semana: 3
lectura: Repaso Stallings semana 3 + README del proyecto M05
evidencia: projects/m05-como-corre/README ampliado (proyecto) + checklist M05
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Integras arquitectura, memoria y representación en un relato técnico: de
      la tecla Enter al output en terminal.


      **Objetivo de esta lección:** Ampliar `projects/m05-como-corre/README.md`
      (o `COMO-CORRE.md`) describiendo el camino desde `node cli.js` hasta el
      output, con procesos, memoria y syscalls a nivel conceptual; cerrar M05
      con autoevaluación.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige un CLI real
    xp: 10
    cuerpo: >-
      ```bash

      node -e "console.log(process.version)"

      ```


      Usa un script tuyo de M02 (`projects/m02-habits/` o similar) o: Debe ser
      un comando que puedas repetir mientras observas el SO.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Redacta el documental
    xp: 10
    cuerpo: |-
      ```bash
      node -e "console.log(process.version)"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Documental “cómo corre node” y cierre», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          README del proyecto describe el camino completo `node` → output con
          secciones pedidas.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Documental “cómo corre
          node” y cierre
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
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
          Ampliar `projects/m05-como-corre/README.md` (o `COMO-CORRE.md`)
          describiendo el camino desde `node cli.js` hasta el output, con
          procesos, memoria y syscalls a…
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Olvidar syscalls/E/S al hablar solo de CPU."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M05
    xp: 25
    enunciado: >-
      Cierra **Organización de computadoras** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Diagrama CPU–memoria–I/O con tus palabras'
      - 'P2: Ejercicios de representación binaria / enteros / floats (intro)'
      - 'P3: Medir tiempo de un programa y relacionarlo con caché/IO'
      - 'Proyecto: Mini-documental técnico (escrito) de cómo corre tu CLI'
      - projects/m05-como-corre/README ampliado (proyecto) + checklist M05
    rubrica:
      - id: r1
        criterio: >-
          README del proyecto describe el camino completo `node` → output con
          secciones pedidas.
      - id: r2
        criterio: Enlaces a evidencias L01–L11.
      - id: r3
        criterio: >-
          Commit final; puedes explicar RAM vs disco y por qué más hilos no
          siempre ayuda.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        README del proyecto describe el camino completo `node` → output con
        secciones pedidas.
      - Enlaces a evidencias L01–L11.
      - >-
        Commit final; puedes explicar RAM vs disco y por qué más hilos no
        siempre ayuda.
    siguiente: Materia M05 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Documental “cómo corre `node`” y cierre

**~5 h · Semana 3**

Integras arquitectura, memoria y representación en un relato técnico: de la tecla Enter al output en terminal.

## Objetivo

Ampliar `projects/m05-como-corre/README.md` (o `COMO-CORRE.md`) describiendo el camino desde `node cli.js` hasta el output, con procesos, memoria y syscalls a nivel conceptual; cerrar M05 con autoevaluación.

## Pasos

### 1. Elige un CLI real (30 min)

Usa un script tuyo de M02 (`projects/m02-habits/` o similar) o:

```bash
node -e "console.log(process.version)"
```

Debe ser un comando que puedas repetir mientras observas el SO.

### 2. Redacta el documental (120–150 min)

Estructura mínima del README del proyecto:

```markdown
# Cómo corre mi CLI

## Comando estudiado
## 1. Shell y exec
## 2. Proceso Node (V8, heap, stack)
## 3. Carga de módulos / disco
## 4. CPU durante la lógica
## 5. E/S: stdout y terminal
## 6. Límites del modelo (caché, JIT, async)
## Referencias cruzadas
(enlaces a diagrama.md, benchmark, notas L01–L11)
```

Tono: ensayo técnico breve, no lista de buzzwords.

### 3. Diagrama de secuencia (60 min)

Añade diagrama ASCII o mermaid de 8–12 pasos desde invocación hasta output.

### 4. Checklist y criterios (45 min)

Verifica evidencia P1–P3 y proyecto. Marca criterios de dominio en la ficha solo si puedes demostrarlo oralmente.

### 5. Commit final (15 min)

```bash
git add projects/m05-como-corre/
git commit -m "docs(m05): documental como corre node y cierre M05"
```

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Repaso representación + sistema |
| Ficha M05 | Criterios de dominio |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. README del proyecto describe el camino completo `node` → output con secciones pedidas.
2. Enlaces a evidencias L01–L11.
3. Commit final; puedes explicar RAM vs disco y por qué más hilos no siempre ayuda.

## Errores comunes

- Copiar definiciones de Wikipedia sin anclarlas a **tu** comando.
- Olvidar syscalls/E/S al hablar solo de CPU.

## Siguiente

Siguiente materia del plan: **M06 — Programación II** ([ficha](../M06-programacion-ii.md), lección [L01](../M06/L01-dominio-inicial-y-entorno.md)).
