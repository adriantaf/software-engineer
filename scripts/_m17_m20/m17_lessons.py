"""M17 lessons: RAW specs + BODIES (M01/M09 quality)."""
from __future__ import annotations

import json

FILENAMES = {
    1: "L01-scaffold-agenda-ops-api-db-y-stack-md.md",
    2: "L02-registro-con-hash-de-contrasena.md",
    3: "L03-login-sesion-y-get-me-protegido.md",
    4: "L04-cierre-semana-1-suite-auth-p1.md",
    5: "L05-modelo-de-dominio-citas-clientes-y-servicios.md",
    6: "L06-api-citas-crear-y-listar-con-reglas.md",
    7: "L07-crud-clientes-y-servicios.md",
    8: "L08-seeds-demo-y-datos-design-partner.md",
    9: "L09-matriz-de-permisos-owner-y-staff.md",
    10: "L10-middleware-de-autorizacion-en-api.md",
    11: "L11-panel-admin-minimo-gestion-staff.md",
    12: "L12-demo-roles-y-inicio-p3-whatsapp.md",
    13: "L13-scaffold-front-y-rutas-protegidas.md",
    14: "L14-flujo-login-logout-en-ui.md",
    15: "L15-listas-con-loading-error-y-vacio.md",
    16: "L16-formularios-citas-y-clientes-accesibles.md",
    17: "L17-deep-links-whatsapp-diseno-del-mensaje.md",
    18: "L18-boton-enviar-recordatorio-desde-ficha-cita.md",
    19: "L19-confirmacion-de-cita-y-estados.md",
    20: "L20-cierre-p3-integracion-whatsapp.md",
    21: "L21-variables-de-entorno-y-secrets.md",
    22: "L22-deploy-staging-en-paas.md",
    23: "L23-https-y-health-checks.md",
    24: "L24-smoke-test-post-deploy.md",
    25: "L25-mapa-owasp-top-10-en-el-piloto.md",
    26: "L26-headers-de-seguridad-y-cors-prod.md",
    27: "L27-rate-limit-en-login.md",
    28: "L28-tests-auth-en-ci-o-script-local-reproducible.md",
    29: "L29-adr-tenant-id-y-modelo-multi-negocio.md",
    30: "L30-checklist-camino-a-saas.md",
    31: "L31-demo-grabable-para-design-partner.md",
    32: "L32-cierre-m17-evidencias-dominio-y-handoff-m19.md",
}

