"""Concrete timed lab steps for M25/M26 (no redundant mkdir).

Imported by overlays.py. L01 of each materia keeps a one-time setup mkdir.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# M25 — ciberseguridad aplicada
# ---------------------------------------------------------------------------

M25_CONCRETE: dict[int, list[tuple[str, str, str]]] = {
    2: [
        (
            "Inventario de tipos de dato",
            "25–35 min",
            """En `projects/m25-ciber/clasificacion-datos.md` crea tabla:

| Tipo | Ejemplos | Tabla/campo (si sabes) | Quién accede | Retención |
|------|----------|------------------------|--------------|-----------|

Filas mínimas: PII cliente (nombre/tel), credenciales, `tenant_id`, metadata billing Stripe, logs de app, backups.""",
        ),
        (
            "Flujos entre componentes",
            "90–110 min",
            """Añade sección **Flujos** con 4 diagramas en prosa (o mermaid):

1. Login → sesión → `tenant_id`
2. Crear cita → DB
3. Webhook Stripe → actualización plan
4. Export/soporte → datos salientes

Marca dónde un leak cruzaría tenants.""",
        ),
        (
            "Reglas de minimización",
            "30–40 min",
            """Sección **Reglas**: ≥5 bullets (qué no loguear, qué no exportar por defecto, retención demo). Bitácora `bitacora/semana-01.md`.""",
        ),
    ],
    3: [
        (
            "Define dos negocios ficticios",
            "20–30 min",
            """En `projects/m25-ciber/tenants-prueba.md`:

| Tenant | Negocio | Email staff | Rol | Notas |
|--------|---------|-------------|-----|-------|

Tres filas: A (barbería), B (clínica), opcional owner platform. **Sin** passwords en claro.""",
        ),
        (
            "Crea o anota IDs reales",
            "90–110 min",
            """En staging (preferido) o local con seed: crea tenants A y B.

Documenta UUIDs/`tenant_id`, user ids, y un recurso de cada uno (`cita_a_id`, `cita_b_id`).

```bash
# ejemplo — adapta a tu CLI/API; no pegues tokens
curl -s -H "Authorization: Bearer $TOKEN" "$API/tenants" | jq '.[].id'
```""",
        ),
        (
            "Mapa de identidades",
            "30–40 min",
            """Sección **Mapa**: usuario → roles → tenant. Confirma que A no tiene membership en B. Bitácora semana-01.""",
        ),
    ],
    5: [
        (
            "Dibuja el flujo authn",
            "25–35 min",
            """En `projects/m25-ciber/review/authn.md` secciones: **Login**, **Sesión/JWT**, **Logout/refresh**.

Anota dónde vive `tenant_id` (claim, cookie, header, fila DB).""",
        ),
        (
            "Inspecciona tokens reales",
            "90–110 min",
            """Login como staff A en staging. Documenta (redactado):

```bash
# captura Set-Cookie o body de login — redacta signature/secret
curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \\
  -H "Content-Type: application/json" \\
  -d '{"email":"staff-a@example.test","password":"$PASS"}'
```

Tabla: cookie/token | HttpOnly | Secure | SameSite | expira | lleva tenant_id?""",
        ),
        (
            "Amenazas y gaps",
            "30–40 min",
            """≥4 amenazas (token en localStorage, refresh eterno, tenant_id solo en client, logout incompleto). Cada una: severidad + mitigación. Bitácora semana-02.""",
        ),
    ],
    6: [
        (
            "Lista recursos y roles",
            "20–30 min",
            """En `projects/m25-ciber/review/authz-matrix.md` define roles: `owner`, `staff`, (opcional `platform`).

Lista ≥8 recursos/acciones: citas CRUD, clientes, servicios, billing, invites, exports.""",
        ),
        (
            "Matriz recurso × rol × tenant",
            "100–120 min",
            """Tabla:

| Recurso | owner | staff | cross-tenant | Evidencia |
|---------|-------|-------|--------------|-----------|

Marca allow/deny. Prueba ≥2 denegaciones con curl (status esperado 403/404).

```bash
curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $TOKEN_STAFF" \\
  -X DELETE "$API/tenants/$TENANT_A/billing"
```""",
        ),
        (
            "Gaps abiertos",
            "25–35 min",
            """Sección **Gaps**: issues enlazados. Bitácora semana-02 con 5 líneas.""",
        ),
    ],
    8: [
        (
            "Elige el hallazgo crítico",
            "20–30 min",
            """En `projects/m25-ciber/hallazgos/hallazgo-01.md`: título, severidad (Crítico/Alto), endpoint, tenants A/B, status observado vs esperado.""",
        ),
        (
            "Reproduce y fija",
            "100–130 min",
            """Secciones **Repro** (curl/test), **Root cause** (query sin `tenant_id`, middleware), **Fix** (PR link).

