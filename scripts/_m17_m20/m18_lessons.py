"""M18 lessons: RAW specs + BODIES (M01/M09 quality)."""
from __future__ import annotations

import json

FILENAMES = {
    1: "L01-activos-actores-y-datos-sensibles-en-agenda-ops.md",
    2: "L02-trust-boundaries-y-flujos-de-confianza.md",
    3: "L03-stride-aplicado-al-crm-de-citas.md",
    4: "L04-threat-model-v0-y-lectura-owasp-top-10.md",
    5: "L05-inventario-de-autenticacion-actual.md",
    6: "L06-hashing-de-contrasenas-con-bcrypt-o-argon2.md",
    7: "L07-sesiones-server-side-vs-jwt-en-agenda-ops.md",
    8: "L08-threat-model-v1-post-autenticacion-p1.md",
    9: "L09-cookies-secure-httponly-y-samesite.md",
    10: "L10-csrf-en-formularios-y-mutaciones-state-changing.md",
    11: "L11-fijacion-de-sesion-y-logout-completo.md",
    12: "L12-checklist-cookies-y-csrf-en-staging.md",
    13: "L13-sqli-reproducir-en-tu-propia-api.md",
    14: "L14-mitigar-sqli-queries-parametrizadas-y-permisos-db.md",
    15: "L15-xss-reflejado-en-campos-de-cliente-o-busqueda.md",
    16: "L16-xss-almacenado-y-escape-en-plantillas-api.md",
    17: "L17-idor-en-citas-y-recursos-por-id.md",
    18: "L18-autorizacion-por-rol-owner-vs-staff.md",
    19: "L19-rate-limiting-en-login-y-endpoints-sensibles.md",
    20: "L20-tests-automatizados-cross-user-p2-avance.md",
    21: "L21-ssrf-superficie-en-webhooks-e-integraciones.md",
    22: "L22-subida-de-archivos-segura.md",
    23: "L23-deserializacion-y-json-peligroso.md",
    24: "L24-consolidar-hallazgos-semana-6-en-p2.md",
    25: "L25-npm-audit-y-cadena-de-dependencias.md",
    26: "L26-secretos-env-y-rotacion.md",
    27: "L27-cabeceras-de-seguridad-con-helmet-o-equivalente.md",
    28: "L28-csp-basica-sin-romper-agenda-ops.md",
    29: "L29-pipeline-ci-lint-test-audit-anti-secretos.md",
    30: "L30-estructura-del-informe-appsec.md",
    31: "L31-tests-de-regresion-de-seguridad-3.md",
    32: "L32-cierre-m18-dominio-y-riesgo-residual.md",
}

