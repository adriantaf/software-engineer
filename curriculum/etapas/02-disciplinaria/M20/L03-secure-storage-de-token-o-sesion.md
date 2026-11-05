---
id: L03
materia: M20
orden: 3
titulo: Secure storage de token o sesión
horas: 5
semana: 1
lectura: Keychain / Keystore vía lib oficial
evidencia: projects/m20-movil/auth-storage.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Persistir access token con flutter_secure_storage o
      equivalente RN; documentar qué guardas.


      - secure storage

      - no password disk
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige secure storage
    xp: 10
    cuerpo: |-
      ```ts
      // pseudocódigo RN
      await Keychain.setGenericPassword('session', token);
      // NUNCA console.log(token)
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Secure storage de token o sesión" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/auth-storage.md
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Token en
      SharedPreferences/AsyncStorage en claro."
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
          Persistir access token con flutter_secure_storage o equivalente RN;
          documentar qué guardas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementa save/read/clear
    xp: 10
    cuerpo: |-
      ```ts
      // pseudocódigo RN
      await Keychain.setGenericPassword('session', token);
      // NUNCA console.log(token)
      ```

      Tras login guarda; al logout borra.
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "feat(m20): L03 secure storage sesion"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m20-movil/auth-storage.md` + implementación Keychain/Keystore
        (no texto claro).
      - 'Commit `docs(m20): L03 secure-storage-de-token-o-sesion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Secure storage de token o sesión

**~5.0 h · Semana 1**

JWT en SharedPreferences plano es hallazgo M18.

## Objetivo

Persistir access token con flutter_secure_storage o equivalente RN; documentar qué guardas.

## Conceptos clave

- secure storage
- no password disk

## Pasos (hazlos en orden)

### 1. Elige secure storage (30 min)

```bash
# Flutter: flutter_secure_storage
# RN: react-native-keychain / expo-secure-store
cat > projects/m20-movil/auth-storage.md << 'EOF'
# Auth storage
API: …  Dónde vive el token/sesión: Keychain/Keystore
Nunca: SharedPreferences / AsyncStorage en claro
EOF
```

### 2. Implementa save/read/clear (80–100 min)

```ts
// pseudocódigo RN
await Keychain.setGenericPassword('session', token);
// NUNCA console.log(token)
```

Tras login guarda; al logout borra.

### 3. Commit (15 min)

```bash
git add projects/m20-movil
git commit -m "feat(m20): L03 secure storage sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Keychain / Keystore vía lib oficial | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/auth-storage.md` + implementación Keychain/Keystore (no texto claro).
2. Commit `docs(m20): L03 secure-storage-de-token-o-sesion`.

## Errores comunes

- Token en SharedPreferences/AsyncStorage en claro.
- Loguear el token.

## Siguiente

[L04 — Errores de validación y flujo 401](L04-errores-de-validacion-y-flujo-401.md)
