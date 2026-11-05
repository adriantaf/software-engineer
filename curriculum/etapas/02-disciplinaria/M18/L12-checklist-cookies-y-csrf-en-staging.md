---
id: L12
materia: M18
orden: 12
titulo: Checklist cookies y CSRF en staging
horas: 5
semana: 3
lectura: Repaso semana 3
evidencia: projects/m18-appsec/docs/checklist-cookies-csrf.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Checklist ≥10 ítems en
      `projects/m18-appsec/docs/checklist-cookies-csrf.md` ejecutado contra
      staging (fecha + URL).


      Operacionalizas controles para M19 deploy y trials M22.
  - id: s2
    tipo: ejemplo
    titulo: 1. Escribe el checklist
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/docs/checklist-cookies-csrf.md <<'EOF'
      Checklist cookies / CSRF — staging

      Fecha: ____ · URL: ____

      | # | Ítem | Sí/No | Nota |
      |---|------|-------|------|
      | 1 | Cookie sesión HttpOnly | | |
      | 2 | Secure en HTTPS | | |
      | 3 | SameSite Lax/Strict | | |
      | 4 | Session id rota post-login | | |
      | 5 | Logout invalida server-side | | |
      | 6 | POST pedidos exige CSRF/equiv | | |
      | 7 | GET no muta estado | | |
      | 8 | Mensajes login genéricos | | |
      | 9 | HTTPS redirect (si aplica) | | |
      | 10 | Sin cookie sesión en document.cookie | | |
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Checklist cookies y CSRF en staging" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/docs/checklist-cookies-csrf.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Checklist nunca ejecutado."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Checklist ≥10 ítems en
          `projects/m18-appsec/docs/checklist-cookies-csrf.md` ejecutado contra
          staging (fecha + URL).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Checklist ejecutado (artefacto:
        `projects/m18-appsec/docs/checklist-cookies-csrf.md`).
      - >-
        Fecha y URL (artefacto:
        `projects/m18-appsec/docs/checklist-cookies-csrf.md`).
      - 'Commit `docs(m18): L12 checklist-cookies-y-csrf-en-staging`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Checklist cookies y CSRF en staging

**~5.0 h · Semana 3**

Operacionalizas controles para M19 deploy y trials M22.

## Objetivo

Checklist ≥10 ítems en `projects/m18-appsec/docs/checklist-cookies-csrf.md` ejecutado contra staging (fecha + URL).

## Pasos

### 1. Escribe el checklist (40–50 min)

```bash
cat > projects/m18-appsec/docs/checklist-cookies-csrf.md <<'EOF'
# Checklist cookies / CSRF — staging

Fecha: ____ · URL: ____

| # | Ítem | Sí/No | Nota |
|---|------|-------|------|
| 1 | Cookie sesión HttpOnly | | |
| 2 | Secure en HTTPS | | |
| 3 | SameSite Lax/Strict | | |
| 4 | Session id rota post-login | | |
| 5 | Logout invalida server-side | | |
| 6 | POST pedidos exige CSRF/equiv | | |
| 7 | GET no muta estado | | |
| 8 | Mensajes login genéricos | | |
| 9 | HTTPS redirect (si aplica) | | |
| 10 | Sin cookie sesión en document.cookie | | |

## Residual CSRF
- …

## Commits semana 3
- …
EOF
```
### 2. Ejecuta en staging/local (60–80 min)

Marca Sí/No con evidencia (curl headers, captura redactada). Corrige ≥1 ítem No si aparece.

```bash
curl -sI https://<tu-staging>/ | rg -i 'strict-transport|set-cookie' || true
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/checklist-cookies-csrf.md
git commit -m "docs(m18): l12 checklist cookies csrf"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Repaso semana 3 | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist ejecutado (artefacto: `projects/m18-appsec/docs/checklist-cookies-csrf.md`).
2. Fecha y URL (artefacto: `projects/m18-appsec/docs/checklist-cookies-csrf.md`).
3. Commit `docs(m18): L12 checklist-cookies-y-csrf-en-staging`.

## Errores comunes

- Checklist nunca ejecutado.
- Marcar todo Sí sin prueba.

## Siguiente

[L13 — SQLi: reproducir en tu propia API](L13-sqli-reproducir-en-tu-propia-api.md)
