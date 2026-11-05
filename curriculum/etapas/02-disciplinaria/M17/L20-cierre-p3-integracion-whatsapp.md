---
id: L20
materia: M17
orden: 20
titulo: Cierre P3 integración WhatsApp
horas: 5
semana: 5
lectura: Ficha P3
evidencia: integracion-whatsapp.md completo
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar doc P3: capturas, límites legales/opt-in, qué no
      hace la integración.


      - P3

      - opt-in

      - gap
  - id: s2
    tipo: ejemplo
    titulo: 1. Cierra doc P3
    xp: 10
    cuerpo: |-
      ```bash
      rg -n "P3|WhatsApp" projects/m17-vitrina/README.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre P3 integración WhatsApp" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: integracion-whatsapp.md completo
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `git add projects/m17-vitrina/docs/integracion-whatsapp.md
      projects/m17-vitrina/README.md`
    comandoEsperado:
      - >-
        git add projects/m17-vitrina/docs/integracion-whatsapp.md
        projects/m17-vitrina/README.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/m17-vitrina/docs/integracion-whatsapp.md
      projects/m17-vitrina/README.md
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar doc P3: capturas, límites legales/opt-in, qué no hace la
          integración.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Checklist README
    xp: 10
    cuerpo: |-
      ```bash
      rg -n "P3|WhatsApp" projects/m17-vitrina/README.md
      ```

      Marca P3 si el botón + doc existen.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: >-
      ```bash

      git add projects/m17-vitrina/docs/integracion-whatsapp.md
      projects/m17-vitrina/README.md

      git commit -m "docs(m17): L20 cierre P3 whatsapp"

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/integracion-whatsapp.md` completo; P3 marcado
        en README.
      - 'Commit `docs(m17): L20 cierre-p3-integracion-whatsapp`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L20 — Cierre P3 integración WhatsApp

**~5.0 h · Semana 5**

P3 no sustituye API oficial si no está configurada — documenta gaps.

## Objetivo

Completar doc P3: capturas, límites legales/opt-in, qué no hace la integración.

## Conceptos clave

- P3
- opt-in
- gap

## Pasos (hazlos en orden)

### 1. Cierra doc P3 (50–60 min)

Completa `projects/m17-vitrina/docs/integracion-whatsapp.md`: flujo, límites (manual), riesgos PII en URL, captura demo.

### 2. Checklist README (30 min)

```bash
rg -n "P3|WhatsApp" projects/m17-vitrina/README.md
```

Marca P3 si el botón + doc existen.

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/integracion-whatsapp.md projects/m17-vitrina/README.md
git commit -m "docs(m17): L20 cierre P3 whatsapp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha P3 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/integracion-whatsapp.md` completo; P3 marcado en README.
2. Commit `docs(m17): L20 cierre-p3-integracion-whatsapp`.

## Errores comunes

- Marcar P3 sin botón + doc.
- Doc genérico sin flujo del piloto.

## Siguiente

[L21 — Variables de entorno y secrets](L21-variables-de-entorno-y-secrets.md)
