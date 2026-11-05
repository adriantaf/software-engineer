---
id: L19
materia: M20
orden: 19
titulo: Release notes y demo cruzada con web
horas: 5
semana: 5
lectura: Paridad auth web/móvil
evidencia: projects/m20-movil/release-notes.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - paridad

      - demo


      **Objetivo de esta lección:** Notas versión; misma cuenta web y móvil ven
      mismas pedidos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Release notes + demo cruzada
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m20-movil/release-notes.md << 'EOF'
      # Release notes móvil
      - Login + lista pedidos (misma API que web)
      - Secure storage
      - Build: ver build-evidence.md
      Demo cruzada: misma pedido visible en web staging y app.
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil/release-notes.md
      git commit -m "docs(m20): L19 release notes demo cruzada"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Release notes y demo cruzada con web», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Release notes y demo
          cruzada con web
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

      `git add projects/m20-movil/release-notes.md`
    comandoEsperado:
      - git add projects/m20-movil/release-notes.md
      - 'git commit -m "docs(m20): L19 release notes demo cruzada"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m20-movil/release-notes.md'
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
        texto: Notas versión; misma cuenta web y móvil ven mismas pedidos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git commit -m "docs(m20): L19 release notes demo cruzada"`
    comandoEsperado:
      - 'git commit -m "docs(m20): L19 release notes demo cruzada"'
    explicacionError: 'Esperado: git commit -m "docs(m20): L19 release notes demo cruzada"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m20-movil/release-notes.md` con demo cruzada web↔app.
      - 'Commit `docs(m20): L19 release-notes-y-demo-cruzada-con-web`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L19 — Release notes y demo cruzada con web

**~5.0 h · Semana 5**

Proyecto M20 demuestra canal móvil de Vitrina.

## Objetivo

Notas versión; misma cuenta web y móvil ven mismas pedidos.

## Conceptos clave

- paridad
- demo

## Pasos (hazlos en orden)

### 1. Release notes + demo cruzada (50–60 min)

```bash
cat > projects/m20-movil/release-notes.md << 'EOF'
# Release notes móvil
- Login + lista pedidos (misma API que web)
- Secure storage
- Build: ver build-evidence.md
Demo cruzada: misma pedido visible en web staging y app.
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil/release-notes.md
git commit -m "docs(m20): L19 release notes demo cruzada"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Paridad auth web/móvil | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m20-movil/release-notes.md` con demo cruzada web↔app.
2. Commit `docs(m20): L19 release-notes-y-demo-cruzada-con-web`.

## Errores comunes

- Release notes genéricas sin Vitrina.
- Demo web y app con datos distintos sin notarlo.

## Siguiente

[L20 — Cierre M20 — dominio y README proyecto](L20-cierre-m20-dominio-y-readme-proyecto.md)