RAW = json.loads(r"""
[
  {
    "titulo": "Activos, actores y datos sensibles en Agenda Ops",
    "semana": 1,
    "horas": 5,
    "lectura": "OWASP Threat Modeling (overview) + notas STRIDE",
    "evidencia": "projects/m18-appsec/threat-model-v0.md sección Activos",
    "objetivo": "Inventariar actores (dueño, staff, cliente final, atacante) y activos (PII, credenciales, citas, tokens, Postgres) del piloto Agenda Ops.",
    "porque": "Sin lista de activos, el threat model es decoración. Esta lección arranca P1 y el hilo OWASP del módulo.",
    "conceptos": [
      "Actor vs rol en el sistema.",
      "PII en citas (nombre, teléfono, notas).",
      "Superficie: panel web + API REST.",
      "Supuesto: solo atacas **tu** staging/local."
    ],
    "pasos_extra": "```bash\nmkdir -p projects/m18-appsec\n```\n\nEn `threat-model-v0.md` crea tablas **Actores** y **Activos** (≥5 activos). Dibuja un diagrama caja-flecha: navegador → API → Postgres. Marca qué datos salen en JSON de `/api/citas`.\n\n```bash\ngit ls-files | rg -i 'env|secret|credential|\\.pem' || true\n```\n\nAnota el resultado en el mismo archivo (sin pegar secretos).",
    "lectura_rows": [
      [
        "OWASP",
        "Threat Modeling (ES/overview)",
        "Cheat Sheet STRIDE"
      ],
      [
        "Plan",
        "[producto-saas.md](../../../producto-saas.md)",
        "M13 trust boundaries"
      ]
    ],
    "hecho": [
      "Existe `projects/m18-appsec/threat-model-v0.md` con actores y ≥5 activos.",
      "Diagrama ASCII o Mermaid del piloto."
    ],
    "errores": [
      "Activos genéricos (“la DB”) sin tablas/campos.",
      "Omitir al cliente final como fuente de datos."
    ]
  },
  {
    "titulo": "Trust boundaries y flujos de confianza",
    "semana": 1,
    "horas": 5,
    "lectura": "STRIDE por boundary + M13 `trust-boundaries`",
    "evidencia": "projects/m18-appsec/trust-boundaries-appsec.md",
    "objetivo": "Dibujar límites de confianza (browser, API, DB, integraciones futuras) y etiquetar protocolo + datos que cruzan cada límite.",
    "porque": "M10 y M13 ya nombraron boundaries; hoy los operacionalizas para amenazas AppSec.",
    "conceptos": [
      "Zona de confianza vs desconfianza.",
      "Datos en tránsito vs en reposo.",
      "Admin vs tenant (futuro)."
    ],
    "pasos_extra": "Abre `projects/m13-diseno/trust-boundaries.md` si existe. Copia o enlaza y extiende en `projects/m18-appsec/trust-boundaries-appsec.md`.\n\nPor cada límite documenta: **origen**, **destino**, **protocolo**, **autenticación**, **datos**. Mínimo 4 límites (ej. browser→API, API→Postgres, API→SMTP futuro, operador→hosting).\n\nPara cada límite escribe una pregunta “¿qué pasa si el atacante controla este lado?”",
    "lectura_rows": [
      [
        "M13",
        "trust-boundaries",
        "M10 amenazas de red"
      ],
      [
        "OWASP",
        "STRIDE en boundaries",
        "—"
      ]
    ],
    "hecho": [
      "≥4 boundaries documentados.",
      "Pregunta de abuso por límite."
    ],
    "errores": [
      "Un solo boundary “internet”.",
      "Ignorar Postgres como activo interno."
    ]
  },
  {
    "titulo": "STRIDE aplicado al CRM de citas",
    "semana": 1,
    "horas": 5,
    "lectura": "STRIDE cheat sheet (una categoría por componente)",
    "evidencia": "projects/m18-appsec/stride-matrix.md",
    "objetivo": "Completar una matriz STRIDE (Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation) sobre login, citas y panel admin de Agenda Ops.",
    "porque": "La matriz obliga a nombrar amenazas antes de buscar exploits al azar.",
    "conceptos": [
      "Spoofing en login.",
      "Tampering en `PUT /api/citas`.",
      "IDOR como Information Disclosure."
    ],
    "pasos_extra": "Crea `projects/m18-appsec/stride-matrix.md` con filas: **Login**, **Lista citas**, **Detalle cita**, **Admin usuarios** (si existe).\n\nColumnas STRIDE: marca S/T/R/I/D/E con una frase concreta (no “hackeo”). Ejemplo fila Login / Spoofing: “fuerza bruta o credenciales robadas”.\n\nPrioriza 3 celdas rojas que atacarás en las próximas semanas.",
    "lectura_rows": [
      [
        "OWASP",
        "STRIDE",
        "Top 10 overview ES"
      ]
    ],
    "hecho": [
      "Matriz ≥4 filas × 6 columnas.",
      "≥3 amenazas priorizadas."
    ],
    "errores": [
      "Copiar tabla de blog sin adaptar.",
      "Dejar celdas vacías con ‘N/A’ en todo."
    ]
  },
  {
    "titulo": "Threat model v0 y lectura OWASP Top 10",
    "semana": 1,
    "horas": 5,
    "lectura": "OWASP Top 10 (2021) — lectura completa en español",
    "evidencia": "projects/m18-appsec/owasp-top10-map.md",
    "objetivo": "Mapear cada categoría del OWASP Top 10 a un endpoint o pantalla concreta de Agenda Ops (aunque aún no tengas el bug).",
    "porque": "Cierras la semana 1 con backlog de riesgo alineado al estándar de la industria.",
    "conceptos": [
      "A01 Broken Access Control.",
      "A03 Injection.",
      "A07 Identification and Authentication Failures."
    ],
    "pasos_extra": "En `projects/m18-appsec/owasp-top10-map.md` tabla: **OWASP id**, **Ejemplo en Agenda Ops**, **Mitigación prevista**, **Semana M18**.\n\nAñade en `threat-model-v0.md` sección **Riesgo residual semana 1** (3 bullets).\n\nRelee la ficha M18: confirma que P1 (threat model v1) llegará tras semana 2 auth.",
    "lectura_rows": [
      [
        "OWASP",
        "Top 10 ES",
        "Cheat Sheets índice"
      ]
    ],
    "hecho": [
      "Mapa 10 filas mínimo.",
      "threat-model-v0 actualizado."
    ],
    "errores": [
      "Marcar ‘no aplica’ en todo.",
      "Atacar sitios que no controlas."
    ]
  },
  {
    "titulo": "Inventario de autenticación actual",
    "semana": 2,
    "horas": 5,
    "lectura": "OWASP A07 + Authentication Cheat Sheet",
    "evidencia": "projects/m18-appsec/docs/auth-inventario.md",
    "objetivo": "Documentar flujo real de registro/login/logout de Agenda Ops: transporte, almacenamiento de sesión, rotación y recuperación de contraseña.",
    "porque": "No puedes endurecer lo que no has descrito. Esta lección es fotografía del estado antes de parches.",
    "conceptos": [
      "Credencial vs sesión vs token.",
      "Transporte HTTPS obligatorio.",
      "Mensajes de error uniformes."
    ],
    "pasos_extra": "En `projects/m18-appsec/docs/auth-inventario.md` describe paso a paso el happy path y 2 edge cases (password malo, usuario inexistente).\n\nCaptura (sin secretos) qué cookie/header usa la API. ¿El ID de usuario va en JWT payload? ¿Sesión en DB?\n\nLista endpoints: `POST /auth/login`, etc. Marca cuáles son públicos vs autenticados.",
    "lectura_rows": [
      [
        "OWASP",
        "A07 + Auth Cheat Sheet",
        "M10 cookies/sesiones"
      ]
    ],
    "hecho": [
      "Inventario con endpoints reales.",
      "Público vs autenticado claro."
    ],
    "errores": [
      "Inventario teórico sin abrir el código.",
      "Loguear tokens en dev."
    ]
  },
  {
    "titulo": "Hashing de contraseñas con bcrypt o argon2",
    "semana": 2,
    "horas": 5,
    "lectura": "Password Storage Cheat Sheet",
    "evidencia": "commit en repo producto + nota en projects/m18-appsec/docs/auth-hashing.md",
    "objetivo": "Verificar o implementar hashing con coste adecuado (bcrypt≥12 o argon2) y eliminar esquemas débiles (MD5/SHA plano).",
    "porque": "A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.",
    "conceptos": [
      "Salt automático.",
      "Cost factor / memoria argon2.",
      "Nunca loguear `plain` password."
    ],
    "pasos_extra": "Audita el servicio de registro/login en tu API de Agenda Ops (repo M17). Si hay `bcrypt`/`argon2`, documenta parámetros en `projects/m18-appsec/docs/auth-hashing.md`.\n\nSi falta: implementa con lib madura, migra usuarios de prueba, añade test que el hash no es igual al plain.\n\n```bash\n# en repo producto\nnpm test -- --testPathPattern=auth 2>/dev/null || npm test\n```",
    "lectura_rows": [
      [
        "OWASP",
        "Password Storage",
        "Ejemplo ficha M18"
      ]
    ],
    "hecho": [
      "Hashing correcto en código o ADR si ya estaba.",
      "Test o script que verifica compare."
    ],
    "errores": [
      "MD5/SHA1 para passwords.",
      "Cost 4 ‘para ir rápido’."
    ]
  },
  {
    "titulo": "Sesiones server-side vs JWT en Agenda Ops",
    "semana": 2,
    "horas": 5,
    "lectura": "Session Management + JWT Cheat Sheets",
    "evidencia": "projects/m18-appsec/docs/adr-sesion-vs-jwt.md (o enlace ADR M13)",
    "objetivo": "Decidir y documentar si Agenda Ops usa sesión en servidor, JWT firmado, o híbrido; consecuencias para XSS, logout y revocación.",
    "porque": "M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.",
    "conceptos": [
      "Revocación inmediata.",
      "HttpOnly cookie vs Authorization header.",
      "Refresh token (si aplica)."
    ],
    "pasos_extra": "Redacta `projects/m18-appsec/docs/adr-sesion-vs-jwt.md`: contexto, decisión, alternativas rechazadas, impacto en móvil M20.\n\nPrueba manual: login → copiar token/cookie → logout → reutilizar credencial vieja (debe fallar).\n\nAnota resultado en la ADR.",
    "lectura_rows": [
      [
        "M13",
        "adr/005-auth si existe",
        "M10 L14 sesiones"
      ]
    ],
    "hecho": [
      "ADR con alternativas.",
      "Prueba logout/reuse documentada."
    ],
    "errores": [
      "JWT en localStorage sin plan anti-XSS.",
      "Sin estrategia de revocación."
    ]
  },
  {
    "titulo": "Threat model v1 post-autenticación (P1)",
    "semana": 2,
    "horas": 5,
    "lectura": "Repaso STRIDE semanas 1–2",
    "evidencia": "projects/m18-appsec/threat-model-v1.md",
    "objetivo": "Actualizar threat model con flujos de auth reales y marcar controles implementados vs pendientes.",
    "porque": "P1 exige v1 revisado tras entender login; hoy entregas el hito.",
    "conceptos": [
      "Control vs amenaza.",
      "Gap analysis.",
      "Priorización por explotabilidad."
    ],
    "pasos_extra": "Copia `threat-model-v0.md` → `threat-model-v1.md`. Añade sección **Controles auth** (hashing, cookies, rate limit planificado).\n\nTabla: Amenaza | Control | Estado (OK/TODO) | Issue/commit.\n\nChecklist P1 de la ficha: confirma que un revisor podría seguir el doc sin abrir el código.",
    "lectura_rows": [
      [
        "Ficha",
        "M18-seguridad.md P1",
        "—"
      ]
    ],
    "hecho": [
      "threat-model-v1.md completo.",
      "Tabla amenaza-control."
    ],
    "errores": [
      "Renombrar v0 sin cambios.",
      "Omitir auth en el modelo."
    ]
  },
  {
    "titulo": "Cookies Secure, HttpOnly y SameSite",
    "semana": 3,
    "horas": 5,
    "lectura": "OWASP Session Management + cookie flags",
    "evidencia": "projects/m18-appsec/pocs/cookies.md",
    "objetivo": "Inspeccionar cookies de sesión de Agenda Ops en DevTools y verificar flags; corregir configuración en el servidor.",
    "porque": "M10 estudió cookies; hoy aplicas flags en **tu** stack.",
    "conceptos": [
      "SameSite=Lax/Strict.",
      "Secure en HTTPS.",
      "HttpOnly vs JS legítimo."
    ],
    "pasos_extra": "Login en staging/local. En `projects/m18-appsec/pocs/cookies.md` tabla: nombre cookie, flags, lifetime, path.\n\nSi falta `Secure` o `HttpOnly` en cookie de sesión, parchea middleware/framework y captura antes/después (sin valor de cookie).\n\nPrueba: ¿JavaScript puede leer la cookie de sesión? Documenta.",
    "lectura_rows": [
      [
        "MDN",
        "Set-Cookie",
        "M10 L13"
      ]
    ],
    "hecho": [
      "Tabla de cookies real.",
      "Parche o justificación documentada."
    ],
    "errores": [
      "SameSite=None sin Secure.",
      "Cookie de sesión accesible desde JS."
    ]
  },
  {
    "titulo": "CSRF en formularios y mutaciones state-changing",
    "semana": 3,
    "horas": 5,
    "lectura": "CSRF Prevention Cheat Sheet",
    "evidencia": "fix + projects/m18-appsec/pocs/csrf-notes.md",
    "objetivo": "Identificar operaciones mutables (POST/PUT/DELETE) y aplicar token CSRF, SameSite estricto o patrón equivalente en Agenda Ops.",
    "porque": "Un atacante no necesita XSS si tu sesión acepta POST cross-site.",
    "conceptos": [
      "Double-submit cookie (si aplica).",
      "Token sincronizado.",
      "API JSON + CORS no sustituye CSRF en cookies."
    ],
    "pasos_extra": "Lista rutas que cambian estado (crear cita, cancelar, perfil). En `projects/m18-appsec/pocs/csrf-notes.md` indica protección por ruta.\n\nImplementa protección mínima en la ruta más crítica (ej. crear cita). Test manual con `curl` sin token (debe 403).\n\nReferencia OWASP CSRF sheet en el doc.",
    "lectura_rows": [
      [
        "OWASP",
        "CSRF Prevention",
        "M10 CORS"
      ]
    ],
    "hecho": [
      "Lista rutas mutables.",
      "≥1 ruta protegida."
    ],
    "errores": [
      "Confiar solo en CORS.",
      "GET que borra datos."
    ]
  },
  {
    "titulo": "Fijación de sesión y logout completo",
    "semana": 3,
    "horas": 5,
    "lectura": "Session fixation + logout best practices",
    "evidencia": "projects/m18-appsec/docs/session-lifecycle.md",
    "objetivo": "Asegurar rotación de ID de sesión tras login y destrucción server-side en logout.",
    "porque": "Robar sesión fija es un clásico en apps que reutilizan el mismo session id.",
    "conceptos": [
      "Regenerar session id post-auth.",
      "Invalidar en logout.",
      "Timeout por inactividad (idea)."
    ],
    "pasos_extra": "Traza el ciclo en código. Documenta en `projects/m18-appsec/docs/session-lifecycle.md`.\n\nPruebas: login dos veces ¿cambia id? logout ¿cookie inválida en siguiente request?\n\nSi usas JWT stateless, documenta blacklist/short TTL en su lugar.",
    "lectura_rows": [
      [
        "OWASP",
        "Session Management",
        "Auth cheat sheet"
      ]
    ],
    "hecho": [
      "Doc ciclo de vida.",
      "Pruebas login/logout documentadas."
    ],
    "errores": [
      "Logout solo borra cookie cliente.",
      "Session id pre-login reutilizado."
    ]
  },
  {
    "titulo": "Checklist cookies y CSRF en staging",
    "semana": 3,
    "horas": 5,
    "lectura": "Repaso semana 3",
    "evidencia": "projects/m18-appsec/docs/checklist-cookies-csrf.md",
    "objetivo": "Checklist binario ejecutable antes de cada deploy: cookies, CSRF, HTTPS, logout.",
    "porque": "Operacionalizas controles para M19 deploy y trials M22.",
    "conceptos": [
      "Checklist reproducible.",
      "Evidencia en staging."
    ],
    "pasos_extra": "Crea `projects/m18-appsec/docs/checklist-cookies-csrf.md` con ≥10 ítems Sí/No. Ejecútalo contra staging y pega resultado (fecha, URL).\n\nEnlaza issues/commits de la semana. Cierra con riesgo residual CSRF.",
    "lectura_rows": [
      [
        "Ficha",
        "M18 semana 3",
        "M19 ambientes futuro"
      ]
    ],
    "hecho": [
      "Checklist ejecutado.",
      "Fecha y URL."
    ],
    "errores": [
      "Checklist nunca ejecutado.",
      "Marcar todo Sí sin prueba."
    ]
  },
  {
    "titulo": "SQLi: reproducir en tu propia API",
    "semana": 4,
    "horas": 5,
    "lectura": "OWASP A03 Injection + SQLi Prevention",
    "evidencia": "projects/m18-appsec/findings/001-sqli.md",
    "objetivo": "Encontrar al menos un punto susceptible (búsqueda, filtro, orden) y demostrar SQLi controlada en local/staging **sin** dañar datos reales.",
    "porque": "P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.",
    "conceptos": [
      "Consulta concatenada vs parametrizada.",
      "Error verbose vs genérico.",
      "Principio de mínimo privilegio DB."
    ],
    "pasos_extra": "Usa cuenta de prueba. Intenta payloads en query params/body (`' OR '1'='1` etc.) en endpoints de búsqueda de clientes/citas.\n\nDocumenta en `projects/m18-appsec/findings/001-sqli.md`: endpoint, payload, respuesta, impacto. **No** pegues datos de clientes reales.\n\nSi no hay SQLi, documenta por qué (ORM parametrizado) y prueba bypass conocido del ORM.",
    "lectura_rows": [
      [
        "OWASP",
        "SQL Injection",
        "ORM docs de tu stack"
      ]
    ],
    "hecho": [
      "Finding documentado o prueba de mitigación.",
      "Solo tu entorno."
    ],
    "errores": [
      "SQLi en producción de terceros.",
      "Drop table en staging compartido."
    ]
  },
  {
    "titulo": "Mitigar SQLi: queries parametrizadas y permisos DB",
    "semana": 4,
    "horas": 5,
    "lectura": "SQLi Prevention Cheat Sheet",
    "evidencia": "commit fix + test en repo producto",
    "objetivo": "Corregir el vector SQLi (o endurecer consulta) y añadir test de regresión que falle si vuelve la concatenación.",
    "porque": "Hallazgo sin fix no cuenta para P2.",
    "conceptos": [
      "Prepared statements.",
      "Validación de entrada en frontera.",
      "Usuario DB sin DDL."
    ],
    "pasos_extra": "Implementa fix en tu API de Agenda Ops (repo M17). Test automatizado: input malicioso → 400 o resultado vacío, nunca error SQL expuesto.\n\nActualiza `001-sqli.md` con commit hash y captura de test verde.",
    "lectura_rows": [
      [
        "OWASP",
        "SQLi Prevention",
        "Tests M15 si aplica"
      ]
    ],
    "hecho": [
      "Test de regresión.",
      "Finding actualizado a Cerrado."
    ],
    "errores": [
      "Escapar manualmente sin parametrizar.",
      "Silenciar error sin arreglar query."
    ]
  },
  {
    "titulo": "XSS reflejado en campos de cliente o búsqueda",
    "semana": 4,
    "horas": 5,
    "lectura": "XSS Prevention Cheat Sheet",
    "evidencia": "projects/m18-appsec/findings/002-xss-reflected.md",
    "objetivo": "Probar XSS reflejado en un campo que se renderiza (nombre, mensaje de error) y documentar contexto HTML/JS.",
    "porque": "XSS roba sesiones si las cookies son legibles por JS.",
    "conceptos": [
      "Reflejado vs almacenado.",
      "Contexto de escape.",
      "Content-Type correcto."
    ],
    "pasos_extra": "Payloads: `<script>alert(1)</script>`, event handlers. En `projects/m18-appsec/findings/002-xss-reflected.md` indica pantalla y si el navegador ejecutó (en tu cuenta de prueba).\n\nNo uses payloads que exfiltruen a dominios externos; solo demuestra impacto local.",
    "lectura_rows": [
      [
        "OWASP",
        "XSS Prevention",
        "CSP intro semana 7"
      ]
    ],
    "hecho": [
      "PoC documentada.",
      "Contexto identificado."
    ],
    "errores": [
      "XSS persistente en prod sin aviso.",
      "Confiar en ‘React escapa todo’."
    ]
  },
  {
    "titulo": "XSS almacenado y escape en plantillas/API",
    "semana": 4,
    "horas": 5,
    "lectura": "DOM XSS + stored XSS",
    "evidencia": "commit fix + findings/002 actualizado",
    "objetivo": "Mitigar XSS (escape, sanitización acotada, CSP futura) en el flujo almacenado (notas de cita, perfil).",
    "porque": "El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.",
    "conceptos": [
      "Sanitizar HTML vs texto plano.",
      "JSON no implica seguro en `dangerouslySetInnerHTML`.",
      "Headers X-Content-Type-Options."
    ],
    "pasos_extra": "Si hay notas/comentarios en citas, prueba almacenamiento. Fix en template/API. Test: payload guardado se muestra escapado.\n\nTabla P2 en `projects/m18-appsec/findings-table.md` con filas SQLi + XSS (hallazgo → PoC → commit → test).",
    "lectura_rows": [
      [
        "OWASP",
        "XSS Prevention",
        "MDN textContent"
      ]
    ],
    "hecho": [
      "≥2 filas en findings-table.",
      "Test o verificación manual repetible."
    ],
    "errores": [
      "strip_tags inventado.",
      "innerHTML con input usuario."
    ]
  },
  {
    "titulo": "IDOR en citas y recursos por ID",
    "semana": 5,
    "horas": 5,
    "lectura": "OWASP A01 Broken Access Control",
    "evidencia": "projects/m18-appsec/findings/003-idor.md",
    "objetivo": "Demostrar acceso cross-user a `GET/PUT /api/citas/:id` (u otro recurso) con dos cuentas de prueba.",
    "porque": "El ejemplo de la ficha M18: ocultar botones no basta.",
    "conceptos": [
      "Autorización server-side.",
      "ID predecible.",
      "UUID no es autorización."
    ],
    "pasos_extra": "Crea usuario A y B. A crea cita. B intenta leer/editar ID de A. Documenta en `003-idor.md`.\n\nSi ya está protegido, muestra test automatizado que falla si quitas el check.",
    "lectura_rows": [
      [
        "OWASP",
        "A01",
        "Ejemplo IDOR ficha M18"
      ]
    ],
    "hecho": [
      "PoC con dos usuarios.",
      "Impacto descrito."
    ],
    "errores": [
      "Probar en datos de design partner real.",
      "Autorización solo en front."
    ]
  },
  {
    "titulo": "Autorización por rol owner vs staff",
    "semana": 5,
    "horas": 5,
    "lectura": "Access Control Cheat Sheet",
    "evidencia": "projects/m18-appsec/docs/rbac-matrix.md",
    "objetivo": "Matriz rol × recurso × acción para Agenda Ops y gaps entre SRS y código.",
    "porque": "Agenda Ops distingue dueño y staff; la API debe hacerlo explícito.",
    "conceptos": [
      "RBAC vs ABAC (idea).",
      "403 vs 404.",
      "Principio mínimo privilegio."
    ],
    "pasos_extra": "`projects/m18-appsec/docs/rbac-matrix.md`: filas citas, clientes, configuración; columnas owner/staff/anónimo.\n\nPrueba un caso staff que no debe ver citas de otro tenant (futuro) o acción admin. Registra resultado.",
    "lectura_rows": [
      [
        "SRS",
        "M12 roles",
        "OWASP A01"
      ]
    ],
    "hecho": [
      "Matriz completa.",
      "≥1 prueba manual rol."
    ],
    "errores": [
      "Un solo rol ‘admin’.",
      "404 para esconder sin authz."
    ]
  },
  {
    "titulo": "Rate limiting en login y endpoints sensibles",
    "semana": 5,
    "horas": 5,
    "lectura": "Brute Force + Rate Limiting Cheat Sheets",
    "evidencia": "commit middleware + nota en findings",
    "objetivo": "Implementar límite de intentos (IP o cuenta) en login y al menos un endpoint costoso.",
    "porque": "Sin rate limit, A07 y A04 (DoS ligero) son triviales.",
    "conceptos": [
      "Ventana fija vs token bucket (idea).",
      "429 Too Many Requests.",
      "No bloquear legítimos sin UX."
    ],
    "pasos_extra": "Añade rate limit (lib o reverse proxy local). Prueba 20 intentos fallidos login → bloqueo temporal.\n\nDocumenta configuración y cómo resetear en dev.",
    "lectura_rows": [
      [
        "OWASP",
        "Brute Force",
        "M11 recursos"
      ]
    ],
    "hecho": [
      "Rate limit activo.",
      "Prueba documentada."
    ],
    "errores": [
      "Rate limit solo en front.",
      "Bloqueo permanente sin unlock."
    ]
  },
  {
    "titulo": "Tests automatizados cross-user (P2 avance)",
    "semana": 5,
    "horas": 5,
    "lectura": "Testing access control",
    "evidencia": "tests en repo producto + projects/m18-appsec/findings-table.md",
    "objetivo": "Escribir ≥2 tests: usuario A no lee/edita recurso de B; rol staff no ejecuta acción de owner.",
    "porque": "P2 pide tabla hallazgo→fix→test; hoy consolidas access control.",
    "conceptos": [
      "Fixture dos usuarios.",
      "Arrange-Act-Assert.",
      "401 vs 403 semántica."
    ],
    "pasos_extra": "```bash\n# ejemplo nombre\nnpm test -- --testPathPattern=authz\n```\n\nActualiza findings-table con IDOR y RBAC. Mínimo 5 hallazgos totales en P2 al cerrar M18 — planifica los que faltan.",
    "lectura_rows": [
      [
        "Ficha",
        "M18 P2",
        "M15 testing"
      ]
    ],
    "hecho": [
      "≥2 tests authz verdes.",
      "findings-table ≥3 filas."
    ],
    "errores": [
      "Tests que mockean auth siempre true.",
      "Un solo usuario en tests."
    ]
  },
  {
    "titulo": "SSRF: superficie en webhooks e integraciones",
    "semana": 6,
    "horas": 5,
    "lectura": "SSRF Prevention Cheat Sheet",
    "evidencia": "projects/m18-appsec/findings/004-ssrf.md",
    "objetivo": "Identificar si Agenda Ops (o roadmap) acepta URLs server-side (webhook, import, avatar remoto) y evaluar riesgo SSRF.",
    "porque": "Aun sin feature, documentar el control evita sorpresas en M26 integraciones.",
    "conceptos": [
      "Allowlist de hosts.",
      "Bloquear metadata IP.",
      "No reutilizar cliente HTTP sin validar."
    ],
    "pasos_extra": "Si no hay feature URL, simula diseño en `004-ssrf.md`: qué pasaría con `http://169.254.169.254`. Define allowlist propuesta.\n\nSi hay fetch server-side, prueba URL interna en staging aislado.",
    "lectura_rows": [
      [
        "OWASP",
        "SSRF",
        "—"
      ]
    ],
    "hecho": [
      "Doc SSRF con allowlist.",
      "Riesgo nombrado."
    ],
    "errores": [
      "curl a metadata cloud en prod.",
      "SSRF ‘para probar AWS’ en cuenta ajena."
    ]
  },
  {
    "titulo": "Subida de archivos segura",
    "semana": 6,
    "horas": 5,
    "lectura": "File Upload Cheat Sheet",
    "evidencia": "projects/m18-appsec/findings/005-upload.md",
    "objetivo": "Revisar o diseñar upload (logo, adjunto) con validación tipo/tamaño, almacenamiento fuera de webroot y nombres aleatorios.",
    "porque": "Un .php disfrazado de .jpg es folklore porque sigue pasando.",
    "conceptos": [
      "MIME sniffing.",
      "Tamaño máximo.",
      "Escaneo opcional."
    ],
    "pasos_extra": "Si el piloto no sube archivos, redacta checklist de aceptación en `005-upload.md` para cuando exista.\n\nSi sube: prueba archivo malicioso en staging, verifica que no se sirve como script.",
    "lectura_rows": [
      [
        "OWASP",
        "File Upload",
        "—"
      ]
    ],
    "hecho": [
      "Checklist o prueba real.",
      "Ruta almacenamiento."
    ],
    "errores": [
      "Guardar en `public/` con nombre usuario.",
      "Confiar en extensión."
    ]
  },
  {
    "titulo": "Deserialización y JSON peligroso",
    "semana": 6,
    "horas": 5,
    "lectura": "Deserialization + API hardening",
    "evidencia": "projects/m18-appsec/docs/json-trust.md",
    "objetivo": "Auditar parsers JSON, `eval`, plantillas dinámicas y tipos inesperados en body de API.",
    "porque": "Node/TS rara vez hace Java deserialization, pero prototype pollution y lógica sí.",
    "conceptos": [
      "Validación schema (zod/joi).",
      "Prototype pollution (idea).",
      "Tamaño body limit."
    ],
    "pasos_extra": "`projects/m18-appsec/docs/json-trust.md`: lista endpoints con body JSON; schema sí/no. Añade límite `express.json({ limit: '100kb' })` o equivalente.\n\nPrueba payload enorme o campos extra; documenta comportamiento.",
    "lectura_rows": [
      [
        "OWASP",
        "API Security Top 10",
        "Input validation"
      ]
    ],
    "hecho": [
      "Lista endpoints + validación.",
      "Límite tamaño body."
    ],
    "errores": [
      "Aceptar cualquier JSON.",
      "Confiar en tipos TS solo compile-time."
    ]
  },
  {
    "titulo": "Consolidar hallazgos semana 6 en P2",
    "semana": 6,
    "horas": 5,
    "lectura": "Repaso findings",
    "evidencia": "projects/m18-appsec/findings-table.md actualizado",
    "objetivo": "Asegurar ≥5 hallazgos con PoC, fix y test o verificación repetible; priorizar los de mayor impacto.",
    "porque": "Mitad del módulo: P2 debe ser visible en git.",
    "conceptos": [
      "Severidad.",
      "Estado.",
      "Regresión."
    ],
    "pasos_extra": "Revisa tabla P2. Cada fila: ID, OWASP, PoC resumen, commit fix, test/link.\n\nAbre issues para hallazgos abiertos con fecha objetivo semana 7–8.",
    "lectura_rows": [
      [
        "Ficha",
        "M18 P2",
        "—"
      ]
    ],
    "hecho": [
      "≥5 filas completas o plan con 5.",
      "Ningún secreto en tabla."
    ],
    "errores": [
      "Hallazgos duplicados.",
      "PoC sin fix planificado."
    ]
  },
  {
    "titulo": "npm audit y cadena de dependencias",
    "semana": 7,
    "horas": 5,
    "lectura": "OWASP A06 Vulnerable Components",
    "evidencia": "projects/m18-appsec/docs/npm-audit.md",
    "objetivo": "Ejecutar auditoría de dependencias, triagear findings (prod vs dev), actualizar o documentar riesgo aceptado.",
    "porque": "Tu app hereda CVEs de `node_modules`.",
    "conceptos": [
      "Semver y lockfile.",
      "DevDependency vs runtime.",
      "Riesgo aceptado con fecha."
    ],
    "pasos_extra": "```bash\ncd <repo Agenda Ops>\nnpm audit --omit=dev 2>/dev/null || npm audit\n```\n\nGuarda salida en `projects/m18-appsec/docs/npm-audit.md`. Arregla al menos 1 high/critical o documenta por qué no aplica.",
    "lectura_rows": [
      [
        "OWASP",
        "A06",
        "npm audit docs"
      ]
    ],
    "hecho": [
      "Audit guardado.",
      "≥1 acción tomada."
    ],
    "errores": [
      "`npm audit fix --force` sin leer.",
      "Ignorar todo."
    ]
  },
  {
    "titulo": "Secretos, .env y rotación",
    "semana": 7,
    "horas": 5,
    "lectura": "Secrets Management Cheat Sheet",
    "evidencia": "projects/m18-appsec/docs/rotacion-secretos.md",
    "objetivo": "Verificar que secretos viven fuera de git; plan de rotación para JWT/session secret y DB.",
    "porque": "Un commit con `.env` es incidente permanente (historial).",
    "conceptos": [
      "`.gitignore`.",
      "Rotación sin downtime (idea).",
      "Pre-commit hooks."
    ],
    "pasos_extra": "```bash\ngit log -p --all -S 'DATABASE_URL' | head -20\n```\n\n`projects/m18-appsec/docs/rotacion-secretos.md`: inventario (sin valores), dónde viven en local/staging, pasos rotar session secret.",
    "lectura_rows": [
      [
        "OWASP",
        "Secrets",
        "M19 secrets-inventory"
      ]
    ],
    "hecho": [
      "Inventario sin valores.",
      "grep historial ejecutado."
    ],
    "errores": [
      "Pegar secretos en issue.",
      "Rotar sin probar logout."
    ]
  },
  {
    "titulo": "Cabeceras de seguridad con Helmet o equivalente",
    "semana": 7,
    "horas": 5,
    "lectura": "Security Headers Cheat Sheet",
    "evidencia": "commit headers + captura curl",
    "objetivo": "Configurar HSTS (si HTTPS), X-Frame-Options/ frame-ancestors, X-Content-Type-Options, Referrer-Policy.",
    "porque": "M10 L16 en tu código de producción.",
    "conceptos": [
      "Helmet middleware.",
      "HSTS solo con HTTPS estable.",
      "Clickjacking."
    ],
    "pasos_extra": "```bash\ncurl -sI https://<tu-staging>/ | rg -i 'strict|frame|content-type|referrer'\n```\n\nDocumenta antes/después en bitácora. No rompas el front (prueba login).",
    "lectura_rows": [
      [
        "OWASP",
        "Secure Headers",
        "M10 L16"
      ]
    ],
    "hecho": [
      "Headers visibles en staging.",
      "Login sigue funcionando."
    ],
    "errores": [
      "HSTS en localhost sin TLS.",
      "CSP rota todo sin reporte."
    ]
  },
  {
    "titulo": "CSP básica sin romper Agenda Ops",
    "semana": 7,
    "horas": 5,
    "lectura": "Content Security Policy Cheat Sheet",
    "evidencia": "projects/m18-appsec/docs/csp.md + commit opcional",
    "objetivo": "Diseñar política CSP mínima (default-src, script-src) y desplegar en report-only o estricta según tolerancia.",
    "porque": "CSP es red de seguridad ante XSS residual.",
    "conceptos": [
      "nonce vs hash.",
      "report-uri / report-to.",
      "inline scripts legacy."
    ],
    "pasos_extra": "`projects/m18-appsec/docs/csp.md`: política propuesta, fuentes externas que usa tu front (CDN, analytics futuro).\n\nImplementa CSP report-only primero; anota violaciones en consola.",
    "lectura_rows": [
      [
        "OWASP",
        "CSP",
        "MDN CSP"
      ]
    ],
    "hecho": [
      "Política escrita.",
      "Prueba report-only o estricta."
    ],
    "errores": [
      "`unsafe-inline` everywhere.",
      "CSP en meta sin HTTPS."
    ]
  },
  {
    "titulo": "Pipeline CI: lint, test, audit, anti-secretos",
    "semana": 8,
    "horas": 5,
    "lectura": "Secure SDLC + CI guides",
    "evidencia": "projects/m18-appsec/ci-appsec.yml snippet o enlace workflow",
    "objetivo": "Añadir job CI con lint, tests, `npm audit` (fail on high), grep básico anti-secretos.",
    "porque": "P3 de la ficha: seguridad en el pipeline, no solo en la cabeza.",
    "conceptos": [
      "Fail build on audit.",
      "Trufflehog/gitleaks lite.",
      "Branch protection (idea)."
    ],
    "pasos_extra": "Crea o extiende workflow GitHub Actions / CI del repo. Documenta en `projects/m18-appsec/ci-appsec.md` qué corre en cada PR.\n\nEjecuta pipeline en branch de prueba y pega enlace/run id.",
    "lectura_rows": [
      [
        "OWASP",
        "DevSecOps guideline",
        "Ficha P3"
      ]
    ],
    "hecho": [
      "CI documentado.",
      "Audit en pipeline."
    ],
    "errores": [
      "CI que nunca falla.",
      "Secretos en workflow logs."
    ]
  },
  {
    "titulo": "Estructura del informe AppSec",
    "semana": 8,
    "horas": 5,
    "lectura": "Reporting + risk rating",
    "evidencia": "projects/m18-appsec/informe-appsec.md (borrador)",
    "objetivo": "Redactar informe ejecutivo+técnico: alcance, metodología, hallazgos, mitigaciones, riesgo residual.",
    "porque": "El proyecto único de M18 es comunicable a un design partner técnico.",
    "conceptos": [
      "Alcance staging/prod.",
      "CVSS lite (opcional).",
      "Residual risk honesto."
    ],
    "pasos_extra": "Plantilla en `informe-appsec.md`: Resumen, Metodología (OWASP+STRIDE), Tabla hallazgos, Recomendaciones, Anexo tests.\n\nEnlaza `findings-table.md` y threat-model-v1.",
    "lectura_rows": [
      [
        "Ficha",
        "proyecto M18",
        "—"
      ]
    ],
    "hecho": [
      "Borrador ≥4 secciones.",
      "Enlaces internos."
    ],
    "errores": [
      "Informe sin hallazgos reales.",
      "Copiar OWASP sin contexto."
    ]
  },
  {
    "titulo": "Tests de regresión de seguridad (≥3)",
    "semana": 8,
    "horas": 5,
    "lectura": "Security unit tests patterns",
    "evidencia": "≥3 tests en repo producto",
    "objetivo": "Consolidar tests: authz cross-user, input malicioso, headers o rate limit — al menos tres automatizados.",
    "porque": "Sin tests, el hardening se erosiona en el próximo feature.",
    "conceptos": [
      "Regression suite.",
      "CI los ejecuta.",
      "Nombres claros."
    ],
    "pasos_extra": "Lista tests en `projects/m18-appsec/security-tests.md` con archivo y qué protege.\n\nVerifica que CI los corre. Añade uno si faltan.",
    "lectura_rows": [
      [
        "Ficha",
        "M18 proyecto",
        "P2/P3"
      ]
    ],
    "hecho": [
      "≥3 tests listados.",
      "CI los ejecuta."
    ],
    "errores": [
      "Tests skipped.",
      "Solo manual."
    ]
  },
  {
    "titulo": "Cierre M18 — dominio y riesgo residual",
    "semana": 8,
    "horas": 5,
    "lectura": "Repaso completo M18",
    "evidencia": "projects/m18-appsec/informe-appsec.md final + README",
    "objetivo": "Finalizar informe, verificar P1–P3, criterios de dominio y handoff a M19 (deploy seguro).",
    "porque": "Cierras la capa B de seguridad antes de exponer el piloto en internet.",
    "conceptos": [
      "Checklist pre-deploy.",
      "Handoff M19.",
      "Dominio M18 checklist."
    ],
    "pasos_extra": "Actualiza `projects/m18-appsec/README.md` con índice de artefactos. Checklist ficha **Criterios de dominio** en `cierre-m18.md` con evidencia por ítem.\n\nEscribe 5 bullets **qué NO cubriste** (ej. pentest externo, WAF) como residual risk.",
    "lectura_rows": [
      [
        "Ficha",
        "M18-seguridad.md",
        "[Hilo seguridad](../../../hilos/seguridad.md)"
      ]
    ],
    "hecho": [
      "Informe final.",
      "P1–P3 verificables."
    ],
    "errores": [
      "Marcar dominio sin tests.",
      "Deploy público sin headers."
    ]
  }
]
""")


