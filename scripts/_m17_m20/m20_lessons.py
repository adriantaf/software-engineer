"""M20 lessons: RAW specs + BODIES (M01/M09 quality)."""
from __future__ import annotations

import json

FILENAMES = {
    1: "L01-stack-movil-y-scaffold-agenda-ops.md",
    2: "L02-pantalla-login-contra-api-staging.md",
    3: "L03-secure-storage-de-token-o-sesion.md",
    4: "L04-errores-de-validacion-y-flujo-401.md",
    5: "L05-lista-de-citas-autenticada.md",
    6: "L06-pull-to-refresh-y-paginacion-simple.md",
    7: "L07-estados-de-carga-en-lista.md",
    8: "L08-roles-confiar-en-la-api-no-solo-en-ui.md",
    9: "L09-pantalla-detalle-de-cita.md",
    10: "L10-navegacion-tabs-o-drawer-minimo.md",
    11: "L11-acciones-permitidas-cancelar-atendida.md",
    12: "L12-deep-link-opcional-a-una-cita.md",
    13: "L13-lista-vacia-con-copy-util.md",
    14: "L14-sin-red-banner-y-reintento.md",
    15: "L15-timeout-5xx-y-mensajes-humanos.md",
    16: "L16-appsec-movil-no-loguear-pii-ni-tokens.md",
    17: "L17-firma-android-y-keystore-fuera-del-repo.md",
    18: "L18-build-release-apk-o-artefacto.md",
    19: "L19-release-notes-y-demo-cruzada-con-web.md",
    20: "L20-cierre-m20-dominio-y-readme-proyecto.md",
}

