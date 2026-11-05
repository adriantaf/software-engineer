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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - PaaS

      - VPS+Docker

      - egress y region


      **Objetivo de esta lección:** Documentar decisión de hosting para Vitrina
      con criterios costo, TLS, Postgres gestionado, DX.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: ADR PaaS vs VPS
    xp: 10
    cuerpo: '```bash cat > projects/m19-ops/adr-hosting.md << ''EOF'' # ADR hosting'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «ADR hosting: PaaS vs VPS», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de ADR hosting: PaaS vs
          VPS
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “ADR sin costos/tiempo ni Vitrina."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
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
          Documentar decisión de hosting para Vitrina con criterios costo, TLS,
          Postgres gestionado, DX.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Elegir VPS sin plan de backups."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m19-ops/adr-hosting.md` con decisión PaaS vs VPS y
        consecuencias.
      - 'Commit `docs(m19): L05 adr-hosting-paas-vs-vps`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