BODIES: dict[int, str] = {}

BODIES[1] = r"""
# L01 — Activos, actores y datos sensibles en Agenda Ops

**~5.0 h · Semana 1**

Sin lista de activos, el threat model es decoración. Hoy arrancas P1 y el hilo OWASP.

## Objetivo

Completar tablas Actores y ≥5 Activos en `projects/m18-appsec/threat-model-v0.md` (PII, credenciales, citas, tokens, Postgres).

## Pasos

### 1. Carpeta de evidencia (15 min)

Crea la estructura si aún no existe:

```bash
mkdir -p projects/m18-appsec/{docs,pocs,fixes,tests,ci,findings}
ls projects/m18-appsec
```
### 2. Actores y activos (80–100 min)

Abre `projects/m18-appsec/threat-model-v0.md`. Completa **Actores** (dueño, staff, cliente final, atacante anónimo) y **Activos** (≥5) con confidencialidad. Diagrama: navegador → API → Postgres.

```markdown
## Actores
| Actor | Objetivos | Capacidades |
|-------|-----------|-------------|
| Dueño (owner) | Gestionar negocio | CRUD total |
| Staff | Operar citas | CRUD limitado |
| Cliente final | Pedir cita | Solo sus datos |
| Atacante anónimo | Robar PII / sesión | Sin credenciales |

## Activos (≥5)
| Activo | Confidencialidad | Dónde vive |
|--------|------------------|------------|
| Teléfono cliente | Alta | `clientes.telefono` |
| Hash password | Crítica | `users.password_hash` |
| Notas de cita | Alta | `citas.notas` |
| Cookie de sesión | Crítica | `Set-Cookie` |
| Postgres | Crítica | volumen / hosting |
```
### 3. Superficie JSON + anti-secretos (30–40 min)

Marca qué campos salen en `GET /api/citas`. Ejecuta el barrido y anota rutas (sin pegar secretos):

```bash
git ls-files | rg -i 'env|secret|credential|\.pem' || true
```
### 4. Commit (10–15 min)

```bash
git add projects/m18-appsec/threat-model-v0.md
git status   # sin .env
git commit -m "docs(m18): l01 activos actores agenda ops"
```
"""