RAW = json.loads(r"""
[
  {
    "titulo": "Stack móvil y scaffold Agenda Ops",
    "semana": 1,
    "horas": 5,
    "lectura": "Flutter o RN — get started",
    "evidencia": "projects/m20-movil/stack.md + repo-url.md",
    "objetivo": "Elegir Flutter o RN, documentar SDK, crear scaffold y enlazar repo.",
    "porque": "Un framework, un camino hasta M20 cierre.",
    "conceptos": [
      "Flutter vs RN",
      "staging URL",
      "lint"
    ],
    "pasos_extra": "mkdir -p projects/m20-movil. stack.md con decisión. Scaffold en app/ o repo enlazado.",
    "lectura_rows": [
      [
        "Docs",
        "oficial stack",
        "producto-saas"
      ]
    ],
    "hecho": [
      "stack.md",
      "scaffold commit",
      "repo-url"
    ],
    "errores": [
      "Cambiar stack semana 3",
      "Sin versión SDK"
    ]
  },
  {
    "titulo": "Pantalla login contra API staging",
    "semana": 1,
    "horas": 5,
    "lectura": "HTTP client + auth API",
    "evidencia": "projects/m20-movil/demo-login-lista.md (inicio)",
    "objetivo": "Implementar login email/password contra HTTPS M19; errores claros sin stack trace.",
    "porque": "Misma API que web M17.",
    "conceptos": [
      "POST login",
      "401 UX",
      "timeout"
    ],
    "pasos_extra": "Probar contra staging. Anota URL base en stack.md. Commit feat(m20): login.",
    "lectura_rows": [
      [
        "M17",
        "auth endpoints",
        "M19 staging"
      ]
    ],
    "hecho": [
      "Login feliz",
      "401 mensaje humano",
      "HTTPS"
    ],
    "errores": [
      "localhost en release",
      "Password en logs"
    ]
  },
  {
    "titulo": "Secure storage de token o sesión",
    "semana": 1,
    "horas": 5,
    "lectura": "Keychain / Keystore vía lib oficial",
    "evidencia": "projects/m20-movil/auth-storage.md",
    "objetivo": "Persistir access token con flutter_secure_storage o equivalente RN; documentar qué guardas.",
    "porque": "JWT en SharedPreferences plano es hallazgo M18.",
    "conceptos": [
      "secure storage",
      "no password disk"
    ],
    "pasos_extra": "auth-storage.md: claves, refresh si aplica, borrado en logout.",
    "lectura_rows": [
      [
        "OWASP",
        "Mobile MASVS storage",
        "M18 JWT"
      ]
    ],
    "hecho": [
      "auth-storage.md",
      "código referenciado",
      "sin password claro"
    ],
    "errores": [
      "Token en logs",
      "AsyncStorage plano"
    ]
  },
  {
    "titulo": "Errores de validación y flujo 401",
    "semana": 1,
    "horas": 5,
    "lectura": "Interceptors HTTP",
    "evidencia": "commit + nota en auth-storage.md",
    "objetivo": "Manejar 401 global (logout), validación formulario, estados loading/error en login.",
    "porque": "Auth móvil real no termina en login exitoso una vez.",
    "conceptos": [
      "interceptor",
      "navigator login"
    ],
    "pasos_extra": "Implementa interceptor 401 como ejemplo ficha M20. Prueba token expirado.",
    "lectura_rows": [
      [
        "Ficha",
        "M20 ejemplo 401",
        "—"
      ]
    ],
    "hecho": [
      "401 redirige login",
      "Loading/error UI",
      "Commit"
    ],
    "errores": [
      "Stack trace al usuario",
      "Ignorar 401"
    ]
  },
  {
    "titulo": "Lista de citas autenticada",
    "semana": 2,
    "horas": 5,
    "lectura": "ListView / FlatList patterns",
    "evidencia": "projects/m20-movil/demo-login-lista.md",
    "objetivo": "GET citas con token; mostrar fecha, cliente, servicio, estado.",
    "porque": "P1 M20: login + lista evidenciada.",
    "conceptos": [
      "Authorization header",
      "JSON parse",
      "orden"
    ],
    "pasos_extra": "Captura lista + commit hash en demo-login-lista.md.",
    "lectura_rows": [
      [
        "API",
        "GET citas",
        "SRS"
      ]
    ],
    "hecho": [
      "Lista con datos reales API",
      "commit hash en doc",
      "token adjunto"
    ],
    "errores": [
      "Mock JSON",
      "Datos inventados"
    ]
  },
  {
    "titulo": "Pull-to-refresh y paginación simple",
    "semana": 2,
    "horas": 5,
    "lectura": "Async refresh UX",
    "evidencia": "commit UI",
    "objetivo": "Refrescar lista; soportar query page/limit si la API lo expone.",
    "porque": "Dueño espera gesto natural en móvil.",
    "conceptos": [
      "refresh",
      "pagination"
    ],
    "pasos_extra": "Documenta comportamiento si API sin paginación (corte client-side temporal).",
    "lectura_rows": [
      [
        "Docs",
        "list refresh",
        "—"
      ]
    ],
    "hecho": [
      "Refresh funciona",
      "Sin crash lista vacía loading"
    ],
    "errores": [
      "Refresh sin indicador",
      "Duplicar fetch infinito"
    ]
  },
  {
    "titulo": "Estados de carga en lista",
    "semana": 2,
    "horas": 5,
    "lectura": "UX loading skeletons",
    "evidencia": "captura en demo-login-lista.md",
    "objetivo": "Skeleton o spinner, deshabilitar doble tap, error con reintento.",
    "porque": "Red móvil es lenta; la UI debe comunicarlo.",
    "conceptos": [
      "loading",
      "error retry"
    ],
    "pasos_extra": "Tres capturas: loading, éxito, error en demo doc.",
    "lectura_rows": [
      [
        "Ficha",
        "M20 semana 2",
        "—"
      ]
    ],
    "hecho": [
      "Tres estados UI",
      "Reintento",
      "Capturas"
    ],
    "errores": [
      "Pantalla blanca",
      "Carga infinita"
    ]
  },
  {
    "titulo": "Roles: confiar en la API, no solo en UI",
    "semana": 2,
    "horas": 5,
    "lectura": "RBAC móvil",
    "evidencia": "nota rbac en demo-login-lista.md",
    "objetivo": "Probar cuenta staff vs owner; ocultar acciones que API niega con 403.",
    "porque": "Doble fuente de verdad mata proyectos.",
    "conceptos": [
      "403 handling",
      "roles"
    ],
    "pasos_extra": "Prueba endpoint prohibido; muestra mensaje adecuado.",
    "lectura_rows": [
      [
        "M18",
        "rbac-matrix",
        "M12 roles"
      ]
    ],
    "hecho": [
      "Prueba rol documentada",
      "403 UX",
      "Sin lógica secreta solo UI"
    ],
    "errores": [
      "Admin hardcoded en app",
      "Ignorar 403"
    ]
  },
  {
    "titulo": "Pantalla detalle de cita",
    "semana": 3,
    "horas": 5,
    "lectura": "Navigation params",
    "evidencia": "commit pantalla detalle",
    "objetivo": "Navegar a detalle con id; mostrar campos completos de la cita.",
    "porque": "Lista sin detalle no sirve al dueño en campo.",
    "conceptos": [
      "route args",
      "fetch by id"
    ],
    "pasos_extra": "Deep link interno navigator.push con id.",
    "lectura_rows": [
      [
        "API",
        "GET cita/:id",
        "—"
      ]
    ],
    "hecho": [
      "Detalle coincide API",
      "Loading en detalle",
      "Commit"
    ],
    "errores": [
      "Detalle mock",
      "IDOR no manejado"
    ]
  },
  {
    "titulo": "Navegación: tabs o drawer mínimo",
    "semana": 3,
    "horas": 5,
    "lectura": "Navigation container",
    "evidencia": "commit nav",
    "objetivo": "Estructura Citas / Perfil / logout accesible.",
    "porque": "App usable sin laberinto de pantallas.",
    "conceptos": [
      "tabs",
      "drawer",
      "logout"
    ],
    "pasos_extra": "Perfil muestra email usuario; logout limpia secure storage.",
    "lectura_rows": [
      [
        "Docs",
        "navigation",
        "—"
      ]
    ],
    "hecho": [
      "Nav estable",
      "Logout limpia token",
      "Commit"
    ],
    "errores": [
      "Sin logout",
      "Back stack roto"
    ]
  },
  {
    "titulo": "Acciones permitidas: cancelar / atendida",
    "semana": 3,
    "horas": 5,
    "lectura": "Mutations HTTP",
    "evidencia": "commit si API expone",
    "objetivo": "Llamar PATCH/POST que la API expone; deshabilitar si 403.",
    "porque": "Solo acciones que el backend autoriza.",
    "conceptos": [
      "mutation",
      "optimistic UI opcional"
    ],
    "pasos_extra": "Si API no tiene acción, documenta en nota y enlaza issue M17.",
    "lectura_rows": [
      [
        "SRS",
        "historias citas",
        "—"
      ]
    ],
    "hecho": [
      "Acción o gap documentado",
      "403 manejado",
      "Commit"
    ],
    "errores": [
      "Reglas negocio solo en app",
      "Silenciar errores"
    ]
  },
  {
    "titulo": "Deep link opcional a una cita",
    "semana": 3,
    "horas": 5,
    "lectura": "Deep linking intro",
    "evidencia": "projects/m20-movil/deep-link.md",
    "objetivo": "Configurar esquema o ruta para abrir detalle desde URL/notificación futura.",
    "porque": "Preparación recordatorios WhatsApp futuro.",
    "conceptos": [
      "deep link",
      "routing"
    ],
    "pasos_extra": "deep-link.md con formato URL y prueba manual (adb xcrun si aplica).",
    "lectura_rows": [
      [
        "Docs",
        "deep linking",
        "—"
      ]
    ],
    "hecho": [
      "Doc deep link",
      "Prueba manual o N/A justificado",
      "Commit config"
    ],
    "errores": [
      "Deep link sin auth",
      "Abrir cita de otro user"
    ]
  },
  {
    "titulo": "Lista vacía con copy útil",
    "semana": 4,
    "horas": 5,
    "lectura": "Empty states UX",
    "evidencia": "capturas P2",
    "objetivo": "UI cuando no hay citas semana; CTA coherente con producto.",
    "porque": "P2 pide estados vacío/error.",
    "conceptos": [
      "empty state",
      "copy"
    ],
    "pasos_extra": "Captura empty state en auth-storage o demo doc.",
    "lectura_rows": [
      [
        "producto-saas",
        "ICP",
        "—"
      ]
    ],
    "hecho": [
      "Copy útil",
      "Captura",
      "Sin crash"
    ],
    "errores": [
      "Lista vacía en blanco",
      "Texto lorem"
    ]
  },
  {
    "titulo": "Sin red: banner y reintento",
    "semana": 4,
    "horas": 5,
    "lectura": "Connectivity plugins",
    "evidencia": "captura offline",
    "objetivo": "Detectar offline o fallo DNS; banner y botón reintentar.",
    "porque": "Dueño en campo pierde señal a menudo.",
    "conceptos": [
      "offline",
      "retry"
    ],
    "pasos_extra": "Simula modo avión; documenta comportamiento.",
    "lectura_rows": [
      [
        "Docs",
        "connectivity",
        "—"
      ]
    ],
    "hecho": [
      "Modo avión probado",
      "Reintento",
      "Captura"
    ],
    "errores": [
      "Crash sin red",
      "Loop infinito retry"
    ]
  },
  {
    "titulo": "Timeout, 5xx y mensajes humanos",
    "semana": 4,
    "horas": 5,
    "lectura": "HTTP timeouts",
    "evidencia": "nota en demo doc",
    "objetivo": "Configurar timeout cliente; distinguir 5xx de error usuario.",
    "porque": "No todo es ‘algo salió mal’.",
    "conceptos": [
      "timeout",
      "5xx"
    ],
    "pasos_extra": "Prueba timeout bajo artificialmente en dev.",
    "lectura_rows": [
      [
        "Ficha",
        "M20 semana 4",
        "—"
      ]
    ],
    "hecho": [
      "Timeout configurado",
      "5xx mensaje",
      "Log dev sin PII"
    ],
    "errores": [
      "Sin timeout",
      "Stack al usuario"
    ]
  },
  {
    "titulo": "AppSec móvil: no loguear PII ni tokens",
    "semana": 4,
    "horas": 5,
    "lectura": "OWASP MASVS logging",
    "evidencia": "projects/m20-movil/logging-policy.md",
    "objetivo": "Revisar print/debug; política de logs en dev vs release.",
    "porque": "Un logcat filtrado filtra tokens.",
    "conceptos": [
      "PII",
      "tokens",
      "crash reports"
    ],
    "pasos_extra": "logging-policy.md + grep prints de token en repo app.",
    "lectura_rows": [
      [
        "M18",
        "informe",
        "MASVS"
      ]
    ],
    "hecho": [
      "Política escrita",
      "Sin token en logs",
      "Commit limpieza si hubo"
    ],
    "errores": [
      "console.log(token)",
      "Sentry con PII"
    ]
  },
  {
    "titulo": "Firma Android y keystore fuera del repo",
    "semana": 5,
    "horas": 5,
    "lectura": "Android signing / iOS profiles",
    "evidencia": "projects/m20-movil/build-evidence.md (prep)",
    "objetivo": "Crear keystore local ignorado; documentar variables CI futuras.",
    "porque": "P3 requiere build instalable real.",
    "conceptos": [
      "keystore",
      "gradle signing"
    ],
    "pasos_extra": "build-evidence.md sección signing sin subir keystore.",
    "lectura_rows": [
      [
        "Docs",
        "release build",
        "—"
      ]
    ],
    "hecho": [
      "Keystore fuera git",
      "gitignore",
      "Doc comando"
    ],
    "errores": [
      "Keystore commiteado",
      "Password en gradle commiteado"
    ]
  },
  {
    "titulo": "Build release APK o artefacto",
    "semana": 5,
    "horas": 5,
    "lectura": "Release build oficial",
    "evidencia": "projects/m20-movil/build-evidence.md",
    "objetivo": "Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.",
    "porque": "Emulador no basta para P3.",
    "conceptos": [
      "release",
      "minify opcional"
    ],
    "pasos_extra": "Comando exacto, tamaño APK, device modelo en build-evidence.",
    "lectura_rows": [
      [
        "Ficha",
        "M20 P3",
        "—"
      ]
    ],
    "hecho": [
      "Artefacto generado",
      "Dispositivo real",
      "SHA commit"
    ],
    "errores": [
      "Solo debug",
      "API localhost"
    ]
  },
  {
    "titulo": "Release notes y demo cruzada con web",
    "semana": 5,
    "horas": 5,
    "lectura": "Paridad auth web/móvil",
    "evidencia": "projects/m20-movil/release-notes.md",
    "objetivo": "Notas versión; misma cuenta web y móvil ven mismas citas.",
    "porque": "Proyecto M20 demuestra canal móvil del CRM.",
    "conceptos": [
      "paridad",
      "demo"
    ],
    "pasos_extra": "release-notes.md + pasos demo 10 segundos del día citas.",
    "lectura_rows": [
      [
        "Ficha",
        "proyecto M20",
        "M17 web"
      ]
    ],
    "hecho": [
      "release-notes",
      "Demo cruzada documentada",
      "Mismas citas"
    ],
    "errores": [
      "Cuentas distintas sin explicar",
      "Datos mock"
    ]
  },
  {
    "titulo": "Cierre M20 — dominio y README proyecto",
    "semana": 5,
    "horas": 5,
    "lectura": "Repaso M20",
    "evidencia": "projects/m20-movil/README.md índice",
    "objetivo": "Verificar P1–P3, criterios dominio, enlaces evidencia.",
    "porque": "Cierras materia móvil antes de emprendimiento M22.",
    "conceptos": [
      "README",
      "dominio"
    ],
    "pasos_extra": "README con enlaces demo-login-lista, auth-storage, build-evidence. cierre-m20.md checklist ficha.",
    "lectura_rows": [
      [
        "Ficha",
        "M20-aplicaciones-moviles.md",
        "—"
      ]
    ],
    "hecho": [
      "README completo",
      "P1–P3",
      "Criterios con evidencia"
    ],
    "errores": [
      "README vacío",
      "Build solo emulador"
    ]
  }
]
""")