RAW = json.loads(r"""
[
  {
    "titulo": "Scaffold Agenda Ops — API, DB y stack",
    "semana": 1,
    "horas": 5,
    "lectura": "producto-saas.md + m13-diseno + M09 esquema",
    "evidencia": "projects/m17-agenda-ops/stack.md + scaffold API",
    "objetivo": "Inicializar `projects/m17-agenda-ops/` con TypeScript strict, conexión Postgres y documentar stack fijo.",
    "porque": "Cambiar stack a mitad de materia sin ADR destruye velocidad.",
    "conceptos": [
      "scaffold.",
      "Postgres.",
      "monolito modular."
    ],
    "pasos_extra": "```bash\nmkdir -p projects/m17-agenda-ops/docs projects/m17-agenda-ops/src\n```\nCrea `stack.md` (framework HTTP, ORM, front). Migra o enlaza esquema M09. Health `GET /health` 200.",
    "lectura_rows": [
      [
        "m13-diseno",
        "endpoints.md",
        "m09 esquema"
      ]
    ],
    "hecho": [
      "Repo scaffold.",
      "stack.md.",
      "DB conecta local.",
      "Health check."
    ],
    "errores": [
      "Stack sin documentar.",
      "Secrets en repo."
    ]
  },
  {
    "titulo": "Registro con hash de contraseña",
    "semana": 1,
    "horas": 5,
    "lectura": "OWASP Password Storage + bcrypt/argon2",
    "evidencia": "POST /auth/register",
    "objetivo": "Implementar registro: validar email/password, hash fuerte, persistir usuario ligado al negocio piloto.",
    "porque": "Auth real desde el MVP — no usuarios en texto plano.",
    "conceptos": [
      "hash.",
      "registro.",
      "validación."
    ],
    "pasos_extra": "Zod (o similar) en body. Test integración 201 y 400 email inválido.",
    "lectura_rows": [
      [
        "OWASP",
        "Password Storage",
        "m13 ADR auth"
      ]
    ],
    "hecho": [
      "Register funciona.",
      "Hash no reversible.",
      "Test 400."
    ],
    "errores": [
      "MD5.",
      "Password en logs."
    ]
  },
  {
    "titulo": "Login, sesión y GET /me protegido",
    "semana": 1,
    "horas": 5,
    "lectura": "MDN cookies + ADR sesión M13",
    "evidencia": "POST /auth/login + GET /me",
    "objetivo": "Login con cookie HttpOnly o JWT en cookie; `GET /me` devuelve 401 sin credencial.",
    "porque": "El panel Agenda Ops necesita identidad servidor-confiable.",
    "conceptos": [
      "sesión.",
      "401.",
      "HttpOnly."
    ],
    "pasos_extra": "Tests: login → me 200; sin cookie → 401. Documenta elección en `docs/auth.md`.",
    "lectura_rows": [
      [
        "MDN",
        "HTTP cookies",
        "hilo seguridad"
      ]
    ],
    "hecho": [
      "Login+me.",
      "401 test.",
      "auth.md."
    ],
    "errores": [
      "JWT localStorage sin doc.",
      "Me devuelve todo el row."
    ]
  },
  {
    "titulo": "Cierre semana 1 — suite auth P1",
    "semana": 1,
    "horas": 5,
    "lectura": "Ficha M17 P1",
    "evidencia": "projects/m17-agenda-ops/tests/auth.test.ts",
    "objetivo": "Consolidar tests auth (register, login, me, logout) y marcar P1 parcial en README.",
    "porque": "P1 es puerta para todo CRUD.",
    "conceptos": [
      "P1.",
      "suite auth.",
      "logout."
    ],
    "pasos_extra": "≥6 tests auth. README comando `npm test`. Commit cierre semana 1.",
    "lectura_rows": [
      [
        "Ficha",
        "../M17-aplicaciones-web.md",
        "m15 CI"
      ]
    ],
    "hecho": [
      "Suite auth verde.",
      "Logout documentado.",
      "P1 parcial README."
    ],
    "errores": [
      "Auth sin tests.",
      "Solo manual Postman."
    ]
  },
  {
    "titulo": "Modelo de dominio citas, clientes y servicios",
    "semana": 2,
    "horas": 5,
    "lectura": "m13 diagrama clases + srs-v1",
    "evidencia": "migraciones / entidades",
    "objetivo": "Alinear tablas y entidades con diseño M13: citas, clientes, servicios, relaciones y reglas en código dominio.",
    "porque": "CRUD sin modelo coherente genera IDOR y datos huérfanos.",
    "conceptos": [
      "entidad.",
      "migración.",
      "dominio."
    ],
    "pasos_extra": "Migraciones aplicadas. Tipos dominio sin dependencia de ORM en reglas puras (carpeta `domain/`).",
    "lectura_rows": [
      [
        "m12-srs",
        "RF citas",
        "m13 clases"
      ]
    ],
    "hecho": [
      "Migraciones.",
      "domain/ con reglas.",
      "Commit."
    ],
    "errores": [
      "Lógica solo en controllers.",
      "Sin FK."
    ]
  },
  {
    "titulo": "API citas — crear y listar con reglas",
    "semana": 2,
    "horas": 5,
    "lectura": "REST + validación horarios",
    "evidencia": "POST/GET /citas",
    "objetivo": "Endpoints crear/listar citas con auth, validación fin>inicio, no pasado sin override documentado.",
    "porque": "Core del piloto Agenda Ops.",
    "conceptos": [
      "REST.",
      "409 solapamiento.",
      "paginación."
    ],
    "pasos_extra": "Tests 201, 400 horario, 409 solapamiento. Listar con filtro fecha.",
    "lectura_rows": [
      [
        "m12",
        "stories citas",
        "—"
      ]
    ],
    "hecho": [
      "POST/GET citas.",
      "Reglas testeadas.",
      "401 sin auth."
    ],
    "errores": [
      "Listar sin auth.",
      "Timezone ignorada."
    ]
  },
  {
    "titulo": "CRUD clientes y servicios",
    "semana": 2,
    "horas": 5,
    "lectura": "SRS RF clientes/servicios",
    "evidencia": "/clientes /servicios",
    "objetivo": "CRUD completo clientes y servicios con autorización owner/staff según matriz preliminar.",
    "porque": "Servicios definen duración y precio base para citas.",
    "conceptos": [
      "CRUD.",
      "servicio.",
      "cliente."
    ],
    "pasos_extra": "Endpoints + tests feliz y 404. Seeds opcionales.",
    "lectura_rows": [
      [
        "m12-srs",
        "Must",
        "m14 precio opcional"
      ]
    ],
    "hecho": [
      "CRUD ambos recursos.",
      "Tests.",
      "Commit."
    ],
    "errores": [
      "Mezclar cliente entre negocios.",
      "Sin validación."
    ]
  },
  {
    "titulo": "Seeds demo y datos design partner",
    "semana": 2,
    "horas": 5,
    "lectura": "Fixtures reproducibles",
    "evidencia": "projects/m17-agenda-ops/scripts/seed.ts",
    "objetivo": "Script seed con negocio piloto, owner, staff, citas ejemplo para demo.",
    "porque": "Demo reproducible evita ‘en mi máquina sí’.",
    "conceptos": [
      "seed.",
      "demo.",
      "idempotencia."
    ],
    "pasos_extra": "seed documentado en README. No PII real del partner en repo.",
    "lectura_rows": [
      [
        "README",
        "demo creds test",
        "—"
      ]
    ],
    "hecho": [
      "Seed corre.",
      "README creds test.",
      "Cierre semana 2."
    ],
    "errores": [
      "Datos reales en git.",
      "Seed no repetible."
    ]
  },
  {
    "titulo": "Matriz de permisos owner y staff",
    "semana": 3,
    "horas": 5,
    "lectura": "m13 casos de uso admin",
    "evidencia": "projects/m17-agenda-ops/docs/permisos.md",
    "objetivo": "Documentar tabla acción×rol (cancelar cita, ver reportes, gestionar staff).",
    "porque": "Roles sin matriz escrita se implementan inconsistente.",
    "conceptos": [
      "RBAC.",
      "owner.",
      "staff."
    ],
    "pasos_extra": "permisos.md enlazado a endpoints. Cada ruta sensible tiene rol en comentario OpenAPI o tabla.",
    "lectura_rows": [
      [
        "m12",
        "stories roles",
        "OWASP access control"
      ]
    ],
    "hecho": [
      "permisos.md.",
      "Cobertura endpoints.",
      "Commit."
    ],
    "errores": [
      "Staff = owner.",
      "Matriz vacía."
    ]
  },
  {
    "titulo": "Middleware de autorización en API",
    "semana": 3,
    "horas": 5,
    "lectura": "Middleware pattern",
    "evidencia": "authorize(role) middleware",
    "objetivo": "Middleware que verifica rol y negocio en cada handler sensible.",
    "porque": "403 debe ser imposible de evitar desde el front.",
    "conceptos": [
      "middleware.",
      "403.",
      "contexto usuario."
    ],
    "pasos_extra": "Tests staff bloqueado en acción owner. Test 403 IDOR entre recursos.",
    "lectura_rows": [
      [
        "m15",
        "tests seguridad",
        "—"
      ]
    ],
    "hecho": [
      "Middleware activo.",
      "403 tests.",
      "Sin lógica duplicada."
    ],
    "errores": [
      "Check solo en UI.",
      "Hardcode user id."
    ]
  },
  {
    "titulo": "Panel admin mínimo — gestión staff",
    "semana": 3,
    "horas": 5,
    "lectura": "UI admin sin adornos",
    "evidencia": "ruta /admin o equivalente",
    "objetivo": "Pantalla admin: listar staff, invitar o crear staff (según SRS), solo owner.",
    "porque": "El dueño del negocio administra su equipo aquí.",
    "conceptos": [
      "admin.",
      "invitación.",
      "UX claro."
    ],
    "pasos_extra": "UI fea pero clara. Errores 403 visibles. Notas en `docs/ui-admin.md`.",
    "lectura_rows": [
      [
        "m16",
        "handoff UX",
        "—"
      ]
    ],
    "hecho": [
      "Admin usable.",
      "Owner-only verificado.",
      "ui-admin.md."
    ],
    "errores": [
      "Admin sin auth.",
      "Confundir roles."
    ]
  },
  {
    "titulo": "Demo roles y inicio P3 WhatsApp",
    "semana": 3,
    "horas": 5,
    "lectura": "Ficha P3 parcial",
    "evidencia": "projects/m17-agenda-ops/docs/demo-roles.md",
    "objetivo": "Grabar o documentar pasos demo: owner vs staff en acción bloqueada.",
    "porque": "P3 requiere evidencia reproducible para el design partner.",
    "conceptos": [
      "demo.",
      "roles.",
      "evidencia."
    ],
    "pasos_extra": "demo-roles.md con usuarios test y pasos. Enlace a tests 403.",
    "lectura_rows": [
      [
        "Ficha",
        "../M17-aplicaciones-web.md",
        "—"
      ]
    ],
    "hecho": [
      "demo-roles.md.",
      "Staff bloqueado demo.",
      "Cierre semana 3."
    ],
    "errores": [
      "Demo sin script.",
      "Cuentas prod."
    ]
  },
  {
    "titulo": "Scaffold front y rutas protegidas",
    "semana": 4,
    "horas": 5,
    "lectura": "React Router / framework docs",
    "evidencia": "front app + router",
    "objetivo": "Crear front con login, layout panel, rutas protegidas redirect a login.",
    "porque": "Agenda Ops se usa desde navegador diario.",
    "conceptos": [
      "SPA.",
      "protected route.",
      "layout."
    ],
    "pasos_extra": "Estructura `apps/web` o `client/`. Env API_URL documentado.",
    "lectura_rows": [
      [
        "MDN",
        "fetch",
        "m16 prototipo"
      ]
    ],
    "hecho": [
      "Front arranca.",
      "Redirect sin sesión.",
      "Commit."
    ],
    "errores": [
      "CORS `*` sin doc.",
      "API_URL hardcode prod."
    ]
  },
  {
    "titulo": "Flujo login/logout en UI",
    "semana": 4,
    "horas": 5,
    "lectura": "Forms accesibles",
    "evidencia": "páginas login",
    "objetivo": "Form login con labels, errores de credencial, logout que limpia sesión.",
    "porque": "Primera impresión del piloto.",
    "conceptos": [
      "login UI.",
      "error auth.",
      "logout."
    ],
    "pasos_extra": "Manejo 401 en login. Test e2e opcional o checklist manual en docs.",
    "lectura_rows": [
      [
        "m16",
        "estados error",
        "—"
      ]
    ],
    "hecho": [
      "Login/logout.",
      "Errores visibles.",
      "Sin password en state."
    ],
    "errores": [
      "Alert genérico.",
      "Token en querystring."
    ]
  },
  {
    "titulo": "Listas con loading, error y vacío",
    "semana": 4,
    "horas": 5,
    "lectura": "m16 estados-ui",
    "evidencia": "projects/m17-agenda-ops/docs/ui-estados.md",
    "objetivo": "Implementar agenda del día y listas con tres estados UX obligatorios.",
    "porque": "P2 exige documentación de estados.",
    "conceptos": [
      "loading.",
      "empty.",
      "error boundary."
    ],
    "pasos_extra": "ui-estados.md con capturas o descripción por pantalla.",
    "lectura_rows": [
      [
        "Ficha",
        "../M17-aplicaciones-web.md",
        "P2"
      ]
    ],
    "hecho": [
      "ui-estados.md.",
      "3 estados en UI.",
      "Commit."
    ],
    "errores": [
      "Spinner eterno.",
      "Lista vacía sin CTA."
    ]
  },
  {
    "titulo": "Formularios citas y clientes accesibles",
    "semana": 4,
    "horas": 5,
    "lectura": "MDN forms a11y básica",
    "evidencia": "formularios create",
    "objetivo": "Crear/editar cita y cliente con validación inline alineada a API.",
    "porque": "Errores server mapeados a campos.",
    "conceptos": [
      "form.",
      "a11y.",
      "validación."
    ],
    "pasos_extra": "Labels, `aria-invalid`, mensajes en español. Commit cierre semana 4 P2 parcial.",
    "lectura_rows": [
      [
        "MDN",
        "formularios",
        "m12 criterios"
      ]
    ],
    "hecho": [
      "Forms create/edit.",
      "Errores campo.",
      "P2 parcial."
    ],
    "errores": [
      "Solo placeholder.",
      "Confiar solo client validation."
    ]
  },
  {
    "titulo": "Deep links WhatsApp — diseño del mensaje",
    "semana": 5,
    "horas": 5,
    "lectura": "Docs proveedor WhatsApp",
    "evidencia": "projects/m17-agenda-ops/docs/integracion-whatsapp.md",
    "objetivo": "Definir plantilla mensaje recordatorio/confirmación con placeholders y enlace wa.me.",
    "porque": "Canal que el design partner ya usa.",
    "conceptos": [
      "deep link.",
      "plantilla.",
      "PII mínima."
    ],
    "pasos_extra": "integracion-whatsapp.md: ejemplo URL encoded, qué datos van (nombre cita, hora).",
    "lectura_rows": [
      [
        "Oficial",
        "WhatsApp Business",
        "—"
      ]
    ],
    "hecho": [
      "Doc plantilla.",
      "Sin secrets.",
      "Commit."
    ],
    "errores": [
      "API keys en front.",
      "Teléfono en logs."
    ]
  },
  {
    "titulo": "Botón enviar recordatorio desde ficha cita",
    "semana": 5,
    "horas": 5,
    "lectura": "UI + API log",
    "evidencia": "acción recordatorio",
    "objetivo": "En UI de cita, acción que abre WhatsApp o registra intento según diseño.",
    "porque": "Cierra loop operativo del negocio.",
    "conceptos": [
      "acción usuario.",
      "auditoría ligera.",
      "opt-in."
    ],
    "pasos_extra": "Implementación + test manual documentado. Log sin PII completa.",
    "lectura_rows": [
      [
        "m14",
        "notificador",
        "—"
      ]
    ],
    "hecho": [
      "Acción en UI.",
      "Log sanitizado.",
      "Test manual pasos."
    ],
    "errores": [
      "Spam sin confirmación.",
      "Log con teléfono."
    ]
  },
  {
    "titulo": "Confirmación de cita y estados",
    "semana": 5,
    "horas": 5,
    "lectura": "Flujo estado cita",
    "evidencia": "campo estado + UI",
    "objetivo": "Estados confirmada/pendiente/cancelada visibles y coherentes API↔UI.",
    "porque": "Staff y owner deben ver el mismo estado.",
    "conceptos": [
      "estado.",
      "sincronización.",
      "cancelación."
    ],
    "pasos_extra": "Tests API cambio estado + UI refleja. Mensaje WhatsApp opcional al confirmar.",
    "lectura_rows": [
      [
        "m12-srs",
        "flujos",
        "—"
      ]
    ],
    "hecho": [
      "Estados en API/UI.",
      "Tests.",
      "Commit."
    ],
    "errores": [
      "Estado solo en front.",
      "Cancelar sin auth."
    ]
  },
  {
    "titulo": "Cierre P3 integración WhatsApp",
    "semana": 5,
    "horas": 5,
    "lectura": "Ficha P3",
    "evidencia": "integracion-whatsapp.md completo",
    "objetivo": "Completar doc P3: capturas, límites legales/opt-in, qué no hace la integración.",
    "porque": "P3 no sustituye API oficial si no está configurada — documenta gaps.",
    "conceptos": [
      "P3.",
      "opt-in.",
      "gap."
    ],
    "pasos_extra": "Checklist P3 en README. Cierre semana 5.",
    "lectura_rows": [
      [
        "Ficha",
        "../M17-aplicaciones-web.md",
        "—"
      ]
    ],
    "hecho": [
      "P3 checklist.",
      "Capturas.",
      "Gaps honestos."
    ],
    "errores": [
      "Prometer API sin credencial.",
      "Sin opt-in."
    ]
  },
  {
    "titulo": "Variables de entorno y secrets",
    "semana": 6,
    "horas": 5,
    "lectura": "12-factor config",
    "evidencia": "projects/m17-agenda-ops/.env.example",
    "objetivo": "Separar config: DATABASE_URL, SESSION_SECRET, etc. `.env.example` sin valores reales.",
    "porque": "Deploy seguro empieza por no commitear secrets.",
    "conceptos": [
      "env.",
      "secrets.",
      "example."
    ],
    "pasos_extra": "Validar arranque si falta variable crítica. Documentar en README.",
    "lectura_rows": [
      [
        "OWASP",
        "Secrets management",
        "—"
      ]
    ],
    "hecho": [
      ".env.example.",
      "Validación arranque.",
      "Commit."
    ],
    "errores": [
      ".env en git.",
      "Secrets en front."
    ]
  },
  {
    "titulo": "Deploy staging en PaaS",
    "semana": 6,
    "horas": 5,
    "lectura": "Docs PaaS elegido",
    "evidencia": "URL staging",
    "objetivo": "Desplegar API+front o API primero en staging con build reproducible.",
    "porque": "Piloto invisible no es piloto.",
    "conceptos": [
      "deploy.",
      "staging.",
      "build."
    ],
    "pasos_extra": "URL en README. Proceso `docs/deploy.md` paso a paso.",
    "lectura_rows": [
      [
        "PaaS",
        "docs",
        "m19 preview"
      ]
    ],
    "hecho": [
      "Staging URL.",
      "deploy.md.",
      "Build CI opcional."
    ],
    "errores": [
      "Deploy manual sin doc.",
      "Solo localhost."
    ]
  },
  {
    "titulo": "HTTPS y health checks",
    "semana": 6,
    "horas": 5,
    "lectura": "TLS Let's Encrypt / proveedor",
    "evidencia": "HTTPS + /health",
    "objetivo": "Forzar HTTPS en prod/staging y health check para monitor.",
    "porque": "Design partner no debe ver “no seguro”.",
    "conceptos": [
      "TLS.",
      "HSTS.",
      "health."
    ],
    "pasos_extra": "Verificar certificado válido. Health usado en deploy script.",
    "lectura_rows": [
      [
        "MDN",
        "HTTPS",
        "—"
      ]
    ],
    "hecho": [
      "HTTPS activo.",
      "Health remoto.",
      "Commit."
    ],
    "errores": [
      "HTTP prod.",
      "Health sin DB check documentado."
    ]
  },
  {
    "titulo": "Smoke test post-deploy",
    "semana": 6,
    "horas": 5,
    "lectura": "Checklist smoke",
    "evidencia": "projects/m17-agenda-ops/docs/smoke-test.md",
    "objetivo": "Script o checklist: register/login/crear cita en staging.",
    "porque": "Detecta config rota antes de la demo.",
    "conceptos": [
      "smoke.",
      "staging.",
      "regresión manual."
    ],
    "pasos_extra": "smoke-test.md con resultado fechado de última corrida.",
    "lectura_rows": [
      [
        "m15",
        "regresión",
        "—"
      ]
    ],
    "hecho": [
      "smoke-test.md.",
      "Corrida fechada.",
      "Cierre semana 6."
    ],
    "errores": [
      "Smoke solo health.",
      "Olvidar auth."
    ]
  },
  {
    "titulo": "Mapa OWASP Top 10 en el piloto",
    "semana": 7,
    "horas": 5,
    "lectura": "OWASP Top 10 overview",
    "evidencia": "projects/m17-agenda-ops/docs/owasp-mapa.md",
    "objetivo": "Tabla: cada riesgo → mitigación actual o gap hacia M18.",
    "porque": "M18 profundiza; hoy ubicas huecos.",
    "conceptos": [
      "OWASP.",
      "gap.",
      "mitigación."
    ],
    "pasos_extra": "owasp-mapa.md con ≥8 filas honestas.",
    "lectura_rows": [
      [
        "OWASP",
        "Top 10",
        "hilo seguridad"
      ]
    ],
    "hecho": [
      "owasp-mapa.md.",
      "Gaps M18.",
      "Commit."
    ],
    "errores": [
      "Marcar todo mitigado.",
      "Ignorar auth."
    ]
  },
  {
    "titulo": "Headers de seguridad y CORS prod",
    "semana": 7,
    "horas": 5,
    "lectura": "MDN security headers",
    "evidencia": "helmet o equivalente",
    "objetivo": "Configurar headers básicos y CORS restrictivo a dominio front.",
    "porque": "Reduce superficie antes de abrir al partner.",
    "conceptos": [
      "helmet.",
      "CORS.",
      "CSP intro."
    ],
    "pasos_extra": "Documenta valores en `docs/seguridad-http.md`. Test manual headers.",
    "lectura_rows": [
      [
        "MDN",
        "CORS",
        "m10 lecciones"
      ]
    ],
    "hecho": [
      "Headers activos prod.",
      "CORS no `*`.",
      "Doc."
    ],
    "errores": [
      "CORS abierto.",
      "CSP rota sin probar."
    ]
  },
  {
    "titulo": "Rate limit en login",
    "semana": 7,
    "horas": 5,
    "lectura": "OWASP brute force",
    "evidencia": "rate limit middleware",
    "objetivo": "Limitar intentos login por IP/usuario con respuesta 429 documentada.",
    "porque": "Piloto público en internet necesita mínimo anti-fuerza bruta.",
    "conceptos": [
      "rate limit.",
      "429.",
      "login."
    ],
    "pasos_extra": "Test 429 tras N intentos. No bloquear CI IPs — config test.",
    "lectura_rows": [
      [
        "OWASP",
        "Authentication",
        "—"
      ]
    ],
    "hecho": [
      "Rate limit.",
      "429 test o manual.",
      "Commit."
    ],
    "errores": [
      "Sin límite.",
      "Lockout permanente sin doc."
    ]
  },
  {
    "titulo": "Tests auth en CI o script local reproducible",
    "semana": 7,
    "horas": 5,
    "lectura": "m15 pipeline",
    "evidencia": ".github/workflows en m17",
    "objetivo": "Asegurar que suite auth+roles corre en CI o script documentado `npm run test:ci`.",
    "porque": "Deploy sin tests es regresión garantizada.",
    "conceptos": [
      "CI.",
      "regresión.",
      "auth tests."
    ],
    "pasos_extra": "Enlaza workflow desde README m17. Verde en main.",
    "lectura_rows": [
      [
        "m15",
        "nota cierre",
        "—"
      ]
    ],
    "hecho": [
      "CI verde.",
      "Auth en pipeline.",
      "Cierre semana 7."
    ],
    "errores": [
      "Tests skipped en CI.",
      "Solo local."
    ]
  },
  {
    "titulo": "ADR tenant_id y modelo multi-negocio",
    "semana": 8,
    "horas": 5,
    "lectura": "producto-saas multi-tenant",
    "evidencia": "projects/m17-agenda-ops/docs/adr-tenant-id.md",
    "objetivo": "ADR: dónde va `tenant_id`/`negocio_id`, migración futura, queries siempre filtradas.",
    "porque": "M26 depende de esta decisión; M17 la prepara.",
    "conceptos": [
      "tenant_id.",
      "ADR.",
      "single-tenant piloto."
    ],
    "pasos_extra": "ADR con contexto M09/M13. Lista tablas afectadas.",
    "lectura_rows": [
      [
        "producto-saas.md",
        "fases",
        "m13 L15"
      ]
    ],
    "hecho": [
      "adr-tenant-id.md.",
      "Tablas listadas.",
      "Commit."
    ],
    "errores": [
      "Multi-tenant completo día 1.",
      "Sin filtro en queries."
    ]
  },
  {
    "titulo": "Checklist camino a SaaS",
    "semana": 8,
    "horas": 5,
    "lectura": "Ficha M17 checklist",
    "evidencia": "projects/m17-agenda-ops/docs/checklist-saas.md",
    "objetivo": "Completar checklist ficha: tablas, roles, HTTPS, tests — gaps honestos.",
    "porque": "Transparencia > checkboxes mentirosos.",
    "conceptos": [
      "checklist.",
      "gap.",
      "SaaS."
    ],
    "pasos_extra": "checklist-saas.md copiado de ficha con Sí/No/Parcial.",
    "lectura_rows": [
      [
        "Ficha",
        "../M17-aplicaciones-web.md",
        "—"
      ]
    ],
    "hecho": [
      "checklist-saas.md.",
      "Gaps con plan.",
      "Commit."
    ],
    "errores": [
      "Todo Sí falso.",
      "Sin fecha para gaps."
    ]
  },
  {
    "titulo": "Demo grabable para design partner",
    "semana": 8,
    "horas": 5,
    "lectura": "Guion demo 10 min",
    "evidencia": "projects/m17-agenda-ops/docs/demo-script.md",
    "objetivo": "Guion demo: onboarding, cita, WhatsApp, roles. URL staging y creds test.",
    "porque": "Validación real del MVP.",
    "conceptos": [
      "demo.",
      "partner.",
      "staging."
    ],
    "pasos_extra": "demo-script.md + video opcional o capturas secuenciales.",
    "lectura_rows": [
      [
        "m12",
        "design partner",
        "—"
      ]
    ],
    "hecho": [
      "demo-script.md.",
      "URL HTTPS.",
      "Credenciales test only."
    ],
    "errores": [
      "Demo en localhost.",
      "Datos partner real."
    ]
  },
  {
    "titulo": "Cierre M17 — evidencias, dominio y handoff M19",
    "semana": 8,
    "horas": 5,
    "lectura": "Ficha M17 criterios dominio",
    "evidencia": "projects/m17-agenda-ops/docs/nota-cierre-m17.md",
    "objetivo": "Auditar P1–P3, proyecto piloto, criterios dominio, README final y handoff deploy M19.",
    "porque": "Cierras la materia más densa del plan disciplinario.",
    "conceptos": [
      "cierre.",
      "handoff M19.",
      "dominio."
    ],
    "pasos_extra": "nota-cierre-m17.md. README con URLs, tests, ADR, checklist. Commit `docs(m17): cierre materia`.",
    "lectura_rows": [
      [
        "Ficha",
        "../M17-aplicaciones-web.md",
        "../M19-nube-devops.md"
      ]
    ],
    "hecho": [
      "P1–P3 verificados.",
      "HTTPS demo.",
      "Criterios dominio.",
      "Handoff M19."
    ],
    "errores": [
      "Marcar completo sin deploy.",
      "Auth solo front."
    ]
  }
]
""")