BODIES[2] = r"""
# L02 — Trust boundaries y flujos de confianza

**~5.0 h · Semana 1**

M10 y M13 nombraron boundaries; hoy los operacionalizas para AppSec.

## Objetivo

Documentar ≥4 límites y 3 flujos (login, crear cita, deep-link WA) en `projects/m18-appsec/trust-boundaries-appsec.md`.

## Pasos

### 1. Ancla M13 (20–30 min)

```bash
ls projects/m13-diseno/trust-boundaries.md 2>/dev/null || echo "(sin M13; parte de cero)"
touch projects/m18-appsec/trust-boundaries-appsec.md
```
### 2. Tabla de límites (70–90 min)

Por cada límite: origen, destino, protocolo, autenticación, datos. Mínimo 4.

```markdown
| Origen | Destino | Protocolo | Auth | Datos |
|--------|---------|-----------|------|-------|
| Browser | API | HTTPS | cookie/JWT | PII citas |
| API | Postgres | TCP | user app | SQL |
| API | SMTP futuro | TLS | API key | recordatorios |
| Operador | Hosting | SSH/HTTPS | MFA | logs, .env |
```
### 3. Flujos + abuso (40–50 min)

Para login, crear cita y deep-link WA: datos en tránsito, auth requerida, fallo si se omite authz. Una pregunta de abuso por límite.

```bash
printf "\n## Flujos\n- login:\n- crear cita:\n- deep-link WA:\n\n## Abuso por límite\n" >> projects/m18-appsec/trust-boundaries-appsec.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/trust-boundaries-appsec.md
git commit -m "docs(m18): l02 trust boundaries"
```
"""