BODIES: dict[int, str] = {}
BODIES[1] = r"""
# L01 — Stack móvil y scaffold Agenda Ops

**~5.0 h · Semana 1**

Elige Flutter **o** RN y no mires atrás sin ADR.

## Objetivo

Scaffold app + `stack-movil.md` + enlace en `projects/m20-movil/README.md`.

## Pasos (hazlos en orden)

### 1. Decide stack (25 min)

Documenta por qué.

### 2. Scaffold (90–110 min)

App corre en emulador/dispositivo. Carpetas `lib/` o `src/`.

### 3. Evidencia (30 min)

README m20 apunta al repo/submódulo.

### 4. Commit

`docs(m20): l01 scaffold stack movil`
"""

BODIES[2] = r"""
# L02 — Pantalla login contra API staging

**~5.0 h · Semana 1**

Misma auth que la web: nada de mock eterno.

## Objetivo

Login UI → `POST /auth/login` staging/local documentado.

## Pasos (hazlos en orden)

### 1. Config API URL (30 min)

Flavor dev/staging. No hardcode prod secrets.

### 2. Pantalla login (90–110 min)

Email/password; maneja errores red.

### 3. Commit

`feat(m20): l02 login contra api`
"""

BODIES[3] = r"""
# L03 — Secure storage de token o sesión

**~5.0 h · Semana 1**

Keychain/Keystore — no SharedPreferences en claro.

## Objetivo

`auth-storage.md` + implementación secure storage.

## Pasos (hazlos en orden)

### 1. Elige API (30 min)

flutter_secure_storage / Keychain RN.

### 2. Implementa (80–100 min)

Guarda/lee/borra token. Nunca loguees el valor.

### 3. Doc (20 min)

### 4. Commit

`feat(m20): l03 secure storage`
"""

