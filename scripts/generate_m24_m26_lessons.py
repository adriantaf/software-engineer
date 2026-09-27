#!/usr/bin/env python3
"""Generate M01-style lesson markdown for M24–M26 (terminal / Agenda Ops)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "curriculum" / "etapas" / "03-terminal"

P24 = "projects/m24-emergentes"
P25 = "projects/m25-ciber"
P26 = "projects/m26-capstone"


def slugify(t: str) -> str:
    t = t.lower()
    t = (
        t.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
    )
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")


def render(
    materia: str,
    orden: int,
    titulo: str,
    semana: int,
    horas: float,
    lectura: str,
    evidencia: str,
    objetivo: str,
    porque: str,
    conceptos: list[str],
    pasos_extra: str,
    lectura_rows: list[tuple[str, str, str]],
    hecho: list[str],
    errores: list[str],
    siguiente_label: str | None,
    siguiente_href: str | None,
) -> str:
    lid = f"L{orden:02d}"
    conceptos_md = "\n".join(f"- {c}" for c in conceptos)
    lectura_table = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in lectura_rows)
    hecho_md = "\n".join(f"{i + 1}. {h}" for i, h in enumerate(hecho))
    errores_md = "\n".join(f"- {e}" for e in errores)
    sig = (
        f"\n## Siguiente\n\n[{siguiente_label}]({siguiente_href})\n"
        if siguiente_label and siguiente_href
        else ""
    )
    tag = materia.lower()

    return f"""---
id: {lid}
materia: {materia}
orden: {orden}
titulo: {titulo}
horas: {horas}
semana: {semana}
lectura: "{lectura}"
evidencia: "{evidencia}"
---

# {lid} — {titulo}

**~{horas:g} h · Semana {semana}**

## Objetivo

{objetivo}

## Por qué importa

{porque}

## Conceptos

{conceptos_md}

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

{pasos_extra}

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs({tag}): {lid.lower()} {slugify(titulo)[:42]}"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
{lectura_table}

## Hecho cuando

{hecho_md}

## Errores comunes

{errores_md}
{sig}"""


def write_materia(materia: str, lessons: list[dict]) -> int:
    out_dir = BASE / materia
    out_dir.mkdir(parents=True, exist_ok=True)
    n = len(lessons)
    for i, spec in enumerate(lessons):
        orden = i + 1
        next_label = next_href = None
        if orden < n:
            nt = lessons[i + 1]["titulo"]
            next_href = f"L{orden + 1:02d}-{slugify(nt)}.md"
            next_label = f"L{orden + 1:02d} — {nt}"
        body = render(
            materia=materia,
            orden=orden,
            siguiente_label=next_label,
            siguiente_href=next_href,
            **spec,
        )
        fname = f"L{orden:02d}-{slugify(spec['titulo'])}.md"
        (out_dir / fname).write_text(body, encoding="utf-8")
    return n


def _lesson(
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
    horas: float = 5,
) -> dict:
    return {
        "titulo": titulo,
        "semana": semana,
        "horas": horas,
        "lectura": lectura,
        "evidencia": evidencia,
        "objetivo": objetivo,
        "porque": porque,
        "conceptos": conceptos,
        "pasos_extra": pasos_extra,
        "lectura_rows": lectura_rows,
        "hecho": hecho,
        "errores": errores,
    }


def _rows(*pairs: tuple[str, str, str]) -> list[tuple[str, str, str]]:
    return list(pairs)


def _m24() -> list[dict]:
    lessons: list[dict] = []

    def add(**kw) -> None:
        lessons.append(_lesson(**kw))

    add(
        titulo="Estructura M24 y tres candidatos al producto",
        semana=1,
        lectura="Ficha M24 + producto-saas (recordatorios / realtime)",
        evidencia=f"{P24}/candidatos.md + bitácora semana-01.md",
        objetivo="Crear carpetas de evidencia y registrar tres tecnologías candidatas alineadas a Agenda Ops (ej. WhatsApp Cloud API, SSE/WebSockets, cola managed).",
        porque="M24 separa hype de utilidad; sin candidatos escritos terminas en tutorial random sin decisión.",
        conceptos=["Spike vs producción", "Fuentes primarias obligatorias", "Hipótesis de producto"],
        pasos_extra=f"""```bash
mkdir -p {P24}/research {P24}/spike
```

En `{P24}/candidatos.md` lista **tres** candidatos con una línea de valor para el ICP (barberías, clínicas dentales, etc.).

