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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 exige v1 revisado tras entender login; hoy entregas el hito.


      **Objetivo de esta lección:** `projects/m18-appsec/threat-model-v1.md` con
      controles auth, tabla amenaza→control y residual.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Diff v0→v1
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Redacción P1
    xp: 10
    cuerpo: >-
      ```bash

      printf "\n## Enlaces\n- auth: docs/auth-inventario.md\n- ADR:
      docs/adr-sesion-vs-jwt.md\n\n## Residual auth\n- ...\n" >>
      projects/m18-appsec/threat-model-v1.md

      ```


      Enlaza `projects/m18-appsec/docs/auth-inventario.md` y ADR. Supuestos de
      staging. Tabla amenaza|control|estado legible sin abrir el código.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Threat model v1 post-autenticación (P1)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Threat model v1
          post-autenticación (P1)
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


      `cp projects/m18-appsec/threat-model-v0.md
      projects/m18-appsec/threat-model-v1.md`
    comandoEsperado:
      - >-
        cp projects/m18-appsec/threat-model-v0.md
        projects/m18-appsec/threat-model-v1.md
      - >-
        git add projects/m18-appsec/threat-model-v1.md
        projects/m18-appsec/README.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: cp projects/m18-appsec/threat-model-v0.md
      projects/m18-appsec/threat-model-v1.md
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
          `projects/m18-appsec/threat-model-v1.md` con controles auth, tabla
          amenaza→control y residual.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README P1
    xp: 10
    cuerpo: >-
      En `projects/m18-appsec/README.md` marca P1 entregado con fecha y ruta a
      `threat-model-v1.md`.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