BODIES[4] = r"""
# L04 — Errores de validación y flujo 401

**~5.0 h · Semana 1**

401 → limpiar storage y volver a login.

## Objetivo

Interceptor/wrapper HTTP con 401 global; mensajes de validación legibles.

## Pasos (hazlos en orden)

### 1. Interceptor (70–90 min)

### 2. Prueba (40 min)

Token inválido fuerza login. Evidencia en checklist.

### 3. Commit

`feat(m20): l04 flujo 401`
"""

BODIES[5] = r"""
# L05 — Lista de citas autenticada

**~5.0 h · Semana 2**

P1: lista real del día/negocio.

## Objetivo

Pantalla lista con `Authorization`/cookie según API; datos seed visibles.

## Pasos (hazlos en orden)

### 1. Fetch lista (90–110 min)

### 2. UI fila cita (40 min)

Hora, cliente, estado.

### 3. Commit

`feat(m20): l05 lista citas`
"""

BODIES[6] = r"""
# L06 — Pull-to-refresh y paginación simple

**~5.0 h · Semana 2**

El dueño tira hacia abajo para ver el día actualizado.

## Objetivo

Refresh gestual + paginación o “cargar más” si la API lo soporta.

## Pasos (hazlos en orden)

### 1. Refresh (50–60 min)

### 2. Paginación (60–80 min)

Si no hay cursor API: documenta límite y TODO.

### 3. Commit

`feat(m20): l06 refresh paginacion`
"""

