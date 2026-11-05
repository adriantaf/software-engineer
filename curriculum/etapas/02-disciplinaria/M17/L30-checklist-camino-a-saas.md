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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - checklist

      - gap

      - SaaS


      **Objetivo de esta lección:** Completar checklist ficha: tablas, roles,
      HTTPS, tests — gaps honestos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist SaaS
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

      Marca hecho/gap con enlace a evidencia.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/checklist-saas.md
      git commit -m "docs(m17): L30 checklist camino saas"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Checklist camino a SaaS», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Checklist camino a SaaS
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

      `git add projects/m17-vitrina/docs/checklist-saas.md`
    comandoEsperado:
      - git add projects/m17-vitrina/docs/checklist-saas.md
      - 'git commit -m "docs(m17): L30 checklist camino saas"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m17-vitrina/docs/checklist-saas.md'
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
          Completar checklist ficha: tablas, roles, HTTPS, tests — gaps
          honestos.
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

      `git commit -m "docs(m17): L30 checklist camino saas"`
    comandoEsperado:
      - 'git commit -m "docs(m17): L30 checklist camino saas"'
    explicacionError: 'Esperado: git commit -m "docs(m17): L30 checklist camino saas"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m17-vitrina/docs/checklist-saas.md` con ítems marcados
        o gaps enlazados.
      - 'Commit `docs(m17): L30 checklist-camino-a-saas`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
