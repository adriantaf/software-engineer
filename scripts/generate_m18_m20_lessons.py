#!/usr/bin/env python3
"""Generate M01-style lesson markdown for M18–M20 (AppSec, DevOps, Móvil)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_m10_m13_lessons import _lesson, write_materia  # noqa: E402

PROJ18 = "projects/m18-appsec"
PROJ19 = "projects/m19-ops"
PROJ20 = "projects/m20-movil"
API = "tu API de Agenda Ops (repo M17)"


def _rows(*pairs: tuple[str, str, str]) -> list[tuple[str, str, str]]:
    return list(pairs)


def _m18() -> list[dict]:
    lessons: list[dict] = []

    def add(
        titulo: str,
        semana: int,
        lectura: str,
        evidencia: str,
        objetivo: str,
        porque: str,
        conceptos: list[str],
        pasos_extra: str,
        lectura_rows: list[tuple[str, str, str]],
        hecho: list[str],
        errores: list[str],
    ) -> None:
        lessons.append(
            _lesson(
                titulo,
                semana,
                lectura,
                evidencia,
                objetivo,
                porque,
                conceptos,
                pasos_extra,
                lectura_rows,
                hecho,
                errores,
            )
        )

    # --- Semana 1: STRIDE ---
    add(
        "Activos, actores y datos sensibles en Agenda Ops",
        1,
        "OWASP Threat Modeling (overview) + notas STRIDE",
        f"{PROJ18}/threat-model-v0.md sección Activos",
        "Inventariar actores (dueño, staff, cliente final, atacante) y activos (PII, credenciales, citas, tokens, Postgres) del piloto Agenda Ops.",
        "Sin lista de activos, el threat model es decoración. Esta lección arranca P1 y el hilo OWASP del módulo.",
        [
            "Actor vs rol en el sistema.",
            "PII en citas (nombre, teléfono, notas).",
            "Superficie: panel web + API REST.",
            "Supuesto: solo atacas **tu** staging/local.",
        ],
        f"""```bash
mkdir -p {PROJ18}
```

En `threat-model-v0.md` crea tablas **Actores** y **Activos** (≥5 activos). Dibuja un diagrama caja-flecha: navegador → API → Postgres. Marca qué datos salen en JSON de `/api/citas`.

```bash
git ls-files | rg -i 'env|secret|credential|\\.pem' || true
```

Anota el resultado en el mismo archivo (sin pegar secretos).""",
        _rows(
            ("OWASP", "Threat Modeling (ES/overview)", "Cheat Sheet STRIDE"),
            ("Plan", "[producto-saas.md](../../../producto-saas.md)", "M13 trust boundaries"),
        ),
        [
            f"Existe `{PROJ18}/threat-model-v0.md` con actores y ≥5 activos.",
            "Diagrama ASCII o Mermaid del piloto.",
            "Comando anti-secretos ejecutado y anotado.",
        ],
        ["Activos genéricos (“la DB”) sin tablas/campos.", "Omitir al cliente final como fuente de datos."],
    )
    add(
        "Trust boundaries y flujos de confianza",
        1,
        "STRIDE por boundary + M13 `trust-boundaries`",
        f"{PROJ18}/trust-boundaries-appsec.md",
        "Dibujar límites de confianza (browser, API, DB, integraciones futuras) y etiquetar protocolo + datos que cruzan cada límite.",
        "M10 y M13 ya nombraron boundaries; hoy los operacionalizas para amenazas AppSec.",
        ["Zona de confianza vs desconfianza.", "Datos en tránsito vs en reposo.", "Admin vs tenant (futuro)."],
        f"""Abre `projects/m13-diseno/trust-boundaries.md` si existe. Copia o enlaza y extiende en `{PROJ18}/trust-boundaries-appsec.md`.

Por cada límite documenta: **origen**, **destino**, **protocolo**, **autenticación**, **datos**. Mínimo 4 límites (ej. browser→API, API→Postgres, API→SMTP futuro, operador→hosting).

Para cada límite escribe una pregunta “¿qué pasa si el atacante controla este lado?”""",
        _rows(("M13", "trust-boundaries", "M10 amenazas de red"), ("OWASP", "STRIDE en boundaries", "—")),
        ["≥4 boundaries documentados.", "Pregunta de abuso por límite.", "Enlace a diseño M13 si aplica."],
        ["Un solo boundary “internet”.", "Ignorar Postgres como activo interno."],
    )
    add(
        "STRIDE aplicado al CRM de citas",
        1,
        "STRIDE cheat sheet (una categoría por componente)",
        f"{PROJ18}/stride-matrix.md",
        "Completar una matriz STRIDE (Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation) sobre login, citas y panel admin de Agenda Ops.",
        "La matriz obliga a nombrar amenazas antes de buscar exploits al azar.",
        ["Spoofing en login.", "Tampering en `PUT /api/citas`.", "IDOR como Information Disclosure."],
        f"""Crea `{PROJ18}/stride-matrix.md` con filas: **Login**, **Lista citas**, **Detalle cita**, **Admin usuarios** (si existe).

Columnas STRIDE: marca S/T/R/I/D/E con una frase concreta (no “hackeo”). Ejemplo fila Login / Spoofing: “fuerza bruta o credenciales robadas”.

Prioriza 3 celdas rojas que atacarás en las próximas semanas.""",
        _rows(("OWASP", "STRIDE", "Top 10 overview ES")),
        ["Matriz ≥4 filas × 6 columnas.", "≥3 amenazas priorizadas.", "Lenguaje del dominio Agenda Ops."],
        ["Copiar tabla de blog sin adaptar.", "Dejar celdas vacías con ‘N/A’ en todo."],
    )
    add(
        "Threat model v0 y lectura OWASP Top 10",
        1,
        "OWASP Top 10 (2021) — lectura completa en español",
        f"{PROJ18}/owasp-top10-map.md",
        "Mapear cada categoría del OWASP Top 10 a un endpoint o pantalla concreta de Agenda Ops (aunque aún no tengas el bug).",
        "Cierras la semana 1 con backlog de riesgo alineado al estándar de la industria.",
        ["A01 Broken Access Control.", "A03 Injection.", "A07 Identification and Authentication Failures."],
        f"""En `{PROJ18}/owasp-top10-map.md` tabla: **OWASP id**, **Ejemplo en Agenda Ops**, **Mitigación prevista**, **Semana M18**.

Añade en `threat-model-v0.md` sección **Riesgo residual semana 1** (3 bullets).

Relee la ficha M18: confirma que P1 (threat model v1) llegará tras semana 2 auth.""",
        _rows(("OWASP", "Top 10 ES", "Cheat Sheets índice")),
        ["Mapa 10 filas mínimo.", "threat-model-v0 actualizado.", "Commit semana 1."],
        ["Marcar ‘no aplica’ en todo.", "Atacar sitios que no controlas."],
    )

    # --- Semana 2: Auth ---
    add(
        "Inventario de autenticación actual",
        2,
        "OWASP A07 + Authentication Cheat Sheet",
        f"{PROJ18}/auth-inventory.md",
        "Documentar flujo real de registro/login/logout de Agenda Ops: transporte, almacenamiento de sesión, rotación y recuperación de contraseña.",
        "No puedes endurecer lo que no has descrito. Esta lección es fotografía del estado antes de parches.",
        ["Credencial vs sesión vs token.", "Transporte HTTPS obligatorio.", "Mensajes de error uniformes."],
        f"""En `{PROJ18}/auth-inventory.md` describe paso a paso el happy path y 2 edge cases (password malo, usuario inexistente).