BODIES[7] = r"""
# L07 — Estados de carga en lista

**~5.0 h · Semana 2**

Loading/error/vacío también en móvil.

## Objetivo

Tres estados implementados; capturas en evidencia P2 parcial.

## Pasos (hazlos en orden)

### 1. Estados (90–110 min)

### 2. Capturas (30 min)

### 3. Commit

`feat(m20): l07 estados carga lista`
"""

BODIES[8] = r"""
# L08 — Roles: confiar en la API, no solo en UI

**~5.0 h · Semana 2**

Ocultar botón ≠ autorización.

## Objetivo

Staff no ejecuta acción owner aunque parchee la UI; demo + nota.

## Pasos (hazlos en orden)

### 1. Lee rol de `/me` (40 min)

### 2. UI condicional + prueba API (80–100 min)

Forzar llamada staff a endpoint owner → 403 manejado.

### 3. Commit

`feat(m20): l08 roles confiar api`
"""

BODIES[9] = r"""
# L09 — Pantalla detalle de cita

**~5.0 h · Semana 3**

Tap en fila → detalle con datos API.

## Objetivo

Detalle: cliente, servicio, estado, notas (escapadas).

## Pasos (hazlos en orden)

### 1. Ruta detalle (90–110 min)

### 2. 404/403 UX (30 min)

### 3. Commit

`feat(m20): l09 detalle cita`
"""

