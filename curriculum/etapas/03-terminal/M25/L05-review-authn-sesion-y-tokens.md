---
id: L05
materia: M25
orden: 5
titulo: Review authn — sesión y tokens
horas: 5
semana: 2
lectura: OWASP — Identity / Authorization testing
evidencia: projects/m25-ciber/review/authn.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cosmética CSS no salva un leak entre barberías.


      Conceptos que debes poder explicar al cerrar:


      - Authn vs authz

      - tenant_id en sesión

      - Tests de regresión


      **Objetivo de esta lección:** Documentar flujo login/logout/refresh y
      dónde vive tenant_id.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      # captura Set-Cookie o body de login — redacta signature/secret
      curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \
        -H "Content-Type: application/json" \
        -d '{"email":"staff-a@example.test","password":"$PASS"}'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Dibuja el flujo authn
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/
      git status
      git commit -m "docs(m25): l05 review-authn-sesi-n-y-tokens"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Review authn — sesión y tokens», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Review authn — sesión y
          tokens
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

      `curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \`
    comandoEsperado:
      - curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \
      - git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \'
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
        texto: Documentar flujo login/logout/refresh y dónde vive tenant_id.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Inspecciona tokens reales
    xp: 10
    cuerpo: >-
      Login como staff A en staging. Documenta (redactado): Tabla: cookie/token
      | HttpOnly | Secure | SameSite | expira | lleva tenant_id?
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m25-ciber/review/authn.md`.'
      - Evidencia en ruta indicada.
      - 'Si es test: corre en CI o documenta por qué no aún.'
      - 'Commit `docs(m25): l05 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Review authn — sesión y tokens

**~5 h · Semana 2**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/review/authn.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Documentar flujo login/logout/refresh y dónde vive tenant_id.

## Por qué empieza así

Cosmética CSS no salva un leak entre barberías.

Conceptos que debes poder explicar al cerrar:

- Authn vs authz
- tenant_id en sesión
- Tests de regresión

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP — Identity / Authorization testing_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Dibuja el flujo authn (25–35 min)

En `projects/m25-ciber/review/authn.md` secciones: **Login**, **Sesión/JWT**, **Logout/refresh**.

Anota dónde vive `tenant_id` (claim, cookie, header, fila DB).

### 3. Inspecciona tokens reales (90–110 min)

Login como staff A en staging. Documenta (redactado):

```bash
# captura Set-Cookie o body de login — redacta signature/secret
curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"staff-a@example.test","password":"$PASS"}'
```

Tabla: cookie/token | HttpOnly | Secure | SameSite | expira | lleva tenant_id?

### 4. Amenazas y gaps (30–40 min)

≥4 amenazas (token en localStorage, refresh eterno, tenant_id solo en client, logout incompleto). Cada una: severidad + mitigación. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l05 review-authn-sesi-n-y-tokens"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP — Identity / Authorization testing | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/review/authn.md`.
2. Evidencia en ruta indicada.
3. Si es test: corre en CI o documenta por qué no aún.
4. Commit `docs(m25): l05 …` en el historial.

## Errores comunes

- 50 hallazgos menores y cero cross-tenant.
- tenant_id solo en frontend.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Review authz — roles staff vs admin](L06-review-authz-roles-staff-vs-admin.md)