BODIES[3] = r"""
# L03 — STRIDE aplicado al CRM de citas

**~5.0 h · Semana 1**

La matriz obliga a nombrar amenazas antes de buscar exploits al azar.

## Objetivo

Matriz STRIDE ≥4×6 en `projects/m18-appsec/stride-matrix.md` (login, citas, admin) con ≥3 amenazas priorizadas.

## Pasos

### 1. Plantilla STRIDE (25–35 min)

```bash
cat > projects/m18-appsec/stride-matrix.md <<'EOF'
# Matriz STRIDE — Agenda Ops

| Componente | S | T | R | I | D | E |
|------------|---|---|---|---|---|---|
| Login | | | | | | |
| Lista citas | | | | | | |
| Detalle cita | | | | | | |
| Admin usuarios | | | | | | |
EOF
```
### 2. Relleno del dominio (90–110 min)

Frases concretas (no “hackeo”). Ejemplo Login/Spoofing: “fuerza bruta o credenciales robadas”. Incluye IDOR en detalle cita e XSS en notas.

```markdown
| Componente | S | T | I |
|------------|---|---|---|
| Login | Fuerza bruta | Tamper cookie | Leak en error |
| Detalle cita | — | PUT sin authz | IDOR lee notas |
```
### 3. Prioriza 3 celdas (30 min)

Marca las 3 amenazas de las semanas 2–5. Enlaza `threat-model-v0.md`.

```bash
printf "\n## Prioridades (rojas)\n1. ...\n2. ...\n3. ...\n" >> projects/m18-appsec/stride-matrix.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/stride-matrix.md
git commit -m "docs(m18): l03 stride crm citas"
```
"""

BODIES[4] = r"""
# L04 — Threat model v0 y lectura OWASP Top 10

**~5.0 h · Semana 1**

Cierras la semana 1 con backlog de riesgo alineado a la industria.

## Objetivo

Mapa Top 10 en `projects/m18-appsec/owasp-top10-map.md` + `threat-model-v0.md` con riesgo residual semana 1.

## Pasos

### 1. Lectura Top 10 (40–50 min)

Lee OWASP Top 10 (2021) ES. Anota A01, A03, A07 como foco M18.

```bash
curl -sI https://owasp.org/Top10/es/ | head -5
```
### 2. Mapa 10 filas (70–90 min)

```bash
cat > projects/m18-appsec/owasp-top10-map.md <<'EOF'
# OWASP Top 10 → Agenda Ops

| Id | Ejemplo Agenda Ops | Mitigación | Semana |
|----|--------------------|------------|--------|
| A01 | GET /api/citas/:id cross-user | authz owner | 5 |
| A02 | secretos en repo | .env + rotación | 7 |
| A03 | búsqueda concat SQL | params/ORM | 4 |
| A04 | sin rate limit login | 429 | 5 |
| A05 | cookies sin flags | Secure/HttpOnly | 3 |
| A06 | deps vulnerables | npm audit | 7 |
| A07 | hash débil / sesión | bcrypt + rotate | 2 |
| A08 | integridad build | CI firmada (idea) | 8 |
| A09 | logs sin retención | política mínima | 8 |
| A10 | SSRF webhook futuro | allowlist | 6 |
EOF
```
### 3. Cierra threat-model-v0 (25–35 min)

Sección **Riesgo residual semana 1** (3 bullets). Confirma P1 tras semana 2 auth.

```bash
printf "\n## Riesgo residual semana 1\n- Auth aún no endurecida\n- Access control por verificar\n- Deps sin audit\n" >> projects/m18-appsec/threat-model-v0.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/owasp-top10-map.md projects/m18-appsec/threat-model-v0.md
git commit -m "docs(m18): l04 threat model v0 owasp"
```
"""

BODIES[5] = r"""
# L05 — Inventario de autenticación actual

**~5.0 h · Semana 2**

Antes de endurecer, documentas qué hay en M17. Fotografía del estado auth.

## Objetivo

`projects/m18-appsec/docs/auth-inventario.md`: mecanismo, almacenamiento token/sesión, endpoints públicos vs autenticados.

## Pasos

### 1. Inspección en el repo producto (40–50 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'bcrypt|argon2|passport|jsonwebtoken|express-session|setCookie|Set-Cookie|sign\(|verify\(' \
  -g '!node_modules' -g '!dist' | head -40
```
### 2. Inventario happy path + edges (70–90 min)

Describe paso a paso registro/login/logout y 2 edge cases (password malo, usuario inexistente). Sin passwords ni tokens reales.

```bash
mkdir -p projects/m18-appsec/docs
cat > projects/m18-appsec/docs/auth-inventario.md <<'EOF'
# Inventario de autenticación — Agenda Ops

## Endpoints
| Método | Ruta | Público | Notas |
|--------|------|---------|-------|
| POST | /auth/login | sí | |
| POST | /auth/logout | auth | |
| POST | /auth/register | ? | |

## Transporte / almacenamiento
- Cookie: nombre=… · HttpOnly=… · Secure=… · SameSite=…
- o `Authorization: Bearer …` (dónde se guarda en el cliente)

## Edge cases
1. Password malo → status/mensaje
2. Usuario inexistente → ¿mismo mensaje genérico?

## Riesgos preliminares
- localStorage vs cookie
- rotación de sesión
- logout incompleto
EOF
```
### 3. Verifica mensajes uniformes (20–30 min)

```bash
# Dos intentos; compara cuerpo (sin pegar tokens)
curl -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"noexiste@test.local","password":"x"}' | head -c 200
echo
curl -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"wrong"}' | head -c 200
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/docs/auth-inventario.md
git commit -m "docs(m18): l05 inventario autenticacion"
```
"""

BODIES[6] = r"""
# L06 — Hashing de contraseñas con bcrypt o argon2

**~5.0 h · Semana 2**

A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.

## Objetivo

Password nunca en MD5/SHA solo; bcrypt (cost ≥12) o argon2id. Nota en `projects/m18-appsec/docs/auth-hashing.md` + test.

## Pasos

### 1. Auditoría de hashes débiles (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'md5|sha1|sha256\(|createHash\(|crypto\.hash' -g '!node_modules' | rg -i 'pass|pwd|hash' || true
rg -n 'bcrypt|argon2' -g '!node_modules' | head -20
```
### 2. Confirmación o fix (70–90 min)

Si falta: lib madura + cost documentado. Ejemplo bcrypt:

```ts
import bcrypt from "bcrypt";

const ROUNDS = 12; // documenta en docs/auth-hashing.md

export async function hashPassword(plain: string): Promise<string> {
  return bcrypt.hash(plain, ROUNDS);
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

```bash
cat > projects/m18-appsec/docs/auth-hashing.md <<'EOF'
# Password hashing
- Algoritmo: bcrypt | argon2id
- Parámetros: cost/rounds = …
- Migación usuarios prueba: sí/no
- Commit fix (si hubo): …
EOF
```
### 3. Test round-trip (30–40 min)

```bash
npm test -- --testPathPattern=auth 2>/dev/null || npm test -- auth
# o: node -e "..." con compare true/false
```

```ts
// tests/security/password-hash.test.ts (ejemplo)
expect(await verifyPassword("secret", await hashPassword("secret"))).toBe(true);
expect(await hashPassword("secret")).not.toEqual("secret");
```
### 4. Commit (10 min)

```bash
git add -A
git commit -m "fix(m18): l06 password hashing"
```
"""

BODIES[7] = r"""
# L07 — Sesiones server-side vs JWT en Agenda Ops

**~5.0 h · Semana 2**

M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.

## Objetivo

ADR en `projects/m18-appsec/docs/adr-sesion-vs-jwt.md`: decisión, alternativas, impacto XSS/CSRF/móvil M20.

## Pasos

### 1. Compara en contexto (40–50 min)

Tabla pros/contras: panel+API same-site vs SPA cross-origin; revocación; HttpOnly vs `Authorization`.

```bash
mkdir -p projects/m18-appsec/docs
cat > projects/m18-appsec/docs/adr-sesion-vs-jwt.md <<'EOF'
# ADR — Sesión server-side vs JWT

## Contexto
Agenda Ops: panel web + API; móvil M20 futuro.

## Opciones
| Opción | Revocación | XSS | CSRF | Móvil |
|--------|------------|-----|------|-------|
| Sesión + cookie HttpOnly | inmediata (DB) | mejor | riesgo CSRF | cookie jar |
| JWT en memoria / header | short TTL / deny-list | si en storage, peor | menos CSRF | natural |
| Híbrido | … | … | … | … |

## Decisión
…

## Consecuencias / mitigaciones obligatorias
- HttpOnly / TTL / revoke / SameSite …
EOF
```
### 2. Prueba logout/reuse (40–50 min)

Login → copiar cookie/token → logout → reutilizar (debe fallar). Anota en la ADR.

```bash
# Ejemplo cookie de sesión (ajusta nombre/URL)
curl -c /tmp/m18-cj -s -X POST localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' -o /dev/null -w "%{http_code}\n"
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout -w "%{http_code}\n"
curl -b /tmp/m18-cj -s localhost:3000/api/citas -w "\n%{http_code}\n" | tail -3
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/adr-sesion-vs-jwt.md
git commit -m "docs(m18): l07 adr sesion jwt"
```
"""

