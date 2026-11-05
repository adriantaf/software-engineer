---
id: L08
materia: M19
orden: 8
titulo: Dominios y deploy-log semana 2
horas: 5
semana: 2
lectura: DNS del proveedor
evidencia: projects/m19-ops/dominios.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Registrar subdominios staging (y prod planificado); enlazar
      con deploy-log.


      - CNAME

      - cert automático
  - id: s2
    tipo: ejemplo
    titulo: 1. Dominios
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m19-ops/dominios.md << 'EOF'
      # Dominios
      | Uso | FQDN | DNS | TLS |
      |-----|------|-----|-----|
      | API staging | api-staging.… | CNAME → PaaS | managed |
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Dominios y deploy-log semana 2" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/dominios.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
      projects/m19-ops/deploy-log.md`
    comandoEsperado:
      - >-
        echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
        projects/m19-ops/deploy-log.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
      projects/m19-ops/deploy-log.md
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Registrar subdominios staging (y prod planificado); enlazar con
          deploy-log.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Actualiza deploy-log semana 2
    xp: 10
    cuerpo: >-
      ```bash

      echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
      projects/m19-ops/deploy-log.md

      git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md

      git commit -m "docs(m19): L08 dominios deploy-log semana2"

      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m19-ops/dominios.md` + fila nueva en `deploy-log.md`.'
      - 'Commit `docs(m19): L08 dominios-y-deploy-log-semana-2`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Dominios y deploy-log semana 2

**~5.0 h · Semana 2**

Trials M22 necesitan URL estable.

## Objetivo

Registrar subdominios staging (y prod planificado); enlazar con deploy-log.

## Conceptos clave

- CNAME
- cert automático

## Pasos (hazlos en orden)

### 1. Dominios (50–60 min)

```bash
cat > projects/m19-ops/dominios.md << 'EOF'
# Dominios
| Uso | FQDN | DNS | TLS |
|-----|------|-----|-----|
| API staging | api-staging.… | CNAME → PaaS | managed |
EOF
```

### 2. Actualiza deploy-log semana 2 (30 min)

```bash
echo "| $(date -I) | staging | … | https://… | DNS OK |" >> projects/m19-ops/deploy-log.md
git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md
git commit -m "docs(m19): L08 dominios deploy-log semana2"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | DNS del proveedor | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/dominios.md` + fila nueva en `deploy-log.md`.
2. Commit `docs(m19): L08 dominios-y-deploy-log-semana-2`.

## Errores comunes

- Dominio sin TLS.
- DNS apuntando a IP efímera sin nota.

## Siguiente

[L09 — Promover configuración a producción](L09-promover-configuracion-a-produccion.md)