Captura (sin secretos) qué cookie/header usa la API. ¿El ID de usuario va en JWT payload? ¿Sesión en DB?

Lista endpoints: `POST /auth/login`, etc. Marca cuáles son públicos vs autenticados.""",
        _rows(("OWASP", "A07 + Auth Cheat Sheet", "M10 cookies/sesiones")),
        ["Inventario con endpoints reales.", "Público vs autenticado claro.", "Sin passwords en el doc."],
        ["Inventario teórico sin abrir el código.", "Loguear tokens en dev."],
    )
    add(
        "Hashing de contraseñas con bcrypt o argon2",
        2,
        "Password Storage Cheat Sheet",
        f"commit en repo producto + nota en {PROJ18}/auth-hashing.md",
        "Verificar o implementar hashing con coste adecuado (bcrypt≥12 o argon2) y eliminar esquemas débiles (MD5/SHA plano).",
        "A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.",
        ["Salt automático.", "Cost factor / memoria argon2.", "Nunca loguear `plain` password."],
        f"""Audita el servicio de registro/login en {API}. Si hay `bcrypt`/`argon2`, documenta parámetros en `{PROJ18}/auth-hashing.md`.

Si falta: implementa con lib madura, migra usuarios de prueba, añade test que el hash no es igual al plain.

```bash
# en repo producto
npm test -- --testPathPattern=auth 2>/dev/null || npm test
```""",
        _rows(("OWASP", "Password Storage", "Ejemplo ficha M18")),
        ["Hashing correcto en código o ADR si ya estaba.", "Test o script que verifica compare.", "Doc de parámetros."],
        ["MD5/SHA1 para passwords.", "Cost 4 ‘para ir rápido’."],
    )
    add(
        "Sesiones server-side vs JWT en Agenda Ops",
        2,
        "Session Management + JWT Cheat Sheets",
        f"{PROJ18}/adr-sesion-vs-jwt.md (o enlace ADR M13)",
        "Decidir y documentar si Agenda Ops usa sesión en servidor, JWT firmado, o híbrido; consecuencias para XSS, logout y revocación.",
        "M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.",
        ["Revocación inmediata.", "HttpOnly cookie vs Authorization header.", "Refresh token (si aplica)."],
        f"""Redacta `{PROJ18}/adr-sesion-vs-jwt.md`: contexto, decisión, alternativas rechazadas, impacto en móvil M20.

Prueba manual: login → copiar token/cookie → logout → reutilizar credencial vieja (debe fallar).

Anota resultado en la ADR.""",
        _rows(("M13", "adr/005-auth si existe", "M10 L14 sesiones")),
        ["ADR con alternativas.", "Prueba logout/reuse documentada.", "Coherente con móvil futuro."],
        ["JWT en localStorage sin plan anti-XSS.", "Sin estrategia de revocación."],
    )
    add(
        "Threat model v1 post-autenticación (P1)",
        2,
        "Repaso STRIDE semanas 1–2",
        f"{PROJ18}/threat-model-v1.md",
        "Actualizar threat model con flujos de auth reales y marcar controles implementados vs pendientes.",
        "P1 exige v1 revisado tras entender login; hoy entregas el hito.",
        ["Control vs amenaza.", "Gap analysis.", "Priorización por explotabilidad."],
        f"""Copia `threat-model-v0.md` → `threat-model-v1.md`. Añade sección **Controles auth** (hashing, cookies, rate limit planificado).

Tabla: Amenaza | Control | Estado (OK/TODO) | Issue/commit.

Checklist P1 de la ficha: confirma que un revisor podría seguir el doc sin abrir el código.""",
        _rows(("Ficha", "M18-seguridad.md P1", "—")),
        ["threat-model-v1.md completo.", "Tabla amenaza-control.", "Listo para marcar P1 en UI."],
        ["Renombrar v0 sin cambios.", "Omitir auth en el modelo."],
    )

    # --- Semana 3: CSRF / cookies ---
    add(
        "Cookies Secure, HttpOnly y SameSite",
        3,
        "OWASP Session Management + cookie flags",
        f"{PROJ18}/cookies-lab.md",
        "Inspeccionar cookies de sesión de Agenda Ops en DevTools y verificar flags; corregir configuración en el servidor.",
        "M10 estudió cookies; hoy aplicas flags en **tu** stack.",
        ["SameSite=Lax/Strict.", "Secure en HTTPS.", "HttpOnly vs JS legítimo."],
        f"""Login en staging/local. En `{PROJ18}/cookies-lab.md` tabla: nombre cookie, flags, lifetime, path.

Si falta `Secure` o `HttpOnly` en cookie de sesión, parchea middleware/framework y captura antes/después (sin valor de cookie).

Prueba: ¿JavaScript puede leer la cookie de sesión? Documenta.""",
        _rows(("MDN", "Set-Cookie", "M10 L13")),
        ["Tabla de cookies real.", "Parche o justificación documentada.", "Prueba HttpOnly."],
        ["SameSite=None sin Secure.", "Cookie de sesión accesible desde JS."],
    )
    add(
        "CSRF en formularios y mutaciones state-changing",
        3,
        "CSRF Prevention Cheat Sheet",
        f"fix + {PROJ18}/csrf-notes.md",
        "Identificar operaciones mutables (POST/PUT/DELETE) y aplicar token CSRF, SameSite estricto o patrón equivalente en Agenda Ops.",
        "Un atacante no necesita XSS si tu sesión acepta POST cross-site.",
        ["Double-submit cookie (si aplica).", "Token sincronizado.", "API JSON + CORS no sustituye CSRF en cookies."],
        f"""Lista rutas que cambian estado (crear cita, cancelar, perfil). En `{PROJ18}/csrf-notes.md` indica protección por ruta.

Implementa protección mínima en la ruta más crítica (ej. crear cita). Test manual con `curl` sin token (debe 403).

Referencia OWASP CSRF sheet en el doc.""",
        _rows(("OWASP", "CSRF Prevention", "M10 CORS")),
        ["Lista rutas mutables.", "≥1 ruta protegida.", "curl sin token falla."],
        ["Confiar solo en CORS.", "GET que borra datos."],
    )
    add(
        "Fijación de sesión y logout completo",
        3,
        "Session fixation + logout best practices",
        f"{PROJ18}/session-lifecycle.md",
        "Asegurar rotación de ID de sesión tras login y destrucción server-side en logout.",
        "Robar sesión fija es un clásico en apps que reutilizan el mismo session id.",
        ["Regenerar session id post-auth.", "Invalidar en logout.", "Timeout por inactividad (idea)."],
        f"""Traza el ciclo en código. Documenta en `{PROJ18}/session-lifecycle.md`.

Pruebas: login dos veces ¿cambia id? logout ¿cookie inválida en siguiente request?

