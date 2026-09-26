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
      "Diagrama ASCII o Mermaid del piloto.",
      "Comando anti-secretos ejecutado y anotado."
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
      "Pregunta de abuso por límite.",
      "Enlace a diseño M13 si aplica."
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
      "≥3 amenazas priorizadas.",
      "Lenguaje del dominio Agenda Ops."
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
      "threat-model-v0 actualizado.",
      "Commit semana 1."
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
    "evidencia": "projects/m18-appsec/auth-inventory.md",
    "objetivo": "Documentar flujo real de registro/login/logout de Agenda Ops: transporte, almacenamiento de sesión, rotación y recuperación de contraseña.",
    "porque": "No puedes endurecer lo que no has descrito. Esta lección es fotografía del estado antes de parches.",
    "conceptos": [
      "Credencial vs sesión vs token.",
      "Transporte HTTPS obligatorio.",
      "Mensajes de error uniformes."
    ],
    "pasos_extra": "En `projects/m18-appsec/auth-inventory.md` describe paso a paso el happy path y 2 edge cases (password malo, usuario inexistente).\n\nCaptura (sin secretos) qué cookie/header usa la API. ¿El ID de usuario va en JWT payload? ¿Sesión en DB?\n\nLista endpoints: `POST /auth/login`, etc. Marca cuáles son públicos vs autenticados.",
    "lectura_rows": [
      [
        "OWASP",
        "A07 + Auth Cheat Sheet",
        "M10 cookies/sesiones"
      ]
    ],
    "hecho": [
      "Inventario con endpoints reales.",
      "Público vs autenticado claro.",
      "Sin passwords en el doc."
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
    "evidencia": "commit en repo producto + nota en projects/m18-appsec/auth-hashing.md",
    "objetivo": "Verificar o implementar hashing con coste adecuado (bcrypt≥12 o argon2) y eliminar esquemas débiles (MD5/SHA plano).",
    "porque": "A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.",
    "conceptos": [
      "Salt automático.",
      "Cost factor / memoria argon2.",
      "Nunca loguear `plain` password."
    ],
    "pasos_extra": "Audita el servicio de registro/login en tu API de Agenda Ops (repo M17). Si hay `bcrypt`/`argon2`, documenta parámetros en `projects/m18-appsec/auth-hashing.md`.\n\nSi falta: implementa con lib madura, migra usuarios de prueba, añade test que el hash no es igual al plain.\n\n```bash\n# en repo producto\nnpm test -- --testPathPattern=auth 2>/dev/null || npm test\n```",
    "lectura_rows": [
      [
        "OWASP",
        "Password Storage",
        "Ejemplo ficha M18"
      ]
    ],
    "hecho": [
      "Hashing correcto en código o ADR si ya estaba.",
      "Test o script que verifica compare.",
      "Doc de parámetros."
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
    "evidencia": "projects/m18-appsec/adr-sesion-vs-jwt.md (o enlace ADR M13)",
    "objetivo": "Decidir y documentar si Agenda Ops usa sesión en servidor, JWT firmado, o híbrido; consecuencias para XSS, logout y revocación.",
    "porque": "M13 pudo dejar la decisión abierta; M18 la cierra con ojos de seguridad.",
    "conceptos": [
      "Revocación inmediata.",
      "HttpOnly cookie vs Authorization header.",
      "Refresh token (si aplica)."
    ],
    "pasos_extra": "Redacta `projects/m18-appsec/adr-sesion-vs-jwt.md`: contexto, decisión, alternativas rechazadas, impacto en móvil M20.\n\nPrueba manual: login → copiar token/cookie → logout → reutilizar credencial vieja (debe fallar).\n\nAnota resultado en la ADR.",
    "lectura_rows": [
      [
        "M13",
        "adr/005-auth si existe",
        "M10 L14 sesiones"
      ]
    ],
    "hecho": [
      "ADR con alternativas.",
      "Prueba logout/reuse documentada.",
      "Coherente con móvil futuro."
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
      "Tabla amenaza-control.",
      "Listo para marcar P1 en UI."
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
    "evidencia": "projects/m18-appsec/cookies-lab.md",
    "objetivo": "Inspeccionar cookies de sesión de Agenda Ops en DevTools y verificar flags; corregir configuración en el servidor.",
    "porque": "M10 estudió cookies; hoy aplicas flags en **tu** stack.",
    "conceptos": [
      "SameSite=Lax/Strict.",
      "Secure en HTTPS.",
      "HttpOnly vs JS legítimo."
    ],
    "pasos_extra": "Login en staging/local. En `projects/m18-appsec/cookies-lab.md` tabla: nombre cookie, flags, lifetime, path.\n\nSi falta `Secure` o `HttpOnly` en cookie de sesión, parchea middleware/framework y captura antes/después (sin valor de cookie).\n\nPrueba: ¿JavaScript puede leer la cookie de sesión? Documenta.",
    "lectura_rows": [
      [
        "MDN",
        "Set-Cookie",
        "M10 L13"
      ]
    ],
    "hecho": [
      "Tabla de cookies real.",
      "Parche o justificación documentada.",
      "Prueba HttpOnly."
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
    "evidencia": "fix + projects/m18-appsec/csrf-notes.md",
    "objetivo": "Identificar operaciones mutables (POST/PUT/DELETE) y aplicar token CSRF, SameSite estricto o patrón equivalente en Agenda Ops.",
    "porque": "Un atacante no necesita XSS si tu sesión acepta POST cross-site.",
    "conceptos": [
      "Double-submit cookie (si aplica).",
      "Token sincronizado.",
      "API JSON + CORS no sustituye CSRF en cookies."
    ],
    "pasos_extra": "Lista rutas que cambian estado (crear cita, cancelar, perfil). En `projects/m18-appsec/csrf-notes.md` indica protección por ruta.\n\nImplementa protección mínima en la ruta más crítica (ej. crear cita). Test manual con `curl` sin token (debe 403).\n\nReferencia OWASP CSRF sheet en el doc.",
    "lectura_rows": [
      [
        "OWASP",
        "CSRF Prevention",
        "M10 CORS"
      ]
    ],
    "hecho": [
      "Lista rutas mutables.",
      "≥1 ruta protegida.",
      "curl sin token falla."
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
    "evidencia": "projects/m18-appsec/session-lifecycle.md",
    "objetivo": "Asegurar rotación de ID de sesión tras login y destrucción server-side en logout.",
    "porque": "Robar sesión fija es un clásico en apps que reutilizan el mismo session id.",
    "conceptos": [
      "Regenerar session id post-auth.",
      "Invalidar en logout.",
      "Timeout por inactividad (idea)."
    ],
    "pasos_extra": "Traza el ciclo en código. Documenta en `projects/m18-appsec/session-lifecycle.md`.\n\nPruebas: login dos veces ¿cambia id? logout ¿cookie inválida en siguiente request?\n\nSi usas JWT stateless, documenta blacklist/short TTL en su lugar.",
    "lectura_rows": [
      [
        "OWASP",
        "Session Management",
        "Auth cheat sheet"
      ]
    ],
    "hecho": [
      "Doc ciclo de vida.",
      "Pruebas login/logout documentadas.",
      "Commit si hubo fix."
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
    "evidencia": "projects/m18-appsec/checklist-cookies-csrf.md",
    "objetivo": "Checklist binario ejecutable antes de cada deploy: cookies, CSRF, HTTPS, logout.",
    "porque": "Operacionalizas controles para M19 deploy y trials M22.",
    "conceptos": [
      "Checklist reproducible.",
      "Evidencia en staging."
    ],
    "pasos_extra": "Crea `projects/m18-appsec/checklist-cookies-csrf.md` con ≥10 ítems Sí/No. Ejecútalo contra staging y pega resultado (fecha, URL).\n\nEnlaza issues/commits de la semana. Cierra con riesgo residual CSRF.",
    "lectura_rows": [
      [
        "Ficha",
        "M18 semana 3",
        "M19 ambientes futuro"
      ]
    ],
    "hecho": [
      "Checklist ejecutado.",
      "Fecha y URL.",
      "≥1 ítem corregido esta semana."
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
      "Solo tu entorno.",
      "Sin PII en el reporte."
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
      "Commit fix.",
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
      "Contexto identificado.",
      "Sin atacar usuarios reales."
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
      "Fix committed.",
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
      "Impacto descrito.",
      "Ruta exacta."
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
    "evidencia": "projects/m18-appsec/rbac-matrix.md",
    "objetivo": "Matriz rol × recurso × acción para Agenda Ops y gaps entre SRS y código.",
    "porque": "Agenda Ops distingue dueño y staff; la API debe hacerlo explícito.",
    "conceptos": [
      "RBAC vs ABAC (idea).",
      "403 vs 404.",
      "Principio mínimo privilegio."
    ],
    "pasos_extra": "`projects/m18-appsec/rbac-matrix.md`: filas citas, clientes, configuración; columnas owner/staff/anónimo.\n\nPrueba un caso staff que no debe ver citas de otro tenant (futuro) o acción admin. Registra resultado.",
    "lectura_rows": [
      [
        "SRS",
        "M12 roles",
        "OWASP A01"
      ]
    ],
    "hecho": [
      "Matriz completa.",
      "≥1 prueba manual rol.",
      "Gaps listados."
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
      "Prueba documentada.",
      "Mensaje usuario claro."
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
      "findings-table ≥3 filas.",
      "Commits referenciados."
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
      "Riesgo nombrado.",
      "Sin escanear terceros."
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
      "Ruta almacenamiento.",
      "Sin ejecución de uploads."
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
    "evidencia": "projects/m18-appsec/json-trust.md",
    "objetivo": "Auditar parsers JSON, `eval`, plantillas dinámicas y tipos inesperados en body de API.",
    "porque": "Node/TS rara vez hace Java deserialization, pero prototype pollution y lógica sí.",
    "conceptos": [
      "Validación schema (zod/joi).",
      "Prototype pollution (idea).",
      "Tamaño body limit."
    ],
    "pasos_extra": "`projects/m18-appsec/json-trust.md`: lista endpoints con body JSON; schema sí/no. Añade límite `express.json({ limit: '100kb' })` o equivalente.\n\nPrueba payload enorme o campos extra; documenta comportamiento.",
    "lectura_rows": [
      [
        "OWASP",
        "API Security Top 10",
        "Input validation"
      ]
    ],
    "hecho": [
      "Lista endpoints + validación.",
      "Límite tamaño body.",
      "≥1 mejora commitada."
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
      "Commits enlazados.",
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
    "evidencia": "projects/m18-appsec/deps-audit.md",
    "objetivo": "Ejecutar auditoría de dependencias, triagear findings (prod vs dev), actualizar o documentar riesgo aceptado.",
    "porque": "Tu app hereda CVEs de `node_modules`.",
    "conceptos": [
      "Semver y lockfile.",
      "DevDependency vs runtime.",
      "Riesgo aceptado con fecha."
    ],
    "pasos_extra": "```bash\ncd <repo Agenda Ops>\nnpm audit --omit=dev 2>/dev/null || npm audit\n```\n\nGuarda salida en `projects/m18-appsec/deps-audit.md`. Arregla al menos 1 high/critical o documenta por qué no aplica.",
    "lectura_rows": [
      [
        "OWASP",
        "A06",
        "npm audit docs"
      ]
    ],
    "hecho": [
      "Audit guardado.",
      "≥1 acción tomada.",
      "Fecha en doc."
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
    "evidencia": "projects/m18-appsec/secrets-rotation.md",
    "objetivo": "Verificar que secretos viven fuera de git; plan de rotación para JWT/session secret y DB.",
    "porque": "Un commit con `.env` es incidente permanente (historial).",
    "conceptos": [
      "`.gitignore`.",
      "Rotación sin downtime (idea).",
      "Pre-commit hooks."
    ],
    "pasos_extra": "```bash\ngit log -p --all -S 'DATABASE_URL' | head -20\n```\n\n`projects/m18-appsec/secrets-rotation.md`: inventario (sin valores), dónde viven en local/staging, pasos rotar session secret.",
    "lectura_rows": [
      [
        "OWASP",
        "Secrets",
        "M19 secrets-inventory"
      ]
    ],
    "hecho": [
      "Inventario sin valores.",
      "grep historial ejecutado.",
      "Plan rotación."
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
      "Login sigue funcionando.",
      "Commit."
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
    "evidencia": "projects/m18-appsec/csp.md + commit opcional",
    "objetivo": "Diseñar política CSP mínima (default-src, script-src) y desplegar en report-only o estricta según tolerancia.",
    "porque": "CSP es red de seguridad ante XSS residual.",
    "conceptos": [
      "nonce vs hash.",
      "report-uri / report-to.",
      "inline scripts legacy."
    ],
    "pasos_extra": "`projects/m18-appsec/csp.md`: política propuesta, fuentes externas que usa tu front (CDN, analytics futuro).\n\nImplementa CSP report-only primero; anota violaciones en consola.",
    "lectura_rows": [
      [
        "OWASP",
        "CSP",
        "MDN CSP"
      ]
    ],
    "hecho": [
      "Política escrita.",
      "Prueba report-only o estricta.",
      "Sin romper build."
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
      "Audit en pipeline.",
      "Run verde o excepciones justificadas."
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
      "Enlaces internos.",
      "Sin jerga vacía."
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
      "CI los ejecuta.",
      "Todos verdes."
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
      "P1–P3 verificables.",
      "README índice.",
      "Residual risk escrito."
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

Sin lista de activos, el threat model es decoración.

## Objetivo

Tablas de actores y ≥5 activos en `threat-model-v0.md` (PII, credenciales, citas, tokens, Postgres).

## Pasos (hazlos en orden)

### 1. Carpeta evidencia (15 min)

```bash
mkdir -p projects/m18-appsec/{pocs,fixes,tests,ci}
```

### 2. Actores y activos (80–100 min)

Dueño, staff, cliente final, atacante anónimo. Activos con clasificación (confidencialidad). Diagrama: navegador → API → Postgres.

### 3. Superficie JSON (30 min)

Marca qué campos salen en `/api/citas`. `git ls-files | rg -i 'env|secret|pem'`.

### 4. Commit

`docs(m18): l01 activos actores agenda ops`
"""

BODIES[2] = r"""
# L02 — Trust boundaries y flujos de confianza

**~5.0 h · Semana 1**

Dibuja dónde termina la confianza: browser, CDN, API, DB, WhatsApp.

## Objetivo

Diagrama de boundaries + 3 flujos (login, crear cita, deep-link WA) en el threat model.

## Pasos (hazlos en orden)

### 1. Boundaries (60–70 min)

ASCII/Mermaid: zonas Trusted/Untrusted. Cookies cruzan cuál frontera.

### 2. Flujos (60–70 min)

Para cada flujo: datos en tránsito, autenticación requerida, qué falla si se omite authz.

### 3. Commit

`docs(m18): l02 trust boundaries`
"""

BODIES[3] = r"""
# L03 — STRIDE aplicado al CRM de citas

**~5.0 h · Semana 1**

STRIDE sobre **tu** CRM, no un ejemplo de blog.

## Objetivo

≥1 amenaza por letra STRIDE mapeada a citas/auth/admin.

## Pasos (hazlos en orden)

### 1. Plantilla STRIDE (30 min)

Spoofing… Elevation — definición en una línea cada una.

### 2. Aplicación (90–110 min)

Tabla: amenaza, componente, impacto, mitigación actual/gap. Incluye IDOR y XSS en notas de cliente.

### 3. Commit

`docs(m18): l03 stride crm citas`
"""

BODIES[4] = r"""
# L04 — Threat model v0 y lectura OWASP Top 10

**~5.0 h · Semana 1**

Consolida v0 y cruza con Top 10.

## Objetivo

`threat-model-v0.md` legible + mapa Top 10 → superficies Agenda Ops.

## Pasos (hazlos en orden)

### 1. Redacta v0 (70–90 min)

Activos, boundaries, STRIDE, supuestos (solo atacas tu staging).

### 2. Cruce OWASP (50–60 min)

Tabla A01–A10 con estado preliminar.

### 3. Commit

`docs(m18): l04 threat model v0 owasp`
"""

BODIES[5] = r"""
# L05 — Inventario de autenticación actual

**~5.0 h · Semana 2**

Antes de endurecer, documentas qué hay en M17.

## Objetivo

`docs/auth-inventario.md`: mecanismo, almacenamiento token/sesión, endpoints auth.

## Pasos (hazlos en orden)

### 1. Inspección código (60–80 min)

Dónde se hashea, dónde se setea cookie, refresh o no.

### 2. Tabla riesgos (40–50 min)

localStorage vs cookie; falta rotación; logout incompleto.

### 3. Commit

`docs(m18): l05 inventario autenticacion`
"""

BODIES[6] = r"""
# L06 — Hashing de contraseñas con bcrypt o argon2

**~5.0 h · Semana 2**

Verifica cost factor y ausencia de hashes débiles.

## Objetivo

PoC o test: password nunca en MD5/SHA solo; bcrypt/argon2 con cost documentado; fix si hace falta.

## Pasos (hazlos en orden)

### 1. Auditoría (40 min)

Busca `md5|sha1|sha256\\(password` en el repo app.

### 2. Fix/confirmación (70–90 min)

Cost ≥12 bcrypt o argon2id razonable. Test verify round-trip.

### 3. Evidencia (20 min)

Entrada hallazgo o “N/A — ya conforme” con commit hash.

### 4. Commit

`fix(m18): l06 password hashing`
"""

BODIES[7] = r"""
# L07 — Sesiones server-side vs JWT en Agenda Ops

**~5.0 h · Semana 2**

Elige o ratifica con ADR corto de seguridad.

## Objetivo

`docs/adr-sesion-vs-jwt.md` + riesgos XSS/CSRF de la opción.

## Pasos (hazlos en orden)

### 1. Compara (50 min)

Tabla pros/contras en contexto panel+API same-site vs SPA cross-origin.

### 2. ADR (60–70 min)

Decisión, mitigaciones obligatorias (HttpOnly, TTL, revoke).

### 3. Commit

`docs(m18): l07 adr sesion jwt`
"""

BODIES[8] = r"""
# L08 — Threat model v1 post-autenticación (P1)

**~5.0 h · Semana 2**

P1: threat model v1 revisado tras endurecer auth.

## Objetivo

`threat-model-v1.md` (o sección v1) con cambios vs v0 y residual risk auth.

## Pasos (hazlos en orden)

### 1. Diff v0→v1 (40 min)

Qué amenazas bajaron de severidad.

### 2. Redacción P1 (80–100 min)

Incluye supuestos de staging. Enlace inventario + ADR.

### 3. README P1 (15 min)

### 4. Commit

`docs(m18): l08 threat model v1 p1`
"""

BODIES[9] = r"""
# L09 — Cookies Secure, HttpOnly y SameSite

**~5.0 h · Semana 3**

Atributos correctos o sesión robable.

## Objetivo

Checklist de cookie de sesión en staging/local documentado; fix flags faltantes.

## Pasos (hazlos en orden)

### 1. Inspección (40 min)

DevTools / `Set-Cookie` en login.

### 2. Hardening (70–90 min)

Secure (prod), HttpOnly, SameSite=Lax o Strict justificado.

### 3. Evidencia (20 min)

Captura headers redactados en `pocs/cookies.md`.

### 4. Commit

`fix(m18): l09 cookie flags`
"""

BODIES[10] = r"""
# L10 — CSRF en formularios y mutaciones state-changing

**~5.0 h · Semana 3**

Si usas cookies de sesión, CSRF importa.

## Objetivo

PoC CSRF (en tu app) o justificación SameSite+método; mitigación (token o SameSite estricto).

## Pasos (hazlos en orden)

### 1. Analiza superficie (40 min)

POST/PATCH/DELETE que cambian estado con cookie.

### 2. PoC controlada (60–80 min)

HTML local que intenta mutar. Documenta resultado.

### 3. Mitiga (40 min)

Token CSRF o política SameSite+JSON-only documentada.

### 4. Commit

`fix(m18): l10 csrf mitigacion`
"""

BODIES[11] = r"""
# L11 — Fijación de sesión y logout completo

**~5.0 h · Semana 3**

Login debe rotar session id; logout debe invalidar servidor.

## Objetivo

Demo: session id cambia post-login; logout invalida; test o checklist.

## Pasos (hazlos en orden)

### 1. Prueba fijación (50–60 min)

Intenta fijar cookie pre-login (en tu local). Documenta.

### 2. Logout servidor (50–60 min)

Almacén de sesiones: borrar id. JWT: blacklist/TTL corto documentado.

### 3. Commit

`fix(m18): l11 session fixation logout`
"""

BODIES[12] = r"""
# L12 — Checklist cookies y CSRF en staging

**~5.0 h · Semana 3**

Cierra semana 3 con checklist firmada contra staging.

## Objetivo

`docs/checklist-cookies-csrf.md` ejecutado en URL staging (o local prod-like).

## Pasos (hazlos en orden)

### 1. Checklist (40 min)

Flags, CSRF, logout, HTTPS.

### 2. Ejecución fechada (70–90 min)

Resultados Sí/No. Bugs → issues/hallazgos.

### 3. Commit

`docs(m18): l12 checklist cookies csrf staging`
"""

BODIES[13] = r"""
# L13 — SQLi: reproducir en tu propia API

**~5.0 h · Semana 4**

Solo contra tu API. Busca concatenación SQL en búsquedas de cliente/cita.

## Objetivo

PoC SQLi o “no reproducible con ORM” con evidencia de query parametrizada.

## Pasos (hazlos en orden)

### 1. Caza (60 min)

`rg` de SQL string concat / `$query` peligrosos.

### 2. PoC (60–80 min)

Payload en campo búsqueda; captura en `pocs/sqli.md`. Si ORM puro: documenta intento fallido.

### 3. Commit

`docs(m18): l13 poc sqli`
"""

BODIES[14] = r"""
# L14 — Mitigar SQLi: queries parametrizadas y permisos DB

**~5.0 h · Semana 4**

Fix + least privilege del rol app en Postgres de Agenda Ops.

## Objetivo

Commit fix (si había) + nota de rol DB sin DDL; test de regresión en búsquedas de clientes/citas.

## Pasos (hazlos en orden)

### 1. Parametriza (60–80 min)

Reemplaza concat en la API del piloto. Test con payload previo → seguro.

### 2. Permisos DB (40 min)

Usuario app de Agenda Ops: DML limitado (sin DDL). Documenta en hallazgos.

### 3. Commit

`fix(m18): l14 sqli parametrizado`
"""

BODIES[15] = r"""
# L15 — XSS reflejado en campos de cliente o búsqueda

**~5.0 h · Semana 4**

Busca reflejo de input en HTML.

## Objetivo

PoC XSS reflejado en tu UI o evidencia de escape; entrada en tabla hallazgos.

## Pasos (hazlos en orden)

### 1. Prueba (70–90 min)

Payloads simples en nombre/búsqueda. Solo tu staging.

### 2. Documenta (40 min)

`pocs/xss-reflected.md` con pasos y resultado.

### 3. Commit

`docs(m18): l15 poc xss reflejado`
"""

BODIES[16] = r"""
# L16 — XSS almacenado y escape en plantillas/API

**~5.0 h · Semana 4**

Notas de cita/cliente son candidatas clásicas.

## Objetivo

PoC stored XSS o fix escape/encoding; no confiar solo en CSP aún.

## Pasos (hazlos en orden)

### 1. Inserta payload (50 min)

Guarda `<script>` en nota (seed/test user).

### 2. Verifica render (50–60 min)

¿Ejecuta? Fix con escape del framework. Test.

### 3. Commit

`fix(m18): l16 xss almacenado escape`
"""

BODIES[17] = r"""
# L17 — IDOR en citas y recursos por ID

**~5.0 h · Semana 5**

`GET /citas/:id` sin comprobar dueño = IDOR.

## Objetivo

PoC cross-user + fix autorización + test automatizado.

## Pasos (hazlos en orden)

### 1. Dos usuarios (30 min)

Owner A y B (o staff) con citas distintas.

### 2. PoC (50–60 min)

Token A pide id de B. Documenta status code.

### 3. Fix + test (60–80 min)

Filtro por negocio/usuario. Test 403/404.

### 4. Commit

`fix(m18): l17 idor citas`
"""

BODIES[18] = r"""
# L18 — Autorización por rol owner vs staff

**~5.0 h · Semana 5**

Matriz M17 debe cumplirse en servidor.

## Objetivo

Tests 403 staff→admin; hallazgos si UI ocultaba y API no.

## Pasos (hazlos en orden)

### 1. Matriz vs código (40 min)

Diff permisos.md vs middleware.

### 2. Tests roles (80–100 min)

Cobertura de acciones Deny.

### 3. Commit

`test(m18): l18 authz roles owner staff`
"""

BODIES[19] = r"""
# L19 — Rate limiting en login y endpoints sensibles

**~5.0 h · Semana 5**

Confirma o añade rate limit; mide 429.

## Objetivo

Evidencia 429 en login; hallazgo/fix documentado.

## Pasos (hazlos en orden)

### 1. Prueba carga ligera (50 min)

Script de N logins fallidos.

### 2. Ajuste (60–80 min)

Umbrales; no ban eterno sin doc.

### 3. Commit

`fix(m18): l19 rate limit evidenciado`
"""

BODIES[20] = r"""
# L20 — Tests automatizados cross-user (P2 avance)

**~5.0 h · Semana 5**

P2 avanza con tests que fallen si vuelve el IDOR.

## Objetivo

≥2 tests cross-user en CI local; tabla hallazgos con ≥3 filas PoC→fix→test.

## Pasos (hazlos en orden)

### 1. Escribe tests (90–110 min)

Usuario A no lee/edita recurso B.

### 2. Tabla P2 (40 min)

`hallazgos.md` columnas requeridas.

### 3. Commit

`test(m18): l20 cross-user p2 avance`
"""

BODIES[21] = r"""
# L21 — SSRF: superficie en webhooks e integraciones

**~5.0 h · Semana 6**

¿La API fetcha URLs controladas por usuario?

## Objetivo

Inventario SSRF (webhooks, previews, imports) + mitigación o N/A justificado.

## Pasos (hazlos en orden)

### 1. Busca fetch/axios a URLs user-controlled (50 min)

### 2. Documenta (60–70 min)

Allowlist, bloqueo link-local. PoC solo local.

### 3. Commit

`docs(m18): l21 superficie ssrf`
"""

BODIES[22] = r"""
# L22 — Subida de archivos segura

**~5.0 h · Semana 6**

Si no hay uploads, documenta N/A; si hay, endurece.

## Objetivo

Política: tipos MIME, tamaño, path traversal, no ejecutar en mismo origen.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

### 2. Controles o N/A (80–100 min)

Evidencia en `docs/uploads.md`.

### 3. Commit

`docs(m18): l22 uploads seguros`
"""

BODIES[23] = r"""
# L23 — Deserialización y JSON peligroso

**~5.0 h · Semana 6**

`JSON.parse` de fuentes no confiables + prototipos / eval.

## Objetivo

Grep de `eval|deserialize|yaml.load` peligroso; endurece parsers.

## Pasos (hazlos en orden)

### 1. Caza (50 min)

### 2. Hardening (60–70 min)

Schema validation en boundaries. Hallazgo o clean bill.

### 3. Commit

`fix(m18): l23 json boundaries`
"""

BODIES[24] = r"""
# L24 — Consolidar hallazgos semana 6 en P2

**~5.0 h · Semana 6**

P2 exige ≥5 hallazgos con PoC→fix→test.

## Objetivo

`hallazgos.md` con ≥5 filas completas; gaps explícitos.

## Pasos (hazlos en orden)

### 1. Consolida (90–110 min)

Unifica L13–L23. Prioridad.

### 2. README P2 (20 min)

### 3. Commit

`docs(m18): l24 hallazgos p2 consolidados`
"""

BODIES[25] = r"""
# L25 — npm audit y cadena de dependencias

**~5.0 h · Semana 7**

A06: componentes vulnerables.

## Objetivo

`npm audit` (o equivalente) corrido; severidades altas tratadas o aceptadas con justificación.

## Pasos (hazlos en orden)

### 1. Audit (40 min)

```bash
npm audit --json > projects/m18-appsec/docs/npm-audit.json || true
```

### 2. Triage (70–90 min)

Tabla: CVE, impacto en Agenda Ops, acción.

### 3. Commit

`docs(m18): l25 npm audit triage`
"""

BODIES[26] = r"""
# L26 — Secretos, .env y rotación

**~5.0 h · Semana 7**

Historial git no debe tener SESSION_SECRET real.

## Objetivo

Inventario secretos; rotación documentada; grep limpio.

## Pasos (hazlos en orden)

### 1. Busca fugas (50 min)

`git log -p | rg -i 'password|secret|api_key' | head` (cuidado output).

### 2. Proceso rotación (60–70 min)

`docs/rotacion-secretos.md` pasos staging.

### 3. Commit

`docs(m18): l26 secretos rotacion`
"""

BODIES[27] = r"""
# L27 — Cabeceras de seguridad con Helmet o equivalente

**~5.0 h · Semana 7**

Confirma headers en staging; completa gaps M17.

## Objetivo

Headers activos verificados; doc en appsec.

## Pasos (hazlos en orden)

### 1. curl -I (40 min)

### 2. Ajustes (60–80 min)

X-Content-Type-Options, Frame, Referrer-Policy, etc.

### 3. Commit

`fix(m18): l27 security headers`
"""

BODIES[28] = r"""
# L28 — CSP básica sin romper Agenda Ops

**~5.0 h · Semana 7**

CSP report-only o enforce gradual.

## Objetivo

CSP que no rompa panel; documenta excepciones.

## Pasos (hazlos en orden)

### 1. Política borrador (50 min)

default-src 'self'; script-src cuidadoso.

### 2. Prueba UI (70–90 min)

Login, agenda, WA link. Ajusta.

### 3. Commit

`feat(m18): l28 csp basica`
"""

BODIES[29] = r"""
# L29 — Pipeline CI: lint, test, audit, anti-secretos

**~5.0 h · Semana 8**

P3: CI con lint+test+audit+grep secretos.

## Objetivo

Workflow verde documentado en `projects/m18-appsec/ci/`.

## Pasos (hazlos en orden)

### 1. Pipeline (100–120 min)

Enlace al workflow del repo app. Job anti-secretos básico.

### 2. Evidencia (30 min)

Log CI o script local reproducible.

### 3. Commit

`ci(m18): l29 pipeline p3`
"""

BODIES[30] = r"""
# L30 — Estructura del informe AppSec

**~5.0 h · Semana 8**

El entregable del proyecto es el informe.

## Objetivo

`informe-appsec.md` con ejecutivo, alcance, hallazgos, mitigaciones, residual.

## Pasos (hazlos en orden)

### 1. Plantilla (30 min)

### 2. Redacción (100–120 min)

Enlaza PoCs y commits fix. Sin datos reales del partner.

### 3. Commit

`docs(m18): l30 informe appsec`
"""

BODIES[31] = r"""
# L31 — Tests de regresión de seguridad (≥3)

**~5.0 h · Semana 8**

≥3 tests que fallen si reabres agujeros.

## Objetivo

Suite seguridad documentada: IDOR, XSS escape, authz rol (o equivalentes).

## Pasos (hazlos en orden)

### 1. Selecciona 3 (20 min)

### 2. Implementa/verde (100–120 min)

Nombres claros `security.*.test.ts`.

### 3. Commit

`test(m18): l31 regresion seguridad`
"""

BODIES[32] = r"""
# L32 — Cierre M18 — dominio y riesgo residual

**~5.0 h · Semana 8**

Riesgo residual explícito > “somos seguros”.

## Objetivo

Cierre P1–P3, criterios dominio, residual risk y handoff a M19/M25.

## Pasos (hazlos en orden)

### 1. Auditoría evidencias (50 min)

### 2. Residual (50–60 min)

Top 3 riesgos aceptados con dueño/fecha.

### 3. README final (30 min)

### 4. Commit

`docs(m18): l32 cierre dominio residual`
"""

