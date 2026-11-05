---
id: L15
materia: M17
orden: 15
titulo: 'Listas con loading, error y vacío'
horas: 5
semana: 4
lectura: m16 estados-ui
evidencia: projects/m17-vitrina/docs/ui-estados.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - loading

      - empty

      - error boundary


      **Objetivo de esta lección:** Implementar agenda del día y listas con tres
      estados UX obligatorios.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Estados de lista
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/ui-estados.md << 'EOF'
      # UI estados (P2)
      | Vista | loading | error | vacío |
      |-------|---------|-------|-------|
      | /pedidos | … | … | … |
      EOF
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta ui-estados.md
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/ui-estados.md << 'EOF'
      # UI estados (P2)
      | Vista | loading | error | vacío |
      |-------|---------|-------|-------|
      | /pedidos | … | … | … |
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Listas con loading, error y vacío», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Listas con loading,
          error y vacío
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


      `git add projects/m17-vitrina/docs/ui-estados.md
      projects/m17-vitrina/apps`
    comandoEsperado:
      - >-
        git add projects/m17-vitrina/docs/ui-estados.md
        projects/m17-vitrina/apps
      - 'git commit -m "feat(m17): L15 listas loading error vacio"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/m17-vitrina/docs/ui-estados.md
      projects/m17-vitrina/apps
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
        texto: Implementar agenda del día y listas con tres estados UX obligatorios.
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
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/ui-estados.md projects/m17-vitrina/apps
      git commit -m "feat(m17): L15 listas loading error vacio"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/ui-estados.md` con loading/error/vacío
        para listas.
      - 'Commit `docs(m17): L15 listas-con-loading-error-y-vacio`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Listas con loading, error y vacío

**~5.0 h · Semana 4**

P2 exige documentación de estados.

## Objetivo

Implementar agenda del día y listas con tres estados UX obligatorios.

## Conceptos clave

- loading
- empty
- error boundary

## Pasos (hazlos en orden)

### 1. Estados de lista (70–90 min)

Loading skeleton/spinner; error con reintento; vacío con CTA “Crear pedido”.

### 2. Documenta ui-estados.md (30–40 min)

```bash
cat > projects/m17-vitrina/docs/ui-estados.md << 'EOF'
# UI estados (P2)
| Vista | loading | error | vacío |
|-------|---------|-------|-------|
| /pedidos | … | … | … |
EOF
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/ui-estados.md projects/m17-vitrina/apps
git commit -m "feat(m17): L15 listas loading error vacio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m16 estados-ui | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/ui-estados.md` con loading/error/vacío para listas.
2. Commit `docs(m17): L15 listas-con-loading-error-y-vacio`.

## Errores comunes

- Spinner eterno sin timeout/error.
- Vacío idéntico a error.

## Siguiente

[L16 — Formularios pedidos y clientes accesibles](L16-formularios-pedidos-y-clientes-accesibles.md)
