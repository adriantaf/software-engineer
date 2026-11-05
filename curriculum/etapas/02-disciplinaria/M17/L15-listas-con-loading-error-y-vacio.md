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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar agenda del día y listas con tres estados UX
      obligatorios.


      - loading

      - empty

      - error boundary
  - id: s2
    tipo: ejemplo
    titulo: 1. Estados de lista
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Listas con loading, error y vacío" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/ui-estados.md
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


      `git add projects/m17-vitrina/docs/ui-estados.md
      projects/m17-vitrina/apps`
    comandoEsperado:
      - >-
        git add projects/m17-vitrina/docs/ui-estados.md
        projects/m17-vitrina/apps
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/m17-vitrina/docs/ui-estados.md
      projects/m17-vitrina/apps
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Implementar agenda del día y listas con tres estados UX obligatorios.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta ui-estados.md
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/ui-estados.md << 'EOF'
      UI estados (P2)
      | Vista | loading | error | vacío |
      |-------|---------|-------|-------|
      | /pedidos | … | … | … |
      EOF
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
