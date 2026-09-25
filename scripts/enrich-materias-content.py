#!/usr/bin/env python3
"""Añade En cristiano + Semana tipo + Evidencia de hecho a todas las materias."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/workspace/curriculum/etapas")

# Contenido por materia: cristiano, semana_tipo (markdown body), evidencias (p1,p2,p3,proj)
ENRICH: dict[str, dict] = {
    "M01": {
        "cristiano": "hoy configuras tu entorno, haces commits claros en **este** repo y escribes una decisión corta (ADR). No es un curso de Git de 8 horas: es hábito.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Método + shell | 6–8 | Terminal, docs, bitácora |
| Git en este repo | 6–8 | Commits atómicos, ramas, diff |
| Proyecto diario | 4–6 | `projects/m01-diario/` + `progress.json` |
| Retro | 1 | Qué bloqueó / qué sigue |""",
        "evid": [
            ("P1", "Entorno", "`projects/m01-diario/entorno.md` con SO, Git, Node; commit `docs(m01): registrar entorno`."),
            ("P2", "Commits", "≥7 commits atómicos en 7 días (mensajes qué/porqué); `git log --oneline` pegado en la bitácora."),
            ("P3", "ADR", "`projects/m01-diario/adr-001-*.md` con contexto / decisión / consecuencias."),
            ("Proyecto", "Diario", "Al menos 2 notas `semana-NNNN.md` + `progress.json` actualizado."),
        ],
    },
    "M02": {
        "cristiano": "aprendes TypeScript de verdad con katas, un script real y tests. El cierre es una CLI de hábitos que puedes enseñar.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + tipado | 6–8 | EJ / Handbook según tabla Lecturas |
| Katas / labs | 6–8 | Exercism/Codewars en TS strict |
| Proyecto CLI | 4–6 | `projects/m02-habits/` + Vitest |
| Retro | 1 | 3 dudas tipadas resueltas |""",
        "evid": [
            ("P1", "Katas", "Repo `projects/m02-katas/` con ≥20 soluciones TS + README."),
            ("P2", "Script", "Script que lee JSON y reporta; maneja archivo faltante con error claro."),
            ("P3", "Tests", "`npm test` verde con ≥10 tests Vitest."),
            ("Proyecto", "CLI", "Comandos add/list/done/stats/export; JSON local; README con ejemplos."),
        ],
    },
    "M03": {
        "cristiano": "lógica, conjuntos y grafos no son adorno: los usas al razonar algoritmos y modelos. Demuestras a mano y codeas lo esencial.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría Rosen | 6–8 | Capítulos de la semana + 3 demos |
| Implementación | 6–8 | Ops de conjuntos / grafos en TS |
| Proyecto CLI | 4–6 | Visualizador BFS/DFS |
| Retro | 1 | Una prueba que aún no te sale |""",
        "evid": [
            ("P1", "Demos", "10 demostraciones cortas en `projects/m03-discretas/demos.md`."),
            ("P2", "Código", "Ops de conjuntos + matriz de relación + adyacencia con tests."),
            ("P3", "Big-O", "5 funciones tuyas con Big-O justificado en Markdown."),
            ("Proyecto", "Grafo CLI", "Lee grafo JSON, imprime BFS/DFS y grados; README con teoría."),
        ],
    },
    "M04": {
        "cristiano": "usas datos para preguntar mejor (no solo calcular). Simulas, describes un CSV y escribes un informe que un negocio entendería.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Probabilidad | 6–8 | Caps. Lecturas + simulación TS |
| Descriptiva | 6–8 | CSV real → media/mediana/σ |
| Informe | 4–6 | `informe.md` con limitaciones |
| Retro | 1 | Correlación ≠ causalidad (ejemplo tuyo) |""",
        "evid": [
            ("P1", "Simulación", "`projects/m04-stats/` con 10_000 lanzamientos y conclusión escrita."),
            ("P2", "CSV", "Pipeline limpia → tablas descriptivas; notebook o script."),
            ("P3", "Hipótesis", "Una pregunta de negocio + conclusión cuidadosa (sin overclaim)."),
            ("Proyecto", "Informe", "`informe.md`: pregunta, datos, método, resultado, limitaciones."),
        ],
    },
    "M05": {
        "cristiano": "entiendes qué pasa cuando corres `node`: CPU, RAM, disco. Dejas de tratar la máquina como magia.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Arquitectura | 6–8 | Diagrama + lectura Stallings |
| Memoria / I/O | 6–8 | Labs de medición |
| Documento | 4–6 | `projects/m05-como-corre/` |
| Retro | 1 | RAM vs disco en tus palabras |""",
        "evid": [
            ("P1", "Diagrama", "1 página CPU–RAM–I/O en Markdown/imagen."),
            ("P2", "Binario", "Ejercicios de overflow/conversión en código + notas."),
            ("P3", "Benchmark", "Loop vs I/O medido ≥3 veces; explicación."),
            ("Proyecto", "Cómo corre", "README desde `node cli.js` hasta el output."),
        ],
    },
    "M06": {
        "cristiano": "modelas un dominio con tipos serios, refactorizas con Código limpio y empaquetas algo reutilizable.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| OO + tipos | 6–8 | Dominio + interfaces |
| Refactor CC | 6–8 | Diff antes/después |
| Lib + tests | 4–6 | `npm pack` local |
| Retro | 1 | Cuándo NO usar herencia |""",
        "evid": [
            ("P1", "Dominio", "`projects/m06-*` con modelo TS (sin Express)."),
            ("P2", "Refactor", "Commit/diff mostrando nombres y funciones pequeñas."),
            ("P3", "Bordes", "Tests de null, vacío, duplicados."),
            ("Proyecto", "Librería", "README, semver, tests, ejemplo de uso."),
        ],
    },
    "M07": {
        "cristiano": "implementas estructuras a mano para elegir bien (no solo usar `Array`). Mides y documentas trade-offs.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + diseño | 6–8 | Capítulos ED de la semana |
| Implementar + tests | 6–8 | Estructura + 5 tests |
| Benchmark | 4–6 | Vs nativas documentado |
| Retro | 1 | Cuándo hash gana a árbol |""",
        "evid": [
            ("P1", "Básicas", "Lista, pila, cola, hash con tests en `projects/m07-estructuras/`."),
            ("P2", "BST", "Árbol + recorridos + tests."),
            ("P3", "Bench", "Tabla tiempos vs `Array`/`Map`."),
            ("Proyecto", "Lib ED", "README “cuándo usar cada una” + suite verde."),
        ],
    },
    "M08": {
        "cristiano": "clasificas problemas por patrón, mides complejidad y construyes algo útil (autocomplete) para tu producto.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Teoría CLRS | 6–8 | Caps. Lecturas |
| Problemas | 6–8 | 2–3 problemas con editorial |
| Proyecto | 4–6 | Autocomplete / búsqueda |
| Retro | 1 | Un medio que aún no sale |""",
        "evid": [
            ("P1", "15 problemas", "Carpeta con enunciado, complejidad, código, 3 tests c/u."),
            ("P2", "Sorts", "≥2 ordenamientos + análisis Big-O."),
            ("P3", "DP intro", "3 problemas DP con caso base explicado."),
            ("Proyecto", "Autocomplete", "Demo con dataset de prueba + README de complejidad."),
        ],
    },
    "M09": {
        "cristiano": "diseñas el esquema del producto: ER, SQL real, índices y migraciones sin SQL injection.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Modelo ER | 6–8 | Diagrama + normalización |
| SQL + EXPLAIN | 6–8 | Queries del dominio |
| Migraciones | 4–6 | Seeds + least privilege |
| Retro | 1 | Una query lenta explicada |""",
        "evid": [
            ("P1", "ER", "Diagrama hasta 3FN del CRM/Agenda."),
            ("P2", "SQL", "Joins/agregaciones + `EXPLAIN` comentado."),
            ("P3", "Migraciones", "Migraciones versionadas + usuario BD con least privilege."),
            ("Proyecto", "Esquema", "Seeds + 2 reportes útiles documentados."),
        ],
    },
    "M10": {
        "cristiano": "sigues el viaje de una petición (DNS → TCP → TLS → HTTP) y anotas qué puede fallar en **tu** producto.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura redes | 6–8 | Caps. Tanenbaum / MDN |
| Labs curl/TLS | 6–8 | Bitácora de labs |
| Doc amenazas | 4–6 | Superficie de tu API |
| Retro | 1 | Qué protege TLS y qué no |""",
        "evid": [
            ("P1", "Labs", "`projects/m10-redes/` con logs curl/TLS."),
            ("P2", "TCP", "Echo TCP mínimo + diagrama de una request."),
            ("P3", "Superficie", "Mapa puertos/headers/cookies de tu servicio."),
            ("Proyecto", "Doc", "Amenazas de red del producto web enlazadas a M18."),
        ],
    },
    "M11": {
        "cristiano": "administras procesos, permisos y un contenedor sin hacer tonterías de root/secretos.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Procesos/permisos | 6–8 | Labs Linux |
| Scripts ops | 6–8 | Backup / logs |
| Docker | 4–6 | Imagen sin root innecesario |
| Retro | 1 | Un permiso que te salvó |""",
        "evid": [
            ("P1", "Labs", "Notas de procesos/señales/permisos con comandos."),
            ("P2", "Scripts", "Backup + rotación de logs versionados."),
            ("P3", "Docker", "Dockerfile Node + volumen; user no-root."),
            ("Proyecto", "Playbook", "`projects/m11-so/` operación local del stack."),
        ],
    },
    "M12": {
        "cristiano": "congelas qué construir: entrevistas, stories y un SRS con seguridad, no pantallas bonitas primero.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Entrevistas | 6–8 | Guion + notas |
| Stories + RNF | 6–8 | Aceptación + seguridad |
| SRS v1 | 4–6 | Plantilla llenada |
| Retro | 1 | Un “no” dicho con alternativa |""",
        "evid": [
            ("P1", "Entrevista", "Notas de negocio real/simulado serio."),
            ("P2", "Stories", "≥8 stories con criterios de aceptación."),
            ("P3", "SRS", "SRS con ≥3 RNF de seguridad/privacidad."),
            ("Proyecto", "SRS Agenda", "`projects/m12-srs/` listo para M13/M17."),
        ],
    },
    "M13": {
        "cristiano": "traduces el SRS a diseño usable: flujos, diagramas y ADRs que el yo-de-M17 pueda seguir.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Flujos | 6–8 | Casos de uso |
| Diagramas | 6–8 | Clases / secuencia |
| Arquitectura | 4–6 | Capas + trust boundaries |
| Retro | 1 | Por qué monolito modular |""",
        "evid": [
            ("P1", "Flujos", "Casos de uso principales del Agenda."),
            ("P2", "UML", "Diagrama clases + 1 secuencia crítica."),
            ("P3", "Boundaries", "Diagrama con trust boundaries marcados."),
            ("Proyecto", "Paquete", "ADRs + diagramas enlazados al repo."),
        ],
    },
    "M14": {
        "cristiano": "aplicas pocos patrones con justificación (no nombres de adorno) en el código del CRM.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura patrones | 6–8 | GoF / Refactoring.Guru |
| Implementar | 6–8 | Strategy/Factory/etc. |
| ADR | 4–6 | Por qué cada patrón |
| Retro | 1 | Un anti-patrón que cometiste |""",
        "evid": [
            ("P1", "3 patrones", "Strategy, Observer, Factory con tests."),
            ("P2", "Repo/Service", "Capa backend del CRM."),
            ("P3", "Refactor", "Módulo legacy refactorizado + diff."),
            ("Proyecto", "≥5 patrones", "ADR justificando cada uno en contexto."),
        ],
    },
    "M15": {
        "cristiano": "la calidad deja de ser opcional: pirámide de tests, CI y reviews que incluyen seguridad.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Tests | 6–8 | Unit/integration en CRM |
| CI | 6–8 | Actions lint+test+audit |
| Review | 4–6 | Checklist aplicada |
| Retro | 1 | Bug → test de regresión |""",
        "evid": [
            ("P1", "Pirámide", "Tests en ≥2 capas del CRM."),
            ("P2", "CI", "Workflow verde en GitHub Actions."),
            ("P3", "Checklist", "PR review con ítems de seguridad marcados."),
            ("Proyecto", "Pipeline", "Coverage útil en dominio + audit en CI."),
        ],
    },
    "M16": {
        "cristiano": "dejas de diseñar solo para ti: heurísticas, test con 5 personas e iteración documentada.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Heurísticas | 6–8 | Nielsen sobre tu UI |
| Tests usuarios | 6–8 | 5 sesiones |
| Iteración | 4–6 | Cambios + informe |
| Retro | 1 | Hallazgo que te sorprendió |""",
        "evid": [
            ("P1", "Heurísticas", "Lista de hallazgos con severidad."),
            ("P2", "5 usuarios", "Notas de sesión (consentimiento básico)."),
            ("P3", "Iteración", "Diff/UI antes-después."),
            ("Proyecto", "Informe", "Usabilidad del CRM con cambios hechos."),
        ],
    },
    "M17": {
        "cristiano": "nacen el piloto web de Agenda Ops: auth real, CRUD de citas, roles y base para multi-tenant.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth + API | 6–8 | Sesiones/JWT bien hechos |
| Front | 6–8 | Rutas protegidas + estados |
| Integración | 4–6 | WhatsApp links / admin |
| Retro | 1 | ADR `tenant_id` |""",
        "evid": [
            ("P1", "API auth", "Registro/login + validación; demo roles."),
            ("P2", "Front", "Rutas protegidas; loading/error/vacío."),
            ("P3", "Admin", "Roles owner/staff + deep-links WhatsApp."),
            ("Proyecto", "Piloto", "Deploy HTTPS + checklist camino a SaaS."),
        ],
    },
    "M18": {
        "cristiano": "amenazas → PoC en **tu** app → fix → test. Las siglas azules están en el glosario.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Threat model | 6–8 | STRIDE del producto |
| Exploits propios | 6–8 | Hallazgo → fix |
| CI seguridad | 4–6 | Audit/headers/secrets |
| Retro | 1 | Riesgo residual escrito |""",
        "evid": [
            ("P1", "STRIDE", "Documento de threat model v1."),
            ("P2", "≥5 hallazgos", "Tabla PoC → commit fix → test."),
            ("P3", "CI", "Lint+test+audit (+ grep secretos)."),
            ("Proyecto", "Informe", "`projects/m18-appsec/` + PRs hardening."),
        ],
    },
    "M19": {
        "cristiano": "el piloto sobrevive fuera de tu laptop: Docker, secretos, HTTPS, backup con restore probado.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Docker | 6–8 | Multi-stage |
| Deploy | 6–8 | Staging/prod + secrets |
| Backup | 4–6 | Restore real una vez |
| Retro | 1 | Runbook actualizado |""",
        "evid": [
            ("P1", "Imágenes", "Dockerfile multi-stage + Compose."),
            ("P2", "Deploy", "URL estable; secretos fuera de la imagen."),
            ("P3", "Restore", "Prueba de restore documentada."),
            ("Proyecto", "Runbook", "`projects/m19-ops/` del SaaS."),
        ],
    },
    "M20": {
        "cristiano": "el dueño vive en el teléfono: misma auth que la web, sesión segura, build instalable.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth móvil | 6–8 | Login API |
| Listas/detalle | 6–8 | Citas |
| Build | 4–6 | APK/IPA o equivalente |
| Retro | 1 | Dónde NO guardar secretos |""",
        "evid": [
            ("P1", "Login+lista", "App contra API real."),
            ("P2", "Estados", "Vacío/error + storage seguro de sesión."),
            ("P3", "Build", "Instalable en dispositivo real."),
            ("Proyecto", "App CRM", "Misma sesión/auth que la web."),
        ],
    },
    "M21": {
        "cristiano": "dejas de “hacer lo que salga”: roadmap, sprints y riesgos (incluye seguridad) en el repo.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Roadmap | 6–8 | Trimestre Agenda Ops |
| Sprints | 6–8 | Meta/hecho/aprendizaje |
| Riesgos | 4–6 | Mitigaciones |
| Retro | 1 | Estimación vs real |""",
        "evid": [
            ("P1", "Roadmap", "Markdown trimestral priorizado."),
            ("P2", "4 sprints", "Registro meta/hecho/aprendizaje."),
            ("P3", "Riesgos", "Tabla con mitigaciones de seguridad."),
            ("Proyecto", "Tablero", "Board vivo en el repo."),
        ],
    },
    "M22": {
        "cristiano": "vendes **suscripción SaaS**, no agencia: oferta clara, 10 demos reales y pricing MXN.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Oferta | 6–8 | Pitch 60s |
| Demos | 6–8 | Conversaciones reales |
| Pricing | 4–6 | Free/Pro escrito |
| Retro | 1 | Objeción más frecuente |""",
        "evid": [
            ("P1", "Oferta", "One-pager SaaS (no “hacemos de todo”)."),
            ("P2", "10 demos", "`projects/m22-bektor/` con aprendizajes."),
            ("P3", "Pricing", "Propuesta Free/Pro MXN."),
            ("Proyecto", "Pivote", "Bektor → Agenda Ops documentado."),
        ],
    },
    "M23": {
        "cristiano": "métricas del SaaS + LLM con evaluación; RAG **por tenant** sin filtrar datos ajenos.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Métricas | 6–8 | Por tenant |
| LLM API | 6–8 | Prompts evaluados |
| RAG aislado | 4–6 | Tests cross-tenant |
| Retro | 1 | Costo vs valor |""",
        "evid": [
            ("P1", "Pipeline", "Métricas SaaS por tenant."),
            ("P2", "LLM", "Scripts + rúbrica de calidad."),
            ("P3", "RAG", "Demo A no ve corpus de B + test."),
            ("Proyecto", "FAQ", "Asistente scoped por tenant."),
        ],
    },
    "M24": {
        "cristiano": "separas hype de utilidad: research, criterios (incluye seguridad) y un spike go/no-go.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Research | 6–8 | 3 candidatos |
| Criterios | 6–8 | Matriz adopción |
| Spike | 4–6 | PoC + decisión |
| Retro | 1 | Qué descartaste y por qué |""",
        "evid": [
            ("P1", "Notes", "3 tecnologías con fuentes primarias."),
            ("P2", "Matriz", "Costo/riesgo/valor/seguridad/fit."),
            ("P3", "Spike", "PoC de ≤1 semana."),
            ("Proyecto", "Go/no-go", "Decisión escrita argumentada."),
        ],
    },
    "M25": {
        "cristiano": "ciber aplicada al SaaS multi-tenant: el bug #1 a cazar es IDOR cross-tenant.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Inventario | 6–8 | Superficie prod/staging |
| Cross-tenant | 6–8 | Tests + fixes |
| Tabletop | 4–6 | Incidente simulado |
| Retro | 1 | Riesgo residual |""",
        "evid": [
            ("P1", "Inventario", "Activos + clasificación por tenant."),
            ("P2", "Review", "≥2 issues aislamiento cerrados con tests."),
            ("P3", "Tabletop", "30 min documentados (.env/fuga)."),
            ("Proyecto", "Security review", "`projects/m25-ciber/security-review.md`."),
        ],
    },
    "M26": {
        "cristiano": "cierras la academia con Agenda Ops en producción: ≥2 tenants, Stripe test, evidencia de egreso.",
        "semana": """| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Build SaaS | 8–10 | Tenancy + features |
| Billing/sec | 4–6 | Stripe test + tests cross-tenant |
| Memoria/demo | 4–6 | Video + rúbrica egreso |
| Retro | 1 | Gaps honestos |""",
        "evid": [
            ("P1", "Alcance", "`alcance.md` congelado + plan 8 semanas."),
            ("P2", "Memoria", "Arquitectura, tenancy, billing, seguridad."),
            ("P3", "Demo", "Video público multi-tenant sin tutorial de fondo."),
            ("Proyecto", "Egreso", "Prod + Stripe test + review M25 + demos M22."),
        ],
    },
}