BODIES: dict[int, str] = {}
BODIES[1] = r"""
# L01 — Scaffold Agenda Ops — API, DB y stack

**~5.0 h · Semana 1**

Sin stack fijo, M17 se convierte en un tour de frameworks. Hoy clavas el monolito modular del piloto.

## Objetivo

Dejar `projects/m17-agenda-ops/` con TypeScript strict, Postgres conectado y `stack.md` inmutable (salvo ADR).

## Por qué empieza así

Cada lección siguiente asume `GET /health` 200 y un esquema alineado a M09 (clientes, servicios, citas).

## Pasos (hazlos en orden)

### 1. Revisa producto y diseño previo (30–40 min)

```bash
cat curriculum/producto-saas.md | head -80
ls projects/m13-diseno projects/m09-bases-datos/migrations 2>/dev/null | head
```

Anota en un scratch: endpoints Must del piloto (auth, citas, clientes, servicios, admin).

### 2. Scaffold de carpetas (20 min)

```bash
mkdir -p projects/m17-agenda-ops/{docs,src,tests,scripts,apps}
cp projects/m17-agenda-ops/README.md /tmp/m17-readme.bak 2>/dev/null || true
```

Inicializa el repo app (npm/pnpm) **dentro** de `projects/m17-agenda-ops/` o documenta monorepo. TypeScript `strict: true`.

### 3. Documenta stack.md (40–50 min)

Crea `projects/m17-agenda-ops/stack.md` con: runtime, framework HTTP, ORM/query builder, front, test runner, por qué **no** cambiarás a mitad de materia.

### 4. Conecta Postgres y health (60–80 min)

Reusa Compose M09 o añade el tuyo. Variables en `.env.example` (sin secretos). Implementa `GET /health` que confirme proceso + (ideal) ping DB.

```bash
curl -sS http://localhost:3000/health
```

### 5. Commit

`docs(m17): l01 scaffold stack health postgres`
"""

