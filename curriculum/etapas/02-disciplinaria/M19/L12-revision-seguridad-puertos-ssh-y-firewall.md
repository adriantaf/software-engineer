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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - firewall

      - SSH

      - least privilege


      **Objetivo de esta lección:** Checklist puertos expuestos, SSH (clave, no
      password), firewall si VPS.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Revisión host
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m19-ops/security-host.md
      git commit -m "docs(m19): L12 seguridad puertos ssh firewall"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Revisión seguridad: puertos, SSH y firewall», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Revisión seguridad:
          puertos, SSH y fire…
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

      `git add projects/m19-ops/security-host.md`
    comandoEsperado:
      - git add projects/m19-ops/security-host.md
      - 'git commit -m "docs(m19): L12 seguridad puertos ssh firewall"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m19-ops/security-host.md'
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
          Checklist puertos expuestos, SSH (clave, no password), firewall si
          VPS.
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

      `git commit -m "docs(m19): L12 seguridad puertos ssh firewall"`
    comandoEsperado:
      - 'git commit -m "docs(m19): L12 seguridad puertos ssh firewall"'
    explicacionError: 'Esperado: git commit -m "docs(m19): L12 seguridad puertos ssh firewall"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m19-ops/security-host.md` (SSH, firewall, DB no
        pública).
      - 'Commit `docs(m19): L12 revision-seguridad-puertos-ssh-y-firewall`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