```bash
# antes/después — mismo request; redacta tokens
curl -s -w "\\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \\
  "$API/citas/$CITA_B_ID"
```

Merge el fix en la rama que deploya staging.""",
        ),
        (
            "Evidencia de cierre",
            "25–35 min",
            """**Cierre**: test o curl post-fix → 403/404. Enlace issue+PR. Bitácora semana-02.""",
        ),
    ],
    9: [
        (
            "Mide headers en staging/prod",
            "30–40 min",
            """En `projects/m25-ciber/hardening/headers.md` pega salida redactada:

```bash
curl -sI "https://TU-STAGING.example" | tee /tmp/headers.txt
```

Tabla: HSTS | CSP | X-Content-Type-Options | X-Frame-Options | Referrer-Policy | Permissions-Policy.""",
        ),
        (
            "TLS y redirects",
            "80–100 min",
            """Verifica HTTPS obligatorio (http→https), certificado válido, no mixed content en panel.

Documenta URL exacta + fecha del check. Si falta header: issue + plan de fix (no solo “poner nginx”).""",
        ),
        (
            "Prioriza remediación",
            "25–35 min",
            """Top 3 gaps con dueño=tú y evidencia esperada. Bitácora semana-03.""",
        ),
    ],
    10: [
        (
            "Inventario de secretos Stripe",
            "25–35 min",
            """En `projects/m25-ciber/hardening/stripe-secrets.md` tabla:

| Secreto | Ambiente | Dónde vive | Rotación |
|---------|----------|------------|----------|

Incluye `sk_test`/`sk_live`, `pk_*`, webhook signing secret. **Nunca** pegues valores.""",
        ),
        (
            "Busca fugas en repo e historial",
            "90–110 min",
            """Busca patrones sin imprimir valores:

```bash
rg -n "sk_live|sk_test|whsec_" --glob '!.git' . || true
rg -n "STRIPE_" .env.example apps/ || true
```

Documenta hallazgos (path + tipo). Si hay key en git: plan de rotación + `.gitignore`/secret scanning.""",
        ),
        (
            "Plan de rotación",
            "30–40 min",
            """Checklist de 6 pasos para rotar webhook secret en staging. Bitácora semana-03.""",
        ),
    ],
    11: [
        (
            "Inventario de privilegios",
            "25–35 min",
            """En `projects/m25-ciber/hardening/least-privilege.md`: rol DB app, rol CI deploy, quién puede `DROP`/`ALTER`.

Sin passwords.""",
        ),
        (
            "Verifica usuario DB no-superuser",
            "90–110 min",
            """En staging (o mirror), documenta:

```sql
-- corre como el rol de la app; pega solo el resultado
SELECT current_user, current_setting('is_superuser');
-- o \\du en psql — sin passwords
```

Si es superuser: issue + migración a rol con grants mínimos (SELECT/INSERT/UPDATE/DELETE en schemas de app).""",
        ),
        (
            "CI y deploy mínimos",
            "30–40 min",
            """Lista tokens GitHub/Actions con scopes. Quita permisos write innecesarios o documenta por qué quedan. Bitácora semana-03.""",
        ),
    ],
    12: [
        (
            "Documenta backup actual",
            "20–30 min",
            """En `projects/m25-ciber/hardening/restore-test.md`: provider, frecuencia, retención, dónde vive el artefacto (sin keys).""",
        ),
        (
            "Restore en entorno aislado",
            "100–130 min",
            """Restaura a DB/temporal **no prod**. Cronometra.

```bash
# ejemplo — adapta a tu provider; no uses prod
# pg_restore -d agenda_ops_restore_test backup.dump
```

Tabla: paso | comando/UI | minutos | resultado.""",
        ),
        (
            "RTO/RPO honestos",
            "25–35 min",
            """Declara RPO/RTO medidos (no marketing). Gaps + próxima prueba. Bitácora semana-03.""",
        ),
    ],
    13: [
        (
            "Audita logs recientes",
            "30–40 min",
            """En `projects/m25-ciber/logging/politica-logs.md` pega **2** ejemplos redactados: uno inseguro (PII/token) y uno seguro.

```text
# INSEGURO (ejemplo a capturar y redactar)
{"msg":"login","authorization":"Bearer eyJ…","email":"ana@…"}
# SEGURO
{"msg":"login_ok","request_id":"req_…","tenant_id":"t_…","user_id":"u_…"}
```