BODIES[2] = r"""
# L02 — Registro con hash de contraseña

**~5.0 h · Semana 1**

Agenda Ops no admite usuarios en texto plano. Hoy nace `POST /auth/register`.

## Objetivo

Registro con validación (email/password), hash bcrypt/argon2 y usuario ligado al negocio piloto.

## Pasos (hazlos en orden)

### 1. Lectura OWASP Password Storage (25–35 min)

Cheat Sheet: cost factor, no MD5/SHA solo, never log passwords.

### 2. Esquema usuarios (30–40 min)

Tabla `usuarios` (o migración): email único, `password_hash`, `rol`, `negocio_id`/`tenant_id` nullable documentado. Sin password en claro.

### 3. Endpoint register (70–90 min)

`POST /auth/register` con Zod/valibot: email válido, password ≥8 (o política documentada). Respuesta 201 sin devolver el hash. 400 en inválido.

### 4. Tests (40–50 min)

```bash
npm test -- auth   # o vitest filter
```

Casos: 201 feliz; 400 email malo; hash ≠ plaintext en DB.

### 5. Commit

`feat(m17): l02 register con hash`
"""

BODIES[3] = r"""
# L03 — Login, sesión y GET /me protegido

**~5.0 h · Semana 1**

El panel necesita identidad servidor-confiable: cookie HttpOnly (preferida) o JWT en cookie documentada.

## Objetivo

`POST /auth/login` + `GET /me` con 401 sin credencial; documentar elección en `docs/auth.md`.

## Pasos (hazlos en orden)

### 1. Decide sesión vs JWT-cookie (20–30 min)

Escribe en `docs/auth.md`: opción, por qué, riesgos XSS/CSRF. Evita localStorage sin justificar.

### 2. Implementa login + me (80–100 min)

Login verifica hash; setea cookie Secure/HttpOnly/SameSite (en local puedes relajar Secure documentándolo). `GET /me` lee sesión y devuelve id, email, rol — no el hash.

### 3. Tests 401/200 (40–50 min)

Login → me 200; request sin cookie → 401; password malo → 401 (sin filtrar “email existe” si puedes).

### 4. Commit

`feat(m17): l03 login sesion y me`
"""

