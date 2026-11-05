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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Secretos en git son incidentes. Inventario (sin valores) + plan de
      rotación.


      **Objetivo de esta lección:**
      `projects/m18-appsec/docs/rotacion-secretos.md`: inventario, dónde viven,
      pasos rotar session secret / DB URL.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Busca secretos en historial
    xp: 10
    cuerpo: |-
      ```bash
      git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
      git ls-files | rg -i '\.env|credential|secret|\.pem' || true
      # gitleaks / trufflehog si los tienes instalados
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Inventario + rotación
    xp: 10
    cuerpo: |-
      ```bash
      git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
      git ls-files | rg -i '\.env|credential|secret|\.pem' || true
      # gitleaks / trufflehog si los tienes instalados
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Secretos, .env y rotación», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Secretos, .env y
          rotación
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

      `git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true`
    comandoEsperado:
      - git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
      - git ls-files | rg -i '\.env|credential|secret|\.pem' || true
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 ||
      true
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
          `projects/m18-appsec/docs/rotacion-secretos.md`: inventario, dónde
          viven, pasos rotar session secret / DB URL.
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

      `git ls-files | rg -i '\.env|credential|secret|\.pem' || true`
    comandoEsperado:
      - git ls-files | rg -i '\.env|credential|secret|\.pem' || true
    explicacionError: 'Esperado: git ls-files | rg -i ''\.env|credential|secret|\.pem'' || true'
  - id: s8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