Fuentes: app logs, access logs, errores.""",
        ),
        (
            "Escribe la política",
            "80–100 min",
            """Secciones: **Qué se loguea**, **Qué nunca** (Authorization, passwords, bodies de pago), **Retención**, **Quién accede**, **correlation id**.

≥8 reglas concretas ligadas a tu stack.""",
        ),
        (
            "Ejemplo de cambio",
            "30–40 min",
            """Si encontraste fuga: PR o issue. Si no: checklist de revisión trimestral. Bitácora `semana-04.md`.""",
        ),
    ],
    14: [
        (
            "Define umbrales",
            "20–30 min",
            """En `projects/m25-ciber/abuso/rate-limit.md`: endpoint login (y opcional signup/webhook) → req/min → respuesta (429).""",
        ),
        (
            "Prueba o implementa límite",
            "100–120 min",
            """Dispara ráfaga controlada contra staging:

```bash
for i in $(seq 1 30); do
  curl -s -o /dev/null -w "%{http_code}\\n" -X POST "$API/auth/login" \\
    -H "Content-Type: application/json" \\
    -d '{"email":"nope@test","password":"x"}'
done | sort | uniq -c
```

Documenta códigos observados. Si no hay 429: implementa o configura WAF/middleware y re-prueba.""",
        ),
        (
            "Abuso adyacente",
            "25–35 min",
            """Nota 3 vectores (credential stuffing, brute invite, webhook flood) + estado. Bitácora semana-04.""",
        ),
    ],
    15: [
        (
            "Elige señales que te despiertan",
            "25–35 min",
            """En `projects/m25-ciber/alertas/minimas.md` tabla:

| Señal | Umbral | Canal | Dueño | Acción |
|-------|--------|-------|-------|--------|

Mínimo: 5xx spike, disco/DB, failed logins, webhook Stripe fallando.""",
        ),
        (
            "Configura o documenta canal",
            "90–110 min",
            """Deja al menos **un** canal real (email, Slack webhook, provider alert). Prueba con un evento falso o synthetic.

```bash
# ejemplo synthetic — adapta a tu provider
curl -s -X POST "$ALERT_WEBHOOK_URL" \\
  -H "Content-Type: application/json" \\
  -d '{"text":"m25 synthetic alert — safe to ignore"}'
```

Pega evidencia (screenshot path o mensaje redactado).""",
        ),
        (
            "Runbook de 5 líneas por alerta",
            "25–35 min",
            """Por cada señal: qué mirar primero. Bitácora semana-04.""",
        ),
    ],
    16: [
        (
            "Provoca o captura un 500",
            "25–35 min",
            """En staging, provoca error controlado (ruta inválida / force error). En `projects/m25-ciber/logging/errores.md` documenta body al cliente.""",
        ),
        (
            "Busca fugas de stack",
            "90–110 min",
            """Revisa respuestas 4xx/5xx del panel y API:

```bash
curl -s -o /tmp/err.json -w "%{http_code}" "$API/ruta-que-falla"
# ¿hay stack, SQL, paths absolutos, env?
```

Tabla: endpoint | status | fuga? | fix.""",
        ),
        (
            "Política de errores",
            "30–40 min",
            """Cliente ve mensaje genérico + request id; detalle solo en logs. Issue/PR si aplica. Bitácora semana-04.""",
        ),
    ],
    17: [
        (
            "Política de retención",
            "30–40 min",
            """En `projects/m25-ciber/privacidad/retencion.md`:

| Dato | Retención | Base | Cómo se borra |
|------|-----------|------|---------------|

Citas, logs, backups, tenants demo, exports temporales.""",
        ),
        (
            "Borrado de tenant demo",
            "90–110 min",
            """Describe (o ejecuta en staging) borrado de un tenant de prueba: tablas afectadas, orden, qué queda en backups.

```sql
-- ejemplo de inventario — adapta schemas
-- SELECT count(*) FROM citas WHERE tenant_id = $1;
```

**No** borres prod real de un cliente.""",
        ),
        (
            "Gaps legales vs técnicos",
            "25–35 min",
            """3 bullets: qué es decisión técnica hoy vs qué requiere abogado. Bitácora semana-05.""",
        ),
    ],
    18: [
        (
            "Inventario de exports",
            "25–35 min",
            """En `projects/m25-ciber/privacidad/exports.md`: CSV/PDF/admin dumps, quién puede, qué columnas.""",
        ),
        (
            "Minimiza un export real",
            "90–110 min",
            """Toma un export de soporte o admin. Propón columna set mínimo (sin teléfonos/notas si no hacen falta).

Si hay endpoint: verifica que staff de A no exporta B.

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" \\
  "$API/exports/clientes" | head -c 400
