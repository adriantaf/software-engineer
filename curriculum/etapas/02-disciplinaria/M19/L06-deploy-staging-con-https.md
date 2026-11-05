---
id: L06
materia: M19
orden: 6
titulo: Deploy staging con HTTPS
horas: 5
semana: 2
lectura: 'Proveedor: deploy + TLS'
evidencia: projects/m19-ops/deploy-log.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Desplegar staging con HTTPS forzado y variables en panel del
      host.


      - HTTP→HTTPS

      - env vars

      - build remoto
  - id: s2
    tipo: ejemplo
    titulo: 1. Deploy staging HTTPS
    xp: 10
    cuerpo: |-
      ```bash
      curl -sSI https://TU-STAGING.example/health | head -15
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Deploy staging con HTTPS" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m19-ops/deploy-log.md
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

      `curl -sSI https://TU-STAGING.example/health | head -15`
    comandoEsperado:
      - 'curl -sSI https://TU-STAGING.example/health | head -15'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sSI https://TU-STAGING.example/health | head -15'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Desplegar staging con HTTPS forzado y variables en panel del host.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. deploy-log.md
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/deploy-log.md << 'EOF'
      Deploy log
      | Fecha | Env | Versión/commit | URL | Resultado |
      |-------|-----|----------------|-----|-----------|
      | YYYY-MM-DD | staging | abc123 | https://… | OK health |
      EOF
      git add projects/m19-ops/deploy-log.md
      git commit -m "docs(m19): L06 deploy staging https"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m19-ops/deploy-log.md` con URL HTTPS staging y commit/versión.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Deploy staging con HTTPS

**~5.0 h · Semana 2**

Primera URL pública del piloto.

## Objetivo

Desplegar staging con HTTPS forzado y variables en panel del host.

## Conceptos clave

- HTTP→HTTPS
- env vars
- build remoto

## Pasos (hazlos en orden)

### 1. Deploy staging HTTPS (90–120 min)

Sigue el ADR. Inyecta secrets en el panel.

```bash
curl -sSI https://TU-STAGING.example/health | head -15
```

### 2. deploy-log.md (30–40 min)

```bash
cat > projects/m19-ops/deploy-log.md << 'EOF'
# Deploy log
| Fecha | Env | Versión/commit | URL | Resultado |
|-------|-----|----------------|-----|-----------|
| YYYY-MM-DD | staging | abc123 | https://… | OK health |
EOF
git add projects/m19-ops/deploy-log.md
git commit -m "docs(m19): L06 deploy staging https"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Proveedor: deploy + TLS | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/deploy-log.md` con URL HTTPS staging y commit/versión.

## Errores comunes

- Deploy ‘OK’ sin URL en deploy-log.
- Secrets en el Dockerfile.

## Siguiente

[L07 — Smoke test: login, pedido y health externo](L07-smoke-test-login-pedido-y-health-externo.md)