Abre `{P24}/bitacora/semana-01.md` (crea la carpeta) con objetivo de la semana: research completo antes del spike.""",
        lectura_rows=_rows(
            ("Plan", "[producto-saas.md](../../producto-saas.md)", "M21 backlog"),
            ("Ficha", "M24-tecnologias-emergentes.md", "—"),
        ),
        hecho=["Tres candidatos nombrados con valor ICP.", "Carpetas research/ y spike/ existen.", "Bitácora semana 1 iniciada."],
        errores=["Elegir blockchain sin caso de uso en citas.", "Copiar stack de un tutorial sin leer límites."],
    )
    add(
        titulo="Research candidato 1 — fuentes primarias",
        semana=1,
        lectura="Documentación oficial del candidato 1 (pricing + límites)",
        evidencia=f"{P24}/research/candidato-1.md",
        objetivo="Documentar candidato 1 con enlaces oficiales, pricing, regiones, rate limits y al menos una limitación crítica.",
        porque="Sin docs del vendor no puedes puntuar seguridad ni costo en la matriz.",
        conceptos=["Rate limits", "Webhook security", "Vendor lock-in"],
        pasos_extra=f"""Completa `{P24}/research/candidato-1.md` con secciones: **Problema**, **Docs**, **Precio**, **Límites**, **Seguridad (secretos/webhooks)**, **Crítica**.

Incluye ≥5 bullets accionables y ≥2 URLs oficiales (no blogs).""",
        lectura_rows=_rows(("Vendor", "Docs oficiales candidato 1", "Changelog seguridad")),
        hecho=["candidato-1.md completo.", "≥1 limitación honesta citada.", "Sin pegar API keys."],
        errores=["Solo marketing del vendor.", "Omitir costo por conversación/mensaje."],
    )
    add(
        titulo="Research candidatos 2 y 3",
        semana=1,
        lectura="Docs oficiales candidatos 2 y 3",
        evidencia=f"{P24}/research/candidato-2.md y candidato-3.md",
        objetivo="Mismo estándar que candidato 1 para los otros dos candidatos.",
        porque="Comparar tres opciones evita enamorarte del primer tutorial que viste.",
        conceptos=["Madurez del ecosistema", "Datos fuera del perímetro", "Operación (on-call)"],
        pasos_extra=f"""Completa `candidato-2.md` y `candidato-3.md` con el mismo template que L02.

Tabla comparativa rápida en `{P24}/research/comparacion-v0.md` (valor, complejidad, riesgo).""",
        lectura_rows=_rows(("Vendor", "Docs 2 y 3", "Issues conocidos GitHub")),
        hecho=["Dos archivos research completos.", "comparacion-v0.md con 3 filas."],
        errores=["Tres candidatos idénticos (solo cambia nombre).", "Ignorar si datos de clientes salen a terceros."],
    )
    add(
        titulo="Cierre research semana 1 y backlog M21",
        semana=1,
        lectura="Repaso research + issues Agenda Ops",
        evidencia=f"{P24}/research/README.md + enlace issue M21",
        objetivo="Cerrar P1 research: índice de notas y al menos un issue o comentario en backlog relacionado (spike futuro o descarte).",
        porque="El spike debe resolver duda del producto, no curiosidad técnica aislada.",
        conceptos=["Definition of spike", "Non-goals", "Evidencia en git"],
        pasos_extra=f"""`{P24}/research/README.md` enlaza los tres candidatos y resume en 10 líneas cuál parece más prometedor **sin** decidir aún.

En el repo del producto o `projects/m21-proyectos/`, abre issue “M24 spike: …” o comenta en roadmap.

Cierra `bitacora/semana-01.md` con horas reales vs plan.""",
        lectura_rows=_rows(("Ficha", "Práctica P1 M24", "M21 roadmap")),
        hecho=["README research.", "Enlace a issue/comentario backlog.", "Bitácora semana 1 cerrada."],
        errores=["Marcar P1 sin tres archivos.", "Prometer feature en M26 sin go/no-go."],
    )

    add(
        titulo="Matriz de adopción y pesos",
        semana=2,
        lectura="Criterios M24 + threat modeling ligero",
        evidencia=f"{P24}/matriz-adopcion.md",
        objetivo="Crear matriz con criterios ponderados: valor ICP, costo, riesgo ops, seguridad, fit M26.",
        porque="P2 obliga a explicitar trade-offs antes de escribir código del spike.",
        conceptos=["Peso ≥ hype", "Columna seguridad", "Score transparente"],
        pasos_extra=f"""En `{P24}/matriz-adopcion.md` define pesos (suma 100%). Filas = candidatos; columnas = criterios.

