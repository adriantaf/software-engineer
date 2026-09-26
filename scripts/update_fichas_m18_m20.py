#!/usr/bin/env python3
"""Inject M01-style Lecciones section into M18–M20 fichas."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DISC = ROOT / "curriculum" / "etapas" / "02-disciplinaria"


def lesson_table(materia: str, week_titles: list[str]) -> str:
    folder = DISC / materia
    files = sorted(folder.glob("L*.md"))
    by_week: dict[int, list[tuple[str, str, float, str]]] = {
        i: [] for i in range(1, len(week_titles) + 1)
    }
    for f in files:
        raw = f.read_text(encoding="utf-8")
        m = re.search(r"^semana:\s*(\d+)", raw, re.M)
        h = re.search(r"^horas:\s*([\d.]+)", raw, re.M)
        t = re.search(r"^titulo:\s*(.+)$", raw, re.M)
        lid = re.search(r"^id:\s*(L\d+)", raw, re.M)
        if not (m and h and t and lid):
            continue
        sem = int(m.group(1))
        by_week.setdefault(sem, []).append(
            (lid.group(1), t.group(1).strip(), float(h.group(1)), f.name)
        )

    parts = ["## Lecciones\n"]
    for i, wtitle in enumerate(week_titles, start=1):
        parts.append(f"### Semana {i} — {wtitle} (~20 h)\n")
        parts.append("| ID | Lección | ~h |")
        parts.append("|----|---------|-----|")
        for lid, tit, hrs, fname in by_week.get(i, []):
            parts.append(f"| {lid} | [{tit}]({materia}/{fname}) | {hrs:g} |")
        parts.append("")
    parts.append("Empieza por **L01** hoy.\n")
    return "\n".join(parts)


FICHAS = {
    "M18": {
        "file": "M18-seguridad.md",
        "weeks": [
            "Threat modeling STRIDE y OWASP Top 10",
            "Autenticación: hashing, sesiones y JWT",
            "Cookies, CSRF y ciclo de sesión",
            "Inyección: SQLi y XSS en Agenda Ops",
            "Control de acceso, IDOR y rate limiting",
            "SSRF, uploads y JSON de confianza",
            "Dependencias, secretos, headers y CSP",
            "Secure SDLC, informe y tests de regresión",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M18 es la **capa B** de AppSec con lecciones L01–L32 (formato M01): amenaza → PoC en **tu** Agenda Ops → fix → test.

1. Orden **L01 → L32**; marca solo con “Hecho cuando” cumplido.
2. **Solo** atacas localhost/staging que controlas.
3. Evidencia en `projects/m18-appsec/` y commits de hardening en el repo del producto.
4. OWASP Top 10 y Cheat Sheets en español; mapa cada lectura a un endpoint real.
5. [Cómo estudiar](../../como-estudiar.md) y [hilo seguridad](../../hilos/seguridad.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lecciones OWASP | 10–12 | 4× ~5 h (lectura + lab en tu API) |
| Hallazgos P2 | 4–6 | Tabla PoC → fix → test |
| CI / informe (P3) | 4–6 | Pipeline, headers, informe |
| Retro | 1 | Riesgo residual escrito |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la lectura OWASP de esa lección.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: **OWASP Top 10** + Cheat Sheets. Ver [bibliografía](../../bibliografia.md) y [hilo seguridad](../../hilos/seguridad.md).

| Semana | Lecciones | Lectura OWASP / recurso | Enfoque Agenda Ops |
|--------|-----------|-------------------------|-------------------|
| 1 | L01–L04 | STRIDE / Threat Modeling | Activos, boundaries, mapa Top 10 |
| 2 | L05–L08 | **A07** Auth + Password Storage | Hashing, sesión/JWT, threat model v1 (P1) |
| 3 | L09–L12 | CSRF + Session Management | Cookies, CSRF, checklist staging |
| 4 | L13–L16 | **A03** Injection + XSS Prevention | SQLi/XSS en citas y clientes |
| 5 | L17–L20 | **A01** Access Control + Rate Limit | IDOR, roles, tests cross-user |
| 6 | L21–L24 | SSRF, File Upload, API hardening | Hallazgos P2 ≥5 |
| 7 | L25–L28 | **A06** + Secrets + Headers + CSP | audit, rotación, Helmet, CSP |
| 8 | L29–L32 | Secure SDLC + informe | CI P3, informe, ≥3 tests seguridad |

**Regla:** hallazgo → PoC en **tu** app → fix → test. Nada de laboratorio genérico sin trasladar al piloto.""",
    },
    "M19": {
        "file": "M19-nube-devops.md",
        "weeks": [
            "Docker multi-stage y Compose prod-like",
            "Deploy staging HTTPS y dominios",
            "Producción, logs y rollback",
            "Backup, restore y runbook",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M19 lleva **Agenda Ops** fuera de tu laptop: L01–L16 con evidencia en `projects/m19-ops/` y en el repo del producto.

1. Orden **L01 → L16**; cada lección termina en commit de infra o doc ops.
2. Trabaja sobre el **repo real** del piloto; no un hello-world Docker aparte.
3. **Nunca** secretos en imagen ni en git; inventario sin valores.
4. Staging para experimentos; prod para design partner y demos M22.
5. [Cómo estudiar](../../como-estudiar.md) y [hilo producto](../../hilos/producto.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Docker / deploy | 10–12 | 4 lecciones (~5 h) |
| Operación y backup | 6–8 | Restore real, runbook |
| Retro | 1 | Runbook actualizado |

Si un día solo tienes 2 h: **una lección** (Dockerfile, deploy-log o restore). No saltes healthcheck ni smoke test.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: documentación oficial **Docker** + docs del PaaS/VPS elegido. Ver [bibliografía](../../bibliografia.md) y [producto-saas](../../producto-saas.md).

| Semana | Lecciones | Lectura | Entrega |
|--------|-----------|---------|---------|
| 1 | L01–L04 | Docker Get started + Dockerfile best practices | P1 Compose + `docker.md` |
| 2 | L05–L08 | Deploy proveedor (HTTPS, dominio, env) | `deploy-log.md`, staging URL |
| 3 | L09–L12 | Logs, rollback, postura host | `runbook.md` borrador, prod |
| 4 | L13–L16 | PostgreSQL backup/restore | P3 `restore-test.md`, runbook final |

**Regla:** un restore de BD probado vale más que tutoriales de Kubernetes que no usarás en el egreso.""",
    },
    "M20": {
        "file": "M20-aplicaciones-moviles.md",
        "weeks": [
            "Scaffold, login y secure storage",
            "Lista de citas y roles",
            "Detalle, navegación y acciones",
            "Vacío, error, red y logging",
            "Build release y entrega",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M20 construye la app **cliente** de Agenda Ops contra la API de M17/M19: L01–L20, evidencia en `projects/m20-movil/`.

1. **Un** stack (Flutter **o** RN); no cambies a mitad.
2. API **staging HTTPS** de M19; no mocks eternos.
3. Cada pantalla: commit + captura o nota en `projects/m20-movil/`.
4. Secure storage para tokens; 401 → logout; sin secretos de servidor en el binario.
5. [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth / listas / detalle | 10–12 | 4× ~5 h lecciones |
| Estados y red | 4–6 | Vacío, offline, timeouts |
| Build instalable | 4–6 | APK/artefacto en dispositivo real |
| Retro | 1 | Política de logs y storage |

Si un día solo tienes 2 h: **una lección** con UI o build verificable.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: documentación oficial de **Flutter** o **React Native** (el stack elegido). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Docs oficiales | Enfoque |
|--------|-----------|----------------|---------|
| 1 | L01–L04 | Get started + HTTP + secure storage | Login staging, 401 |
| 2 | L05–L08 | Listas, refresh, async | P1 login+lista |
| 3 | L09–L12 | Navegación, detalle, deep links | Detalle cita |
| 4 | L13–L16 | Errores / conectividad / MASVS logging | P2 estados + storage |
| 5 | L17–L20 | Release build | P3 APK + demo web |

**Regla:** misma auth que la web; nada de secretos de API de servidor en el repositorio móvil.""",
    },
}


def patch_ficha(materia: str, spec: dict) -> None:
    path = DISC / spec["file"]
    text = path.read_text(encoding="utf-8")
    table = lesson_table(materia, spec["weeks"])
    block = (
        spec["estudio"]
        + "\n\n"
        + spec["semana_tipo"]
        + "\n\n"
        + table
        + "\n"
        + spec["lecturas"]
    )
    pattern = re.compile(
        r"## Cómo estudiar esta materia.*?(?=\n## (?:Prácticas|Ejemplo|Temario|Lecturas|Día 1))",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise SystemExit(f"No patch anchor in {path}")
    text = pattern.sub(block + "\n\n", text, count=1)
    text = re.sub(r"\n## Día 1 \(2–3 h\).*?(?=\n## )", "\n", text, flags=re.DOTALL)
    text = re.sub(
        r"\n## Temario semanal\n\n(?:\| Semana|\### Semana).*?(?=\n## )",
        "\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\n## Lecturas\n\n(?:Canon:.*?(?=\n## Prácticas)|\| Semana.*?(?=\n## Prácticas))",
        "\n",
        text,
        flags=re.DOTALL,
        count=1,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for mid, spec in FICHAS.items():
        patch_ficha(mid, spec)
        print("patched", spec["file"])


if __name__ == "__main__":
    main()
