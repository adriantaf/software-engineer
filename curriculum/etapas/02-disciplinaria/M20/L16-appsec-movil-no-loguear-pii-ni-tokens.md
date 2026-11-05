---
id: L16
materia: M20
orden: 16
titulo: 'AppSec móvil: no loguear PII ni tokens'
horas: 5
semana: 4
lectura: OWASP MASVS logging
evidencia: projects/m20-movil/logging-policy.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Revisar print/debug; política de logs en dev vs release.

      - PII
      - tokens
      - crash reports
  - id: s2
    tipo: ejemplo
    titulo: 1. Política de logging
    xp: 10
    cuerpo: >-
      ```bash

      cat > projects/m20-movil/logging-policy.md << 'EOF'

      # Logging móvil

      Prohibido: tokens, passwords, teléfonos completos, bodies de auth.

      Permitido: request id, status code, ruta sin query sensible.

      EOF

      rg -n "console\\.(log|debug)|print\\(|Log\\." projects/m20-movil/app
      2>/dev/null | head || true

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "AppSec móvil: no loguear PII ni tokens" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/logging-policy.md
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

      `git add projects/m20-movil/logging-policy.md`
    comandoEsperado:
      - git add projects/m20-movil/logging-policy.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m20-movil/logging-policy.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Revisar print/debug; política de logs en dev vs release.
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
      git add projects/m20-movil/logging-policy.md
      git commit -m "docs(m20): L16 logging policy appsec"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m20-movil/logging-policy.md`; sin logs de tokens/PII en
        código revisado.
      - 'Commit `docs(m20): L16 appsec-movil-no-loguear-pii-ni-tokens`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — AppSec móvil: no loguear PII ni tokens

**~5.0 h · Semana 4**

Un logcat filtrado filtra tokens.

## Objetivo

Revisar print/debug; política de logs en dev vs release.

## Conceptos clave

- PII
- tokens
- crash reports

## Pasos (hazlos en orden)

### 1. Política de logging (50–60 min)

```bash
cat > projects/m20-movil/logging-policy.md << 'EOF'
# Logging móvil
Prohibido: tokens, passwords, teléfonos completos, bodies de auth.
Permitido: request id, status code, ruta sin query sensible.
EOF
rg -n "console\\.(log|debug)|print\\(|Log\\." projects/m20-movil/app 2>/dev/null | head || true
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil/logging-policy.md
git commit -m "docs(m20): L16 logging policy appsec"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | OWASP MASVS logging | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m20-movil/logging-policy.md`; sin logs de tokens/PII en código revisado.
2. Commit `docs(m20): L16 appsec-movil-no-loguear-pii-ni-tokens`.

## Errores comunes

- `console.log` del Bearer token.
- Telemetría con teléfono completo.

## Siguiente

[L17 — Firma Android y keystore fuera del repo](L17-firma-android-y-keystore-fuera-del-repo.md)