Documenta **cómo** puntuas (1–5) con ejemplos por celda del candidato más fuerte.""",
        lectura_rows=_rows(("Ficha", "Ejemplo matriz M24", "OWASP threat sketch")),
        hecho=["Matriz con pesos y ≥3 candidatos.", "Columna seguridad no vacía."],
        errores=["Todos 5/5 sin justificación.", "Olvidar costo mensual estimado."],
    )
    add(
        titulo="Costo, operación y vendor lock-in",
        semana=2,
        lectura="Pricing pages + SLA del candidato elegido preliminar",
        evidencia=f"{P24}/matriz-adopcion.md sección Costo",
        objetivo="Estimar costo mensual a 10 / 100 tenants y documentar dependencia del vendor (migración, export).",
        porque="Agenda Ops es SaaS; un canal de mensajería caro por conversación puede matar margen.",
        conceptos=["Costo marginal por tenant", "Exit strategy", "Fallback manual"],
        pasos_extra="""Actualiza la matriz con escenarios de costo (tabla tenants × mensajes/mes).

Para el candidato líder, escribe párrafo **Si el vendor sube precio 2×** en `matriz-adopcion.md`.""",
        lectura_rows=_rows(("Vendor", "Pricing oficial", "Términos de datos")),
        hecho=["Escenarios de costo documentados.", "Párrafo exit/lock-in."],
        errores=["Costo ‘gratis’ sin leer tier de producción.", "No considerar tiempo de ingeniería."],
    )
    add(
        titulo="Threat sketch del candidato para spike",
        semana=2,
        lectura="Webhook security + secret management",
        evidencia=f"{P24}/spike/threat-sketch.md",
        objetivo="Una página de amenazas del integración elegida: secretos, replay, PII en payloads, supply chain.",
        porque="Emergente ≠ inseguro por defecto, pero sí suele traer webhooks y tokens nuevos.",
        conceptos=["Firma HMAC webhooks", "PII en mensajes", "Principio mínimo privilegio"],
        pasos_extra=f"""`{P24}/spike/threat-sketch.md`: actores, datos que cruzan el límite, ≥5 amenazas, mitigaciones previstas en el spike.

Lista secretos nuevos (nombres, no valores) en tabla.""",
        lectura_rows=_rows(("OWASP", "Webhook / API security notes", "hilo seguridad")),
        hecho=["threat-sketch.md ≥1 página.", "Secretos nombrados sin valores."],
        errores=["Spike sin pensar en replay.", "Loguear payloads con teléfonos reales."],
    )
    add(
        titulo="Plan del spike — hipótesis, alcance y éxito",
        semana=2,
        lectura="Spike-driven development (notas ficha)",
        evidencia=f"{P24}/spike/hipotesis.md + spike/plan.md",
        objetivo="Elegir **un** candidato para semana 3; definir hipótesis medible, non-goals y criterio de éxito/fallo.",
        porque="Un spike sin timebox se convierte en feature a medias en producción.",
        conceptos=["Hipótesis falsable", "Timebox ≤1 semana", "Demo script"],
        pasos_extra=f"""`{P24}/spike/hipotesis.md`: “Si integramos X, entonces Y métrica mejora Z%” (aunque midas manualmente).

`{P24}/spike/plan.md`: entradas, salidas, comandos demo, **fuera de alcance** (lista explícita).

Actualiza matriz con candidato **elegido para spike**.""",
        lectura_rows=_rows(("Ficha", "Semana 3 spike", "P2 matriz")),
        hecho=["hipotesis.md y plan.md.", "Non-goals ≥3 ítems.", "Candidato spike único."],
        errores=["Spike de tres tecnologías a la vez.", "Hipótesis ‘aprender X’ sin métrica."],
    )

    add(
        titulo="Scaffold del spike y entorno aislado",
        semana=3,
        lectura="Quickstart oficial de la tecnología elegida",
        evidencia=f"{P24}/spike/README.md",
        objetivo="Bootstrap del PoC en rama/carpeta aislada sin tocar prod de Agenda Ops.",
        porque="M24 prohíbe merge experimental a prod sin go explícito.",
        conceptos=["Rama spike/*", "Secrets locales", "Staging vs prod"],
        pasos_extra=f"""`{P24}/spike/README.md`: prerequisitos, variables de entorno (nombres), comando para arrancar.

