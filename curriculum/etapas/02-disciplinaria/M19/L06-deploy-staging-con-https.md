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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - HTTP→HTTPS

      - env vars

      - build remoto


      **Objetivo de esta lección:** Desplegar staging con HTTPS forzado y
      variables en panel del host.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Deploy staging HTTPS
    xp: 10
    cuerpo: |-
      ```bash
      curl -sSI https://TU-STAGING.example/health | head -15
      ```

      Sigue el ADR. Inyecta secrets en el panel.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: deploy-log.md
    xp: 10
    cuerpo: |-
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Deploy staging con HTTPS», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Deploy staging con
          HTTPS
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

      `curl -sSI https://TU-STAGING.example/health | head -15`
    comandoEsperado:
      - 'curl -sSI https://TU-STAGING.example/health | head -15'
      - git add projects/m19-ops/deploy-log.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sSI https://TU-STAGING.example/health | head -15'
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
        texto: Desplegar staging con HTTPS forzado y variables en panel del host.
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

      `git add projects/m19-ops/deploy-log.md`
    comandoEsperado:
      - git add projects/m19-ops/deploy-log.md
    explicacionError: 'Esperado: git add projects/m19-ops/deploy-log.md'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m19-ops/deploy-log.md` con URL HTTPS staging y commit/versión.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