def ensure_cristiano(text: str, cristiano: str) -> str:
    if re.search(r"\*\*En cristiano:\*\*", text):
        # replace existing
        return re.sub(
            r"\*\*En cristiano:\*\*[^\n]*\n",
            f"**En cristiano:** {cristiano}\n",
            text,
            count=1,
        )
    # insert after first paragraph block under Por qué existe
    m = re.search(r"(## Por qué existe\n\n.*?\n\n)(?=## )", text, re.S)
    if not m:
        m = re.search(r"(## Por qué existe\n\n.*?)(\n## )", text, re.S)
        if not m:
            return text
        return text[: m.end(1)] + f"\n**En cristiano:** {cristiano}\n" + text[m.start(2) :]
    insert = m.group(1) + f"**En cristiano:** {cristiano}\n\n"
    return text[: m.start()] + insert + text[m.end() :]


def ensure_section(text: str, heading: str, body: str, after_patterns: list[str]) -> str:
    if re.search(rf"^## {re.escape(heading)}\s*$", text, re.M):
        # replace whole section until next ##
        return re.sub(
            rf"^## {re.escape(heading)}\n.*?(?=\n## |\Z)",
            f"## {heading}\n\n{body.strip()}\n\n",
            text,
            count=1,
            flags=re.S | re.M,
        )
    block = f"## {heading}\n\n{body.strip()}\n\n"
    for pat in after_patterns:
        m = re.search(pat, text, re.S | re.M)
        if m:
            # insert after the matched section (end of section = next ## or we insert after match end)
            # Find end of the section that starts at m.start()
            start = m.start()
            # find next ## after this section's first line
            rest = text[m.end() :]
            nxt = re.search(r"^## ", rest, re.M)
            if nxt:
                pos = m.end() + nxt.start()
            else:
                pos = len(text)
            # Actually we want AFTER the whole matched section
            # Better: insert before first of after_patterns' FOLLOWING heading
            pass
    # Insert before Criterios / Errores / Prácticas / Entregables
    for marker in (
        r"^## Evidencia de hecho\s*$",
        r"^## Criterios",
        r"^## Errores comunes\s*$",
        r"^## Entregables\s*$",
        r"^## Prácticas\s*$",
    ):
        m = re.search(marker, text, re.M)
        if m and heading.startswith("Semana"):
            continue
        if m and heading.startswith("Evidencia"):
            return text[: m.start()] + block + text[m.start() :]
    for marker in (
        r"^## Lecturas\s*$",
        r"^## Temario",
        r"^## Cómo estudiar",
        r"^## Objetivos",
    ):
        m = re.search(marker, text, re.M)
        if not m:
            continue
        # end of that section
        rest = text[m.end() :]
        nxt = re.search(r"^## ", rest, re.M)
        pos = m.end() + nxt.start() if nxt else len(text)
        if heading.startswith("Semana"):
            return text[:pos] + block + text[pos:]
    # fallback append before last criterios
    m = re.search(r"^## Criterios", text, re.M)
    if m:
        return text[: m.start()] + block + text[m.start() :]
    return text.rstrip() + "\n\n" + block


