---
id: L04
materia: M19
orden: 4
titulo: Stack local documentado y P1 Docker
horas: 5
semana: 1
lectura: Repaso semana 1
evidencia: projects/m19-ops/docker.md completo
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - reproducibilidad

      - logs compose


      **Objetivo de esta lección:** Consolidar instrucciones un comando,
      troubleshooting y evidencia de login/pedido en contenedores.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Cierra docker.md P1
    xp: 10
    cuerpo: '```bash cat >> projects/m19-ops/docker.md << ''EOF'''
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Stack local documentado y P1 Docker», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Stack local documentado
          y P1 Docker
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
    pregunta: >-
      ¿Es recomendable en esta lección? “docker.md sin comandos
      copy-pasteables."
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
          Consolidar instrucciones un comando, troubleshooting y evidencia de
          login/pedido en contenedores.
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
    pregunta: ¿Debes hacer esto? “Marcar P1 sin `compose up` real."
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
      - '`projects/m19-ops/docker.md` completo (build/up/down/logs) — P1.'
      - 'Commit `docs(m19): L04 stack-local-documentado-y-p1-docker`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Stack local documentado y P1 Docker

**~5.0 h · Semana 1**

Cierra semana 1 con P1 listo para marcar.

## Objetivo

Consolidar instrucciones un comando, troubleshooting y evidencia de login/pedido en contenedores.

## Conceptos clave

- reproducibilidad
- logs compose

## Pasos (hazlos en orden)

### 1. Cierra docker.md P1 (60–80 min)

```bash
cat >> projects/m19-ops/docker.md << 'EOF'
## Comandos
- build: `docker build -t vitrina-api:dev .`
- up: `docker compose up -d`
- down: `docker compose down`
- logs: `docker compose logs -f api`
EOF
```

### 2. Verifica end-to-end local (40 min)

```bash
docker compose down && docker compose up -d --build
curl -sS http://localhost:3000/health
# login smoke local (cookie) — anota OK en docker.md
git add projects/m19-ops/docker.md
git commit -m "docs(m19): L04 docker.md P1 completo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Repaso semana 1 | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/docker.md` completo (build/up/down/logs) — P1.
2. Commit `docs(m19): L04 stack-local-documentado-y-p1-docker`.

## Errores comunes

- docker.md sin comandos copy-pasteables.
- Marcar P1 sin `compose up` real.

## Siguiente

[L05 — ADR hosting: PaaS vs VPS](L05-adr-hosting-paas-vs-vps.md)
