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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - P3

      - opt-in

      - gap


      **Objetivo de esta lección:** Completar doc P3: capturas, límites
      legales/opt-in, qué no hace la integración.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Cierra doc P3
    xp: 10
    cuerpo: |-
      ```bash
      rg -n "P3|WhatsApp" projects/m17-vitrina/README.md
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Checklist README
    xp: 10
    cuerpo: |-
      ```bash
      rg -n "P3|WhatsApp" projects/m17-vitrina/README.md
      ```

      Marca P3 si el botón + doc existen.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre P3 integración WhatsApp», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre P3 integración
          WhatsApp
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `git add projects/m17-vitrina/docs/integracion-whatsapp.md
      projects/m17-vitrina/README.md`
    comandoEsperado:
      - >-
        git add projects/m17-vitrina/docs/integracion-whatsapp.md
        projects/m17-vitrina/README.md
      - 'git commit -m "docs(m17): L20 cierre P3 whatsapp"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/m17-vitrina/docs/integracion-whatsapp.md
      projects/m17-vitrina/README.md
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
          Completar doc P3: capturas, límites legales/opt-in, qué no hace la
          integración.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
