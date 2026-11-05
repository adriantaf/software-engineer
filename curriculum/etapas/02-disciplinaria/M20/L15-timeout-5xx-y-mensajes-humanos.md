---
id: L15
materia: M20
orden: 15
titulo: 'Timeout, 5xx y mensajes humanos'
horas: 5
semana: 4
lectura: HTTP timeouts
evidencia: nota en demo doc
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Configurar timeout cliente; distinguir 5xx de error usuario.

      - timeout
      - 5xx
  - id: s2
    tipo: ejemplo
    titulo: 1. Timeouts y 5xx
    xp: 10
    cuerpo: |-
      ```ts
      // timeout 10–15s → mensaje "El servidor no respondió"
      // 502/503 → "Estamos reiniciando — reintenta"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Timeout, 5xx y mensajes humanos" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: nota en demo doc
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
    pregunta: ¿Es buena práctica en esta lección? “Mostrar stack trace al usuario."
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
        texto: Configurar timeout cliente; distinguir 5xx de error usuario.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Nota + commit
    xp: 10
    cuerpo: |-
      ```bash
      cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Timeouts/5xx muestran mensajes humanos (sin stack traces).
      - 'Commit `docs(m20): L15 timeout-5xx-y-mensajes-humanos`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — Timeout, 5xx y mensajes humanos

**~5.0 h · Semana 4**

No todo es ‘algo salió mal’.

## Objetivo

Configurar timeout cliente; distinguir 5xx de error usuario.

## Conceptos clave

- timeout
- 5xx

## Pasos (hazlos en orden)

### 1. Timeouts y 5xx (60–80 min)

```ts
// timeout 10–15s → mensaje "El servidor no respondió"
// 502/503 → "Estamos reiniciando — reintenta"
```

### 2. Nota + commit (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Timeouts / 5xx
Mensajes humanos documentados; no stack traces al usuario.
EOF
git add projects/m20-movil
git commit -m "feat(m20): L15 timeout 5xx mensajes humanos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | HTTP timeouts | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Timeouts/5xx muestran mensajes humanos (sin stack traces).
2. Commit `docs(m20): L15 timeout-5xx-y-mensajes-humanos`.

## Errores comunes

- Mostrar stack trace al usuario.
- Timeout infinito.

## Siguiente

[L16 — AppSec móvil: no loguear PII ni tokens](L16-appsec-movil-no-loguear-pii-ni-tokens.md)