Si usas JWT stateless, documenta blacklist/short TTL en su lugar.""",
        _rows(("OWASP", "Session Management", "Auth cheat sheet")),
        ["Doc ciclo de vida.", "Pruebas login/logout documentadas.", "Commit si hubo fix."],
        ["Logout solo borra cookie cliente.", "Session id pre-login reutilizado."],
    )
    add(
        "Checklist cookies y CSRF en staging",
        3,
        "Repaso semana 3",
        f"{PROJ18}/checklist-cookies-csrf.md",
        "Checklist binario ejecutable antes de cada deploy: cookies, CSRF, HTTPS, logout.",
        "Operacionalizas controles para M19 deploy y trials M22.",
        ["Checklist reproducible.", "Evidencia en staging."],
        f"""Crea `{PROJ18}/checklist-cookies-csrf.md` con ≥10 ítems Sí/No. Ejecútalo contra staging y pega resultado (fecha, URL).

Enlaza issues/commits de la semana. Cierra con riesgo residual CSRF.""",
        _rows(("Ficha", "M18 semana 3", "M19 ambientes futuro")),
        ["Checklist ejecutado.", "Fecha y URL.", "≥1 ítem corregido esta semana."],
        ["Checklist nunca ejecutado.", "Marcar todo Sí sin prueba."],
    )

    # --- Semana 4: Injection ---
    add(
        "SQLi: reproducir en tu propia API",
        4,
        "OWASP A03 Injection + SQLi Prevention",
        f"{PROJ18}/findings/001-sqli.md",
        "Encontrar al menos un punto susceptible (búsqueda, filtro, orden) y demostrar SQLi controlada en local/staging **sin** dañar datos reales.",
        "P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.",
        ["Consulta concatenada vs parametrizada.", "Error verbose vs genérico.", "Principio de mínimo privilegio DB."],
        f"""Usa cuenta de prueba. Intenta payloads en query params/body (`' OR '1'='1` etc.) en endpoints de búsqueda de clientes/citas.

Documenta en `{PROJ18}/findings/001-sqli.md`: endpoint, payload, respuesta, impacto. **No** pegues datos de clientes reales.

Si no hay SQLi, documenta por qué (ORM parametrizado) y prueba bypass conocido del ORM.""",
        _rows(("OWASP", "SQL Injection", "ORM docs de tu stack")),
        ["Finding documentado o prueba de mitigación.", "Solo tu entorno.", "Sin PII en el reporte."],
        ["SQLi en producción de terceros.", "Drop table en staging compartido."],
    )
    add(
        "Mitigar SQLi: queries parametrizadas y permisos DB",
        4,
        "SQLi Prevention Cheat Sheet",
        "commit fix + test en repo producto",
        "Corregir el vector SQLi (o endurecer consulta) y añadir test de regresión que falle si vuelve la concatenación.",
        "Hallazgo sin fix no cuenta para P2.",
        ["Prepared statements.", "Validación de entrada en frontera.", "Usuario DB sin DDL."],
        f"""Implementa fix en {API}. Test automatizado: input malicioso → 400 o resultado vacío, nunca error SQL expuesto.

Actualiza `001-sqli.md` con commit hash y captura de test verde.""",
        _rows(("OWASP", "SQLi Prevention", "Tests M15 si aplica")),
        ["Commit fix.", "Test de regresión.", "Finding actualizado a Cerrado."],
        ["Escapar manualmente sin parametrizar.", "Silenciar error sin arreglar query."],
    )
    add(
        "XSS reflejado en campos de cliente o búsqueda",
        4,
        "XSS Prevention Cheat Sheet",
        f"{PROJ18}/findings/002-xss-reflected.md",
        "Probar XSS reflejado en un campo que se renderiza (nombre, mensaje de error) y documentar contexto HTML/JS.",
        "XSS roba sesiones si las cookies son legibles por JS.",
        ["Reflejado vs almacenado.", "Contexto de escape.", "Content-Type correcto."],
        f"""Payloads: `<script>alert(1)</script>`, event handlers. En `{PROJ18}/findings/002-xss-reflected.md` indica pantalla y si el navegador ejecutó (en tu cuenta de prueba).

No uses payloads que exfiltruen a dominios externos; solo demuestra impacto local.""",
        _rows(("OWASP", "XSS Prevention", "CSP intro semana 7")),
        ["PoC documentada.", "Contexto identificado.", "Sin atacar usuarios reales."],
        ["XSS persistente en prod sin aviso.", "Confiar en ‘React escapa todo’."],
    )
    add(
        "XSS almacenado y escape en plantillas/API",
        4,
        "DOM XSS + stored XSS",
        "commit fix + findings/002 actualizado",
        "Mitigar XSS (escape, sanitización acotada, CSP futura) en el flujo almacenado (notas de cita, perfil).",
        "El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.",
        ["Sanitizar HTML vs texto plano.", "JSON no implica seguro en `dangerouslySetInnerHTML`.", "Headers X-Content-Type-Options."],
        f"""Si hay notas/comentarios en citas, prueba almacenamiento. Fix en template/API. Test: payload guardado se muestra escapado.

Tabla P2 en `{PROJ18}/findings-table.md` con filas SQLi + XSS (hallazgo → PoC → commit → test).""",
        _rows(("OWASP", "XSS Prevention", "MDN textContent")),
        ["≥2 filas en findings-table.", "Fix committed.", "Test o verificación manual repetible."],
        ["strip_tags inventado.", "innerHTML con input usuario."],
    )

    # --- Semana 5: Access control ---
    add(
        "IDOR en citas y recursos por ID",
        5,
        "OWASP A01 Broken Access Control",
        f"{PROJ18}/findings/003-idor.md",
        "Demostrar acceso cross-user a `GET/PUT /api/citas/:id` (u otro recurso) con dos cuentas de prueba.",
        "El ejemplo de la ficha M18: ocultar botones no basta.",
        ["Autorización server-side.", "ID predecible.", "UUID no es autorización."],
        f"""Crea usuario A y B. A crea cita. B intenta leer/editar ID de A. Documenta en `003-idor.md`.

Si ya está protegido, muestra test automatizado que falla si quitas el check.""",
        _rows(("OWASP", "A01", "Ejemplo IDOR ficha M18")),
        ["PoC con dos usuarios.", "Impacto descrito.", "Ruta exacta."],
        ["Probar en datos de design partner real.", "Autorización solo en front."],
    )
    add(
        "Autorización por rol owner vs staff",
        5,
        "Access Control Cheat Sheet",
        f"{PROJ18}/rbac-matrix.md",
        "Matriz rol × recurso × acción para Agenda Ops y gaps entre SRS y código.",
        "Agenda Ops distingue dueño y staff; la API debe hacerlo explícito.",
        ["RBAC vs ABAC (idea).", "403 vs 404.", "Principio mínimo privilegio."],
        f"""`{PROJ18}/rbac-matrix.md`: filas citas, clientes, configuración; columnas owner/staff/anónimo.