Código mínimo o script en `spike/`; `.env.example` sin valores reales.""",
        lectura_rows=_rows(("Vendor", "Quickstart", "Sandbox/test mode")),
        hecho=["README con comando reproducible.", ".env.example sin secretos."],
        errores=["Commit de tokens.", "PoC directo en rama main del SaaS."],
    )
    add(
        titulo="Flujo mínimo demostrable",
        semana=3,
        lectura="API reference secciones usadas en el spike",
        evidencia=f"{P24}/spike/ + demo-log.md",
        objetivo="Implementar un flujo que un mentor pueda ver en ≤10 min (webhook, evento UI, mensaje test, etc.).",
        porque="P3 exige PoC, no repositorio vacío con intenciones.",
        conceptos=["Happy path", "Idempotencia básica", "Logs sin PII"],
        pasos_extra="""Completa el happy path del plan. Registra en `spike/demo-log.md` pasos + capturas o salida terminal.

Si usas webhooks: verifica firma o documenta TODO explícito.""",
        lectura_rows=_rows(("Vendor", "API usada en spike", "threat-sketch")),
        hecho=["Flujo demo reproducible.", "demo-log.md con pasos."],
        errores=["Demo solo en tu máquina sin instrucciones.", "PII real en prueba."],
    )
    add(
        titulo="Medición contra la hipótesis",
        semana=3,
        lectura="Notas de experimento / métricas manuales",
        evidencia=f"{P24}/spike/resultados.md",
        objetivo="Registrar qué observaste vs hipótesis (latencia, costo estimado, complejidad, fallos).",
        porque="Un spike que ‘más o menos funcionó’ sin números no alimenta go/no-go.",
        conceptos=["Éxito / fallo honesto", "Deuda si hay go", "Aprendizaje"],
        pasos_extra=f"""`{P24}/spike/resultados.md`: tabla **Esperado / Observado / Conclusión**.

Si falló, documenta por qué — sigue siendo entrega válida.""",
        lectura_rows=_rows(("Ficha", "Hipótesis L08", "Matriz costo")),
        hecho=["resultados.md con ≥3 mediciones.", "Conclusión explícita."],
        errores=["Declarar éxito sin probar hipótesis.", "Ocultar blockers."],
    )
    add(
        titulo="Go/no-go, cierre M24 y handoff",
        semana=3,
        lectura="Repaso ficha M24 criterios dominio",
        evidencia=f"{P24}/go-no-go.md + bitácora semana-03.md",
        objetivo="Redactar decisión go/no-go argumentada; actualizar backlog; cerrar prácticas P2–P3 y criterios dominio.",
        porque="Un ‘no’ bien fundado cumple el proyecto si el spike demostró costo/riesgo > valor.",
        conceptos=["Go / no-go / defer", "Issue derivado", "Archivar spike"],
        pasos_extra=f"""`{P24}/go-no-go.md`: decisión, criterios, próximos pasos si go, qué archivar si no.

