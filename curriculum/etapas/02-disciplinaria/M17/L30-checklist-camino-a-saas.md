---
id: L30
materia: M17
orden: 30
titulo: Checklist camino a SaaS
horas: 5
semana: 8
lectura: Ficha M17 checklist
evidencia: projects/m17-vitrina/docs/checklist-saas.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar checklist ficha: tablas, roles, HTTPS, tests —
      gaps honestos.


      - checklist

      - gap

      - SaaS
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist SaaS
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/checklist-saas.md << 'EOF'
      # Camino a SaaS
      - [ ] Aislamiento tenant en queries
      - [ ] Billing (out of scope piloto)
      - [ ] Backups (→ M19)
      - [ ] Observabilidad
      - [ ] Onboarding self-serve
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Checklist camino a SaaS" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/checklist-saas.md
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

      `git add projects/m17-vitrina/docs/checklist-saas.md`
    comandoEsperado:
      - git add projects/m17-vitrina/docs/checklist-saas.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m17-vitrina/docs/checklist-saas.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Completar checklist ficha: tablas, roles, HTTPS, tests — gaps
          honestos.
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
      git add projects/m17-vitrina/docs/checklist-saas.md
      git commit -m "docs(m17): L30 checklist camino saas"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/checklist-saas.md` con ítems marcados
        o gaps enlazados.
      - 'Commit `docs(m17): L30 checklist-camino-a-saas`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L30 — Checklist camino a SaaS

**~5.0 h · Semana 8**

Transparencia > checkboxes mentirosos.

## Objetivo

Completar checklist ficha: tablas, roles, HTTPS, tests — gaps honestos.

## Conceptos clave

- checklist
- gap
- SaaS

## Pasos (hazlos en orden)

### 1. Checklist SaaS (70–90 min)

```bash
cat > projects/m17-vitrina/docs/checklist-saas.md << 'EOF'
# Camino a SaaS
- [ ] Aislamiento tenant en queries
- [ ] Billing (out of scope piloto)
- [ ] Backups (→ M19)
- [ ] Observabilidad
- [ ] Onboarding self-serve
EOF
```

Marca hecho/gap con enlace a evidencia.

### 2. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/checklist-saas.md
git commit -m "docs(m17): L30 checklist camino saas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 checklist | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/docs/checklist-saas.md` con ítems marcados o gaps enlazados.
2. Commit `docs(m17): L30 checklist-camino-a-saas`.

## Errores comunes

- Checklist todo OK sin enlaces a evidencia.
- Olvidar backups → M19.

## Siguiente

[L31 — Demo grabable para design partner](L31-demo-grabable-para-design-partner.md)
