"""Helpers to build M09-depth lesson bodies with mandatory code fences."""
from __future__ import annotations

from .builder import bullets, numbered_hecho, slug_commit


def build_body(
    *,
    orden: int,
    titulo: str,
    horas: float,
    semana: int,
    porque: str,
    objetivo: str,
    steps: list[tuple[str, str]],
    commit_msg: str,
    conceptos: list[str] | None = None,
    por_que_asi: str | None = None,
) -> str:
    lid = f"L{orden:02d}"
    conceptos_md = ""
    if conceptos:
        conceptos_md = (
            "\n## Conceptos clave\n\n"
            + "\n".join(f"- {c.rstrip('.')}" for c in conceptos)
            + "\n"
        )
    por_md = ""
    if por_que_asi:
        por_md = f"\n## Por qué empieza así\n\n{por_que_asi.strip()}\n"

    steps_md = []
    for i, (heading, content) in enumerate(steps, 1):
        steps_md.append(f"### {i}. {heading}\n\n{content.strip()}")
    # Always end with explicit commit fence if last step isn't already one
    joined = "\n\n".join(steps_md)
    if "git commit" not in joined:
        steps_md.append(
            f"### {len(steps_md) + 1}. Commit (10–15 min)\n\n"
            f"```bash\n"
            f"git add -A\n"
            f"git status   # sin .env, dumps con PII, keystores\n"
            f'git commit -m "{commit_msg}"\n'
            f"```"
        )
        joined = "\n\n".join(steps_md)

    return f"""# {lid} — {titulo}

**~{horas:.1f} h · Semana {semana}**

{porque.strip()}

## Objetivo

{objetivo.rstrip('.')}.
{por_md}{conceptos_md}
## Pasos (hazlos en orden)

{joined}
""".strip()


def polish_hecho(items: list[str], commit_msg: str, evidencia: str) -> str:
    """Hecho con rutas exactas; no reescribe ítems que ya traen backticks."""
    return numbered_hecho(items, commit_msg, evidencia=evidencia)


def polish_errores(items: list[str]) -> str:
    return bullets(items)


def default_commit(materia: str, orden: int, titulo: str) -> str:
    return f"docs({materia.lower()}): L{orden:02d} {slug_commit(titulo)}"
