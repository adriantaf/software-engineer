---
id: L04
materia: M05
orden: 4
titulo: Diagrama CPU–RAM–I/O (P1)
horas: 5
semana: 1
lectura: Repaso Stallings semana 1 + síntesis en diagrama.md
evidencia: projects/m05-como-corre/diagrama.md (P1) commiteado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la semana integrando L01–L03 en un documento de una página que
      alimenta la **práctica P1**.


      **Objetivo de esta lección:** Redactar `diagrama.md`: CPU, memoria
      principal, almacenamiento y E/S, con flujos de datos al ejecutar un
      programa Node, en lenguaje claro y académico.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Consolidar apuntes
    xp: 10
    cuerpo: >-
      Relee `notas-L01.md`, `ciclo-instruccion.md`, `es-y-buses.md`. Lista **10
      conceptos** que deben aparecer en el diagrama final (marca los que
      faltan).
  - id: s3
    tipo: ejemplo
    titulo: Redacción `diagrama.md`
    xp: 10
    cuerpo: >-
      Crea `projects/m05-como-corre/diagrama.md` (máx. ~1 página impresa; puedes
      usar imagen + texto): Estructura sugerida: ```markdown # Diagrama
      CPU–RAM–I/O — M05
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Diagrama CPU–RAM–I/O (P1)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `diagrama.md` cumple P1 (1 página clara, CPU–RAM–I/O + flujo con
          `node`).
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Diagrama CPU–RAM–I/O
          (P1)
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
      ¿Es recomendable en esta lección? “Diagrama bonito sin explicación en
      prosa."
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
          Redactar `diagrama.md`: CPU, memoria principal, almacenamiento y E/S,
          con flujos de datos al ejecutar un programa Node, en lenguaje claro y
          académico.
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
    pregunta: ¿Debes hacer esto? “Olvidar buses o el rol del SO en E/S."
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
        `diagrama.md` cumple P1 (1 página clara, CPU–RAM–I/O + flujo con
        `node`).
      - Incluye interpretación de `free -h` y `df -h` (o equivalente en tu SO).
      - Hay commit en git con la evidencia de la semana 1.
      - Marca P1 en la ficha solo cuando el diagrama esté completo y commiteado.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Diagrama CPU–RAM–I/O (P1)

**~5 h · Semana 1**

Cierras la semana integrando L01–L03 en un documento de una página que alimenta la **práctica P1**.

## Objetivo

Redactar `diagrama.md`: CPU, memoria principal, almacenamiento y E/S, con flujos de datos al ejecutar un programa Node, en lenguaje claro y académico.

## Pasos

### 1. Consolidar apuntes (45 min)

Relee `notas-L01.md`, `ciclo-instruccion.md`, `es-y-buses.md`. Lista **10 conceptos** que deben aparecer en el diagrama final (marca los que faltan).

### 2. Redacción `diagrama.md` (90–120 min)

Crea `projects/m05-como-corre/diagrama.md` (máx. ~1 página impresa; puedes usar imagen + texto):

Estructura sugerida:

```markdown
# Diagrama CPU–RAM–I/O — M05

## Vista general
(diagrama ASCII o enlace a imagen)

## Componentes
### CPU
### Memoria principal
### Almacenamiento
### E/S y buses

## Flujo al ejecutar `node script.js`
1. ...
2. ...

## Límites de este modelo
(qué simplificamos: caché, múltiples núcleos, etc.)
```

Escribe para un compañero de primer año de ingeniería: preciso, sin jerga vacía.

### 3. Comandos de sistema (30 min)

```bash
free -h    # memoria
df -h      # disco montado
```

Integra en el documento una subsección **“En mi máquina hoy”** interpretando salida (memoria usada vs disponible; filesystem vs RAM).

### 4. Commit de evidencia (20 min)

```bash
git add projects/m05-como-corre/
git commit -m "docs(m05): diagrama CPU-RAM-I/O y apuntes semana 1"
```

### 5. Autoexamen (30 min)

Sin mirar apuntes, explica en voz alta el diagrama. Graba bullet points de lagunas y corrige el Markdown.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Repaso caps. semana 1 |
| Tus archivos | L01–L03 en `projects/m05-como-corre/` |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. `diagrama.md` cumple P1 (1 página clara, CPU–RAM–I/O + flujo con `node`).
2. Incluye interpretación de `free -h` y `df -h` (o equivalente en tu SO).
3. Hay commit en git con la evidencia de la semana 1.

Marca **P1** en la ficha solo cuando el diagrama esté completo y commiteado.

## Errores comunes

- Diagrama bonito sin explicación en prosa.
- Olvidar buses o el rol del SO en E/S.
- Página interminable (más de ~800 palabras sin necesidad).

## Siguiente

[L05 — Memoria principal y direccionamiento](L05-memoria-principal-y-direccionamiento.md)