BODIES[10] = r"""
# L10 — Navegación: tabs o drawer mínimo

**~5.0 h · Semana 3**

Agenda / Clientes (opcional) / Ajustes-logout.

## Objetivo

Navegación mínima usable con una mano.

## Pasos (hazlos en orden)

### 1. Tabs/drawer (90–110 min)

### 2. Logout accesible (30 min)

### 3. Commit

`feat(m20): l10 navegacion tabs`
"""

BODIES[11] = r"""
# L11 — Acciones permitidas: cancelar / atendida

**~5.0 h · Semana 3**

Mutaciones con confirmación y manejo 403.

## Objetivo

Cambiar estado desde móvil respetando matriz.

## Pasos (hazlos en orden)

### 1. Acciones (100–120 min)

Confirm dialog. Optimistic UI opcional + rollback.

### 2. Prueba roles (30 min)

### 3. Commit

`feat(m20): l11 acciones estado cita`
"""

BODIES[12] = r"""
# L12 — Deep link opcional a una cita

**~5.0 h · Semana 3**

Opcional pero útil: `agendaops://citas/:id`.

## Objetivo

Deep link documentado **o** N/A con justificación en README.

## Pasos (hazlos en orden)

### 1. Decide (20 min)

### 2. Implementa o N/A (90–110 min)

### 3. Commit

`feat(m20): l12 deep link cita`
"""

