---
id: L16
materia: M19
orden: 16
titulo: Cierre M19 — checklist pre-demo M22
horas: 5
semana: 4
lectura: Repaso M19
evidencia: projects/m19-ops/cierre-m19.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Verificar P1–P3, criterios dominio, prod estable para
      trials.


      - checklist

      - dominio
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist pre-demo M22
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/cierre-m19.md << 'EOF'
      # Cierre M19
      - [ ] docker.md P1
      - [ ] deploy-log HTTPS P2
      - [ ] restore-test.md P3
      - [ ] runbook.md
      Handoff: URL staging para M20/M22
      EOF
      ls projects/m19-ops
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M19 — checklist pre-demo M22" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/cierre-m19.md
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

      `ls projects/m19-ops`
    comandoEsperado:
      - ls projects/m19-ops
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: ls projects/m19-ops'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Verificar P1–P3, criterios dominio, prod estable para trials.'
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
      git add projects/m19-ops
      git commit -m "docs(m19): L16 cierre checklist pre-demo"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m19-ops/cierre-m19.md` checklist P1–P3 + handoff URL staging.'
      - 'Commit `docs(m19): L16 cierre-m19-checklist-pre-demo-m22`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Cierre M19 — checklist pre-demo M22

**~5.0 h · Semana 4**

Handoff a M20 (API staging HTTPS) y M22.

## Objetivo

Verificar P1–P3, criterios dominio, prod estable para trials.

## Conceptos clave

- checklist
- dominio

## Pasos (hazlos en orden)

### 1. Checklist pre-demo M22 (50–60 min)

```bash
cat > projects/m19-ops/cierre-m19.md << 'EOF'
# Cierre M19
- [ ] docker.md P1
- [ ] deploy-log HTTPS P2
- [ ] restore-test.md P3
- [ ] runbook.md
Handoff: URL staging para M20/M22
EOF
ls projects/m19-ops
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops
git commit -m "docs(m19): L16 cierre checklist pre-demo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Repaso M19 | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/cierre-m19.md` checklist P1–P3 + handoff URL staging.
2. Commit `docs(m19): L16 cierre-m19-checklist-pre-demo-m22`.

## Errores comunes

- Cerrar sin restore-test.
- No dejar URL staging para M20/M22.

## Siguiente

Materia siguiente: [M20 — Aplicaciones móviles](../M20-aplicaciones-moviles.md) (consume tu staging).