BODIES[8] = r"""
# L08 — Threat model v1 post-autenticación (P1)

**~5.0 h · Semana 2**

P1 exige v1 revisado tras entender login; hoy entregas el hito.

## Objetivo

`projects/m18-appsec/threat-model-v1.md` con controles auth, tabla amenaza→control y residual.

## Pasos

### 1. Diff v0→v1 (30–40 min)

```bash
cp projects/m18-appsec/threat-model-v0.md projects/m18-appsec/threat-model-v1.md
printf "\n## Controles auth (post L05–L07)\n| Amenaza | Control | Estado | Commit/issue |\n|---------|---------|--------|--------------|\n| Hash débil | bcrypt/argon2 | OK/TODO | |\n| Sesión robable | HttpOnly plan | | |\n| Sin revoke | ADR decisión | | |\n" >> projects/m18-appsec/threat-model-v1.md
```
### 2. Redacción P1 (80–100 min)

Enlaza `projects/m18-appsec/docs/auth-inventario.md` y ADR. Supuestos de staging. Tabla amenaza|control|estado legible sin abrir el código.

```bash
printf "\n## Enlaces\n- auth: docs/auth-inventario.md\n- ADR: docs/adr-sesion-vs-jwt.md\n\n## Residual auth\n- ...\n" >> projects/m18-appsec/threat-model-v1.md
```
### 3. README P1 (15 min)

En `projects/m18-appsec/README.md` marca P1 entregado con fecha y ruta a `threat-model-v1.md`.

```bash
rg -n "P1|threat-model-v1" projects/m18-appsec/README.md || printf "\n- **P1:** threat-model-v1.md $(date -I)\n" >> projects/m18-appsec/README.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/threat-model-v1.md projects/m18-appsec/README.md
git commit -m "docs(m18): l08 threat model v1 p1"
```
"""

BODIES[9] = r"""
# L09 — Cookies Secure, HttpOnly y SameSite

**~5.0 h · Semana 3**

Atributos correctos o sesión robable. Hoy aplicas flags en tu stack.

## Objetivo

Tabla real de cookies en `projects/m18-appsec/pocs/cookies.md`; fix Secure/HttpOnly/SameSite si faltan.

## Pasos

### 1. Inspección Set-Cookie (30–40 min)

```bash
curl -sI -X POST localhost:3000/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' | rg -i 'set-cookie|HTTP/
```
### 2. Documenta + harden (70–90 min)

```bash
cat > projects/m18-appsec/pocs/cookies.md <<'EOF'
# Cookies lab
| Nombre | HttpOnly | Secure | SameSite | Path | Max-Age |
|--------|----------|--------|----------|------|---------|
| sid? | | | | | |

## Antes / después
- Antes: …
- Después: …
## ¿JS puede leer la cookie de sesión?
document.cookie → …
EOF
```

Ejemplo Express / cookie-session:

```ts
res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: "lax", // o "strict" si no hay cross-site legítimo
  path: "/",
});
```
### 3. Prueba HttpOnly (20 min)

En DevTools Console (sesión logueada): `document.cookie` no debe mostrar la cookie de sesión. Captura redactada en `pocs/cookies.md`.
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/cookies.md
git commit -m "fix(m18): l09 cookie flags"
```
"""

BODIES[10] = r"""
# L10 — CSRF en formularios y mutaciones state-changing

**~5.0 h · Semana 3**

Un atacante no necesita XSS si tu sesión acepta POST cross-site.

## Objetivo

Lista rutas mutables + protección en `projects/m18-appsec/pocs/csrf-notes.md`; ≥1 ruta crítica con token/SameSite; curl sin token → 403.

## Pasos

### 1. Inventario mutaciones (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\.(post|put|patch|delete)\(" -g '*.ts' -g '!node_modules' | head -40
cat > projects/m18-appsec/pocs/csrf-notes.md <<'EOF'
# CSRF notes
| Ruta | Método | Protección | Estado |
|------|--------|------------|--------|
| /api/citas | POST | | |
| /api/citas/:id | PUT/DELETE | | |
| /auth/logout | POST | | |
EOF
```
### 2. Protege la ruta crítica (70–90 min)

Token sincronizado, double-submit o SameSite estricto + método seguro. Ejemplo chequeo:

```ts
// middleware mínimo (ilustrativo)
export function requireCsrf(req, res, next) {
  const token = req.headers["x-csrf-token"] || req.body?._csrf;
  if (!token || token !== req.session?.csrfToken) {
    return res.status(403).json({ error: "csrf" });
  }
  next();
}
```
### 3. curl sin token (20–30 min)

```bash
# Con cookie de sesión válida pero sin CSRF → 403
curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/citas \
  -H 'content-type: application/json' -b /tmp/m18-cj \
  -d '{"clienteId":"…","inicio":"2026-01-01T10:00:00Z"}'
# esperado: 403
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/csrf-notes.md
git commit -m "fix(m18): l10 csrf mutaciones"
```
"""

BODIES[11] = r"""
# L11 — Fijación de sesión y logout completo

**~5.0 h · Semana 3**

Robar sesión fija es clásico en apps que reutilizan el mismo session id.

## Objetivo

Ciclo de vida en `projects/m18-appsec/docs/session-lifecycle.md`: rotate post-login + destroy server-side en logout.

## Pasos

### 1. Traza el ciclo en código (40–50 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'regenerate|session\.id|destroy|logout|revoke' -g '!node_modules' | head -30
cat > projects/m18-appsec/docs/session-lifecycle.md <<'EOF'
# Session lifecycle
1. Pre-login id: …
2. Post-login (¿rota?): …
3. Logout server-side: …
4. Request posterior con cookie vieja: esperado 401
EOF
```
### 2. Pruebas login/logout (50–60 min)

```bash
# Dos logins: ¿cambia el valor de Set-Cookie?
curl -sI -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"owner@test.local","password":"***"}' | rg -i set-cookie
# Logout + reuse (debe fallar)
curl -b /tmp/m18-cj -s -X POST localhost:3000/auth/logout
curl -b /tmp/m18-cj -s -o /dev/null -w "%{http_code}\n" localhost:3000/api/citas
```

Si JWT stateless: documenta deny-list o TTL corto en el mismo archivo.
### 3. Commit (10–15 min)

```bash
git add projects/m18-appsec/docs/session-lifecycle.md
git commit -m "fix(m18): l11 session lifecycle"
```
"""

BODIES[12] = r"""
# L12 — Checklist cookies y CSRF en staging

**~5.0 h · Semana 3**

Operacionalizas controles para M19 deploy y trials M22.

## Objetivo

Checklist ≥10 ítems en `projects/m18-appsec/docs/checklist-cookies-csrf.md` ejecutado contra staging (fecha + URL).

## Pasos

### 1. Escribe el checklist (40–50 min)

```bash
cat > projects/m18-appsec/docs/checklist-cookies-csrf.md <<'EOF'
# Checklist cookies / CSRF — staging

Fecha: ____ · URL: ____

| # | Ítem | Sí/No | Nota |
|---|------|-------|------|
| 1 | Cookie sesión HttpOnly | | |
| 2 | Secure en HTTPS | | |
| 3 | SameSite Lax/Strict | | |
| 4 | Session id rota post-login | | |
| 5 | Logout invalida server-side | | |
| 6 | POST citas exige CSRF/equiv | | |
| 7 | GET no muta estado | | |
| 8 | Mensajes login genéricos | | |
| 9 | HTTPS redirect (si aplica) | | |
| 10 | Sin cookie sesión en document.cookie | | |

## Residual CSRF
- …

## Commits semana 3
- …
EOF
```
### 2. Ejecuta en staging/local (60–80 min)

Marca Sí/No con evidencia (curl headers, captura redactada). Corrige ≥1 ítem No si aparece.

```bash
curl -sI https://<tu-staging>/ | rg -i 'strict-transport|set-cookie' || true
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/checklist-cookies-csrf.md
git commit -m "docs(m18): l12 checklist cookies csrf"
```
"""

BODIES[13] = r"""
# L13 — SQLi: reproducir en tu propia API

**~5.0 h · Semana 4**

Solo contra tu API. P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.

## Objetivo

PoC o “no reproducible con ORM” en `projects/m18-appsec/findings/001-sqli.md` (sin PII real).

## Pasos

### 1. Caza concatenación SQL (50–60 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\$\{|query\(|\.query\(|execute\(|raw\(|sql`" -g '!node_modules' | head -50
rg -n "SELECT.*\+|WHERE.*\+" -g '*.ts' -g '*.js' | head -20 || true
```
### 2. PoC controlada (60–80 min)

Cuenta de prueba. Payload en búsqueda clientes/citas. **No** `DROP` en staging compartido.

```bash
mkdir -p projects/m18-appsec/findings projects/m18-appsec/pocs
cat > projects/m18-appsec/findings/001-sqli.md <<'EOF'
# Finding 001 — SQLi
- Endpoint:
- Payload (ejemplo): `' OR '1'='1`
- Respuesta / impacto:
- ¿ORM parametrizado? evidencia:
- PII: ninguna en este reporte
EOF
# Ejemplo de prueba (ajusta query param)
curl -sG "localhost:3000/api/clientes" --data-urlencode "q=' OR '1'='1" | head -c 400
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/001-sqli.md
git commit -m "docs(m18): l13 poc sqli"
```
"""

BODIES[14] = r"""
# L14 — Mitigar SQLi: queries parametrizadas y permisos DB

**~5.0 h · Semana 4**

Hallazgo sin fix no cuenta para P2.

## Objetivo

Fix parametrizado + test de regresión; `001-sqli.md` → Cerrado con commit hash.

## Pasos

### 1. Parametriza la query (60–80 min)

```ts
// MAL
// db.query(`SELECT * FROM clientes WHERE nombre LIKE '%${q}%'`)

// BIEN (pg)
await db.query(
  "SELECT id, nombre, telefono FROM clientes WHERE nombre ILIKE $1 LIMIT 50",
  [`%${q}%`],
);
```

```sql
-- Usuario app sin DDL (idea)
-- CREATE ROLE agenda_app LOGIN PASSWORD '...';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO agenda_app;
-- (sin CREATE/DROP)
```
### 2. Test de regresión (40–50 min)

```ts
// tests/security/sqli-search.test.ts
it("rejects or safely handles SQLi-like search", async () => {
  const res = await api.get("/api/clientes", { q: "' OR '1'='1" });
  expect(res.status).not.toBe(500);
  expect(String(res.body)).not.toMatch(/syntax error|pg_|SQL/i);
});
```

```bash
npm test -- --testPathPattern=sqli || npm test -- security
```
### 3. Cierra finding (20 min)

```bash
printf "\n## Estado: Cerrado\n- Commit fix: \n- Test: \n" >> projects/m18-appsec/findings/001-sqli.md
git add -A && git commit -m "fix(m18): l14 sqli parametrized"
```
"""

BODIES[15] = r"""
# L15 — XSS reflejado en campos de cliente o búsqueda

**~5.0 h · Semana 4**

XSS roba sesiones si las cookies son legibles por JS.

## Objetivo

PoC reflejado en `projects/m18-appsec/findings/002-xss-reflected.md` (solo tu cuenta de prueba; sin exfiltración externa).

## Pasos

### 1. Localiza render de input (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'dangerouslySetInnerHTML|innerHTML|\$\{.*q|searchParams|mensaje' -g '!node_modules' | head -30
```
### 2. PoC local (60–80 min)

Payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`. Solo impacto local.

```bash
cat > projects/m18-appsec/findings/002-xss-reflected.md <<'EOF'
# Finding 002 — XSS reflejado
- Pantalla / query:
- Payload:
- ¿Ejecutó en el navegador? sí/no
- Contexto (HTML text / attr / JS):
EOF
# Ejemplo
curl -sG "localhost:3000/clientes" --data-urlencode "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/002-xss-reflected.md
git commit -m "docs(m18): l15 poc xss reflected"
```
"""