def insert_after_section(text: str, section_heading_re: str, block: str) -> str:
    m = re.search(rf"^## {section_heading_re}\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end() :]
    nxt = re.search(r"^## ", rest, re.M)
    pos = m.end() + nxt.start() if nxt else len(text)
    return text[:pos] + block + text[pos:]


def insert_before_heading(text: str, heading_res: list[str], block: str) -> str:
    for hr in heading_res:
        m = re.search(rf"^## {hr}\s*$", text, re.M)
        if m:
            return text[: m.start()] + block + text[m.start() :]
    return text.rstrip() + "\n\n" + block


def replace_or_insert_section(text: str, heading: str, body: str, *, after=None, before=None) -> str:
    block = f"## {heading}\n\n{body.strip()}\n\n"
    if re.search(rf"^## {re.escape(heading)}\s*$", text, re.M):
        return re.sub(
            rf"^## {re.escape(heading)}\n.*?(?=\n## |\Z)",
            block.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.S | re.M,
        )
    if after:
        for a in after:
            out = insert_after_section(text, a, block)
            if out is not None:
                return out
    if before:
        return insert_before_heading(text, before, block)
    return text.rstrip() + "\n\n" + block


def format_evid(items: list[tuple[str, str, str]]) -> str:
    lines = [
        "Marca la práctica en la UI solo si existe **esto** (o equivalente claro):",
        "",
    ]
    for code, label, detail in items:
        lines.append(f"- **{code} — {label}:** {detail}")
    return "\n".join(lines)


def process(path: Path) -> bool:
    mid = path.name[:3]
    if mid not in ENRICH:
        print("skip", path)
        return False
    data = ENRICH[mid]
    text = path.read_text()
    orig = text
    text = ensure_cristiano(text, data["cristiano"])
    text = replace_or_insert_section(
        text,
        "Semana tipo (20 h)",
        data["semana"]
        + "\n\nSi un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.",
        after=[
            r"Cómo estudiar esta materia",
            r"Cómo estudiar",
            r"Objetivos de aprendizaje",
            r"Objetivos",
            r"Stack",
            r"Día 1 \(2–3 h\) — hazlo hoy",
            r"Día 1 \(2–3 h\)",
        ],
        before=[
            r"Temario.*",
            r"Lecturas",
            r"Día 1.*",
            r"Ejemplo.*",
        ],
    )
    # Fix after patterns - insert_after_section needs exact heading without regex in my impl
    # Re-do semana with simpler logic if missing
    if "## Semana tipo (20 h)" not in text:
        text = orig
        text = ensure_cristiano(text, data["cristiano"])
        body = (
            data["semana"]
            + "\n\nSi un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta."
        )
        block = f"## Semana tipo (20 h)\n\n{body}\n\n"
        placed = False
        for h in (
            "Cómo estudiar esta materia",
            "Cómo estudiar",
            "Objetivos de aprendizaje",
            "Objetivos",
            "Stack",
        ):
            out = insert_after_section(text, re.escape(h) if False else h, block)
            # insert_after_section uses exact match in ^## {re}$
            m = re.search(rf"^## {re.escape(h)}\s*$", text, re.M)
            if m:
                rest = text[m.end() :]
                nxt = re.search(r"^## ", rest, re.M)
                pos = m.end() + nxt.start() if nxt else len(text)
                text = text[:pos] + block + text[pos:]
                placed = True
                break
        if not placed:
            text = insert_before_heading(
                text, [r"Temario.*", r"Lecturas", r"Día 1.*"], block
            )
            # insert_before_heading uses exact - fix
            for pat in (r"^## Temario", r"^## Lecturas", r"^## Día 1"):
                m = re.search(pat, text, re.M)
                if m:
                    text = text[: m.start()] + block + text[m.start() :]
                    placed = True
                    break
            if not placed:
                text = text.rstrip() + "\n\n" + block

    evid_body = format_evid(data["evid"])
    if "## Evidencia de hecho" in text:
        text = re.sub(
            r"^## Evidencia de hecho\n.*?(?=\n## |\Z)",
            f"## Evidencia de hecho\n\n{evid_body}\n\n",
            text,
            count=1,
            flags=re.S | re.M,
        )
    else:
        block = f"## Evidencia de hecho\n\n{evid_body}\n\n"
        placed = False
        for pat in (
            r"^## Criterios",
            r"^## Errores comunes\s*$",
            r"^## Entregables\s*$",
            r"^## Prácticas\s*$",
        ):
            m = re.search(pat, text, re.M)
            if m:
                text = text[: m.start()] + block + text[m.start() :]
                placed = True
                break
        if not placed:
            text = text.rstrip() + "\n\n" + block

    if text != path.read_text():
        path.write_text(text)
        return True
    return False


def main():
    # Rewrite process more cleanly
    changed = 0
    for path in sorted(ROOT.glob("**/M*.md")):
        mid = path.name[:3]
        if mid not in ENRICH:
            continue
        data = ENRICH[mid]
        text = path.read_text()
        text = ensure_cristiano(text, data["cristiano"])

        semana_body = (
            data["semana"]
            + "\n\nSi un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta."
        )
        semana_block = f"## Semana tipo (20 h)\n\n{semana_body}\n\n"
        if re.search(r"^## Semana tipo \(20 h\)\s*$", text, re.M):
            text = re.sub(
                r"^## Semana tipo \(20 h\)\n.*?(?=\n## |\Z)",
                semana_block.rstrip() + "\n\n",
                text,
                count=1,
                flags=re.S | re.M,
            )
        else:
            placed = False
            for h in (
                "Cómo estudiar esta materia",
                "Cómo estudiar",
                "Objetivos de aprendizaje",
                "Objetivos",
                "Stack",
            ):
                m = re.search(rf"^## {re.escape(h)}\s*$", text, re.M)
                if not m:
                    continue
                rest = text[m.end() :]
                nxt = re.search(r"^## ", rest, re.M)
                pos = m.end() + nxt.start() if nxt else len(text)
                text = text[:pos] + semana_block + text[pos:]
                placed = True
                break
            if not placed:
                for pat in (r"^## Temario", r"^## Lecturas", r"^## Día 1"):
                    m = re.search(pat, text, re.M)
                    if m:
                        text = text[: m.start()] + semana_block + text[m.start() :]
                        placed = True
                        break
            if not placed:
                text = text.rstrip() + "\n\n" + semana_block

        evid_body = format_evid(data["evid"])
        evid_block = f"## Evidencia de hecho\n\n{evid_body}\n\n"
        if re.search(r"^## Evidencia de hecho\s*$", text, re.M):
            text = re.sub(
                r"^## Evidencia de hecho\n.*?(?=\n## |\Z)",
                evid_block.rstrip() + "\n\n",
                text,
                count=1,
                flags=re.S | re.M,
            )
        else:
            placed = False
            for pat in (
                r"^## Criterios",
                r"^## Errores comunes\s*$",
                r"^## Entregables\s*$",
                r"^## Prácticas\s*$",
            ):
                m = re.search(pat, text, re.M)
                if m:
                    text = text[: m.start()] + evid_block + text[m.start() :]
                    placed = True
                    break
            if not placed:
                text = text.rstrip() + "\n\n" + evid_block

        path.write_text(text)
        changed += 1
        print("updated", path.name)
    print("done", changed)


if __name__ == "__main__":
    main()
