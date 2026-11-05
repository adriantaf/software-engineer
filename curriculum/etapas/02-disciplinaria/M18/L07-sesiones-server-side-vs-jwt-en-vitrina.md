---
id: L07
materia: M18
orden: 7
titulo: Sesiones server-side vs JWT en Vitrina
horas: 5
semana: 2
lectura: Session Management + JWT Cheat Sheets
evidencia: projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Vitrina: panel web + API; móvil M20 futuro.


      **Objetivo de esta lección:** ADR en
      `projects/m18-appsec/docs/adr-sesion-vs-jwt.md`: decisión, alternativas,
      impacto XSS/CSRF/móvil M20.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Compara en contexto
    xp: 10
    cuerpo: >-
      Tabla pros/contras: panel+API same-site vs SPA cross-origin; revocación;
      HttpOnly vs `Authorization`. ```bash mkdir -p projects/m18-appsec/docs cat
      > projects/m18-appsec/docs/adr-sesion-vs-jwt.md <<'EOF' # ADR — Sesión
      server-side vs JWT
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Sesiones server-side vs JWT en Vitrina», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Sesiones server-side vs
          JWT en Vitrina
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
    pregunta: ¿Es recomendable en esta lección? “JWT en localStorage sin plan anti-XSS."
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
          ADR en `projects/m18-appsec/docs/adr-sesion-vs-jwt.md`: decisión,
          alternativas, impacto XSS/CSRF/móvil M20.
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
    pregunta: ¿Debes hacer esto? “Sin estrategia de revocación."
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
      - >-
        ADR con alternativas (artefacto:
        `projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
      - >-
        Prueba logout/reuse documentada (artefacto:
        `projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
      - 'Commit `docs(m18): L07 sesiones-server-side-vs-jwt-en-vitrina`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Sesiones server-side vs JWT en Vitrina

**~5.0 h · Semana 2**

M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.

## Objetivo

ADR en `projects/m18-appsec/docs/adr-sesion-vs-jwt.md`: decisión, alternativas, impacto XSS/CSRF/móvil M20.

## Pasos

### 1. Compara en contexto (40–50 min)

Tabla pros/contras: panel+API same-site vs SPA cross-origin; revocación; HttpOnly vs `Authorization`.

```bash
mkdir -p projects/m18-appsec/docs
cat > projects/m18-appsec/docs/adr-sesion-vs-jwt.md <<'EOF'
# ADR — Sesión server-side vs JWT

## Contexto
Vitrina: panel web + API; móvil M20 futuro.

## Opciones
| Opción | Revocación | XSS | CSRF | Móvil |
|--------|------------|-----|------|-------|
| Sesión + cookie HttpOnly | inmediata (DB) | mejor | riesgo CSRF | cookie jar |
| JWT en memoria / header | short TTL / deny-list | si en storage, peor | menos CSRF | natural |
| Híbrido | … | … | … | … |

## Decisión
…

## Consecuencias / mitigaciones obligatorias
- HttpOnly / TTL / revoke / SameSite …
EOF
```
### 2. Prueba logout/reuse (40–50 min)

Login → copiar cookie/token → logout → reutilizar (debe fallar). Anota en la ADR.

```bash
# Ejemplo cookie de sesión (ajusta nombre/URL)
curl -c /tmp/m18-cj -s -X POST localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' -o /dev/null -w "%{http_code}\n"
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout -w "%{http_code}\n"
curl -b /tmp/m18-cj -s localhost:3000/api/pedidos -w "\n%{http_code}\n" | tail -3
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/adr-sesion-vs-jwt.md
git commit -m "docs(m18): l07 adr sesion jwt"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Session Management + JWT Cheat Sheets | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR con alternativas (artefacto: `projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
2. Prueba logout/reuse documentada (artefacto: `projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)`).
3. Commit `docs(m18): L07 sesiones-server-side-vs-jwt-en-vitrina`.

## Errores comunes

- JWT en localStorage sin plan anti-XSS.
- Sin estrategia de revocación.

## Siguiente

[L08 — Threat model v1 post-autenticación (P1)](L08-threat-model-v1-post-autenticacion-p1.md)