BODIES[16] = r"""
# L16 — XSS almacenado y escape en plantillas/API

**~5.0 h · Semana 4**

El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.

## Objetivo

Fix escape/sanitización; actualizar finding; filas SQLi+XSS en `projects/m18-appsec/findings-table.md`.

## Pasos

### 1. Stored en notas de cita (50–60 min)

```bash
# Crea cita con payload en notas (cuenta prueba)
curl -s -X POST localhost:3000/api/citas -H 'content-type: application/json' -b /tmp/m18-cj \
  -d '{"clienteId":"…","inicio":"2026-01-02T10:00:00Z","notas":"<img src=x onerror=alert(1)>"}'
# Lista y verifica escape en HTML
```
### 2. Fix + test (60–80 min)

Usa textContent / escape del framework; evita `dangerouslySetInnerHTML` con input usuario.

```ts
// API: devolver texto; el front escapa al render
// Test:
it("escapes stored XSS in notas", async () => {
  const payload = "<script>alert(1)</script>";
  await createCita({ notas: payload });
  const html = await renderListaCitas();
  expect(html).not.toContain("<script>");
  expect(html).toContain("&lt;script&gt;") // o equivalente escapado
});
```
### 3. Tabla P2 (20–30 min)

```bash
cat > projects/m18-appsec/findings-table.md <<'EOF'
# Findings P2
| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | | |
| 002 | A03/XSS | findings/002-xss-reflected.md | | |
EOF
git add -A && git commit -m "fix(m18): l16 xss stored escape"
```
"""

BODIES[17] = r"""
# L17 — IDOR en citas y recursos por ID

**~5.0 h · Semana 5**

Ocultar botones no basta: autorización server-side.

## Objetivo

PoC cross-user en `projects/m18-appsec/findings/003-idor.md` con dos cuentas de prueba.

## Pasos

### 1. Dos usuarios de prueba (20–30 min)

```bash
# Login A y B; guarda cookies separadas
curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"a@test.local","password":"***"}' -o /dev/null
curl -c /tmp/m18-b -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"b@test.local","password":"***"}' -o /dev/null
```
### 2. PoC IDOR (60–80 min)

A crea cita → B intenta `GET/PUT /api/citas/:id`.

```bash
CITA_ID=…  # id creado por A
curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-b localhost:3000/api/citas/$CITA_ID
# esperado tras fix: 403 o 404 (no 200 con datos de A)

cat > projects/m18-appsec/findings/003-idor.md <<'EOF'
# Finding 003 — IDOR
- Ruta: GET/PUT /api/citas/:id
- Pasos:
- Impacto:
- Estado:
EOF
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/003-idor.md
git commit -m "docs(m18): l17 poc idor"
```
"""

BODIES[18] = r"""
# L18 — Autorización por rol owner vs staff

**~5.0 h · Semana 5**

Agenda Ops distingue dueño y staff; la API debe hacerlo explícito.

## Objetivo

Matriz rol×recurso×acción en `projects/m18-appsec/docs/rbac-matrix.md` + ≥1 prueba manual de gap.

## Pasos

### 1. Matriz RBAC (50–60 min)

```bash
cat > projects/m18-appsec/docs/rbac-matrix.md <<'EOF'
# RBAC — Agenda Ops
| Recurso / acción | Owner | Staff | Anónimo |
|------------------|-------|-------|---------|
| Listar citas | ✓ | ✓ (alcance) | ✗ |
| Crear cita | ✓ | ✓ | ✗ |
| Borrar cualquier cita | ✓ | ? | ✗ |
| Configuración negocio | ✓ | ✗ | ✗ |
| Gestionar usuarios | ✓ | ✗ | ✗ |

## Gaps código vs SRS
- …
## Prueba manual
- Actor: staff · Acción: … · Resultado HTTP: …
EOF
```
### 2. Prueba staff vs owner (50–70 min)

```bash
curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-staff \
  -X PATCH localhost:3000/api/settings -H 'content-type: application/json' -d '{"tz":"UTC"}'
# esperado: 403
```

```ts
// guard ilustrativo
if (req.user.role !== "owner") return res.status(403).json({ error: "forbidden" });
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/rbac-matrix.md
git commit -m "docs(m18): l18 rbac matrix"
```
"""

BODIES[19] = r"""
# L19 — Rate limiting en login y endpoints sensibles

**~5.0 h · Semana 5**

Sin rate limit, A07 y DoS ligero son triviales.

## Objetivo

Límite en login (+1 endpoint costoso); prueba 429 documentada; nota en findings.

## Pasos

### 1. Middleware o proxy (60–80 min)

```ts
import rateLimit from "express-rate-limit";

export const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "too_many_requests" },
});

// app.post("/auth/login", loginLimiter, loginHandler);
```
### 2. Prueba de bloqueo (40–50 min)

```bash
for i in $(seq 1 25); do
  curl -s -o /dev/null -w "$i:%{http_code}\n" -X POST localhost:3000/auth/login \
    -H 'content-type: application/json' \
    -d '{"email":"owner@test.local","password":"wrong"}'
done | tail -5
# espera ver 429

printf "\n## Rate limit login\n- window: 15m · max: 20\n- prueba: ver 429 tras N intentos\n- reset dev: reiniciar proceso / redis FLUSH\n" >> projects/m18-appsec/findings-table.md
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "fix(m18): l19 rate limit login"
```
"""

BODIES[20] = r"""
# L20 — Tests automatizados cross-user (P2 avance)

**~5.0 h · Semana 5**

P2 pide hallazgo→fix→test; hoy consolidas access control.

## Objetivo

≥2 tests authz (cross-user + rol) + `projects/m18-appsec/findings-table.md` con ≥3 filas.

## Pasos

### 1. Fixture dos usuarios (30–40 min)

```ts
// tests/security/authz-cross-user.test.ts
async function login(email: string) { /* cookie jar / token */ }

it("B cannot read A's cita", async () => {
  const a = await login("a@test.local");
  const b = await login("b@test.local");
  const cita = await a.post("/api/citas", { /* … */ });
  const res = await b.get(`/api/citas/${cita.id}`);
  expect([403, 404]).toContain(res.status);
});

it("staff cannot patch settings", async () => {
  const staff = await login("staff@test.local");
  const res = await staff.patch("/api/settings", { tz: "UTC" });
  expect(res.status).toBe(403);
});
```
### 2. Corre tests + actualiza tabla (60–80 min)

```bash
npm test -- --testPathPattern=authz || npm test -- security
# Actualiza findings-table: 001–003 + rate limit
rg -n '^\|' projects/m18-appsec/findings-table.md
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "test(m18): l20 authz cross-user"
```
"""

BODIES[21] = r"""
# L21 — SSRF: superficie en webhooks e integraciones

**~5.0 h · Semana 6**

Aun sin feature URL, documentar el control evita sorpresas en M26.

## Objetivo

Doc SSRF + allowlist en `projects/m18-appsec/findings/004-ssrf.md`. Sin escanear terceros ni metadata cloud en prod.

## Pasos

### 1. Busca fetch server-side (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'fetch\(|axios\.|got\(|request\(|http\.get' -g '!node_modules' | head -40
```
### 2. Diseño / PoC aislada (70–90 min)

Si no hay feature: simula diseño. Si hay: prueba URL interna **solo en staging aislado**.

```bash
cat > projects/m18-appsec/findings/004-ssrf.md <<'EOF'
# Finding 004 — SSRF (superficie)
## ¿Hay URL server-side hoy?
- webhook / import / avatar: sí/no · ruta:

## Riesgo ilustrativo
`http://169.254.169.254/` (metadata) — **no probar en cloud compartido**

## Allowlist propuesta
- hosts: `hooks.stripe.com`, …
- schemata: https only
- bloqueo: link-local, RFC1918, localhost

## Estado
- N/A feature | Mitigado | Abierto
EOF
```

```ts
function assertSafeUrl(raw: string) {
  const u = new URL(raw);
  if (u.protocol !== "https:") throw new Error("scheme");
  const allow = new Set(["hooks.example.com"]);
  if (!allow.has(u.hostname)) throw new Error("host");
}
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/004-ssrf.md
git commit -m "docs(m18): l21 ssrf superficie"
```
"""

BODIES[22] = r"""
# L22 — Subida de archivos segura

**~5.0 h · Semana 6**

Un .php disfrazado de .jpg es folklore porque sigue pasando.

## Objetivo

Checklist o prueba real en `projects/m18-appsec/findings/005-upload.md`: tipo/tamaño, nombre aleatorio, fuera de webroot.

## Pasos

### 1. Superficie upload (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'multer|formidable|multipart|upload|createWriteStream' -g '!node_modules' | head -30
```
### 2. Checklist / prueba (70–90 min)

```bash
cat > projects/m18-appsec/findings/005-upload.md <<'EOF'
# Finding 005 — Upload
## ¿Hay upload hoy?
- ruta / campo:

## Controles
| Control | Sí/No |
|---------|-------|
| Allowlist MIME + magic bytes | |
| Tamaño máximo | |
| Nombre aleatorio (uuid) | |
| Fuera de `public/` / webroot | |
| No ejecutable por el server | |

## Prueba (si aplica)
- archivo: `pocs/evil.jpg.html` o similar
- resultado:
EOF
```

```ts
// multer sketch
const upload = multer({
  storage: multer.diskStorage({
    destination: "/var/agenda/uploads", // fuera de public
    filename: (_req, _file, cb) => cb(null, `${crypto.randomUUID()}`),
  }),
  limits: { fileSize: 2_000_000 },
  fileFilter: (_req, file, cb) => {
    cb(null, ["image/png", "image/jpeg"].includes(file.mimetype));
  },
});
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/005-upload.md
git commit -m "docs(m18): l22 upload checklist"
```
"""

BODIES[23] = r"""
# L23 — Deserialización y JSON peligroso

**~5.0 h · Semana 6**

Node rara vez hace Java deserialization, pero prototype pollution y lógica sí.

## Objetivo

`projects/m18-appsec/docs/json-trust.md`: endpoints + schema; límite de body; ≥1 mejora commitada.

## Pasos

### 1. Inventario JSON bodies (40–50 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "express\.json|bodyParser|z\.object|Joi\.|safeParse" -g '!node_modules' | head -40
cat > projects/m18-appsec/docs/json-trust.md <<'EOF'
# JSON trust
| Endpoint | Schema (zod/joi/…) | Límite body | Notas |
|----------|--------------------|-------------|-------|
| POST /auth/login | | | |
| POST /api/citas | | | |
EOF
```
### 2. Límite + rechazo campos extra (60–80 min)

```ts
app.use(express.json({ limit: "100kb" }));

// zod: strip o strict
const CitaInput = z.object({
  clienteId: z.string().uuid(),
  inicio: z.string().datetime(),
  notas: z.string().max(2000).optional(),
}).strict();
```

```bash
# Payload enorme → 413
python3 - <<'PY'
print('{"x":"' + ('a'*200000) + '"}')
PY | curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/citas \
  -H 'content-type: application/json' -b /tmp/m18-cj --data-binary @-
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/json-trust.md
git commit -m "fix(m18): l23 json trust limits"
```
"""