BODIES[4] = r"""
# L04 — Cierre semana 1 — suite auth P1

**~5.0 h · Semana 1**

P1 es la puerta del CRUD. Hoy consolidas la suite auth.

## Objetivo

≥6 tests auth verdes (register, login, me, logout) y README con comando reproducible.

## Pasos (hazlos en orden)

### 1. Completa logout (40–50 min)

Invalida sesión/cookie. Test: tras logout, `/me` → 401.

### 2. Suite y CI local (60–80 min)

```bash
npm test
```

Documenta en README: `npm test` / `npm run test:auth`. Enlaza P1 parcial.

### 3. Bitácora semana 1 (30 min)

`docs/semana-01.md`: commits, gaps, decisión auth.

### 4. Commit

`test(m17): l04 suite auth cierre p1`
"""

BODIES[5] = r"""
# L05 — Modelo de dominio citas, clientes y servicios

**~5.0 h · Semana 2**

CRUD sin dominio coherente genera IDOR y huérfanos. Hoy alineas entidades a M13/M09.

## Objetivo

Migraciones + carpeta `domain/` (o equivalente) con reglas puras sin ORM.

## Pasos (hazlos en orden)

### 1. Contrasta diseño (30 min)

Abre diagrama M13 y migraciones M09. Lista diferencias a resolver hoy.

### 2. Migraciones (70–90 min)

Asegura tablas `clientes`, `servicios`, `citas` con FKs, estados, duración/precio base. Aplica y `\dt`.

### 3. Reglas de dominio (50–60 min)

Funciones puras: `fin > inicio`, solapamiento, cancelación permitida. Tests unitarios sin DB si puedes.

### 4. Commit

`feat(m17): l05 dominio citas clientes servicios`
"""

