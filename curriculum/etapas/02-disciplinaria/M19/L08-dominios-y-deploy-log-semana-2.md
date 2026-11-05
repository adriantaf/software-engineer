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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - CNAME

      - cert automático


      **Objetivo de esta lección:** Registrar subdominios staging (y prod
      planificado); enlazar con deploy-log.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dominios
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Actualiza deploy-log semana 2
    xp: 10
    cuerpo: >-
      ```bash

      echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
      projects/m19-ops/deploy-log.md

      git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md

      git commit -m "docs(m19): L08 dominios deploy-log semana2"

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dominios y deploy-log semana 2», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dominios y deploy-log
          semana 2
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
      projects/m19-ops/deploy-log.md`
    comandoEsperado:
      - >-
        echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
        projects/m19-ops/deploy-log.md
      - git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: echo "| $(date -I) | staging | … | https://… | DNS OK |" >>
      projects/m19-ops/deploy-log.md
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
          Registrar subdominios staging (y prod planificado); enlazar con
          deploy-log.
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

      `git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md`
    comandoEsperado:
      - git add projects/m19-ops/dominios.md projects/m19-ops/deploy-log.md
    explicacionError: >-
      Esperado: git add projects/m19-ops/dominios.md
      projects/m19-ops/deploy-log.md
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m19-ops/dominios.md` + fila nueva en `deploy-log.md`.'
      - 'Commit `docs(m19): L08 dominios-y-deploy-log-semana-2`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
