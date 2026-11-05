---
id: L10
materia: M19
orden: 10
titulo: 'Logs, rollback y versión desplegada'
horas: 5
semana: 3
lectura: Runbook ops
evidencia: projects/m19-ops/runbook.md sección rollback
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Documentar dónde ver logs, cómo identificar versión y
      rollback a imagen/tag anterior.


      - rollback

      - tag git

      - logs PaaS
  - id: s2
    tipo: ejemplo
    titulo: 1. Rollback + versión
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m19-ops
      cat > projects/m19-ops/runbook.md << 'EOF'
      Runbook (borrador)
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Logs, rollback y versión desplegada" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/runbook.md sección rollback
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
      ¿Es buena práctica en esta lección? “Rollback ‘reiniciar el server’ sin
      versión pinneada."
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
          Documentar dónde ver logs, cómo identificar versión y rollback a
          imagen/tag anterior.
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
      - '`projects/m19-ops/runbook.md` tiene secciones versión, logs y rollback.'
      - 'Commit `docs(m19): L10 logs-rollback-y-version-desplegada`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Logs, rollback y versión desplegada

**~5.0 h · Semana 3**

A las 11 p.m. solo cuenta el runbook.

## Objetivo

Documentar dónde ver logs, cómo identificar versión y rollback a imagen/tag anterior.

## Conceptos clave

- rollback
- tag git
- logs PaaS

## Pasos (hazlos en orden)

### 1. Rollback + versión (60–80 min)

```bash
mkdir -p projects/m19-ops
cat > projects/m19-ops/runbook.md << 'EOF'
# Runbook (borrador)
## Versión desplegada
Cómo ver commit/tag en runtime (header, /health.version, o CLI PaaS).
## Rollback
1. Redeploy imagen/tag anterior
2. Verificar /health
3. Anotar en deploy-log.md
## Logs
comando CLI o URL del provider
EOF
```

```bash
# ejemplo
# fly releases / render releases / docker compose images
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/runbook.md
git commit -m "docs(m19): L10 logs rollback version"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Runbook ops | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/runbook.md` tiene secciones versión, logs y rollback.
2. Commit `docs(m19): L10 logs-rollback-y-version-desplegada`.

## Errores comunes

- Rollback ‘reiniciar el server’ sin versión pinneada.
- Logs inaccesibles documentados.

## Siguiente

[L11 — Monitoreo mínimo y alertas manuales](L11-monitoreo-minimo-y-alertas-manuales.md)
