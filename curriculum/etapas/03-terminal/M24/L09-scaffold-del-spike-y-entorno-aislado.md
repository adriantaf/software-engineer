---
id: L09
materia: M24
orden: 9
titulo: Scaffold del spike y entorno aislado
horas: 5
semana: 3
lectura: Quickstart oficial de la tecnología elegida
evidencia: projects/m24-emergentes/spike/README.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Bootstrap del PoC en rama/carpeta aislada sin tocar prod de
      Vitrina.


      M24 prohíbe merge experimental a prod sin go explícito.


      Conceptos que debes poder explicar al cerrar:


      - Rama spike/*

      - Secrets locales

      - Staging vs prod
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l09 scaffold-del-spike-y-entorno-aislado"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Scaffold del spike y entorno aislado" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m24-emergentes/spike/README.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Bootstrap del PoC en rama/carpeta aislada sin tocar prod de Vitrina.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m24-emergentes/spike`.


      `projects/m24-emergentes/spike/README.md`: prerequisitos, variables de
      entorno (nombres), comando para arrancar.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: Código mínimo o script en `spike/`; `.env.example` sin valores reales.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m24-emergentes/spike/README.md`.'
      - README con comando reproducible.
      - .env.example sin secretos.
      - 'Commit `docs(m24): l09 …` en el historial.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Scaffold del spike y entorno aislado

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/README.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Bootstrap del PoC en rama/carpeta aislada sin tocar prod de Vitrina.

## Por qué empieza así

M24 prohíbe merge experimental a prod sin go explícito.

Conceptos que debes poder explicar al cerrar:

- Rama spike/*
- Secrets locales
- Staging vs prod

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Quickstart oficial de la tecnología elegida_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/README.md`: prerequisitos, variables de entorno (nombres), comando para arrancar.

### 3. Laboratorio principal (90–120 min)

Código mínimo o script en `spike/`; `.env.example` sin valores reales.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l09 scaffold-del-spike-y-entorno-aislado"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Quickstart oficial de la tecnología elegida | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/README.md`.
2. README con comando reproducible.
3. .env.example sin secretos.
4. Commit `docs(m24): l09 …` en el historial.

## Errores comunes

- Commit de tokens.
- PoC directo en rama main del SaaS.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Flujo mínimo demostrable](L10-flujo-minimo-demostrable.md)