```""",
        ),
        (
            "Política soporte",
            "30–40 min",
            """Checklist de 6 pasos antes de pedir dump completo. Bitácora semana-05.""",
        ),
    ],
    19: [
        (
            "Localiza avisos actuales",
            "20–30 min",
            """En `projects/m25-ciber/privacidad/aviso-borrador.md`: URLs de landing/panel donde debería vivir aviso/privacidad.""",
        ),
        (
            "Borrador técnico-operativo",
            "100–120 min",
            """Redacta aviso **corto** (no copies plantilla legal genérica): qué datos, para qué, con quién (Stripe), retención, contacto.

Marca claramente: *borrador técnico del plan — no es asesoría legal*.""",
        ),
        (
            "Enlaces en producto",
            "25–35 min",
            """Issue/PR para linkear aviso desde footer o signup. Bitácora semana-05.""",
        ),
    ],
    20: [
        (
            "Segundo hallazgo distinto",
            "25–35 min",
            """En `projects/m25-ciber/hallazgos/hallazgo-02.md`: debe ser **otro** vector (p.ej. listado, update, export) distinto a hallazgo-01.""",
        ),
        (
            "Fix + test",
            "100–130 min",
            """Repro, root cause, PR, test automatizado o curl post-fix.

```bash
# post-fix — mismo vector que el hallazgo-02
curl -s -w "\\n%{http_code}" -H "Authorization: Bearer $TOKEN_A" \\
  "$API/EXPORT_O_UPDATE_DE_B"
```

Actualiza `hallazgos/README.md` con tabla acumulada (≥2 cerrados).""",
        ),
        (
            "Regresión",
            "25–35 min",
            """Confirma que hallazgo-01 sigue cerrado. Bitácora semana-05.""",
        ),
    ],
    22: [
        (
            "Escenario cross-tenant en prod",
            "30–40 min",
            """En `projects/m25-ciber/tabletop/cross-tenant-incident.md`: cliente B reporta ver datos de A. Define detección inicial.""",
        ),
        (
            "Timeline de contención",
            "90–110 min",
            """T+0 … T+120: verificar, deshabilitar endpoint/feature flag, notificar, rotar si aplica, comunicar.

Roles: tú = on-call. Sin copiar blog genérico — usa tus URLs/servicios.""",
        ),
        (
            "Acciones y dueños",
            "25–35 min",
            """Checklist ≥8 acciones con evidencia esperada. Bitácora semana-06.""",
        ),
    ],
    23: [
        (
            "Índice de playbooks",
            "25–35 min",
            """En `projects/m25-ciber/runbook-incidentes.md` enlaza tabletops L21–L22 + hardening relevante.""",
        ),
        (
            "Runbook operable",
            "100–120 min",
            """Secciones fijas: **Severidad**, **Contactos**, **Contención 15 min**, **Evidencia a preservar**, **Comunicación**, **Post-mortem**.

Cada sección con pasos numerados ejecutables a las 3 a.m.""",
        ),
        (
            "Enlace desde ops",
            "20–30 min",
            """Añade link desde `projects/m25-ciber/README.md` o runbook M19. Bitácora semana-06.""",
        ),
    ],
}

# ---------------------------------------------------------------------------
# M26 — proyecto integrador
# ---------------------------------------------------------------------------

M26_CONCRETE: dict[int, list[tuple[str, str, str]]] = {
    2: [
        (
            "Esqueleto de 8 sprints",
            "30–40 min",
            """En `projects/m26-capstone/plan-8-semanas.md` tabla:

| Semana | Entregable | Demo | Riesgo |
|--------|------------|------|--------|

Una fila por semana 1–8. Fechas reales.""",
        ),
        (
            "Checklist de egreso honesto",
            "90–110 min",
            """Crea/actualiza `projects/m26-capstone/egreso-checklist.md` copiando ítems de [egreso](../../../egreso.md).

Columnas: ítem | estado (hecho/parcial/no) | evidencia (path/URL) | gap.

Marca en rojo lo que aún es “no” — sin autoengaño.""",
        ),
        (
            "Bitácora semana 1",
            "20–30 min",
            """`bitacora/semana-01.md`: horas plan vs real; 1 dependencia bloqueante.""",
        ),
    ],
    3: [
        (
            "Documenta resolución de tenant",
            "30–40 min",
            """En `projects/m26-capstone/memoria/tenancy-modelo.md`: subdomain vs header vs sesión — **cuál usas**.

Diagrama request → middleware → `tenant_id`.""",
        ),
        (
            "Prueba el contexto en API",
            "90–110 min",
            """Muestra código o pseudo de dónde se setea el contexto. Verifica con dos tokens:

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/me" | jq '{tenant_id, role}'
curl -s -H "Authorization: Bearer $TOKEN_B" "$API/me" | jq '{tenant_id, role}'
```

