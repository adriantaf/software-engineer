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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - timeout

      - 5xx


      **Objetivo de esta lección:** Configurar timeout cliente; distinguir 5xx
      de error usuario.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Timeouts y 5xx
    xp: 10
    cuerpo: |-
      ```ts
      // timeout 10–15s → mensaje "El servidor no respondió"
      // 502/503 → "Estamos reiniciando — reintenta"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Nota + commit
    xp: 10
    cuerpo: |-
      ```ts
      // timeout 10–15s → mensaje "El servidor no respondió"
      // 502/503 → "Estamos reiniciando — reintenta"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Timeout, 5xx y mensajes humanos», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Timeout, 5xx y mensajes
          humanos
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Mostrar stack trace al usuario."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Configurar timeout cliente; distinguir 5xx de error usuario.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Timeout infinito."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Timeouts/5xx muestran mensajes humanos (sin stack traces).
      - 'Commit `docs(m20): L15 timeout-5xx-y-mensajes-humanos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