Prueba un caso staff que no debe ver citas de otro tenant (futuro) o acción admin. Registra resultado.""",
        _rows(("SRS", "M12 roles", "OWASP A01")),
        ["Matriz completa.", "≥1 prueba manual rol.", "Gaps listados."],
        ["Un solo rol ‘admin’.", "404 para esconder sin authz."],
    )
    add(
        "Rate limiting en login y endpoints sensibles",
        5,
        "Brute Force + Rate Limiting Cheat Sheets",
        "commit middleware + nota en findings",
        "Implementar límite de intentos (IP o cuenta) en login y al menos un endpoint costoso.",
        "Sin rate limit, A07 y A04 (DoS ligero) son triviales.",
        ["Ventana fija vs token bucket (idea).", "429 Too Many Requests.", "No bloquear legítimos sin UX."],
        f"""Añade rate limit (lib o reverse proxy local). Prueba 20 intentos fallidos login → bloqueo temporal.

Documenta configuración y cómo resetear en dev.""",
        _rows(("OWASP", "Brute Force", "M11 recursos")),
        ["Rate limit activo.", "Prueba documentada.", "Mensaje usuario claro."],
        ["Rate limit solo en front.", "Bloqueo permanente sin unlock."],
    )
    add(
        "Tests automatizados cross-user (P2 avance)",
        5,
        "Testing access control",
        f"tests en repo producto + {PROJ18}/findings-table.md",
        "Escribir ≥2 tests: usuario A no lee/edita recurso de B; rol staff no ejecuta acción de owner.",
        "P2 pide tabla hallazgo→fix→test; hoy consolidas access control.",
        ["Fixture dos usuarios.", "Arrange-Act-Assert.", "401 vs 403 semántica."],
        f"""```bash
# ejemplo nombre
npm test -- --testPathPattern=authz
```

Actualiza findings-table con IDOR y RBAC. Mínimo 5 hallazgos totales en P2 al cerrar M18 — planifica los que faltan.""",
        _rows(("Ficha", "M18 P2", "M15 testing")),
        ["≥2 tests authz verdes.", "findings-table ≥3 filas.", "Commits referenciados."],
        ["Tests que mockean auth siempre true.", "Un solo usuario en tests."],
    )

    # --- Semana 6: SSRF / upload / deser ---
    add(
        "SSRF: superficie en webhooks e integraciones",
        6,
        "SSRF Prevention Cheat Sheet",
        f"{PROJ18}/findings/004-ssrf.md",
        "Identificar si Agenda Ops (o roadmap) acepta URLs server-side (webhook, import, avatar remoto) y evaluar riesgo SSRF.",
        "Aun sin feature, documentar el control evita sorpresas en M26 integraciones.",
        ["Allowlist de hosts.", "Bloquear metadata IP.", "No reutilizar cliente HTTP sin validar."],
        f"""Si no hay feature URL, simula diseño en `004-ssrf.md`: qué pasaría con `http://169.254.169.254`. Define allowlist propuesta.

Si hay fetch server-side, prueba URL interna en staging aislado.""",
        _rows(("OWASP", "SSRF", "—")),
        ["Doc SSRF con allowlist.", "Riesgo nombrado.", "Sin escanear terceros."],
        ["curl a metadata cloud en prod.", "SSRF ‘para probar AWS’ en cuenta ajena."],
    )
    add(
        "Subida de archivos segura",
        6,
        "File Upload Cheat Sheet",
        f"{PROJ18}/findings/005-upload.md",
        "Revisar o diseñar upload (logo, adjunto) con validación tipo/tamaño, almacenamiento fuera de webroot y nombres aleatorios.",
        "Un .php disfrazado de .jpg es folklore porque sigue pasando.",
        ["MIME sniffing.", "Tamaño máximo.", "Escaneo opcional."],
        f"""Si el piloto no sube archivos, redacta checklist de aceptación en `005-upload.md` para cuando exista.

Si sube: prueba archivo malicioso en staging, verifica que no se sirve como script.""",
        _rows(("OWASP", "File Upload", "—")),
        ["Checklist o prueba real.", "Ruta almacenamiento.", "Sin ejecución de uploads."],
        ["Guardar en `public/` con nombre usuario.", "Confiar en extensión."],
    )
    add(
        "Deserialización y JSON peligroso",
        6,
        "Deserialization + API hardening",
        f"{PROJ18}/json-trust.md",
        "Auditar parsers JSON, `eval`, plantillas dinámicas y tipos inesperados en body de API.",
        "Node/TS rara vez hace Java deserialization, pero prototype pollution y lógica sí.",
        ["Validación schema (zod/joi).", "Prototype pollution (idea).", "Tamaño body limit."],
        f"""`{PROJ18}/json-trust.md`: lista endpoints con body JSON; schema sí/no. Añade límite `express.json({{ limit: '100kb' }})` o equivalente.

Prueba payload enorme o campos extra; documenta comportamiento.""",
        _rows(("OWASP", "API Security Top 10", "Input validation")),
        ["Lista endpoints + validación.", "Límite tamaño body.", "≥1 mejora commitada."],
        ["Aceptar cualquier JSON.", "Confiar en tipos TS solo compile-time."],
    )
    add(
        "Consolidar hallazgos semana 6 en P2",
        6,
        "Repaso findings",
        f"{PROJ18}/findings-table.md actualizado",
        "Asegurar ≥5 hallazgos con PoC, fix y test o verificación repetible; priorizar los de mayor impacto.",
        "Mitad del módulo: P2 debe ser visible en git.",
        ["Severidad.", "Estado.", "Regresión."],
        f"""Revisa tabla P2. Cada fila: ID, OWASP, PoC resumen, commit fix, test/link.

Abre issues para hallazgos abiertos con fecha objetivo semana 7–8.""",
        _rows(("Ficha", "M18 P2", "—")),
        ["≥5 filas completas o plan con 5.", "Commits enlazados.", "Ningún secreto en tabla."],
        ["Hallazgos duplicados.", "PoC sin fix planificado."],
    )

    # --- Semana 7: Secrets / deps / headers ---
    add(
        "npm audit y cadena de dependencias",
        7,
        "OWASP A06 Vulnerable Components",
        f"{PROJ18}/deps-audit.md",
        "Ejecutar auditoría de dependencias, triagear findings (prod vs dev), actualizar o documentar riesgo aceptado.",
        "Tu app hereda CVEs de `node_modules`.",
        ["Semver y lockfile.", "DevDependency vs runtime.", "Riesgo aceptado con fecha."],
        f"""```bash
cd <repo Agenda Ops>
npm audit --omit=dev 2>/dev/null || npm audit
```

Guarda salida en `{PROJ18}/deps-audit.md`. Arregla al menos 1 high/critical o documenta por qué no aplica.""",
        _rows(("OWASP", "A06", "npm audit docs")),
        ["Audit guardado.", "≥1 acción tomada.", "Fecha en doc."],
        ["`npm audit fix --force` sin leer.", "Ignorar todo."],
    )
    add(
        "Secretos, .env y rotación",
        7,
        "Secrets Management Cheat Sheet",
        f"{PROJ18}/secrets-rotation.md",
        "Verificar que secretos viven fuera de git; plan de rotación para JWT/session secret y DB.",
        "Un commit con `.env` es incidente permanente (historial).",
        ["`.gitignore`.", "Rotación sin downtime (idea).", "Pre-commit hooks."],
        f"""```bash
git log -p --all -S 'DATABASE_URL' | head -20
```