Pega JSON redactado.""",
        ),
        (
            "Límites de confianza",
            "30–40 min",
            """≥5 bullets: qué el cliente no puede forjar, qué falla cerrado. Bitácora semana-01.""",
        ),
    ],
    4: [
        (
            "Lista riesgos P0–P2",
            "25–35 min",
            """En `projects/m26-capstone/riesgos.md` tabla: riesgo | impacto | probabilidad | mitigación | dueño | enlace M25 si aplica.""",
        ),
        (
            "Cubre dependencias críticas",
            "90–110 min",
            """Filas mínimas: aislamiento cross-tenant, Stripe webhooks, hosting/DB, scope creep WhatsApp/móvil, restore backups, secretos.

Cada P0 con mitigación accionable esta semana.""",
        ),
        (
            "Revisión con plan-8",
            "25–35 min",
            """Enlaza cada P0 a una semana del plan. Bitácora semana-01.""",
        ),
    ],
    5: [
        (
            "Mapea el flujo signup",
            "25–35 min",
            """En `projects/m26-capstone/onboarding.md`: pasos UI/API desde “crear negocio” hasta primer login staff.""",
        ),
        (
            "Ejecuta onboarding de un tenant nuevo",
            "100–120 min",
            """En staging: crea tenant C (o re-crea A limpio) **sin** SQL manual si el producto ya lo permite.

Documenta: URLs, IDs, tiempo, qué aún es manual (gap explícito).

```bash
# ejemplo — adapta endpoint real
curl -s -X POST "$API/tenants" -H "Content-Type: application/json" \\
  -d '{"name":"Barbería Demo C","owner_email":"owner-c@example.test"}'
```""",
        ),
        (
            "Criterio self-service",
            "25–35 min",
            """PASS si un tercero podría completar sin tu SSH. Si no: lista tareas para cerrar gap. Bitácora semana-02.""",
        ),
    ],
    6: [
        (
            "Diseña seeds A/B",
            "25–35 min",
            """En `projects/m26-capstone/demo-tenants.md`: negocio A vs B, 3 clientes, 3 servicios, 5 citas cada uno — PII ficticia.""",
        ),
        (
            "Script seed idempotente",
            "100–120 min",
            """Implementa o documenta comando:

```bash
# ejemplo
pnpm seed:demo   # o npm run db:seed:demo
```

Debe poder re-correrse sin duplicar basura. Verifica que citas de A no aparecen en queries de B.""",
        ),
        (
            "Evidencia de aislamiento en seed",
            "25–35 min",
            """Tabla counts por tenant. Bitácora semana-02.""",
        ),
    ],
    7: [
        (
            "Inventario de rutas admin",
            "25–35 min",
            """En `projects/m26-capstone/memoria/panel-admin.md` lista rutas del panel (dashboard, citas, clientes, staff, billing).""",
        ),
        (
            "Prueba UI scoped",
            "100–120 min",
            """Login A: captura o anota IDs visibles. Login B: confirma que no ves recursos de A.

Para ≥1 ruta API detrás del panel:

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/admin/clientes" | jq 'length'
curl -s -H "Authorization: Bearer $TOKEN_B" "$API/admin/clientes" | jq 'length'
```""",
        ),
        (
            "Nota de authz",
            "25–35 min",
            """Staff vs owner: qué pantallas cambian. Bitácora semana-02.""",
        ),
    ],
    8: [
        (
            "Guion demo semana 2",
            "25–35 min",
            """En `projects/m26-capstone/demos/semana-02.md`: guion ≤6 min — login A, dato, login B, contraste.""",
        ),
        (
            "Ejecuta y registra",
            "100–120 min",
            """Graba Loom/OBS o escribe narrativa paso a paso con timestamps. URLs staging reales.

Resultado: PASS/FAIL aislamiento + 3 bugs vistos.""",
        ),
        (
            "Acciones post-demo",
            "20–30 min",
            """Issues creados. Bitácora semana-02.""",
        ),
    ],
    9: [
        (
            "Matriz CRUD citas",
            "25–35 min",
            """En `projects/m26-capstone/memoria/citas-crud.md` tabla create/read/update/cancel × status esperado por tenant.""",
        ),
        (
            "Implementa/verifica flujos + aislamiento",
            "100–130 min",
            """Ejecuta create/edit/cancel en A y B. Ningún hardcode de un solo design partner.

```bash
# create en A
curl -s -X POST "$API/citas" -H "Authorization: Bearer $TOKEN_A" \\
  -H "Content-Type: application/json" \\
  -d '{"servicio_id":"…","cliente_id":"…","starts_at":"2026-10-01T16:00:00Z"}'

