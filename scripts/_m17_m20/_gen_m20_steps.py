"""Generated step labs for M20 polish."""
STEPS: dict[int, list[tuple[str, str]]] = {}
STEPS[1] = [
    ('Decide Flutter o RN (25–35 min)', r"""
```bash
mkdir -p projects/m20-movil/docs
cat > projects/m20-movil/stack-movil.md << 'EOF'
# Stack móvil Agenda Ops
- Elección: Flutter X.Y  **o** React Native X.Y
- Por qué: …
- SDK / JDK: …
- No cambiar sin ADR
EOF
```
"""),
    ('Scaffold app (90–110 min)', r"""
```bash
# Flutter:
# flutter create agenda_ops_app
# React Native:
# npx @react-native-community/cli init AgendaOpsApp
```

App corre en emulador/dispositivo. Deja el código en submódulo o `projects/m20-movil/app/` y enlázalo en README.
"""),
    ('Evidencia + commit (30 min)', r"""
```bash
cat > projects/m20-movil/repo-url.md << 'EOF'
# Código móvil
Repo / ruta: …
Commit scaffold: …
EOF
# README m20 apunta a repo-url.md y stack-movil.md
git add projects/m20-movil
git commit -m "docs(m20): L01 scaffold stack movil"
```
"""),
]
STEPS[2] = [
    ('Config API URL (30–40 min)', r"""
```dart
// Flutter ejemplo — adapta a RN
const apiBase = String.fromEnvironment('API_BASE', defaultValue: 'http://10.0.2.2:3000');
```

```bash
# Dev: apunta a staging M19 o local documentado en demo-login-lista.md
```
"""),
    ('Pantalla login (90–110 min)', r"""
Email/password → `POST /auth/login`. Muestra error de red/credenciales.

```bash
# Prueba contra staging:
curl -sS -X POST "$API_BASE/auth/login" -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"***"}'
```
"""),
    ('Commit (15 min)', r"""
```bash
echo "## Login" > projects/m20-movil/demo-login-lista.md
git add projects/m20-movil
git commit -m "feat(m20): L02 login contra api staging"
```
"""),
]
STEPS[3] = [
    ('Elige secure storage (30 min)', r"""
```bash
# Flutter: flutter_secure_storage
# RN: react-native-keychain / expo-secure-store
cat > projects/m20-movil/auth-storage.md << 'EOF'
# Auth storage
API: …  Dónde vive el token/sesión: Keychain/Keystore
Nunca: SharedPreferences / AsyncStorage en claro
EOF
```
"""),
    ('Implementa save/read/clear (80–100 min)', r"""
```ts
// pseudocódigo RN
await Keychain.setGenericPassword('session', token);
// NUNCA console.log(token)
```

Tras login guarda; al logout borra.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil
git commit -m "feat(m20): L03 secure storage sesion"
```
"""),
]
STEPS[4] = [
    ('Interceptor 401 (70–90 min)', r"""
```ts
// si response.status === 401 → clearSecureStorage(); navigate('Login');
```

Mensajes de validación 400 legibles (campo email/password).
"""),
    ('Prueba manual (30 min)', r"""
```bash
# 1) Login OK  2) Invalida token en storage  3) Pull lista → vuelve a Login
# Anota en auth-storage.md
git add projects/m20-movil/auth-storage.md
git commit -m "feat(m20): L04 flujo 401 y validacion"
```
"""),
]
STEPS[5] = [
    ('GET /citas autenticado (80–100 min)', r"""
```bash
# Misma cookie/Bearer que web — documenta el esquema en stack-movil.md
curl -sS -b /tmp/st.ck "$API_BASE/citas"
```

Lista en UI con fecha/cliente/servicio.
"""),
    ('Evidencia P1 (30 min)', r"""
```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Lista citas
Fecha demo: …  API: staging …  Resultado: OK
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L05 lista citas autenticada"
```
"""),
]
STEPS[6] = [
    ('Pull-to-refresh (50–60 min)', r"""
```dart
// RefreshIndicator onRefresh: () => controller.reload()
```
"""),
    ('Paginación simple (50–60 min)', r"""
```bash
# API: GET /citas?cursor=… o ?page=2 — documenta contrato
curl -sS -b /tmp/st.ck "$API_BASE/citas?limit=20"
```

```bash
git add projects/m20-movil
git commit -m "feat(m20): L06 pull-to-refresh paginacion"
```
"""),
]
STEPS[7] = [
    ('Estados loading/error (60–80 min)', r"""
Spinner inicial; banner error con “Reintentar”; no lista fantasma.
"""),
    ('Captura en demo doc (30 min)', r"""
```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Estados carga
loading: …  error: … (captura redactada opcional)
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L07 estados carga lista"
```
"""),
]
STEPS[8] = [
    ('Confía en API para RBAC (50–60 min)', r"""
```bash
# staff token → acción owner debe fallar 403 aunque el botón exista
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" "$API_BASE/admin/staff"
```
"""),
    ('Nota rbac (30 min)', r"""
```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## RBAC
UI puede ocultar; autorización real = API 403. Probado: …
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "docs(m20): L08 roles confiar en api"
```
"""),
]
STEPS[9] = [
    ('Detalle de cita (70–90 min)', r"""
```bash
curl -sS -b /tmp/st.ck "$API_BASE/citas/<id>"
```

Pantalla: cliente, servicio, horario, estado. Tap desde lista.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil
git commit -m "feat(m20): L09 pantalla detalle cita"
```
"""),
]
STEPS[10] = [
    ('Tabs o drawer (60–80 min)', r"""
```dart
// BottomNavigation: Citas | Clientes | Cuenta
// o Drawer equivalente en RN
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil
git commit -m "feat(m20): L10 navegacion tabs drawer"
```
"""),
]
STEPS[11] = [
    ('Acciones cancelar/atendida (70–90 min)', r"""
```bash
curl -sS -b /tmp/st.ck -X PATCH "$API_BASE/citas/<id>/estado" \
  -H 'content-type: application/json' \
  -d '{"estado":"cancelada"}'
```

Botones solo si el rol/API lo permiten; maneja 403.
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil
git commit -m "feat(m20): L11 acciones cancelar atendida"
```
"""),
]
STEPS[12] = [
    ('Deep link cita (60–80 min)', r"""
```bash
# Android intent-filter / iOS universal link — scheme agendaops://cita/<id>
cat > projects/m20-movil/deep-link.md << 'EOF'
# Deep links
Scheme: agendaops://cita/:id
Prueba: adb shell am start -a android.intent.action.VIEW -d "agendaops://cita/UUID"
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil/deep-link.md
git commit -m "feat(m20): L12 deep link cita"
```
"""),
]
STEPS[13] = [
    ('Empty state útil (50–60 min)', r"""
Copy: “No hay citas hoy — crea la primera en la web o aquí”. CTA claro.
"""),
    ('Evidencia P2 (30 min)', r"""
```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Lista vacía
Copy: …  Captura: …
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "feat(m20): L13 lista vacia copy util"
```
"""),
]
STEPS[14] = [
    ('Banner offline (60–80 min)', r"""
```dart
// connectivity_plus / NetInfo → banner "Sin red" + botón Reintentar
```
"""),
    ('Prueba avión (30 min)', r"""
```bash
# Activa modo avión → banner visible → reintento al volver
echo "Offline OK $(date -I)" >> projects/m20-movil/demo-login-lista.md
git add projects/m20-movil
git commit -m "feat(m20): L14 banner sin red reintento"
```
"""),
]
STEPS[15] = [
    ('Timeouts y 5xx (60–80 min)', r"""
```ts
// timeout 10–15s → mensaje "El servidor no respondió"
// 502/503 → "Estamos reiniciando — reintenta"
```
"""),
    ('Nota + commit (30 min)', r"""
```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Timeouts / 5xx
Mensajes humanos documentados; no stack traces al usuario.
EOF
git add projects/m20-movil
git commit -m "feat(m20): L15 timeout 5xx mensajes humanos"
```
"""),
]
STEPS[16] = [
    ('Política de logging (50–60 min)', r"""
```bash
cat > projects/m20-movil/logging-policy.md << 'EOF'
# Logging móvil
Prohibido: tokens, passwords, teléfonos completos, bodies de auth.
Permitido: request id, status code, ruta sin query sensible.
EOF
rg -n "console\\.(log|debug)|print\\(|Log\\." projects/m20-movil/app 2>/dev/null | head || true
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil/logging-policy.md
git commit -m "docs(m20): L16 logging policy appsec"
```
"""),
]
STEPS[17] = [
    ('Keystore fuera del repo (60–80 min)', r"""
```bash
# keytool -genkey ... (local)
# NUNCA commits de *.jks / *.keystore
printf '%s\n' '*.jks' '*.keystore' 'key.properties' >> .gitignore
cat > projects/m20-movil/build-evidence.md << 'EOF'
# Build evidence (prep)
Keystore: ubicación local / CI secret (NO en git)
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add .gitignore projects/m20-movil/build-evidence.md
git commit -m "docs(m20): L17 keystore fuera del repo"
```
"""),
]
STEPS[18] = [
    ('Build release (80–110 min)', r"""
```bash
# Flutter: flutter build apk --release
# RN: cd android && ./gradlew assembleRelease
ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
```
"""),
    ('Documenta artefacto (30 min)', r"""
```bash
cat >> projects/m20-movil/build-evidence.md << 'EOF'
## Release
Fecha: …  Hash/archivo: app-release.apk  Instalado en dispositivo: sí/no
EOF
git add projects/m20-movil/build-evidence.md
git commit -m "docs(m20): L18 build release apk"
```
"""),
]
STEPS[19] = [
    ('Release notes + demo cruzada (50–60 min)', r"""
```bash
cat > projects/m20-movil/release-notes.md << 'EOF'
# Release notes móvil
- Login + lista citas (misma API que web)
- Secure storage
- Build: ver build-evidence.md
Demo cruzada: misma cita visible en web staging y app.
EOF
```
"""),
    ('Commit (15 min)', r"""
```bash
git add projects/m20-movil/release-notes.md
git commit -m "docs(m20): L19 release notes demo cruzada"
```
"""),
]
STEPS[20] = [
    ('README índice proyecto (50–60 min)', r"""
```bash
ls projects/m20-movil
# README debe enlazar: stack-movil.md, auth-storage.md, demo-login-lista.md,
# build-evidence.md, logging-policy.md, release-notes.md, repo-url.md
rg -n "stack-movil|auth-storage|demo-login|build-evidence" projects/m20-movil/README.md
```
"""),
    ('Commit cierre (15 min)', r"""
```bash
git add projects/m20-movil
git commit -m "docs(m20): L20 cierre dominio readme"
```
"""),
]