`{PROJ18}/secrets-rotation.md`: inventario (sin valores), dónde viven en local/staging, pasos rotar session secret.""",
        _rows(("OWASP", "Secrets", "M19 secrets-inventory")),
        ["Inventario sin valores.", "grep historial ejecutado.", "Plan rotación."],
        ["Pegar secretos en issue.", "Rotar sin probar logout."],
    )
    add(
        "Cabeceras de seguridad con Helmet o equivalente",
        7,
        "Security Headers Cheat Sheet",
        "commit headers + captura curl",
        "Configurar HSTS (si HTTPS), X-Frame-Options/ frame-ancestors, X-Content-Type-Options, Referrer-Policy.",
        "M10 L16 en tu código de producción.",
        ["Helmet middleware.", "HSTS solo con HTTPS estable.", "Clickjacking."],
        f"""```bash
curl -sI https://<tu-staging>/ | rg -i 'strict|frame|content-type|referrer'
```

Documenta antes/después en bitácora. No rompas el front (prueba login).""",
        _rows(("OWASP", "Secure Headers", "M10 L16")),
        ["Headers visibles en staging.", "Login sigue funcionando.", "Commit."],
        ["HSTS en localhost sin TLS.", "CSP rota todo sin reporte."],
    )
    add(
        "CSP básica sin romper Agenda Ops",
        7,
        "Content Security Policy Cheat Sheet",
        f"{PROJ18}/csp.md + commit opcional",
        "Diseñar política CSP mínima (default-src, script-src) y desplegar en report-only o estricta según tolerancia.",
        "CSP es red de seguridad ante XSS residual.",
        ["nonce vs hash.", "report-uri / report-to.", "inline scripts legacy."],
        f"""`{PROJ18}/csp.md`: política propuesta, fuentes externas que usa tu front (CDN, analytics futuro).

Implementa CSP report-only primero; anota violaciones en consola.""",
        _rows(("OWASP", "CSP", "MDN CSP")),
        ["Política escrita.", "Prueba report-only o estricta.", "Sin romper build."],
        ["`unsafe-inline` everywhere.", "CSP en meta sin HTTPS."],
    )

    # --- Semana 8: SDLC ---
    add(
        "Pipeline CI: lint, test, audit, anti-secretos",
        8,
        "Secure SDLC + CI guides",
        f"{PROJ18}/ci-appsec.yml snippet o enlace workflow",
        "Añadir job CI con lint, tests, `npm audit` (fail on high), grep básico anti-secretos.",
        "P3 de la ficha: seguridad en el pipeline, no solo en la cabeza.",
        ["Fail build on audit.", "Trufflehog/gitleaks lite.", "Branch protection (idea)."],
        f"""Crea o extiende workflow GitHub Actions / CI del repo. Documenta en `{PROJ18}/ci-appsec.md` qué corre en cada PR.

Ejecuta pipeline en branch de prueba y pega enlace/run id.""",
        _rows(("OWASP", "DevSecOps guideline", "Ficha P3")),
        ["CI documentado.", "Audit en pipeline.", "Run verde o excepciones justificadas."],
        ["CI que nunca falla.", "Secretos en workflow logs."],
    )
    add(
        "Estructura del informe AppSec",
        8,
        "Reporting + risk rating",
        f"{PROJ18}/informe-appsec.md (borrador)",
        "Redactar informe ejecutivo+técnico: alcance, metodología, hallazgos, mitigaciones, riesgo residual.",
        "El proyecto único de M18 es comunicable a un design partner técnico.",
        ["Alcance staging/prod.", "CVSS lite (opcional).", "Residual risk honesto."],
        f"""Plantilla en `informe-appsec.md`: Resumen, Metodología (OWASP+STRIDE), Tabla hallazgos, Recomendaciones, Anexo tests.

Enlaza `findings-table.md` y threat-model-v1.""",
        _rows(("Ficha", "proyecto M18", "—")),
        ["Borrador ≥4 secciones.", "Enlaces internos.", "Sin jerga vacía."],
        ["Informe sin hallazgos reales.", "Copiar OWASP sin contexto."],
    )
    add(
        "Tests de regresión de seguridad (≥3)",
        8,
        "Security unit tests patterns",
        "≥3 tests en repo producto",
        "Consolidar tests: authz cross-user, input malicioso, headers o rate limit — al menos tres automatizados.",
        "Sin tests, el hardening se erosiona en el próximo feature.",
        ["Regression suite.", "CI los ejecuta.", "Nombres claros."],
        f"""Lista tests en `{PROJ18}/security-tests.md` con archivo y qué protege.

Verifica que CI los corre. Añade uno si faltan.""",
        _rows(("Ficha", "M18 proyecto", "P2/P3")),
        ["≥3 tests listados.", "CI los ejecuta.", "Todos verdes."],
        ["Tests skipped.", "Solo manual."],
    )
    add(
        "Cierre M18 — dominio y riesgo residual",
        8,
        "Repaso completo M18",
        f"{PROJ18}/informe-appsec.md final + README",
        "Finalizar informe, verificar P1–P3, criterios de dominio y handoff a M19 (deploy seguro).",
        "Cierras la capa B de seguridad antes de exponer el piloto en internet.",
        ["Checklist pre-deploy.", "Handoff M19.", "Dominio M18 checklist."],
        f"""Actualiza `{PROJ18}/README.md` con índice de artefactos. Checklist ficha **Criterios de dominio** en `cierre-m18.md` con evidencia por ítem.

Escribe 5 bullets **qué NO cubriste** (ej. pentest externo, WAF) como residual risk.""",
        _rows(("Ficha", "M18-seguridad.md", "[Hilo seguridad](../../../hilos/seguridad.md)")),
        ["Informe final.", "P1–P3 verificables.", "README índice.", "Residual risk escrito."],
        ["Marcar dominio sin tests.", "Deploy público sin headers."],
    )

    return lessons


def _m19() -> list[dict]:
    lessons: list[dict] = []

    def add(*args, **kwargs):
        lessons.append(_lesson(*args, **kwargs))

    # Week 1 Docker
    add(
        "Inventario de secretos y ambientes staging/prod",
        1,
        "Docker docs — env vars + 12-factor",
        f"{PROJ19}/secrets-inventory.md + ambientes.md",
        "Crear inventario de secretos sin valores y definir URLs/objetivo de staging y prod para Agenda Ops.",
        "M19 empieza donde M18 dejó: nada de secretos en git antes de empaquetar.",
        ["DATABASE_URL", "SESSION_SECRET", "Stripe test futuro"],
        f"""```bash
mkdir -p {PROJ19}
git ls-files | rg -i '\\.env|secret|credential' || true
```

Completa `secrets-inventory.md` y `ambientes.md` según ficha M19.""",
        _rows(("Plan", "producto-saas.md", "M18 secrets")),
        ["Ambos archivos existen.", "Sin valores secretos.", "URLs objetivo anotadas."],
        ["Pegar JWT en markdown.", "Un solo ambiente ‘prod’."],
    )
    add(
        "Dockerfile multi-stage para la API",
        1,
        "Dockerfile best practices (oficial)",
        f"Dockerfile en repo + {PROJ19}/docker.md",
        "Escribir Dockerfile multi-stage: build TS/bundle y runtime slim sin devDependencies ni fuentes.",
        "Imagen pequeña y sin toolchain reduce superficie.",
        ["multi-stage", "USER node", "HEALTHCHECK"],
        f"""Implementa patrón de la ficha M19. Documenta comandos build en `{PROJ19}/docker.md`.