# A intenta leer cita de B → 403/404
curl -s -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" "$API/citas/$CITA_B"
```

Pega status codes en la memoria.""",
        ),
        (
            "Test mínimo",
            "30–40 min",
            """Añade o enlaza test de regresión. Bitácora semana-03.""",
        ),
    ],
    10: [
        (
            "Modelo dominio en memoria",
            "25–35 min",
            """En `projects/m26-capstone/memoria/clientes-servicios.md`: entidades Cliente y Servicio (campos, `tenant_id`, duración, precio).""",
        ),
        (
            "CRUD scoped + prueba cross-tenant",
            "100–130 min",
            """Crea cliente y servicio en A y en B. Verifica listados:

```bash
curl -s -H "Authorization: Bearer $TOKEN_A" "$API/clientes" | jq '[.[]|.id]'
curl -s -H "Authorization: Bearer $TOKEN_B" "$API/clientes" | jq '[.[]|.id]'
# sets disjuntos
```

Documenta endpoints y status de un GET cruzado.""",
        ),
        (
            "Captura o nota UI",
            "25–35 min",
            """Enlace a ruta UI o screenshot path en repo. Bitácora semana-03.""",
        ),
    ],
    11: [
        (
            "Define roles mínimos",
            "25–35 min",
            """En `projects/m26-capstone/memoria/roles.md`: `owner` vs `staff` — permisos allow/deny (≥8 filas).""",
        ),
        (
            "Aplica y prueba",
            "100–120 min",
            """Invite/crea staff en tenant A. Prueba acción prohibida (p.ej. borrar negocio / ver billing).

```bash
curl -s -w "%{http_code}" -X DELETE -H "Authorization: Bearer $TOKEN_STAFF_A" \\
  "$API/tenants/$TENANT_A"
```

Espera 403. Documenta.""",
        ),
        (
            "Test authz",
            "30–40 min",
            """Al menos un test automatizado o script documentado en CI local. Bitácora semana-03.""",
        ),
    ],
    12: [
        (
            "Elige suite mínima",
            "25–35 min",
            """En `projects/m26-capstone/tests-regresion.md`: lista tests (auth, citas CRUD, cross-tenant). Comando exacto.""",
        ),
        (
            "Corre en CI o documenta pipeline",
            "100–120 min",
            """```bash