BODIES[6] = r"""
# L06 — API citas — crear y listar con reglas

**~5.0 h · Semana 2**

Core del piloto: `POST/GET /citas` con auth y reglas de horario.

## Objetivo

Crear/listar citas; 201/400/409; listado filtrable por fecha; 401 sin auth.

## Pasos (hazlos en orden)

### 1. Contratos OpenAPI o tabla (20 min)

Documenta body: clienteId, servicioId, inicio, notas. Errores esperados.

### 2. Implementa endpoints (90–110 min)

Validación + regla solapamiento → 409. Listar exige sesión y filtra por negocio.

### 3. Tests (40–50 min)

201 feliz; 400 fin≤inicio; 409 solape; 401 sin cookie.

### 4. Commit

`feat(m17): l06 api citas crear listar`
"""

BODIES[7] = r"""
# L07 — CRUD clientes y servicios

**~5.0 h · Semana 2**

Servicios definen duración/precio; clientes son PII — trázalos al SRS.

## Objetivo

CRUD `/clientes` y `/servicios` con auth y 404 coherente.

## Pasos (hazlos en orden)

### 1. Endpoints (100–120 min)

Create/read/update/(soft)delete. Validar teléfono/nombre. No mezclar clientes entre negocios.

### 2. Tests (40–50 min)

Feliz + 404 + 401. Update servicio cambia duración usada en citas nuevas (documenta comportamiento).

### 3. Commit

`feat(m17): l07 crud clientes servicios`
"""

BODIES[8] = r"""
# L08 — Seeds demo y datos design partner

**~5.0 h · Semana 2**

Demo reproducible > “en mi máquina hay datos”.

## Objetivo

`scripts/seed.ts` (o SQL) idempotente: negocio, owner, staff, citas ejemplo — sin PII real.

## Pasos (hazlos en orden)

### 1. Diseño seed (25 min)

Usuarios test `owner@agenda.test` / `staff@agenda.test` con passwords solo en `.env.example` como placeholders.

### 2. Script idempotente (80–100 min)

Correr dos veces no duplica. README: cómo seedear y limpiar.

### 3. Cierre semana 2 (30 min)

`docs/semana-02.md` + captura de `\dt` o conteos.

### 4. Commit

`feat(m17): l08 seeds demo design partner`
"""

BODIES[9] = r"""
# L09 — Matriz de permisos owner y staff

**~5.0 h · Semana 3**

Roles sin matriz escrita se implementan a ojo.

## Objetivo

`docs/permisos.md`: acción × rol (cancelar, reportes, gestionar staff, CRUD).

## Pasos (hazlos en orden)

### 1. Inventario de rutas (40 min)

Lista endpoints sensibles actuales.

### 2. Matriz (70–90 min)

Tabla Markdown: Owner / Staff / Anónimo → Allow/Deny. Enlaza a stories M12.

### 3. Gaps (30 min)

Marca lo aún no enforced en API (L10 lo cierra).

### 4. Commit

`docs(m17): l09 matriz permisos owner staff`
"""

BODIES[10] = r"""
# L10 — Middleware de autorización en API

**~5.0 h · Semana 3**

403 debe ser imposible de saltar desde el front.

## Objetivo

Middleware `authorize(roles)` (o políticas) en handlers sensibles + tests 403/IDOR.

## Pasos (hazlos en orden)

### 1. Implementa middleware (80–100 min)

Inyecta usuario de sesión; rechaza rol insuficiente; opcional: scope por `negocio_id`.

### 2. Aplica a rutas (40 min)

Admin staff, borrar servicio, etc. según matriz.

### 3. Tests (40–50 min)

Staff en acción owner → 403. Usuario A no lee cita de B si aplica.

### 4. Commit

`feat(m17): l10 middleware autorizacion`
"""

BODIES[11] = r"""
# L11 — Panel admin mínimo — gestión staff

**~5.0 h · Semana 3**

El dueño administra su equipo aquí — feo pero claro.

## Objetivo

Ruta admin: listar/crear staff solo owner; `docs/ui-admin.md`.

## Pasos (hazlos en orden)

### 1. API admin si falta (40–50 min)

Endpoints alineados a matriz.

### 2. UI mínima (80–100 min)

Lista + formulario. Errores 403 visibles. Sin CSS hero.

### 3. Doc (20 min)

`docs/ui-admin.md` con pasos de demo.

### 4. Commit

`feat(m17): l11 panel admin staff`
"""

BODIES[12] = r"""
# L12 — Demo roles y inicio P3 WhatsApp

**~5.0 h · Semana 3**

Evidencia reproducible para el design partner.

## Objetivo

`docs/demo-roles.md` con usuarios test y acción bloqueada; anotar inicio P3 WhatsApp.

## Pasos (hazlos en orden)

### 1. Script demo (50–60 min)

Pasos numerados: login owner → OK; login staff → 403 en admin.

### 2. Evidencia (40 min)

Capturas o log HTTP (sin cookies completas). Enlace a tests 403.

### 3. Kickoff WhatsApp (30 min)

Sección en doc: deep-link vs API oficial; qué harás en L17–L20.

### 4. Commit

`docs(m17): l12 demo roles inicio p3`
"""