`.dockerignore`: node_modules, .git, .env.""",
        _rows(("Docker", "multi-stage", "M11 Docker")),
        ["Dockerfile multi-stage.", "docker.md con comandos.", ".dockerignore."],
        ["COPY .env", "root en runtime"],
    )
    add(
        "Compose prod-like: API + Postgres + volúmenes",
        1,
        "Compose file reference",
        f"compose.yml + {PROJ19}/docker.md",
        "Orquestar API y PostgreSQL con volúmenes persistentes, red interna y healthchecks.",
        "P1 M19 es stack local idéntico en espíritu a prod.",
        ["depends_on healthy", "volumen db-data", "puerto 5432 no publicado"],
        f"""`compose.yml`: servicios api, db; env desde `.env.example` sin secretos reales.

`docker compose up --build` documentado con tiempo de arranque y curl `/health`.""",
        _rows(("Docker", "Compose", "M11 compose")),
        ["Compose levanta stack.", "Healthcheck OK.", "Postgres con volumen."],
        ["5432:5432 público", "password en compose commiteado"],
    )
    add(
        "Stack local documentado y P1 Docker",
        1,
        "Repaso semana 1",
        f"{PROJ19}/docker.md completo",
        "Consolidar instrucciones un comando, troubleshooting y evidencia de login/cita en contenedores.",
        "Cierra semana 1 con P1 listo para marcar.",
        ["reproducibilidad", "logs compose"],
        f"""Añade sección Troubleshooting a docker.md. Captura `docker compose ps` y respuesta `/health`.

Smoke: crear cita desde UI contra stack dockerizado.""",
        _rows(("Ficha", "M19 P1", "—")),
        ["docker.md completo.", "Smoke test anotado.", "Commit P1."],
        ["Solo README vacío", "Imagen sin healthcheck"],
    )

    # Week 2 staging
    add(
        "ADR hosting: PaaS vs VPS",
        2,
        "Docs Fly/Railway/Render o VPS",
        f"{PROJ19}/adr-hosting.md",
        "Documentar decisión de hosting para Agenda Ops con criterios costo, TLS, Postgres gestionado, DX.",
        "Evitas re-decidir cada semana.",
        ["PaaS", "VPS+Docker", "egress y region"],
        f"""ADR con alternativas y consecuencias operativas (logs, secrets panel).""",
        _rows(("Ficha", "M19 semana 2", "—")),
        ["ADR firmada.", "Proveedor elegido.", "Riesgos listados."],
        ["Sin ADR", "Elegir solo por tutorial viejo"],
    )
    add(
        "Deploy staging con HTTPS",
        2,
        "Proveedor: deploy + TLS",
        f"{PROJ19}/deploy-log.md",
        "Desplegar staging con HTTPS forzado y variables en panel del host.",
        "Primera URL pública del piloto.",
        ["HTTP→HTTPS", "env vars", "build remoto"],
        f"""Registra URL, fecha, commit SHA en deploy-log. Secretos solo en panel.