Cierra bitácora semana 3. README del proyecto enlaza toda la evidencia P1–P3.""",
        lectura_rows=_rows(("Ficha", "Criterios dominio M24", "M26 alcance")),
        hecho=["go-no-go.md publicado.", "README proyecto actualizado.", "Backlog M21 tocado."],
        errores=["Go sin plan de seguridad.", "No-go sin spike ejecutado."],
    )
    return lessons


def _m25() -> list[dict]:
    lessons: list[dict] = []

    def add(**kw) -> None:
        lessons.append(_lesson(**kw))

    w1 = [
        (
            "Inventario de activos SaaS prod y staging",
            "Listar URLs, repos, DB, colas, webhooks Stripe, CI y clasificar sin secretos.",
            f"""```bash
mkdir -p {P25}
```
`{P25}/inventario.md`: tabla Activo | Tipo | Ambiente | Dueño | Notas. Incluye Agenda Ops API, panel, Postgres, dominios, GitHub Actions.""",
            ["Superficie de ataque", "Staging ≠ prod", "Activo sin dueño = riesgo"],
        ),
        (
            "Clasificación de datos por tenant",
            "Etiquetar datos (PII citas, credenciales, billing metadata) y flujo entre componentes.",
            f"`{P25}/clasificacion-datos.md`: por tipo de dato, ¿en qué tabla/campo?, ¿quién accede?, retención esperada.",
            ["PII mínima", "tenant_id como control", "Logs y PII"],
        ),
        (
            "Dos tenants de prueba y mapa de identidades",
            "Crear tenant A y B con usuarios staff distintos; documentar IDs y roles.",
            f"`{P25}/tenants-prueba.md`: nombres de negocio ficticios, emails de prueba, roles. Sin contraseñas en claro.",
            ["Tenant de prueba realista", "Separación de datos", "No tenant1 genérico"],
        ),
        (
            "Primera prueba manual cross-tenant",
            "Intentar leer recurso del tenant B autenticado como A; documentar resultado.",
            f"`{P25}/aislamiento/nota-l01.md`: endpoint, IDs usados, status code, captura o curl redactado.",
            ["IDOR", "403 vs 404", "Evidencia reproducible"],
        ),
    ]
    for i, (tit, obj, pasos, conc) in enumerate(w1, start=1):
        add(
            titulo=tit,
            semana=1,
            lectura="OWASP Testing Guide — information gathering",
            evidencia=f"{P25}/ inventario o aislamiento según lección",
            objetivo=obj,
            porque="M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.",
            conceptos=conc,
            pasos_extra=pasos,
            lectura_rows=_rows(
                ("OWASP", "Testing Guide inventario", "[producto-saas](../../producto-saas.md)"),
                ("Ficha", "M25 checklist SaaS", "M18 access control"),
            ),
            hecho=[f"Archivo de evidencia de L{i:02d} en git.", "Sin secretos en markdown.", "Conexión Agenda Ops escrita en bitácora."],
            errores=["Inventario sin staging.", "Probar solo en localhost sin deploy."],
        )

    w2_titles = [
        ("Review authn — sesión y tokens", "Documentar flujo login/logout/refresh y dónde vive tenant_id.", f"{P25}/review/authn.md"),
        ("Review authz — roles staff vs admin", "Matriz recurso × rol × tenant; gaps en endpoints.", f"{P25}/review/authz-matrix.md"),
        ("Automatizar test cross-tenant en CI", "Al menos un test que falle si A lee cita de B.", f"test en repo producto + nota en {P25}/aislamiento/tests.md"),
        ("Cerrar ≥1 hallazgo crítico de aislamiento", "Fix + PR + evidencia antes de seguir cosméticos.", f"{P25}/hallazgos/hallazgo-01.md"),
    ]
    for tit, obj, ev in w2_titles:
        add(
            titulo=tit,
            semana=2,
            lectura="OWASP — Identity / Authorization testing",
            evidencia=ev,
            objetivo=obj,
            porque="Cosmética CSS no salva un leak entre barberías.",
            conceptos=["Authn vs authz", "tenant_id en sesión", "Tests de regresión"],
            pasos_extra=f"Trabaja en **tu** Agenda Ops desplegado. Registra comandos `curl` o Vitest/Jest con tokens de A y B.\n\nActualiza `{P25}/bitacora/semana-02.md`.",
            lectura_rows=_rows(("OWASP", "Access control testing", "M18 IDOR")),
            hecho=["Evidencia en ruta indicada.", "Si es test: corre en CI o documenta por qué no aún."],
            errores=["50 hallazgos menores y cero cross-tenant.", "tenant_id solo en frontend."],
        )

    w3 = [
        ("HTTPS, headers y configuración prod", "Verificar TLS, HSTS, headers seguridad en URL prod/staging.", f"{P25}/hardening/headers.md"),
        ("Secretos Stripe y rotación", "Inventario claves test/live; ninguna en repo; webhook secret.", f"{P25}/hardening/stripe-secrets.md"),
        ("Least privilege DB y deploy", "Usuario DB no superuser; permisos CI mínimos.", f"{P25}/hardening/least-privilege.md"),
        ("Backup y restore probado", "Restore en entorno aislado; anotar tiempo y pasos.", f"{P25}/hardening/restore-test.md"),
    ]
    for tit, obj, ev in w3:
        add(
            titulo=tit,
            semana=3,
            lectura="OWASP Configuration + Stripe webhooks docs",
            evidencia=ev,
            objetivo=obj,
            porque="Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.",
            conceptos=["Stripe signature", "Secrets manager / env", "Restore ≠ backup"],
            pasos_extra="Ejecuta checks reales (`curl -I`, `pg_restore`, etc.) y pega **salida redactada** en el archivo de evidencia.",
            lectura_rows=_rows(("Stripe", "Webhooks signing", "M19 backup")),
            hecho=["Checklist ítem demostrado.", "Sin valores de API keys."],
            errores=["Solo checklist teórico.", "Restore nunca probado."],
        )

    w4 = [
        ("Logging sin secretos ni PII innecesaria", "Auditar logs recientes; redactar campos; política breve.", f"{P25}/logging/politica-logs.md"),
        ("Rate limit login y abuso básico", "Confirmar o implementar límite; documentar umbrales.", f"{P25}/abuso/rate-limit.md"),
        ("Alertas mínimas operativas", "Qué te despierta: 5xx, disco, failed logins — aunque sea email manual.", f"{P25}/alertas/minimas.md"),
        ("Errores HTTP y fugas de stack", "Revisar 500 en staging; mensajes al cliente sin stack trace.", f"{P25}/logging/errores.md"),
    ]
    for tit, obj, ev in w4:
        add(
            titulo=tit,
            semana=4,
            lectura="OWASP Error handling / logging",
            evidencia=ev,
            objetivo=obj,
            porque="Un atacante lee tus logs si exfiltras tokens; un cliente lee tus stack traces.",
            conceptos=["Structured logging", "Correlation id", "Fail closed"],
            pasos_extra=f"Bitácora semana 4 en `{P25}/bitacora/semana-04.md`.",
            lectura_rows=_rows(("OWASP", "Logging cheat sheet", "M19 runbook")),
            hecho=["Política o config documentada.", "Ejemplo de log seguro vs inseguro."],
            errores=["Loguear Authorization header.", "Alertas imposibles de actuar."],
        )

    w5 = [
        ("Retención y borrado por tenant", "Política corta: cuánto guardas citas/logs; cómo borrar tenant demo.", f"{P25}/privacidad/retencion.md"),
        ("Minimización en exports y soporte", "Qué exporta soporte; sin dumps completos por defecto.", f"{P25}/privacidad/exports.md"),
        ("Consentimiento y avisos (contexto MX)", "Aviso privacidad en landing o panel; enlaces en repo marketing.", f"{P25}/privacidad/aviso-borrador.md"),
        ("Segundo hallazgo aislamiento cerrado", "Otro fix cross-tenant con test; tabla hallazgos actualizada.", f"{P25}/hallazgos/README.md"),
    ]
    for tit, obj, ev in w5:
        add(
            titulo=tit,
            semana=5,
            lectura="OWASP Privacy / LFPDPPP notas (contexto)",
            evidencia=ev,
            objetivo=obj,
            porque="Multi-tenant amplifica impacto de una fuga; privacidad es feature de confianza.",
            conceptos=["Retención", "Derecho de cancelación", "Datos por negocio"],
            pasos_extra="No copies plantillas legales sin revisión; borrador técnico-operativo basta para el plan.",
            lectura_rows=_rows(("Plan", "producto-saas privacidad", "M23 política LLM")),
            hecho=["Documento en ruta indicada.", "≥2 hallazgos aislamiento cerrados acumulado."],
            errores=["Política genérica sin tu producto.", "Un solo hallazgo en todo M25."],
        )

    w6 = [
        ("Tabletop — fuga de .env", "Simulación 30 min: secretos filtrados; pasos; comunicación.", f"{P25}/tabletop/env-leak.md"),
        ("Tabletop — acceso cross-tenant en prod", "Simulación: reporte cliente; contención; fix.", f"{P25}/tabletop/cross-tenant-incident.md"),
        ("Runbook de respuesta incidentes", "Unificar playbooks en runbook corto enlazado desde ops.", f"{P25}/runbook-incidentes.md"),
        ("Security review final y cierre M25", "Completar `security-review.md`; checklist dominio; handoff M26.", f"{P25}/security-review.md"),
    ]
    for tit, obj, ev in w6:
        add(
            titulo=tit,
            semana=6,
            lectura="OWASP Reporting + ficha M25",
            evidencia=ev,
            objetivo=obj,
            porque="M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.",
            conceptos=["Contención", "Rotación credenciales", "Post-mortem blameless"],
            pasos_extra="Cada tabletop: línea de tiempo, decisiones, acciones con dueño y fecha.",
            lectura_rows=_rows(("Ficha", "Proyecto security-review", "egreso.md")),
            hecho=["Narrativa ≥30 min equivalente escrita.", "security-review.md enlaza PRs y tests."],
            errores=["Tabletop copiado de blog.", "Review sin pruebas cross-tenant."],
        )
    return lessons


def _m26() -> list[dict]:
    """32 lecciones — máxima profundidad producción Agenda Ops."""
    lessons: list[dict] = []
    specs: list[tuple[int, str, str, str, list[str], str]] = []

    def S(sem, tit, lect, ev, conc, pasos):
        specs.append((sem, tit, lect, ev, conc, pasos))

    # Semana 1 — Alcance y tenancy
    S(1, "Alcance SaaS v1 congelado", "producto-saas.md completo + egreso.md", f"{P26}/alcance.md", ["MVP vs v1.1", "In/out scope", "Congelar"], f"Redacta `{P26}/alcance.md` con features in/out, dependencias M17/M19/M25. Lista explícita de **no** para v1.")
    S(1, "Plan 8 semanas y egreso-checklist honesto", "egreso.md rúbrica", f"{P26}/plan-8-semanas.md + egreso-checklist.md", ["Sprint semanal", "Demo interna", "Riesgos"], f"`plan-8-semanas.md` con 8 sprints, entregable y fecha demo pública. `egreso-checklist.md` estado actual sin autoengaño.")
    S(1, "Modelo tenant_id y resolución de tenant", "ADRs tenancy del repo", f"{P26}/memoria/tenancy-modelo.md", ["Row-level", "Subdomain vs header", "Middleware"], "Documenta cómo se resuelve tenant en API y UI. Diagrama request → tenant context.")
    S(1, "Riesgos integrador y dependencias", "M21 riesgos + M25 pendientes", f"{P26}/riesgos.md", ["Stripe", "Hosting", "Scope creep"], f"`{P26}/riesgos.md` con mitigaciones; enlaza review M25 si existe.")

    S(2, "Onboarding self-service de nuevo tenant", "Flujo registro negocio", "repo producto + nota onboarding", ["Signup", "Seed datos", "Aislamiento día 1"], "Implementa o documenta gap: nuevo negocio sin tu intervención manual. Dos tenants con nombres reales ficticios.")
    S(2, "Seeds y datos demo por tenant", "Datos prueba multi-tenant", f"{P26}/demo-tenants.md", ["No datos compartidos", "PII ficticia"], "Barbería A y clínica B con citas distintas; script seed idempotente.")
    S(2, "Panel admin por tenant", "Roles dueño/staff", "capturas o rutas en memoria", ["RBAC", "UI scoped"], "Verifica que cada pantalla filtra por tenant autenticado.")
    S(2, "Demo interna semana 2 — dos tenants", "Checklist demo", f"{P26}/demos/semana-02.md", ["Grabación corta", "Narrativa"], "Video o notas: login A, login B, datos no se mezclan.")

    S(3, "Citas CRUD multi-tenant", "Paridad M17 sin hardcode piloto", "tests citas", ["Regresión", "tenant_id en queries"], "Flujos crear/editar/cancelar citas; ningún hardcode del design partner único.")
    S(3, "Clientes y servicios por tenant", "Modelo dominio Agenda Ops", "evidencia repo", ["Catálogo servicios", "Duración"], "CRUD clientes/servicios scoped; prueba A no lista clientes de B.")
    S(3, "Staff y permisos mínimos", "authz matrix", f"{P26}/memoria/roles.md", ["Staff vs owner"], "Documenta permisos; al menos un test authz.")
    S(3, "Tests regresión flujos críticos", "CI verde", "pipeline + nota", ["Smoke E2E opcional", "API tests"], "Suite mínima en CI para citas + auth.")

    S(4, "Notificaciones o WhatsApp si en alcance", "M24 go/no-go o gap doc", f"{P26}/integraciones.md", ["Feature flag", "Fallback email"], "Si no está en alcance: gap documentado con fecha; si sí: webhook staging.")
    S(4, "App móvil M20 conectada o plan cierre", "m20-movil README", f"{P26}/mobile-gap.md", ["Misma API", "Staging HTTPS"], "Estado conexión móvil; APK contra staging o plan con fecha.")
    S(4, "Métricas M22 en producto", "metricas.md capstone", f"{P26}/metricas.md", ["Trials", "Activación"], "Registra métricas mínimas del SaaS; no vanity.")
    S(4, "Demo interna semana 4 — flujos completos", "demo script", f"{P26}/demos/semana-04.md", ["Vertical completo"], "Cita de punta a punta en dos tenants.")

    S(5, "Stripe test — productos Free/Pro", "Stripe docs test mode", "Stripe dashboard + doc", ["Price ids", "Test cards"], "Crea productos/planes; documenta IDs en memoria (sin secretos).")
    S(5, "Landing pública de precios", "Marketing repo o /pricing", "URL staging/prod", ["CTA trial", "Planes claros"], "Página pública enlazada desde README capstone.")
    S(5, "Checkout test end-to-end", "Stripe Checkout", f"{P26}/memoria/billing-flujo.md", ["Webhook", "Customer portal opcional"], "Usuario prueba completa suscripción test; eventos registrados.")
    S(5, "Webhooks Stripe verificados en deploy", "Signing secret", "config prod/staging", ["Idempotencia", "Replay"], "Webhook URL pública; firma verificada; log sin payload completo de tarjeta.")

    S(6, "Re-ejecutar review M25 y cerrar gaps", "security-review.md", f"{P26}/seguridad-m25.md", ["Cross-tenant CI", "Headers"], "Enlaza informe M25; lista issues abiertos y cierre.")
    S(6, "CI con tests cross-tenant obligatorios", "pipeline", "repo CI config", ["Bloqueo merge"], "PR no pasa sin test aislamiento.")
    S(6, "Backups prod y runbook ops", "M19 runbook", f"{P26}/memoria/ops.md", ["RTO/RPO honesto", "Restore"], "Copia o enlaza runbook; última fecha restore.")
    S(6, "Hardening final pre-demo pública", "checklist M25", f"{P26}/hardening-final.md", ["Secrets", "TLS"], "Checklist firmado con evidencia links.")

    S(7, "Memoria — arquitectura y diagramas", "plantilla memoria", f"{P26}/memoria/arquitectura.md", ["C4 ligero", "Deploy"], "Diagrama actualizado del SaaS en prod.")
    S(7, "Memoria — tenancy, billing, seguridad", "secciones P2", f"{P26}/memoria/*.md", ["Narrativa tercero"], "Un tercero entiende sin tu voz en vivo.")
    S(7, "Registro comercial M22 y trials", "m22-bektor", f"{P26}/comercial.md", ["Pipeline trials", "Demos"], "Enlaza evidencia comercial; estado honesto.")
    S(7, "Métricas y post-mortem técnico v1", "métricas semana 7", f"{P26}/post-mortem-v1.md", ["Deuda", "v1.1"], "Qué quedó fuera y por qué.")

    S(8, "Video demo público multi-tenant", "guion demo", f"{P26}/demo.md", ["YouTube/Loom", "Sin tutorial fondo"], "Graba: dos negocios, billing test, seguridad mencionada.")
    S(8, "Checklist egreso con evidencia enlazada", "egreso.md", f"{P26}/egreso-checklist.md final", ["Hashes commit", "URLs"], "Cada ítem con link o captura.")
    S(8, "README capstone índice maestro", "README proyecto", f"{P26}/README.md", ["Prod URL", "Repos"], "Un solo punto de entrada para evaluadores.")
    S(8, "Cierre integrador y handoff v1.1", "retrospectiva 8 semanas", f"{P26}/cierre.md", ["Aprendizaje", "Mantenimiento"], "Carta al yo futuro: operar Agenda Ops en prod.")

    for sem, tit, lect, ev, conc, pasos in specs:
        lessons.append(
            _lesson(
                titulo=tit,
                semana=sem,
                horas=5,
                lectura=lect,
                evidencia=ev,
                objetivo=f"Entregar evidencia de: {tit} para el capstone Agenda Ops en producción.",
                porque="M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.",
                conceptos=conc,
                pasos_extra=f"""```bash
mkdir -p {P26}/memoria {P26}/demos {P26}/bitacora
```

{pasos}

Registra horas y bloqueos en `{P26}/bitacora/semana-{sem:02d}.md`.""",
                lectura_rows=_rows(
                    ("Plan", "[producto-saas.md](../../producto-saas.md)", "[egreso.md](../../egreso.md)"),
                    ("Ficha", "M26-proyecto-integrador.md", "M25 security-review"),
                ),
                hecho=[
                    f"Artefacto indicado existe: {ev.split()[0]}.",
                    "Commit en git con mensaje docs(m26).",
                    "Bitácora de la semana actualizada.",
                ],
                errores=[
                    "Un solo tenant de mentira.",
                    "Stripe solo en localhost sin webhook desplegado.",
                    "Memoria genérica sin tu tenancy real.",
                ],
            )
        )
    return lessons


def main() -> None:
    counts = {
        "M24": write_materia("M24", _m24()),
        "M25": write_materia("M25", _m25()),
        "M26": write_materia("M26", _m26()),
    }
    print("Generated:", counts)


if __name__ == "__main__":
    main()