BODIES[13] = r"""
# L13 — Scaffold front y rutas protegidas

**~5.0 h · Semana 4**

Agenda Ops se usa desde el navegador a diario.

## Objetivo

Front (`apps/web` o `client/`) con login, layout y redirect si no hay sesión.

## Pasos (hazlos en orden)

### 1. Scaffold UI (60–80 min)

Router + página login + shell panel. `VITE_API_URL` / equivalente en `.env.example`.

### 2. Protected routes (50–60 min)

Sin sesión → `/login`. Con sesión → agenda.

### 3. CORS documentado (20 min)

Origen front permitido en API; nada de `*` en prod.

### 4. Commit

`feat(m17): l13 scaffold front rutas protegidas`
"""

BODIES[14] = r"""
# L14 — Flujo login/logout en UI

**~5.0 h · Semana 4**

Primera impresión del piloto: labels claros, error de credencial, logout limpio.

## Objetivo

Form login accesible + logout que limpia sesión en cliente y servidor.

## Pasos (hazlos en orden)

### 1. Form (70–90 min)

Labels, autocomplete, mensaje 401 en español. No meter token en querystring.

### 2. Logout (30–40 min)

Botón visible; limpia cookie/estado; redirect login.

### 3. Checklist manual (20 min)

`docs/ui-login-checklist.md` con 5 pasos.

### 4. Commit

`feat(m17): l14 login logout ui`
"""

BODIES[15] = r"""
# L15 — Listas con loading, error y vacío

**~5.0 h · Semana 4**

P2 exige los tres estados UX en agenda/listas.

## Objetivo

Agenda del día (o lista citas) con loading/error/vacío; `docs/ui-estados.md`.

## Pasos (hazlos en orden)

### 1. Implementa estados (90–110 min)

Skeleton/spinner; error con reintento; vacío con CTA “Nueva cita”.

### 2. Documenta (40 min)

`docs/ui-estados.md`: pantalla → cómo forzar cada estado (throttle, API down, seed vacío).

### 3. Commit

`feat(m17): l15 ui estados loading error vacio`
"""

BODIES[16] = r"""
# L16 — Formularios citas y clientes accesibles

**~5.0 h · Semana 4**

Errores de servidor mapeados a campos — no solo `alert`.

## Objetivo

Create/edit cita y cliente con labels, `aria-invalid` y validación alineada a API. Cierre P2 parcial.

## Pasos (hazlos en orden)

### 1. Forms (100–120 min)

Mapear 400 de API a mensajes por campo. Confiar también en validación servidor.

### 2. A11y rápida (30 min)

Tab order, labels for/id, contraste mínimo deje de ser accidente.

### 3. README P2 (20 min)

Marca P2 parcial: rutas protegidas + ui-estados + forms.

### 4. Commit

`feat(m17): l16 formularios accesibles p2`
"""

BODIES[17] = r"""
# L17 — Deep links WhatsApp — diseño del mensaje

**~5.0 h · Semana 5**

Canal que el design partner ya usa: wa.me con plantilla mínima de PII.

## Objetivo

`docs/integracion-whatsapp.md` con plantilla, placeholders y ejemplo URL-encoded.

## Pasos (hazlos en orden)

### 1. Diseña mensaje (50–60 min)

Ej.: “Hola {nombre}, te recordamos tu cita el {fecha} a las {hora}”. Sin notas clínicas sensibles.

### 2. Construye deep link (40 min)

Documenta `https://wa.me/52XXXXXXXXXX?text=...` y límites (no es API oficial).

### 3. Opt-in (30 min)

Cómo el negocio obtiene consentimiento; qué no harás (spam).

### 4. Commit

`docs(m17): l17 diseno deep link whatsapp`
"""

BODIES[18] = r"""
# L18 — Botón enviar recordatorio desde ficha cita

**~5.0 h · Semana 5**

Cierra el loop operativo: desde la ficha, abrir WhatsApp o registrar intento.

## Objetivo

Acción en UI + log sanitizado (sin teléfono completo si puedes) + pasos de prueba manual.

## Pasos (hazlos en orden)

### 1. API/UI acción (80–100 min)

Botón “Recordar por WhatsApp” genera link o abre ventana. Confirmación anti-spam.

### 2. Auditoría ligera (30 min)

Tabla/log: citaId, userId, timestamp — no dump de mensaje con PII.

### 3. Prueba manual (20 min)

Pasos en `docs/integracion-whatsapp.md`.

### 4. Commit

`feat(m17): l18 boton recordatorio whatsapp`
"""

BODIES[19] = r"""
# L19 — Confirmación de cita y estados

**~5.0 h · Semana 5**

Staff y owner deben ver el mismo estado en API y UI.

## Objetivo

Estados pendiente/confirmada/cancelada/atendida coherentes; tests de transición.

## Pasos (hazlos en orden)

### 1. Modelo de estados (30 min)

Diagrama ASCII de transiciones permitidas.

### 2. API + UI (90–110 min)

PATCH estado con auth; UI refleja; cancelar respeta matriz.

### 3. Tests (30–40 min)

Transición ilegal → 400/409; sin auth → 401.

### 4. Commit

`feat(m17): l19 estados confirmacion cita`
"""

BODIES[20] = r"""
# L20 — Cierre P3 integración WhatsApp

**~5.0 h · Semana 5**

P3 no inventa API oficial sin credencial: documenta gaps.

## Objetivo

`integracion-whatsapp.md` completo + checklist P3 en README + capturas.

## Pasos (hazlos en orden)

### 1. Completa doc (60–70 min)

Plantilla, botón, opt-in, límites legales, gaps.

### 2. Capturas (30 min)

Flujo recordatorio (datos seed).

### 3. README P3 (20 min)

Checklist Sí/Parcial/No.

### 4. Commit

`docs(m17): l20 cierre p3 whatsapp`
"""

BODIES[21] = r"""
# L21 — Variables de entorno y secrets

**~5.0 h · Semana 6**

Deploy seguro empieza por no commitear secretos.

## Objetivo

`.env.example` completo; validación de arranque si falta `DATABASE_URL`/`SESSION_SECRET`.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

Lista vars: DB, session, CORS origin, WhatsApp phone opcional.

### 2. Example + validación (70–90 min)

Fail-fast al boot con mensaje claro. Confirma `.gitignore` cubre `.env`.

### 3. Grep anti-secretos (20 min)

```bash
git ls-files | rg -i 'env|pem|secret' || true
```

### 4. Commit

`chore(m17): l21 env example y validacion`
"""

BODIES[22] = r"""
# L22 — Deploy staging en PaaS

**~5.0 h · Semana 6**

Piloto invisible no es piloto.

## Objetivo

URL staging + `docs/deploy.md` paso a paso (build, env, migraciones).

## Pasos (hazlos en orden)

### 1. Elige PaaS (20 min)

Render/Fly/Railway/etc. Anota límites free tier.

### 2. Deploy (100–130 min)

Build reproducible; secrets en panel; migra DB staging.

### 3. Documenta (30 min)

URL en README (staging). `docs/deploy.md`.

### 4. Commit

`docs(m17): l22 deploy staging paas`
"""