curl -I staging URL.""",
        _rows(("Proveedor", "HTTPS docs", "M10 TLS")),
        ["URL HTTPS viva.", "deploy-log entrada.", "Sin secretos en repo."],
        ["HTTP plano", "TLS solo en front"],
    )
    add(
        "Smoke test: login, cita y health externo",
        2,
        "Runbook borrador",
        f"{PROJ19}/smoke-staging.md",
        "Ejecutar checklist smoke desde fuera de tu laptop: login, crear cita, GET /health.",
        "‘Contenedor verde’ ≠ producto usable.",
        ["smoke test", "datos prueba"],
        f"""Checklist binario en smoke-staging.md con capturas o salidas curl anonimizadas.""",
        _rows(("Ficha", "M19", "M17 API")),
        ["Smoke completo.", "health externo.", "Fecha registrada."],
        ["Solo health sin login", "Smoke nunca repetido"],
    )
    add(
        "Dominios y deploy-log semana 2",
        2,
        "DNS del proveedor",
        f"{PROJ19}/dominios.md",
        "Registrar subdominios staging (y prod planificado); enlazar con deploy-log.",
        "Trials M22 necesitan URL estable.",
        ["CNAME", "cert automático"],
        f"""dominios.md con registros y TTL. Verifica cert válido en navegador.""",
        _rows(("M10", "DNS", "—")),
        ["dominios.md", "Cert OK", "deploy-log actualizado"],
        ["IP directa sin nombre", "Cert expirado ignorado"],
    )

    # Week 3 prod
    add(
        "Promover configuración a producción",
        3,
        "12-factor config",
        f"{PROJ19}/ambientes.md actualizado",
        "Desplegar prod con misma imagen que staging y distintas env vars; documentar diferencias.",
        "Prod es para design partner, no laboratorio.",
        ["promoción imagen", "separación datos"],
        f"""Segunda entrada deploy-log prod. Tabla diff staging vs prod en ambientes.md.""",
        _rows(("Ficha", "M19 semana 3", "—")),
        ["Prod URL.", "Diff documentado.", "Datos separados."],
        ["Migrar en prod primero", "Misma DB staging/prod"],
    )
    add(
        "Logs, rollback y versión desplegada",
        3,
        "Runbook ops",
        f"{PROJ19}/runbook.md sección rollback",
        "Documentar dónde ver logs, cómo identificar versión y rollback a imagen/tag anterior.",
        "A las 11 p.m. solo cuenta el runbook.",
        ["rollback", "tag git", "logs PaaS"],
        f"""runbook.md: Rollback en ≤10 pasos numerados. Prueba rollback en staging si es seguro.""",
        _rows(("Proveedor", "logs", "—")),
        ["Rollback documentado.", "Versión en runbook.", "Prueba o simulacro."],
        ["Rollback ‘redeploy main’ sin tag", "Sin logs"],
    )
    add(
        "Monitoreo mínimo y alertas manuales",
        3,
        "Uptime básico",
        f"{PROJ19}/monitoring.md",
        "Configurar healthcheck externo o calendario de revisión manual; definir qué hacer si cae.",
        "No necesitas Datadog para el piloto; sí necesitas saber si está caído.",
        ["uptime", "on-call manual"],
        f"""monitoring.md: herramienta o ritual calendario + contacto. Enlaza /health prod.""",
        _rows(("Ficha", "M19", "—")),
        ["Monitoreo definido.", "Contacto.", "health prod"],
        ["Asumir siempre up", "Alertas sin acción"],
    )
    add(
        "Revisión seguridad: puertos, SSH y firewall",
        3,
        "M18 + M11 seguridad host",
        f"{PROJ19}/security-host.md",
        "Checklist puertos expuestos, SSH (clave, no password), firewall si VPS.",
        "Deploy sin postura de host revierte M18.",
        ["firewall", "SSH", "least privilege"],
        f"""security-host.md checklist. Si PaaS, documenta qué gestiona el proveedor vs tú.""",
        _rows(("Hilo", "seguridad", "M18")),
        ["Checklist completo.", "SSH seguro o N/A PaaS.", "Sin Postgres público."],
        ["SSH password root", "22 abierto al mundo sin necesidad"],
    )

    # Week 4 backup
    add(
        "Backup automático PostgreSQL",
        4,
        "pg_dump + proveedor backups",
        f"{PROJ19}/backup.md",
        "Automatizar pg_dump o backup gestionado; retención y ubicación segura.",
        "P3 sin backup es teatro.",
        ["pg_dump", "cron", "cifrado opcional"],
        f"""backup.md: script o procedimiento, frecuencia, dónde se guarda (sin credenciales).""",
        _rows(("PostgreSQL", "backup", "Proveedor docs")),
        ["Procedimiento escrito.", "Job programado o gestionado.", "Tamaño estimado."],
        ["Backup manual olvidado", "Dump en repo git"],
    )
    add(
        "Prueba de restore en entorno aislado",
        4,
        "Restore docs",
        f"{PROJ19}/restore-test.md",
        "Restaurar dump en DB de prueba, verificar citas visibles, registrar tiempo y resultado.",
        "Un restore nunca probado no cuenta.",
        ["restore", "RTO idea", "vacuum"],
        f"""restore-test.md: fecha, dump usado, duración, éxito/fallo, captura query count citas.""",
        _rows(("Ficha", "M19 P3", "—")),
        ["Restore real documentado.", "Verificación datos.", "Fecha."],
        ["Solo teoría", "Restore sobre prod"],
    )
    add(
        "Runbook completo de producción",
        4,
        "SRE runbook lite",
        f"{PROJ19}/runbook.md completo",
        "Unificar deploy, rollback, backup, restore, URLs, secretos (referencias), health.",
        "Proyecto único M19.",
        ["runbook", "handoff"],
        f"""runbook.md enlazado desde README m19-ops. Índice al inicio.""",
        _rows(("Ficha", "proyecto M19", "—")),
        ["Runbook navegable.", "Enlaces internos.", "URLs prod/staging."],
        ["Runbook disperso", "Sin restore"],
    )
    add(
        "Cierre M19 — checklist pre-demo M22",
        4,
        "Repaso M19",
        f"{PROJ19}/cierre-m19.md",
        "Verificar P1–P3, criterios dominio, prod estable para trials.",
        "Handoff a M20 (API staging HTTPS) y M22.",
        ["checklist", "dominio"],
        f"""cierre-m19.md con evidencia por criterio ficha. Actualiza README.""",
        _rows(("Ficha", "M19-nube-devops.md", "producto")),
        ["P1–P3 OK.", "cierre escrito.", "README índice."],
        ["Prod inestable", "Sin restore probado"],
    )

    return lessons


def _m20() -> list[dict]:
    lessons: list[dict] = []

    def add(*args, **kwargs):
        lessons.append(_lesson(*args, **kwargs))

    add(
        "Stack móvil y scaffold Agenda Ops",
        1,
        "Flutter o RN — get started",
        f"{PROJ20}/stack.md + repo-url.md",
        "Elegir Flutter o RN, documentar SDK, crear scaffold y enlazar repo.",
        "Un framework, un camino hasta M20 cierre.",
        ["Flutter vs RN", "staging URL", "lint"],
        f"""mkdir -p {PROJ20}. stack.md con decisión. Scaffold en app/ o repo enlazado.""",
        _rows(("Docs", "oficial stack", "producto-saas")),
        ["stack.md", "scaffold commit", "repo-url"],
        ["Cambiar stack semana 3", "Sin versión SDK"],
    )
    add(
        "Pantalla login contra API staging",
        1,
        "HTTP client + auth API",
        f"{PROJ20}/demo-login-lista.md (inicio)",
        "Implementar login email/password contra HTTPS M19; errores claros sin stack trace.",
        "Misma API que web M17.",
        ["POST login", "401 UX", "timeout"],
        f"""Probar contra staging. Anota URL base en stack.md. Commit feat(m20): login.""",
        _rows(("M17", "auth endpoints", "M19 staging")),
        ["Login feliz", "401 mensaje humano", "HTTPS"],
        ["localhost en release", "Password en logs"],
    )
    add(
        "Secure storage de token o sesión",
        1,
        "Keychain / Keystore vía lib oficial",
        f"{PROJ20}/auth-storage.md",
        "Persistir access token con flutter_secure_storage o equivalente RN; documentar qué guardas.",
        "JWT en SharedPreferences plano es hallazgo M18.",
        ["secure storage", "no password disk"],
        f"""auth-storage.md: claves, refresh si aplica, borrado en logout.""",
        _rows(("OWASP", "Mobile MASVS storage", "M18 JWT")),
        ["auth-storage.md", "código referenciado", "sin password claro"],
        ["Token en logs", "AsyncStorage plano"],
    )
    add(
        "Errores de validación y flujo 401",
        1,
        "Interceptors HTTP",
        f"commit + nota en auth-storage.md",
        "Manejar 401 global (logout), validación formulario, estados loading/error en login.",
        "Auth móvil real no termina en login exitoso una vez.",
        ["interceptor", "navigator login"],
        f"""Implementa interceptor 401 como ejemplo ficha M20. Prueba token expirado.""",
        _rows(("Ficha", "M20 ejemplo 401", "—")),
        ["401 redirige login", "Loading/error UI", "Commit"],
        ["Stack trace al usuario", "Ignorar 401"],
    )

    add(
        "Lista de citas autenticada",
        2,
        "ListView / FlatList patterns",
        f"{PROJ20}/demo-login-lista.md",
        "GET citas con token; mostrar fecha, cliente, servicio, estado.",
        "P1 M20: login + lista evidenciada.",
        ["Authorization header", "JSON parse", "orden"],
        f"""Captura lista + commit hash en demo-login-lista.md.""",
        _rows(("API", "GET citas", "SRS")),
        ["Lista con datos reales API", "commit hash en doc", "token adjunto"],
        ["Mock JSON", "Datos inventados"],
    )
    add(
        "Pull-to-refresh y paginación simple",
        2,
        "Async refresh UX",
        f"commit UI",
        "Refrescar lista; soportar query page/limit si la API lo expone.",
        "Dueño espera gesto natural en móvil.",
        ["refresh", "pagination"],
        f"""Documenta comportamiento si API sin paginación (corte client-side temporal).""",
        _rows(("Docs", "list refresh", "—")),
        ["Refresh funciona", "Sin crash lista vacía loading"],
        ["Refresh sin indicador", "Duplicar fetch infinito"],
    )
    add(
        "Estados de carga en lista",
        2,
        "UX loading skeletons",
        f"captura en demo-login-lista.md",
        "Skeleton o spinner, deshabilitar doble tap, error con reintento.",
        "Red móvil es lenta; la UI debe comunicarlo.",
        ["loading", "error retry"],
        f"""Tres capturas: loading, éxito, error en demo doc.""",
        _rows(("Ficha", "M20 semana 2", "—")),
        ["Tres estados UI", "Reintento", "Capturas"],
        ["Pantalla blanca", "Carga infinita"],
    )
    add(
        "Roles: confiar en la API, no solo en UI",
        2,
        "RBAC móvil",
        f"nota rbac en demo-login-lista.md",
        "Probar cuenta staff vs owner; ocultar acciones que API niega con 403.",
        "Doble fuente de verdad mata proyectos.",
        ["403 handling", "roles"],
        f"""Prueba endpoint prohibido; muestra mensaje adecuado.""",
        _rows(("M18", "rbac-matrix", "M12 roles")),
        ["Prueba rol documentada", "403 UX", "Sin lógica secreta solo UI"],
        ["Admin hardcoded en app", "Ignorar 403"],
    )

    add(
        "Pantalla detalle de cita",
        3,
        "Navigation params",
        f"commit pantalla detalle",
        "Navegar a detalle con id; mostrar campos completos de la cita.",
        "Lista sin detalle no sirve al dueño en campo.",
        ["route args", "fetch by id"],
        f"""Deep link interno navigator.push con id.""",
        _rows(("API", "GET cita/:id", "—")),
        ["Detalle coincide API", "Loading en detalle", "Commit"],
        ["Detalle mock", "IDOR no manejado"],
    )
    add(
        "Navegación: tabs o drawer mínimo",
        3,
        "Navigation container",
        f"commit nav",
        "Estructura Citas / Perfil / logout accesible.",
        "App usable sin laberinto de pantallas.",
        ["tabs", "drawer", "logout"],
        f"""Perfil muestra email usuario; logout limpia secure storage.""",
        _rows(("Docs", "navigation", "—")),
        ["Nav estable", "Logout limpia token", "Commit"],
        ["Sin logout", "Back stack roto"],
    )
    add(
        "Acciones permitidas: cancelar / atendida",
        3,
        "Mutations HTTP",
        f"commit si API expone",
        "Llamar PATCH/POST que la API expone; deshabilitar si 403.",
        "Solo acciones que el backend autoriza.",
        ["mutation", "optimistic UI opcional"],
        f"""Si API no tiene acción, documenta en nota y enlaza issue M17.""",
        _rows(("SRS", "historias citas", "—")),
        ["Acción o gap documentado", "403 manejado", "Commit"],
        ["Reglas negocio solo en app", "Silenciar errores"],
    )
    add(
        "Deep link opcional a una cita",
        3,
        "Deep linking intro",
        f"{PROJ20}/deep-link.md",
        "Configurar esquema o ruta para abrir detalle desde URL/notificación futura.",
        "Preparación recordatorios WhatsApp futuro.",
        ["deep link", "routing"],
        f"""deep-link.md con formato URL y prueba manual (adb xcrun si aplica).""",
        _rows(("Docs", "deep linking", "—")),
        ["Doc deep link", "Prueba manual o N/A justificado", "Commit config"],
        ["Deep link sin auth", "Abrir cita de otro user"],
    )

    add(
        "Lista vacía con copy útil",
        4,
        "Empty states UX",
        f"capturas P2",
        "UI cuando no hay citas semana; CTA coherente con producto.",
        "P2 pide estados vacío/error.",
        ["empty state", "copy"],
        f"""Captura empty state en auth-storage o demo doc.""",
        _rows(("producto-saas", "ICP", "—")),
        ["Copy útil", "Captura", "Sin crash"],
        ["Lista vacía en blanco", "Texto lorem"],
    )
    add(
        "Sin red: banner y reintento",
        4,
        "Connectivity plugins",
        f"captura offline",
        "Detectar offline o fallo DNS; banner y botón reintentar.",
        "Dueño en campo pierde señal a menudo.",
        ["offline", "retry"],
        f"""Simula modo avión; documenta comportamiento.""",
        _rows(("Docs", "connectivity", "—")),
        ["Modo avión probado", "Reintento", "Captura"],
        ["Crash sin red", "Loop infinito retry"],
    )
    add(
        "Timeout, 5xx y mensajes humanos",
        4,
        "HTTP timeouts",
        f"nota en demo doc",
        "Configurar timeout cliente; distinguir 5xx de error usuario.",
        "No todo es ‘algo salió mal’.",
        ["timeout", "5xx"],
        f"""Prueba timeout bajo artificialmente en dev.""",
        _rows(("Ficha", "M20 semana 4", "—")),
        ["Timeout configurado", "5xx mensaje", "Log dev sin PII"],
        ["Sin timeout", "Stack al usuario"],
    )
    add(
        "AppSec móvil: no loguear PII ni tokens",
        4,
        "OWASP MASVS logging",
        f"{PROJ20}/logging-policy.md",
        "Revisar print/debug; política de logs en dev vs release.",
        "Un logcat filtrado filtra tokens.",
        ["PII", "tokens", "crash reports"],
        f"""logging-policy.md + grep prints de token en repo app.""",
        _rows(("M18", "informe", "MASVS")),
        ["Política escrita", "Sin token en logs", "Commit limpieza si hubo"],
        ["console.log(token)", "Sentry con PII"],
    )

    add(
        "Firma Android y keystore fuera del repo",
        5,
        "Android signing / iOS profiles",
        f"{PROJ20}/build-evidence.md (prep)",
        "Crear keystore local ignorado; documentar variables CI futuras.",
        "P3 requiere build instalable real.",
        ["keystore", "gradle signing"],
        f"""build-evidence.md sección signing sin subir keystore.""",
        _rows(("Docs", "release build", "—")),
        ["Keystore fuera git", "gitignore", "Doc comando"],
        ["Keystore commiteado", "Password en gradle commiteado"],
    )
    add(
        "Build release APK o artefacto",
        5,
        "Release build oficial",
        f"{PROJ20}/build-evidence.md",
        "Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.",
        "Emulador no basta para P3.",
        ["release", "minify opcional"],
        f"""Comando exacto, tamaño APK, device modelo en build-evidence.""",
        _rows(("Ficha", "M20 P3", "—")),
        ["Artefacto generado", "Dispositivo real", "SHA commit"],
        ["Solo debug", "API localhost"],
    )
    add(
        "Release notes y demo cruzada con web",
        5,
        "Paridad auth web/móvil",
        f"{PROJ20}/release-notes.md",
        "Notas versión; misma cuenta web y móvil ven mismas citas.",
        "Proyecto M20 demuestra canal móvil del CRM.",
        ["paridad", "demo"],
        f"""release-notes.md + pasos demo 10 segundos del día citas.""",
        _rows(("Ficha", "proyecto M20", "M17 web")),
        ["release-notes", "Demo cruzada documentada", "Mismas citas"],
        ["Cuentas distintas sin explicar", "Datos mock"],
    )
    add(
        "Cierre M20 — dominio y README proyecto",
        5,
        "Repaso M20",
        f"{PROJ20}/README.md índice",
        "Verificar P1–P3, criterios dominio, enlaces evidencia.",
        "Cierras materia móvil antes de emprendimiento M22.",
        ["README", "dominio"],
        f"""README con enlaces demo-login-lista, auth-storage, build-evidence. cierre-m20.md checklist ficha.""",
        _rows(("Ficha", "M20-aplicaciones-moviles.md", "—")),
        ["README completo", "P1–P3", "Criterios con evidencia"],
        ["README vacío", "Build solo emulador"],
    )

    return lessons


def main() -> None:
    counts = {
        "M18": write_materia("M18", _m18()),
        "M19": write_materia("M19", _m19()),
        "M20": write_materia("M20", _m20()),
    }
    print("Generated:", counts)


if __name__ == "__main__":
    main()