pnpm test   # o el comando real
```

Pega resumen (passed/failed). Si CI: enlace a workflow verde. Si no: YAML propuesto + issue.""",
        ),
        (
            "Política de merge",
            "25–35 min",
            """Escribe: “no merge a main sin X verde”. Bitácora semana-03.""",
        ),
    ],
    13: [
        (
            "Decisión go/no-go",
            "25–35 min",
            """En `projects/m26-capstone/integraciones.md`: WhatsApp/notificaciones **in** o **out** de v1, citando alcance L01 y M24 si existe.""",
        ),
        (
            "Si in: integra staging; si out: defer escrito",
            "100–120 min",
            """**In:** webhook/provider en staging, feature flag, evidencia de envío test.

**Out:** sección **Defer** con fecha v1.1, riesgo, alternativa (email).

No dejes “tal vez”.""",
        ),
        (
            "Fallback",
            "25–35 min",
            """Cómo se entera el cliente si falla el canal. Bitácora semana-04.""",
        ),
    ],
    14: [
        (
            "Estado móvil M20",
            "25–35 min",
            """En `projects/m26-capstone/mobile-gap.md`: ¿APK/app apunta a staging HTTPS? ¿misma API v1?""",
        ),
        (
            "Conecta o cierra el gap",
            "100–120 min",
            """**Conectado:** login + listar citas desde móvil contra staging; anota build/version.

**Gap:** plan con fecha, qué falta (CORS, auth, store), impacto en egreso.

```bash
# verifica API alcanzable
curl -sI "$API/health"
```""",
        ),
        (
            "Decisión explícita",
            "20–30 min",
            """Una frase: incluido en demo pública / diferido. Bitácora semana-04.""",
        ),
    ],
    15: [
        (
            "Elige métricas M22",
            "25–35 min",
            """En `projects/m26-capstone/metricas.md`: trials, activación (1ª cita), conversion Free→Pro — definiciones.""",
        ),
        (
            "Hazlas visibles",
            "100–120 min",
            """Dashboard interno o sección admin con números **reales** de staging (aunque sean bajos).

Tabla: métrica | fórmula | valor hoy | dónde se ve en producto.""",
        ),
        (
            "Nada vanity",
            "20–30 min",
            """Elimina o marca como no-KPI cualquier contador inútil. Bitácora semana-04.""",
        ),
    ],
    16: [
        (
            "Guion demo semana 4",
            "25–35 min",
            """En `projects/m26-capstone/demos/semana-04.md`: vertical completo — onboarding o login, cita, contraste tenants, mención billing si listo.""",
        ),
        (
            "Ejecuta flujos completos",
            "100–120 min",
            """Graba o documenta con timestamps. Dos tenants. Anexa bugs encontrados como issues.""",
        ),
        (
            "Comparación vs semana 2",
            "20–30 min",
            """Qué mejoró. Bitácora semana-04.""",
        ),
    ],
    18: [
        (
            "Define copy de precios",
            "25–35 min",
            """En `projects/m26-capstone/memoria/landing-precios.md`: planes Free/Pro, precios MXN alineados a M22, CTA trial.""",
        ),
        (
            "Publica página en staging/prod",
            "100–120 min",
            """Ruta `/pricing` o landing marketing. Verifica en navegador:

```bash
curl -sI "https://TU-DOMINIO/pricing" | head -n 15
```

Enlaza URL desde README capstone.""",
        ),
        (
            "Coherencia con Stripe",
            "25–35 min",
            """Tabla: texto landing ↔ price_id (sin secretos). Bitácora semana-05.""",
        ),
    ],
    20: [
        (
            "Endpoint webhook en deploy",
            "30–40 min",
            """En `projects/m26-capstone/memoria/webhooks-stripe.md`: URL pública staging/prod, eventos suscritos (`checkout.session.completed`, etc.).""",
        ),
        (
            "Verifica firma e idempotencia",
            "100–120 min",
            """Confirma verificación de firma Stripe en código desplegado. Prueba evento (CLI o dashboard):

```bash
# ejemplo Stripe CLI — solo test mode
stripe listen --forward-to localhost:3000/api/webhooks/stripe
stripe trigger checkout.session.completed
```

Documenta: replay del mismo event id no duplica side effects.""",
        ),
        (
            "Logs seguros",
            "25–35 min",
            """Qué se loguea (tipo evento, id) y qué no (PAN). Bitácora semana-05.""",
        ),
    ],
    21: [
        (
            "Relee security-review M25",
            "30–40 min",
            """En `projects/m26-capstone/seguridad-m25.md` índice de hallazgos abiertos vs cerrados desde `projects/m25-ciber/security-review.md`.""",
        ),
        (
            "Cierra gaps bloqueantes",
            "100–120 min",
            """Lista P0/P1. Cada uno: issue, fix o waiver firmado con riesgo residual.

Re-corre test cross-tenant:

```bash
pnpm test -- aislamiento   # adapta
```""",
        ),
        (
            "Handoff a demo pública",
            "25–35 min",
            """Qué debe estar verde antes del video. Bitácora semana-06.""",
        ),
    ],
    22: [
        (
            "Localiza el job CI",
            "25–35 min",
            """En `projects/m26-capstone/ci-cross-tenant.md`: path del workflow + nombre del job que corre tests de aislamiento.""",
        ),
        (
            "Haz el test obligatorio",
            "100–120 min",
            """PR de prueba: rompe a propósito el assert o salta el test — el CI debe fallar. Luego restaura.

Documenta: required check en branch protection (o issue si no tienes permisos).

```bash
gh run list --limit 5   # si usas GitHub Actions
```""",
        ),
        (
            "Política escrita",
            "20–30 min",
            """“Merge bloqueado si cross-tenant rojo”. Bitácora semana-06.""",
        ),
    ],
    23: [
        (
            "Estado de backups",
            "25–35 min",
            """En `projects/m26-capstone/memoria/ops.md`: última fecha de backup, retención, enlace a restore-test M25.""",
        ),
        (
            "Runbook ops corto",
            "100–120 min",
            """Secciones: deploy, rollback, restore, rotar secreto, escalación. Comandos reales de **tu** stack:

```bash
# plantilla — sustituye por tus comandos reales
# deploy: …
# rollback: …
# restore dry-run: …
```

Incluye RTO/RPO honestos.""",
        ),
        (
            "Fecha de próxima prueba restore",
            "20–30 min",
            """Agenda en el doc. Bitácora semana-06.""",
        ),
    ],
    24: [
        (
            "Checklist pre-demo",
            "30–40 min",
            """En `projects/m26-capstone/hardening-final.md` tabla: headers | secretos | errores | rate-limit | cross-tenant CI | cada uno con link evidencia.""",
        ),
        (
            "Cierra los rojos",
            "100–120 min",
            """Todo ítem rojo → fix o waiver. Re-verifica:

```bash
curl -sI "https://TU-PROD-O-STAGING" | rg -i "strict-transport|content-security|x-frame"
```""",
        ),
        (
            "Go/no-go demo pública",
            "20–30 min",
            """Frase explícita + fecha. Bitácora semana-06.""",
        ),
    ],
    25: [
        (
            "Bosqueja C4 ligero",
            "30–40 min",
            """En `projects/m26-capstone/memoria/arquitectura.md`: contexto (actores) + contenedores (web, API, DB, Stripe, CI).""",
        ),
        (
            "Diagrama deploy real",
            "90–110 min",
            """Mermaid o imagen en repo: regiones, servicios, secretos (nombres). URLs prod/staging.

Sección **Decisiones**: 5 ADRs cortas (tenancy, auth, billing, logs, mobile).""",
        ),
        (
            "Revisión de frescura",
            "25–35 min",
            """Fecha del diagrama = esta semana. Bitácora semana-07.""",
        ),
    ],
    26: [
        (
            "Outline de narrativa",
            "25–35 min",
            """En `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`: H2 Tenancy | Billing | Seguridad.""",
        ),
        (
            "Escribe para un tercero",
            "100–120 min",
            """Cada H2: cómo funciona en **tu** producto + 2 evidencias (path test, URL, PR).

Un mentor debe entender sin tu voz en vivo. Enlaza L03, L17–L20, L21–L24.""",
        ),
        (
            "Pasa el test del screenshot",
            "25–35 min",
            """Si quitas tu cara del video, ¿el doc basta? Ajusta. Bitácora semana-07.""",
        ),
    ],
    27: [
        (
            "Inventario comercial",
            "25–35 min",
            """En `projects/m26-capstone/comercial.md` enlaza `projects/m22-bektor/` (demos, trials, pricing).""",
        ),
        (
            "Estado honesto del pipeline",
            "90–110 min",
            """Tabla: lead/demo/trial | fecha | resultado | siguiente paso.

Números reales aunque sean cero — declara cero.""",
        ),
        (
            "Puente a producto",
            "25–35 min",
            """Qué métrica del SaaS alimenta el discurso comercial. Bitácora semana-07.""",
        ),
    ],
    28: [
        (
            "Recoge métricas v1",
            "30–40 min",
            """En `projects/m26-capstone/post-mortem-v1.md`: uptime/deploy count, tests, hallazgos seguridad, trials — lo que tengas.""",
        ),
        (
            "Post-mortem técnico",
            "90–110 min",
            """Secciones: **Qué salió bien**, **Qué dolió**, **Deuda consciente**, **v1.1 (5 ítems con fecha)**.

Sin blame theater; con owners.""",
        ),
        (
            "Cierre de alcance",
            "25–35 min",
            """Lista features que quedaron out y por qué. Bitácora semana-07.""",
        ),
    ],
    30: [
        (
            "Congela checklist final",
            "30–40 min",
            """En `projects/m26-capstone/egreso-checklist.md`: cada ítem de [egreso](../../../egreso.md) con estado final.""",
        ),
        (
            "Enlaza evidencias",
            "100–120 min",
            """Cada “hecho” lleva path git, URL, o commit hash. Nada de “está en mi laptop”.

```bash
git log --oneline -20 -- projects/m26-capstone projects/m25-ciber
```

Pega hashes relevantes junto a ítems difíciles.""",
        ),
        (
            "Ítems parciales",
            "25–35 min",
            """Los parciales explican gap + plan. Bitácora semana-08.""",
        ),
    ],
    31: [
        (
            "Estructura del README",
            "25–35 min",
            """En `projects/m26-capstone/README.md`: Prod URL | Staging | Demo video | Memoria | Seguridad | Comercial | Cómo correr tests.""",
        ),
        (
            "Índice maestro clickeable",
            "90–110 min",
            """Links relativos a **todos** los artefactos clave (alcance, demos, billing, security-review, egreso-checklist).

Un evaluador entra solo por este archivo.""",
        ),
        (
            "Smoke del índice",
            "25–35 min",
            """Abre 5 links al azar; arregla rotos. Bitácora semana-08.""",
        ),
    ],
    32: [
        (
            "Carta de cierre",
            "30–40 min",
            """En `projects/m26-capstone/cierre.md`: qué es Agenda Ops hoy (3 párrafos), para quién, URL.""",
        ),
        (
            "Handoff v1.1",
            "90–110 min",
            """Secciones: **Operar en prod** (checklist semanal), **Backlog v1.1**, **Riesgos residuales**, **Aprendizajes**.

Enlaza runbook y post-mortem.""",
        ),
        (
            "Última bitácora",
            "20–30 min",
            """`bitacora/semana-08.md`: horas totales del capstone (estimadas) + una frase de cierre.""",
        ),
    ],
}
