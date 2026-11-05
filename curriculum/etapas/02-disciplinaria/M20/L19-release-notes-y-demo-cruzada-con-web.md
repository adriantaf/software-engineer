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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Notas versión; misma cuenta web y móvil ven mismas pedidos.

      - paridad
      - demo
  - id: s2
    tipo: ejemplo
    titulo: 1. Release notes + demo cruzada
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Release notes y demo cruzada con web" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/release-notes.md
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

      `git add projects/m20-movil/release-notes.md`
    comandoEsperado:
      - git add projects/m20-movil/release-notes.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m20-movil/release-notes.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Notas versión; misma cuenta web y móvil ven mismas pedidos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil/release-notes.md
      git commit -m "docs(m20): L19 release notes demo cruzada"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe `projects/m20-movil/release-notes.md` con demo cruzada web↔app.
      - 'Commit `docs(m20): L19 release-notes-y-demo-cruzada-con-web`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
