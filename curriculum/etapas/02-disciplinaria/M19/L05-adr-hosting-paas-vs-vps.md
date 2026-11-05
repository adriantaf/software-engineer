---
id: L05
materia: M19
orden: 5
titulo: 'ADR hosting: PaaS vs VPS'
horas: 5
semana: 2
lectura: Docs Fly/Railway/Render o VPS
evidencia: projects/m19-ops/adr-hosting.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar decisión de hosting para Vitrina con criterios
      costo, TLS, Postgres gestionado, DX.


      - PaaS

      - VPS+Docker

      - egress y region
  - id: s2
    tipo: ejemplo
    titulo: 1. ADR PaaS vs VPS
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/adr-hosting.md << 'EOF'
      ADR hosting
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "ADR hosting: PaaS vs VPS" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m19-ops/adr-hosting.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “ADR sin costos/tiempo ni Vitrina."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Documentar decisión de hosting para Vitrina con criterios costo, TLS,
          Postgres gestionado, DX.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m19-ops/adr-hosting.md` con decisión PaaS vs VPS y
        consecuencias.
      - 'Commit `docs(m19): L05 adr-hosting-paas-vs-vps`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — ADR hosting: PaaS vs VPS

**~5.0 h · Semana 2**

Evitas re-decidir cada semana.

## Objetivo

Documentar decisión de hosting para Vitrina con criterios costo, TLS, Postgres gestionado, DX.

## Conceptos clave

- PaaS
- VPS+Docker
- egress y region

## Pasos (hazlos en orden)

### 1. ADR PaaS vs VPS (70–90 min)

```bash
cat > projects/m19-ops/adr-hosting.md << 'EOF'
# ADR hosting
## Contexto
Vitrina necesita HTTPS + Postgres managed o self-host.
## Opciones
A) PaaS  B) VPS
## Decisión
…
## Consecuencias
costo, SSH, backups, tiempo-a-staging
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/adr-hosting.md
git commit -m "docs(m19): L05 adr hosting paas vs vps"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Docs Fly/Railway/Render o VPS | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m19-ops/adr-hosting.md` con decisión PaaS vs VPS y consecuencias.
2. Commit `docs(m19): L05 adr-hosting-paas-vs-vps`.

## Errores comunes

- ADR sin costos/tiempo ni Vitrina.
- Elegir VPS sin plan de backups.

## Siguiente

[L06 — Deploy staging con HTTPS](L06-deploy-staging-con-https.md)
