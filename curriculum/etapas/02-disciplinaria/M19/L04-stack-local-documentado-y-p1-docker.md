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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Consolidar instrucciones un comando, troubleshooting y
      evidencia de login/pedido en contenedores.


      - reproducibilidad

      - logs compose
  - id: s2
    tipo: ejemplo
    titulo: 1. Cierra docker.md P1
    xp: 10
    cuerpo: |-
      ```bash
      cat >> projects/m19-ops/docker.md << 'EOF'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Stack local documentado y P1 Docker" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/docker.md completo
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “docker.md sin comandos
      copy-pasteables."
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
          Consolidar instrucciones un comando, troubleshooting y evidencia de
          login/pedido en contenedores.
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
      - '`projects/m19-ops/docker.md` completo (build/up/down/logs) — P1.'
      - 'Commit `docs(m19): L04 stack-local-documentado-y-p1-docker`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
