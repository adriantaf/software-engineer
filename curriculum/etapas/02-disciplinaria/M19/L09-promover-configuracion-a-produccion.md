---
id: L09
materia: M19
orden: 9
titulo: Promover configuración a producción
horas: 5
semana: 3
lectura: 12-factor config
evidencia: projects/m19-ops/ambientes.md actualizado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Desplegar prod con misma imagen que staging y distintas env
      vars; documentar diferencias.


      - promoción imagen

      - separación datos
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist promoción a prod
    xp: 10
    cuerpo: |-
      ```bash
      cat >> projects/m19-ops/ambientes.md << 'EOF'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Promover configuración a producción" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/ambientes.md actualizado
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
      ¿Es buena práctica en esta lección? “Promover con mismos secrets que
      staging."
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
          Desplegar prod con misma imagen que staging y distintas env vars;
          documentar diferencias.
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
      - '`projects/m19-ops/ambientes.md` incluye checklist de promoción a prod.'
      - 'Commit `docs(m19): L09 promover-configuracion-a-produccion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Promover configuración a producción

**~5.0 h · Semana 3**

Prod es para design partner, no laboratorio.

## Objetivo

Desplegar prod con misma imagen que staging y distintas env vars; documentar diferencias.

## Conceptos clave

- promoción imagen
- separación datos

## Pasos (hazlos en orden)

### 1. Checklist promoción a prod (60–80 min)

```bash
cat >> projects/m19-ops/ambientes.md << 'EOF'
## Promoción staging → prod
1. Migraciones aplicadas
2. Secrets distintos a staging
3. Smoke health+login
4. Rollback plan listo
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/ambientes.md
git commit -m "docs(m19): L09 promover config a produccion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | 12-factor config | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/ambientes.md` incluye checklist de promoción a prod.
2. Commit `docs(m19): L09 promover-configuracion-a-produccion`.

## Errores comunes

- Promover con mismos secrets que staging.
- Sin plan de rollback.

## Siguiente

[L10 — Logs, rollback y versión desplegada](L10-logs-rollback-y-version-desplegada.md)
