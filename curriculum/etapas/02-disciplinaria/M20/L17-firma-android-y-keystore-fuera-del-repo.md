---
id: L17
materia: M20
orden: 17
titulo: Firma Android y keystore fuera del repo
horas: 5
semana: 5
lectura: Android signing / iOS profiles
evidencia: projects/m20-movil/build-evidence.md (prep)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear keystore local ignorado; documentar variables CI
      futuras.


      - keystore

      - gradle signing
  - id: s2
    tipo: ejemplo
    titulo: 1. Keystore fuera del repo
    xp: 10
    cuerpo: |-
      ```bash
      # keytool -genkey ... (local)
      # NUNCA commits de *.jks / *.keystore
      printf '%s\n' '*.jks' '*.keystore' 'key.properties' >> .gitignore
      cat > projects/m20-movil/build-evidence.md << 'EOF'
      # Build evidence (prep)
      Keystore: ubicación local / CI secret (NO en git)
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Firma Android y keystore fuera del repo" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/build-evidence.md (prep)
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

      `git add .gitignore projects/m20-movil/build-evidence.md`
    comandoEsperado:
      - git add .gitignore projects/m20-movil/build-evidence.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add .gitignore projects/m20-movil/build-evidence.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Crear keystore local ignorado; documentar variables CI futuras.
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
      git add .gitignore projects/m20-movil/build-evidence.md
      git commit -m "docs(m20): L17 keystore fuera del repo"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m20-movil/build-evidence.md` prep + keystore en `.gitignore`.'
      - 'Commit `docs(m20): L17 firma-android-y-keystore-fuera-del-repo`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — Firma Android y keystore fuera del repo

**~5.0 h · Semana 5**

P3 requiere build instalable real.

## Objetivo

Crear keystore local ignorado; documentar variables CI futuras.

## Conceptos clave

- keystore
- gradle signing

## Pasos (hazlos en orden)

### 1. Keystore fuera del repo (60–80 min)

```bash
# keytool -genkey ... (local)
# NUNCA commits de *.jks / *.keystore
printf '%s\n' '*.jks' '*.keystore' 'key.properties' >> .gitignore
cat > projects/m20-movil/build-evidence.md << 'EOF'
# Build evidence (prep)
Keystore: ubicación local / CI secret (NO en git)
EOF
```

### 2. Commit (15 min)

```bash
git add .gitignore projects/m20-movil/build-evidence.md
git commit -m "docs(m20): L17 keystore fuera del repo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Android signing / iOS profiles | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/build-evidence.md` prep + keystore en `.gitignore`.
2. Commit `docs(m20): L17 firma-android-y-keystore-fuera-del-repo`.

## Errores comunes

- Commitear `.jks` / `key.properties`.
- Password del keystore en el README.

## Siguiente

[L18 — Build release APK o artefacto](L18-build-release-apk-o-artefacto.md)