BODIES[13] = r"""
# L13 — Lista vacía con copy útil

**~5.0 h · Semana 4**

“No hay citas” + CTA, no pantalla muerta.

## Objetivo

Empty state con copy del design partner (agendar primera cita).

## Pasos (hazlos en orden)

### 1. Copy (30 min)

### 2. UI (70–90 min)

### 3. Commit

`feat(m20): l13 empty state`
"""

BODIES[14] = r"""
# L14 — Sin red: banner y reintento

**~5.0 h · Semana 4**

Modo avión no debe colgar la app.

## Objetivo

Banner offline + botón reintentar.

## Pasos (hazlos en orden)

### 1. Detecta conectividad (50 min)

### 2. UX (70–90 min)

### 3. Commit

`feat(m20): l14 offline banner`
"""

BODIES[15] = r"""
# L15 — Timeout, 5xx y mensajes humanos

**~5.0 h · Semana 4**

Timeouts explícitos; “servidor no disponible” > stacktrace.

## Objetivo

Timeouts HTTP + mensajes mapeados; sin filtrar detalles internos.

## Pasos (hazlos en orden)

### 1. Timeouts (40 min)

### 2. Mapeo errores (70–90 min)

### 3. Commit

`feat(m20): l15 timeouts mensajes`
"""

BODIES[16] = r"""
# L16 — AppSec móvil: no loguear PII ni tokens

**~5.0 h · Semana 4**

MASVS logging: nada de tokens en Logcat.

## Objetivo

`docs/logging-policy.md` + grep limpio de logs sensibles.

## Pasos (hazlos en orden)

### 1. Política (30 min)

### 2. Audita logs (80–100 min)

Quita prints de responses con PII.

### 3. Commit

`fix(m20): l16 no log pii tokens`
"""

BODIES[17] = r"""
# L17 — Firma Android y keystore fuera del repo

**~5.0 h · Semana 5**

Keystore ≠ git.

## Objetivo

Keystore local + `.gitignore`; doc de firmado en `build-evidence.md` borrador.

## Pasos (hazlos en orden)

### 1. Genera keystore (50–60 min)

### 2. Config signing (70–90 min)

Sin passwords en repo.

### 3. Commit

`docs(m20): l17 keystore fuera repo`
"""

BODIES[18] = r"""
# L18 — Build release APK o artefacto

**~5.0 h · Semana 5**

P3: artefacto instalable.

## Objetivo

APK/AAB (o IPA si aplica) + comandos en `build-evidence.md`.

## Pasos (hazlos en orden)

### 1. Build release (100–130 min)

### 2. Instala en dispositivo real (40 min)

### 3. Commit

`build(m20): l18 release artifact`
"""

BODIES[19] = r"""
# L19 — Release notes y demo cruzada con web

**~5.0 h · Semana 5**

Misma cuenta: web y móvil ven las mismas citas.

## Objetivo

`demo-login-lista.md` + release notes; paridad auth demostrada.

## Pasos (hazlos en orden)

### 1. Demo cruzada (80–100 min)

Crea cita en web → aparece en app (refresh).

### 2. Release notes (40 min)

### 3. Commit

`docs(m20): l19 demo cruzada release notes`
"""

BODIES[20] = r"""
# L20 — Cierre M20 — dominio y README proyecto

**~5.0 h · Semana 5**

Cierra P1–P3 y criterios de dominio móvil.

## Objetivo

README índice + autoevaluación dominio + enlace artefacto.

## Pasos (hazlos en orden)

### 1. Auditoría (50 min)

### 2. Criterios dominio (50–60 min)

### 3. README final (30 min)

### 4. Commit

`docs(m20): l20 cierre dominio`
"""

