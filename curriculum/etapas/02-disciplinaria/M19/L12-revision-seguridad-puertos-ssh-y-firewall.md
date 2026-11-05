---
id: L12
materia: M19
orden: 12
titulo: 'Revisión seguridad: puertos, SSH y firewall'
horas: 5
semana: 3
lectura: M18 + M11 seguridad host
evidencia: projects/m19-ops/security-host.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Checklist puertos expuestos, SSH (clave, no password),
      firewall si VPS.


      - firewall

      - SSH

      - least privilege
  - id: s2
    tipo: ejemplo
    titulo: 1. Revisión host
    xp: 10
    cuerpo: |-
      ```bash
      # Si VPS (ejemplos — adapta; no abras 0.0.0.0:5432 al mundo):
      # sudo ufw status
      # ss -tulpn | head
      cat > projects/m19-ops/security-host.md << 'EOF'
      # Host security
      | Control | Estado | Notas |
      |---------|--------|-------|
      | SSH keys only | | |
      | Firewall | | DB no pública |
      | Updates | | |
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Revisión seguridad: puertos, SSH y firewall" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/security-host.md
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

      `git add projects/m19-ops/security-host.md`
    comandoEsperado:
      - git add projects/m19-ops/security-host.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m19-ops/security-host.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Checklist puertos expuestos, SSH (clave, no password), firewall si
          VPS.
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
      git add projects/m19-ops/security-host.md
      git commit -m "docs(m19): L12 seguridad puertos ssh firewall"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m19-ops/security-host.md` (SSH, firewall, DB no
        pública).
      - 'Commit `docs(m19): L12 revision-seguridad-puertos-ssh-y-firewall`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Revisión seguridad: puertos, SSH y firewall

**~5.0 h · Semana 3**

Deploy sin postura de host revierte M18.

## Objetivo

Checklist puertos expuestos, SSH (clave, no password), firewall si VPS.

## Conceptos clave

- firewall
- SSH
- least privilege

## Pasos (hazlos en orden)

### 1. Revisión host (70–90 min)

```bash
# Si VPS (ejemplos — adapta; no abras 0.0.0.0:5432 al mundo):
# sudo ufw status
# ss -tulpn | head
cat > projects/m19-ops/security-host.md << 'EOF'
# Host security
| Control | Estado | Notas |
|---------|--------|-------|
| SSH keys only | | |
| Firewall | | DB no pública |
| Updates | | |
EOF
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/security-host.md
git commit -m "docs(m19): L12 seguridad puertos ssh firewall"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | M18 + M11 seguridad host | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m19-ops/security-host.md` (SSH, firewall, DB no pública).
2. Commit `docs(m19): L12 revision-seguridad-puertos-ssh-y-firewall`.

## Errores comunes

- Postgres expuesto a 0.0.0.0.
- SSH con password root.

## Siguiente

[L13 — Backup automático PostgreSQL](L13-backup-automatico-postgresql.md)
