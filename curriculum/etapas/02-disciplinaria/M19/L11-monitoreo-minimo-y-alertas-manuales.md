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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - uptime

      - on-call manual


      **Objetivo de esta lección:** Configurar healthcheck externo o calendario
      de revisión manual; definir qué hacer si cae.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Monitoreo mínimo
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m19-ops/monitoring.md
      git commit -m "docs(m19): L11 monitoreo alertas manuales"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Monitoreo mínimo y alertas manuales», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Monitoreo mínimo y
          alertas manuales
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

      `curl -sS https://TU-STAGING.example/health`
    comandoEsperado:
      - 'curl -sS https://TU-STAGING.example/health'
      - git add projects/m19-ops/monitoring.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS https://TU-STAGING.example/health'
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
          Configurar healthcheck externo o calendario de revisión manual;
          definir qué hacer si cae.
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

      `git add projects/m19-ops/monitoring.md`
    comandoEsperado:
      - git add projects/m19-ops/monitoring.md
    explicacionError: 'Esperado: git add projects/m19-ops/monitoring.md'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m19-ops/monitoring.md` con check `/health` y canal de
        alerta.
      - 'Commit `docs(m19): L11 monitoreo-minimo-y-alertas-manuales`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
