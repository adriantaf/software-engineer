---
id: L08
materia: M18
orden: 8
titulo: Threat model v1 post-autenticación (P1)
horas: 5
semana: 2
lectura: Repaso STRIDE semanas 1–2
evidencia: projects/m18-appsec/threat-model-v1.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `projects/m18-appsec/threat-model-v1.md` con controles auth,
      tabla amenaza→control y residual.


      P1 exige v1 revisado tras entender login; hoy entregas el hito.
  - id: s2
    tipo: ejemplo
    titulo: 1. Diff v0→v1
    xp: 10
    cuerpo: >-
      ```bash

      cp projects/m18-appsec/threat-model-v0.md
      projects/m18-appsec/threat-model-v1.md

      printf "\n## Controles auth (post L05–L07)\n| Amenaza | Control | Estado |
      Commit/issue |\n|---------|---------|--------|--------------|\n| Hash
      débil | bcrypt/argon2 | OK/TODO | |\n| Sesión robable | HttpOnly plan | |
      |\n| Sin revoke | ADR decisión | | |\n" >>
      projects/m18-appsec/threat-model-v1.md

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Threat model v1 post-autenticación (P1)" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/threat-model-v1.md
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


      `cp projects/m18-appsec/threat-model-v0.md
      projects/m18-appsec/threat-model-v1.md`
    comandoEsperado:
      - >-
        cp projects/m18-appsec/threat-model-v0.md
        projects/m18-appsec/threat-model-v1.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: cp projects/m18-appsec/threat-model-v0.md
      projects/m18-appsec/threat-model-v1.md
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          `projects/m18-appsec/threat-model-v1.md` con controles auth, tabla
          amenaza→control y residual.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Redacción P1
    xp: 10
    cuerpo: >-
      Enlaza `projects/m18-appsec/docs/auth-inventario.md` y ADR. Supuestos de
      staging. Tabla amenaza|control|estado legible sin abrir el código.


      ```bash

      printf "\n## Enlaces\n- auth: docs/auth-inventario.md\n- ADR:
      docs/adr-sesion-vs-jwt.md\n\n## Residual auth\n- ...\n" >>
      projects/m18-appsec/threat-model-v1.md

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. README P1
    xp: 10
    cuerpo: >-
      ```bash

      rg -n "P1|threat-model-v1" projects/m18-appsec/README.md || printf "\n-
      **P1:** threat-model-v1.md $(date -I)\n" >> projects/m18-appsec/README.md

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        threat-model-v1.md completo (artefacto:
        `projects/m18-appsec/threat-model-v1.md`).
      - >-
        Tabla amenaza-control (artefacto:
        `projects/m18-appsec/threat-model-v1.md`).
      - 'Commit `docs(m18): L08 threat-model-v1-post-autenticacion-p1`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Threat model v1 post-autenticación (P1)

**~5.0 h · Semana 2**

P1 exige v1 revisado tras entender login; hoy entregas el hito.

## Objetivo

`projects/m18-appsec/threat-model-v1.md` con controles auth, tabla amenaza→control y residual.

## Pasos

### 1. Diff v0→v1 (30–40 min)

```bash
cp projects/m18-appsec/threat-model-v0.md projects/m18-appsec/threat-model-v1.md
printf "\n## Controles auth (post L05–L07)\n| Amenaza | Control | Estado | Commit/issue |\n|---------|---------|--------|--------------|\n| Hash débil | bcrypt/argon2 | OK/TODO | |\n| Sesión robable | HttpOnly plan | | |\n| Sin revoke | ADR decisión | | |\n" >> projects/m18-appsec/threat-model-v1.md
```
### 2. Redacción P1 (80–100 min)

Enlaza `projects/m18-appsec/docs/auth-inventario.md` y ADR. Supuestos de staging. Tabla amenaza|control|estado legible sin abrir el código.

```bash
printf "\n## Enlaces\n- auth: docs/auth-inventario.md\n- ADR: docs/adr-sesion-vs-jwt.md\n\n## Residual auth\n- ...\n" >> projects/m18-appsec/threat-model-v1.md
```
### 3. README P1 (15 min)

En `projects/m18-appsec/README.md` marca P1 entregado con fecha y ruta a `threat-model-v1.md`.

```bash
rg -n "P1|threat-model-v1" projects/m18-appsec/README.md || printf "\n- **P1:** threat-model-v1.md $(date -I)\n" >> projects/m18-appsec/README.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/threat-model-v1.md projects/m18-appsec/README.md
git commit -m "docs(m18): l08 threat model v1 p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Repaso STRIDE semanas 1–2 | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. threat-model-v1.md completo (artefacto: `projects/m18-appsec/threat-model-v1.md`).
2. Tabla amenaza-control (artefacto: `projects/m18-appsec/threat-model-v1.md`).
3. Commit `docs(m18): L08 threat-model-v1-post-autenticacion-p1`.

## Errores comunes

- Renombrar v0 sin cambios.
- Omitir auth en el modelo.

## Siguiente

[L09 — Cookies Secure, HttpOnly y SameSite](L09-cookies-secure-httponly-y-samesite.md)
