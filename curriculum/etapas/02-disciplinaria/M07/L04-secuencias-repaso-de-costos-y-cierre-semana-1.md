---
id: L04
materia: M07
orden: 4
titulo: 'Secuencias: repaso de costos y cierre semana 1'
horas: 5
semana: 1
lectura: 'Repaso arrays vs listas: cuándo cada una'
evidencia: COMPLEJIDAD.md completo semana 1 + bitácora semana
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar `COMPLEJIDAD.md` para array y listas, escribir
      bitácora de semana 1 y dejar tests verdes.


      Cierras la semana de secuencias dejando una tabla defendible y la suite
      verde.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría de código
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m07-estructuras
      find src -name '*.ts' | sort
      npm test
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Secuencias: repaso de costos y cierre semana 1" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: COMPLEJIDAD.md completo semana 1 + bitácora semana
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

      `cd projects/m07-estructuras`
    comandoEsperado:
      - cd projects/m07-estructuras
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m07-estructuras'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar `COMPLEJIDAD.md` para array y listas, escribir bitácora de
          semana 1 y dejar tests verdes.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tabla unificada
    xp: 10
    cuerpo: >-
      En `COMPLEJIDAD.md`, una tabla con columnas: operación | DynamicArray |
      Singly | Doubly. Filas: acceso, insert head, append, delete por valor,
      memoria extra por elemento.
  - id: s7
    tipo: explicacion
    titulo: 3. Mini experimento
    xp: 10
    cuerpo: >-
      Script `bench/sequences-smoke.ts` (o test de timing informal): 10_000
      prepends en lista vs unshift en array nativo. Pega 3 números en la
      bitácora (no hace falta microbenchmark serio aún).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `COMPLEJIDAD.md` tiene tabla comparativa array / lista simple / lista
        doble para insert head, append, acceso, delete.
      - >-
        Existe `bitacora/semana-01.md` (o sección en README) con 5–8 líneas de
        lo aprendido.
      - 'Suite `npm test` verde; commit `docs(m07): cierre semana 1 secuencias`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Secuencias: repaso de costos y cierre semana 1

**~5.0 h · Semana 1**

Cierras la semana de secuencias dejando una tabla defendible y la suite verde.

## Objetivo

Completar `COMPLEJIDAD.md` para array y listas, escribir bitácora de semana 1 y dejar tests verdes.

## Pasos

### 1. Auditoría de código (45 min)

```bash
cd projects/m07-estructuras
find src -name '*.ts' | sort
npm test
```

Anota gaps (métodos sin test, Big-O faltante).

### 2. Tabla unificada (75 min)

En `COMPLEJIDAD.md`, una tabla con columnas: operación | DynamicArray | Singly | Doubly. Filas: acceso, insert head, append, delete por valor, memoria extra por elemento.

### 3. Mini experimento (60 min)

Script `bench/sequences-smoke.ts` (o test de timing informal): 10_000 prepends en lista vs unshift en array nativo. Pega 3 números en la bitácora (no hace falta microbenchmark serio aún).

### 4. Bitácora (40 min)

```bash
mkdir -p bitacora
```

`bitacora/semana-01.md`: qué estructura elegirías para cola de impresión vs buffer de edición, en 2 frases cada una.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre semana 1 secuencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Trade-offs arrays vs listas (tiempo y memoria) | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `COMPLEJIDAD.md` tiene tabla comparativa array / lista simple / lista doble para insert head, append, acceso, delete.
2. Existe `bitacora/semana-01.md` (o sección en README) con 5–8 líneas de lo aprendido.
3. Suite `npm test` verde; commit `docs(m07): cierre semana 1 secuencias`.

## Errores comunes

- Tabla de costos inventada sin mirar tu código.
- Cerrar la semana con tests en rojo.
- Bitácora vacía o solo “terminé las lecciones”.

## Siguiente

[L05 — Pila (Stack) tipada](L05-pila-stack-tipada.md)
