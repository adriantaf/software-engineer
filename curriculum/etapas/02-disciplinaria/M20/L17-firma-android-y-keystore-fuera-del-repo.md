---
id: L17
materia: M20
orden: 17
titulo: Firma Android y keystore fuera del repo
horas: 5.0
semana: 5
lectura: Android signing / iOS profiles
evidencia: projects/m20-movil/build-evidence.md (prep)
---

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