BODIES[23] = r"""
# L23 — HTTPS y health checks

**~5.0 h · Semana 6**

El design partner no debe ver “No seguro”.

## Objetivo

HTTPS en staging; `/health` usable por monitor/deploy script.

## Pasos (hazlos en orden)

### 1. Verifica TLS (40 min)

```bash
curl -vI https://TU-STAGING/health
```

Cert válido; redirige HTTP→HTTPS si aplica.

### 2. Health útil (50–60 min)

Incluye status DB o documenta por qué no. Wire al platform healthcheck.

### 3. Notas HSTS (20 min)

Opcional en staging; plan para prod.

### 4. Commit

`feat(m17): l23 https y health`
"""

BODIES[24] = r"""
# L24 — Smoke test post-deploy

**~5.0 h · Semana 6**

Detecta config rota antes de la demo.

## Objetivo

`docs/smoke-test.md` con corrida fechada: login + crear cita (+ health).

## Pasos (hazlos en orden)

### 1. Escribe checklist/script (50 min)

Pasos curl o Playwright mínimo contra staging.

### 2. Ejecuta y registra (60–80 min)

Fecha, resultado, fallos. No uses datos del partner real.

### 3. Cierre semana 6 (20 min)

Enlace smoke desde README.

### 4. Commit

`docs(m17): l24 smoke test staging`
"""

BODIES[25] = r"""
# L25 — Mapa OWASP Top 10 en el piloto

**~5.0 h · Semana 7**

M18 profundiza; hoy ubicas huecos con honestidad.

## Objetivo

`docs/owasp-mapa.md` ≥8 filas: riesgo → mitigación actual / gap M18.

## Pasos (hazlos en orden)

### 1. Recorre Top 10 (50–60 min)

Para cada ítem, ¿dónde pega en citas/auth/admin?

### 2. Tabla (70–90 min)

Columnas: ID OWASP, superficie Agenda Ops, estado (ok/parcial/gap), evidencia (test/commit).

### 3. Commit

`docs(m17): l25 mapa owasp piloto`
"""

BODIES[26] = r"""
# L26 — Headers de seguridad y CORS prod

**~5.0 h · Semana 7**

Reduce superficie antes de abrir al partner.

## Objetivo

Helmet (o equivalente) + CORS restrictivo; `docs/seguridad-http.md`.

## Pasos (hazlos en orden)

### 1. Headers (60–80 min)

Activa en staging; verifica con curl/`securityheaders` mental checklist.

### 2. CORS (40 min)

Solo origen del front. Documenta preflight.

### 3. Doc (20 min)

Valores y cómo probarlos.

### 4. Commit

`feat(m17): l26 headers cors seguridad`
"""

BODIES[27] = r"""
# L27 — Rate limit en login

**~5.0 h · Semana 7**

Piloto en internet ⇒ mínimo anti-fuerza bruta.

## Objetivo

Rate limit login → 429 documentado; no romper CI.

## Pasos (hazlos en orden)

### 1. Middleware (70–90 min)

Por IP y/o email; ventana corta; mensaje claro.

### 2. Prueba (40 min)

N intentos → 429. Config de test con umbral bajo.

### 3. Doc (15 min)

Úsalo en owasp-mapa (A07).

### 4. Commit

`feat(m17): l27 rate limit login`
"""

BODIES[28] = r"""
# L28 — Tests auth en CI o script local reproducible

**~5.0 h · Semana 7**

Deploy sin tests = regresión garantizada.

## Objetivo

Workflow CI o `npm run test:ci` documentado; suite auth+roles en verde.

## Pasos (hazlos en orden)

### 1. Pipeline (80–100 min)

GitHub Actions (u otro) con install + test. Secrets de CI ≠ prod.

### 2. README (20 min)

Badge o instrucción. Enlace a m15 si reutilizas.

### 3. Cierre semana 7 (20 min)

`docs/semana-07.md`.

### 4. Commit

`ci(m17): l28 tests auth en pipeline`
"""

BODIES[29] = r"""
# L29 — ADR tenant_id y modelo multi-negocio

**~5.0 h · Semana 8**

M26 depende de esta decisión; el piloto es single-tenant con cableado listo.

## Objetivo

`docs/adr-tenant-id.md`: dónde vive `tenant_id`/`negocio_id`, tablas, queries siempre filtradas.

## Pasos (hazlos en orden)

### 1. Contexto (30 min)

Relee producto-saas fases multi-tenant.

### 2. ADR (80–100 min)

Opciones; decisión; consecuencias; lista de tablas; qué **no** harás en M17 (SaaS completo).

### 3. Spot-check queries (30 min)

Al menos un listado de citas documenta filtro por negocio.

### 4. Commit

`docs(m17): l29 adr tenant id`
"""

BODIES[30] = r"""
# L30 — Checklist camino a SaaS

**~5.0 h · Semana 8**

Transparencia > checkboxes mentirosos.

## Objetivo

`docs/checklist-saas.md` con Sí/No/Parcial + plan de gaps.

## Pasos (hazlos en orden)

### 1. Copia criterios ficha (20 min)

Auth, CRUD, roles, WhatsApp, HTTPS, tests, tenant ADR.

### 2. Evalúa con evidencia (80–100 min)

Cada ítem enlaza commit/URL/doc. Fechas para gaps.

### 3. Commit

`docs(m17): l30 checklist camino saas`
"""

BODIES[31] = r"""
# L31 — Demo grabable para design partner

**~5.0 h · Semana 8**

Validación real del MVP en 10 minutos.

## Objetivo

`docs/demo-script.md` + URL HTTPS + creds **test** + capturas/video opcional.

## Pasos (hazlos en orden)

### 1. Guion (50–60 min)

Onboarding → cita → recordatorio WA → roles. Tiempos por bloque.

### 2. Ensayo en staging (60–80 min)

Arregla roturas. Anota minutos reales.

### 3. Empaqueta evidencia (20 min)

Capturas secuenciales o link video privado.

### 4. Commit

`docs(m17): l31 demo script design partner`
"""

BODIES[32] = r"""
# L32 — Cierre M17 — evidencias, dominio y handoff M19

**~5.0 h · Semana 8**

Cierras la materia más densa del bloque web: evidencias y handoff deploy.

## Objetivo

Auditar P1–P3, criterios de dominio, README final y `docs/nota-cierre-m17.md` → M19.

## Pasos (hazlos en orden)

### 1. Auditoría P1–P3 (50–60 min)

Tabla evidencias. Nada de “casi”.

### 2. Criterios dominio (40 min)

Autoevaluación honesta con enlaces.

### 3. Handoff M19 (40 min)

Dockerfile pendiente, secretos, URL staging, smoke — qué debe vivir en `projects/m19-ops/`.

### 4. Commit

`docs(m17): l32 cierre materia handoff m19`
"""

