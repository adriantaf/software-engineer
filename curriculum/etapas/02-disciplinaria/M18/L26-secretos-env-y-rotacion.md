---
id: L26
materia: M18
orden: 26
titulo: 'Secretos, .env y rotación'
horas: 5
semana: 7
lectura: Secrets Management Cheat Sheet
evidencia: projects/m18-appsec/docs/rotacion-secretos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `projects/m18-appsec/docs/rotacion-secretos.md`: inventario,
      dónde viven, pasos rotar session secret / DB URL.


      Secretos en git son incidentes. Inventario (sin valores) + plan de
      rotación.
  - id: s2
    tipo: ejemplo
    titulo: 1. Busca secretos en historial
    xp: 10
    cuerpo: |-
      ```bash
      git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
      git ls-files | rg -i '\.env|credential|secret|\.pem' || true
      # gitleaks / trufflehog si los tienes instalados
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Secretos, .env y rotación" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m18-appsec/docs/rotacion-secretos.md
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

      `git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true`
    comandoEsperado:
      - git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 ||
      true
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          `projects/m18-appsec/docs/rotacion-secretos.md`: inventario, dónde
          viven, pasos rotar session secret / DB URL.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario + rotación
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/docs/rotacion-secretos.md <<'EOF'
      Secretos y rotación
      | Secreto | Dónde (local/staging) | En git? | Rotar cómo |
      |---------|----------------------|---------|------------|
      | DATABASE_URL | .env / PaaS | no | … |
      | SESSION_SECRET | .env | no | reiniciar sesiones |
      | SMTP_KEY | … | | |
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Inventario sin valores (artefacto:
        `projects/m18-appsec/docs/rotacion-secretos.md`).
      - >-
        grep historial ejecutado (artefacto:
        `projects/m18-appsec/docs/rotacion-secretos.md`).
      - 'Commit `docs(m18): L26 secretos-env-y-rotacion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L26 — Secretos, .env y rotación

**~5.0 h · Semana 7**

Secretos en git son incidentes. Inventario (sin valores) + plan de rotación.

## Objetivo

`projects/m18-appsec/docs/rotacion-secretos.md`: inventario, dónde viven, pasos rotar session secret / DB URL.

## Pasos

### 1. Busca secretos en historial (30–40 min)

```bash
git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
git ls-files | rg -i '\.env|credential|secret|\.pem' || true
# gitleaks / trufflehog si los tienes instalados
```
### 2. Inventario + rotación (70–90 min)

```bash
cat > projects/m18-appsec/docs/rotacion-secretos.md <<'EOF'
# Secretos y rotación
| Secreto | Dónde (local/staging) | En git? | Rotar cómo |
|---------|----------------------|---------|------------|
| DATABASE_URL | .env / PaaS | no | … |
| SESSION_SECRET | .env | no | reiniciar sesiones |
| SMTP_KEY | … | | |

## Pasos rotar SESSION_SECRET (staging)
1. Generar nuevo valor
2. Deploy
3. Invalidar sesiones previas
4. Verificar login
EOF
```

```bash
# Genera candidato (no lo commits)
openssl rand -hex 32
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/rotacion-secretos.md
git status   # .env no debe aparecer
git commit -m "docs(m18): l26 rotacion secretos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Secrets Management Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Inventario sin valores (artefacto: `projects/m18-appsec/docs/rotacion-secretos.md`).
2. grep historial ejecutado (artefacto: `projects/m18-appsec/docs/rotacion-secretos.md`).
3. Commit `docs(m18): L26 secretos-env-y-rotacion`.

## Errores comunes

- Pegar secretos en issue.
- Rotar sin probar logout.

## Siguiente

[L27 — Cabeceras de seguridad con Helmet o equivalente](L27-cabeceras-de-seguridad-con-helmet-o-equivalente.md)
