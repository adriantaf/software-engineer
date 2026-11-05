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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - promoción imagen

      - separación datos


      **Objetivo de esta lección:** Desplegar prod con misma imagen que staging
      y distintas env vars; documentar diferencias.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist promoción a prod
    xp: 10
    cuerpo: '```bash cat >> projects/m19-ops/ambientes.md << ''EOF'''
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Promover configuración a producción», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Promover configuración
          a producción
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
      ¿Es recomendable en esta lección? “Promover con mismos secrets que
      staging."
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
          Desplegar prod con misma imagen que staging y distintas env vars;
          documentar diferencias.
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
    pregunta: ¿Debes hacer esto? “Sin plan de rollback."
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
      - '`projects/m19-ops/ambientes.md` incluye checklist de promoción a prod.'
      - 'Commit `docs(m19): L09 promover-configuracion-a-produccion`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