BODIES[24] = r"""
# L24 — Consolidar hallazgos semana 6 en P2

**~5.0 h · Semana 6**

Mitad del módulo: P2 debe ser visible en git (≥5 hallazgos).

## Objetivo

`projects/m18-appsec/findings-table.md` con ≥5 filas PoC→fix→test (o plan fechado); sin secretos.

## Pasos

### 1. Auditoría de la tabla (40–50 min)

```bash
wc -l projects/m18-appsec/findings/*.md
cat projects/m18-appsec/findings-table.md
# Completa hasta ≥5 filas (001–005 + rate limit / headers si aplica)
```
### 2. Cierra gaps (80–100 min)

Cada fila: ID, OWASP, PoC, commit fix, test/link. Issues para abiertos con fecha semana 7–8.

```markdown
| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | abc123 | security/sqli |
| 002 | XSS | findings/002-… | | |
| 003 | A01 | findings/003-idor.md | | authz |
| 004 | SSRF | findings/004-ssrf.md | n/a diseño | |
| 005 | Upload | findings/005-upload.md | | |
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings-table.md
git commit -m "docs(m18): l24 findings table p2"
```
"""

BODIES[25] = r"""
# L25 — npm audit y cadena de dependencias

**~5.0 h · Semana 7**

A06: la cadena de deps es superficie. Hoy mides y remedias al menos un high/critical.

## Objetivo

Salida de audit en `projects/m18-appsec/docs/npm-audit.md` (+ mirror `projects/m18-appsec/deps-audit.md` si quieres); ≥1 remediación o justificación.

## Pasos

### 1. Corre audit (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
npm audit --omit=dev 2>/dev/null || npm audit
npm audit --json > /tmp/m18-audit.json || true
mkdir -p projects/m18-appsec/docs
cp /tmp/m18-audit.json projects/m18-appsec/docs/npm-audit.json 2>/dev/null || true
```
### 2. Documenta + remedia (70–90 min)

```bash
cat > projects/m18-appsec/docs/npm-audit.md <<'EOF'
# npm audit — Agenda Ops
Fecha:
High/Critical:
Acción (update / ignore justificado):
Commit:
EOF
# Remedia al menos 1
npm audit fix --omit=dev || true
npm ls --depth=0 | head
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/npm-audit.md
git commit -m "docs(m18): l25 npm audit"
```
"""

BODIES[26] = r"""
# L26 — Secretos, .env y rotación

**~5.0 h · Semana 7**

Secretos en git son incidentes. Inventario (sin valores) + plan de rotación.

## Objetivo

`projects/m18-appsec/docs/rotacion-secretos.md`: inventario, dónde viven, pasos rotar session secret / DB URL.

## Pasos

### 1. Busca secretos en historial (30–40 min)

```bash
git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
git ls-files | rg -i '\.env|credential|secret|\.pem' || true
# gitleaks / trufflehog si los tienes instalados
```
### 2. Inventario + rotación (70–90 min)

```bash
cat > projects/m18-appsec/docs/rotacion-secretos.md <<'EOF'
# Secretos y rotación
| Secreto | Dónde (local/staging) | En git? | Rotar cómo |
|---------|----------------------|---------|------------|
| DATABASE_URL | .env / PaaS | no | … |
| SESSION_SECRET | .env | no | reiniciar sesiones |
| SMTP_KEY | … | | |

## Pasos rotar SESSION_SECRET (staging)
1. Generar nuevo valor
2. Deploy
3. Invalidar sesiones previas
4. Verificar login
EOF
```

```bash
# Genera candidato (no lo commits)
openssl rand -hex 32
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/rotacion-secretos.md
git status   # .env no debe aparecer
git commit -m "docs(m18): l26 rotacion secretos"
```
"""

BODIES[27] = r"""
# L27 — Cabeceras de seguridad con Helmet o equivalente

**~5.0 h · Semana 7**

Headers baratos reducen XSS clickjacking y MIME sniffing.

## Objetivo

Helmet (o equiv) en la API/front; captura `curl -I` en evidencia.

## Pasos

### 1. Baseline headers (20–30 min)

```bash
curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-before.txt | rg -i 'x-|content-security|strict-transport|referrer|permissions'|| true
```
### 2. Activa Helmet (60–80 min)

```ts
import helmet from "helmet";
app.use(helmet({
  contentSecurityPolicy: false, // CSP en L28
  frameguard: { action: "deny" },
  noSniff: true,
  referrerPolicy: { policy: "no-referrer" },
}));
```

```bash
curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-after.txt
diff -u projects/m18-appsec/pocs/headers-before.txt projects/m18-appsec/pocs/headers-after.txt || true
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/headers-*.txt
git commit -m "fix(m18): l27 security headers"
```
"""

BODIES[28] = r"""
# L28 — CSP básica sin romper Agenda Ops

**~5.0 h · Semana 7**

CSP report-only primero: observas violaciones sin romper el panel.

## Objetivo

Política en `projects/m18-appsec/docs/csp.md`; report-only en staging; anota violaciones.

## Pasos

### 1. Inventaria fuentes (30–40 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'cdn\.|googleapis|script src|link href' -g '*.html' -g '*.tsx' -g '*.jsx' | head -30
cat > projects/m18-appsec/docs/csp.md <<'EOF'
# CSP — Agenda Ops
## Fuentes externas
- …

## Política propuesta (report-only)
default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none';

## Violaciones observadas
- …
EOF
```
### 2. Report-Only (60–80 min)

```ts
app.use((_req, res, next) => {
  res.setHeader(
    "Content-Security-Policy-Report-Only",
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'",
  );
  next();
});
```

```bash
curl -sI localhost:3000/ | rg -i content-security-policy
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/csp.md
git commit -m "docs(m18): l28 csp report-only"
```
"""

BODIES[29] = r"""
# L29 — Pipeline CI: lint, test, audit, anti-secretos

**~5.0 h · Semana 8**

P3: cada PR corre lint+test+audit (+ grep secretos).

## Objetivo

Workflow documentado en `projects/m18-appsec/ci/ci-appsec.yml` (o enlace) + `projects/m18-appsec/ci/README.md` con run id.

## Pasos

### 1. Scaffold workflow (40–50 min)

```bash
mkdir -p projects/m18-appsec/ci
cat > projects/m18-appsec/ci/ci-appsec.yml <<'EOF'
# Copiar a .github/workflows/appsec.yml del repo producto
name: appsec
on: [pull_request, push]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm audit --audit-level=high
      - name: anti-secrets
        run: |
          ! git ls-files | rg -i '\.env$|id_rsa|\.pem$'
EOF
```
### 2. Ejecuta en branch de prueba (60–80 min)

Copia al repo producto, push, pega run id en `projects/m18-appsec/ci/README.md`.

```bash
cat > projects/m18-appsec/ci/README.md <<'EOF'
# CI AppSec
- Workflow: .github/workflows/appsec.yml
- Run id / URL:
- Jobs: lint, test, audit, anti-secrets
EOF
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/ci
git commit -m "ci(m18): l29 pipeline p3"
```
"""

BODIES[30] = r"""
# L30 — Estructura del informe AppSec

**~5.0 h · Semana 8**

El entregable del proyecto es el informe: ejecutivo, alcance, hallazgos, mitigaciones, residual.

## Objetivo

Borrador `projects/m18-appsec/informe-appsec.md` enlazando PoCs y commits (sin PII de partner).

## Pasos

### 1. Plantilla (25–35 min)

```bash
cat > projects/m18-appsec/informe-appsec.md <<'EOF'
# Informe AppSec — Agenda Ops

## 1. Ejecutivo
- …

## 2. Alcance y supuestos
- Solo staging/local propio
- Fuera de alcance: …

## 3. Metodología
STRIDE + OWASP Top 10 + PoC en API propia

## 4. Hallazgos
Tabla → ver findings-table.md (severidad, estado)

## 5. Mitigaciones
Commits / PRs: …

## 6. Riesgo residual
Top 3 con dueño/fecha

## 7. Anexos
- threat-model-v1.md
- docs/auth-inventario.md
- ci/
EOF
```
### 2. Redacción con enlaces (90–110 min)

Rellena §§1–6 con datos reales de tu P2/P3. Verifica que no hay secretos ni teléfonos reales.

```bash
rg -n 'password|Bearer |postgresql://|@gmail' projects/m18-appsec/informe-appsec.md || echo "sin secretos obvios"
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/informe-appsec.md
git commit -m "docs(m18): l30 informe appsec"
```
"""

BODIES[31] = r"""
# L31 — Tests de regresión de seguridad (≥3)

**~5.0 h · Semana 8**

≥3 tests que fallen si reabres agujeros (IDOR, XSS escape, authz rol u equivalentes).

## Objetivo

Suite documentada en `projects/m18-appsec/docs/security-tests.md`; CI los corre.

## Pasos

### 1. Selecciona 3 (20–30 min)

```bash
cat > projects/m18-appsec/docs/security-tests.md <<'EOF'
# Security regression tests
| # | Archivo | Protege |
|---|---------|---------|
| 1 | tests/security/authz-cross-user.test.ts | IDOR citas |
| 2 | tests/security/xss-escape.test.ts | stored XSS notas |
| 3 | tests/security/rbac-settings.test.ts | staff≠owner |
EOF
```
### 2. Implementa / verde (100–120 min)

Nombres claros `security.*.test.ts` (o carpeta `tests/security/`).

```bash
npm test -- --testPathPattern=security
# Confirma que el workflow L29 incluye este pattern
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "test(m18): l31 regresion seguridad"
```
"""

BODIES[32] = r"""
# L32 — Cierre M18 — dominio y riesgo residual

**~5.0 h · Semana 8**

Riesgo residual explícito > “somos seguros”. Cierra P1–P3 y handoff a M19/M25.

## Objetivo

`projects/m18-appsec/informe-appsec.md` final + README con residual top-3 y criterios de dominio.

## Pasos

### 1. Auditoría de evidencias (40–50 min)

```bash
ls -la projects/m18-appsec projects/m18-appsec/docs projects/m18-appsec/findings projects/m18-appsec/ci projects/m18-appsec/pocs
test -f projects/m18-appsec/threat-model-v1.md && echo P1=ok
wc -l projects/m18-appsec/findings-table.md
test -f projects/m18-appsec/ci/ci-appsec.yml && echo P3=ok
test -f projects/m18-appsec/docs/auth-inventario.md && echo auth=ok
```
### 2. Residual + handoff (50–60 min)

```bash
printf "\n## Riesgo residual (cierre)\n| Riesgo | Dueño | Fecha revisión |\n|--------|-------|----------------|\n| … | | |\n\n## Handoff\n- M19: secrets en PaaS, HTTPS, backups\n- M25: retest en trial\n" >> projects/m18-appsec/informe-appsec.md
```
### 3. README final (20–30 min)

Actualiza `projects/m18-appsec/README.md`: P1/P2/P3 ✅, enlace informe, residual.

```bash
git add projects/m18-appsec/README.md projects/m18-appsec/informe-appsec.md
git commit -m "docs(m18): l32 cierre dominio residual"
```
"""

