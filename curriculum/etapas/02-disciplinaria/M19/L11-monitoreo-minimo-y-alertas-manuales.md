---
id: L11
materia: M19
orden: 11
titulo: Monitoreo mínimo y alertas manuales
horas: 5
semana: 3
lectura: Uptime básico
evidencia: projects/m19-ops/monitoring.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Configurar healthcheck externo o calendario de revisión
      manual; definir qué hacer si cae.


      - uptime

      - on-call manual
  - id: s2
    tipo: ejemplo
    titulo: 1. Monitoreo mínimo
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/monitoring.md << 'EOF'
      # Monitoreo
      - Check: GET /health cada 5 min (UptimeRobot/Cron/… )
      - Alerta: email/Telegram si 2 fallos
      - Manual: revisar logs tras deploy
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Monitoreo mínimo y alertas manuales" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/monitoring.md
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

      `curl -sS https://TU-STAGING.example/health`
    comandoEsperado:
      - 'curl -sS https://TU-STAGING.example/health'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sS https://TU-STAGING.example/health'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Configurar healthcheck externo o calendario de revisión manual;
          definir qué hacer si cae.
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
      git add projects/m19-ops/monitoring.md
      git commit -m "docs(m19): L11 monitoreo alertas manuales"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m19-ops/monitoring.md` con check `/health` y canal de
        alerta.
      - 'Commit `docs(m19): L11 monitoreo-minimo-y-alertas-manuales`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Monitoreo mínimo y alertas manuales

**~5.0 h · Semana 3**

No necesitas Datadog para el piloto; sí necesitas saber si está caído.

## Objetivo

Configurar healthcheck externo o calendario de revisión manual; definir qué hacer si cae.

## Conceptos clave

- uptime
- on-call manual

## Pasos (hazlos en orden)

### 1. Monitoreo mínimo (60–80 min)

```bash
cat > projects/m19-ops/monitoring.md << 'EOF'
# Monitoreo
- Check: GET /health cada 5 min (UptimeRobot/Cron/… )
- Alerta: email/Telegram si 2 fallos
- Manual: revisar logs tras deploy
EOF
```

```bash
curl -sS https://TU-STAGING.example/health
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/monitoring.md
git commit -m "docs(m19): L11 monitoreo alertas manuales"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Uptime básico | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m19-ops/monitoring.md` con check `/health` y canal de alerta.
2. Commit `docs(m19): L11 monitoreo-minimo-y-alertas-manuales`.

## Errores comunes

- Monitoreo = ‘miro de vez en cuando’.
- Alertas al canal equivocado sin dueño.

## Siguiente

[L12 — Revisión seguridad: puertos, SSH y firewall](L12-revision-seguridad-puertos-ssh-y-firewall.md)
