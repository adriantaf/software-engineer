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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - rollback

      - tag git

      - logs PaaS


      **Objetivo de esta lección:** Documentar dónde ver logs, cómo identificar
      versión y rollback a imagen/tag anterior.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Rollback + versión
    xp: 10
    cuerpo: >-
      ```bash mkdir -p projects/m19-ops cat > projects/m19-ops/runbook.md <<
      'EOF' # Runbook (borrador)
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Logs, rollback y versión desplegada», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Logs, rollback y
          versión desplegada
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
      ¿Es recomendable en esta lección? “Rollback ‘reiniciar el server’ sin
      versión pinneada."
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
          Documentar dónde ver logs, cómo identificar versión y rollback a
          imagen/tag anterior.
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
    pregunta: ¿Debes hacer esto? “Logs inaccesibles documentados."
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
      - '`projects/m19-ops/runbook.md` tiene secciones versión, logs y rollback.'
      - 'Commit `docs(m19): L10 logs-rollback-y-version-desplegada`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
