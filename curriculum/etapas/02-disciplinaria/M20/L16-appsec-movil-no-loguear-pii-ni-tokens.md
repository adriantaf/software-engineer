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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - PII

      - tokens

      - crash reports


      **Objetivo de esta lección:** Revisar print/debug; política de logs en dev
      vs release.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Política de logging
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil/logging-policy.md
      git commit -m "docs(m20): L16 logging policy appsec"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «AppSec móvil: no loguear PII ni tokens», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de AppSec móvil: no
          loguear PII ni tokens
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

      `git add projects/m20-movil/logging-policy.md`
    comandoEsperado:
      - git add projects/m20-movil/logging-policy.md
      - 'git commit -m "docs(m20): L16 logging policy appsec"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m20-movil/logging-policy.md'
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
        texto: Revisar print/debug; política de logs en dev vs release.
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

      `git commit -m "docs(m20): L16 logging policy appsec"`
    comandoEsperado:
      - 'git commit -m "docs(m20): L16 logging policy appsec"'
    explicacionError: 'Esperado: git commit -m "docs(m20): L16 logging policy appsec"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe `projects/m20-movil/logging-policy.md`; sin logs de tokens/PII en
        código revisado.
      - 'Commit `docs(m20): L16 appsec-movil-no-loguear-pii-ni-tokens`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
