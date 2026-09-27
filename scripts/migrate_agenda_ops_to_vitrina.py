#!/usr/bin/env python3
"""Bulk domain migration: Agenda Ops (citas) → Vitrina (menú/pedidos).

Runs on curriculum/ + projects/ markdown and related text files.
Skips M01–M08 and M27/M28 trees for lesson content; still updates
shared docs and product-thread projects.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Order matters: longer / more specific first.
REPLACEMENTS: list[tuple[str, str]] = [
    (r"projects/m17-agenda-ops", "projects/m17-vitrina"),
    (r"m17-agenda-ops", "m17-vitrina"),
    (r"Agenda Ops", "Vitrina"),
    (r"agenda-ops", "vitrina"),
    (r"agenda_ops", "vitrina"),
    (r"AgendaOps", "Vitrina"),
    # Domain phrases
    (r"CRM de citas", "SaaS de menú/pedidos"),
    (r"crm de citas", "saas de menú/pedidos"),
    (r"citas/ops", "menú/pedidos"),
    (r"citas \+ clientes \+ panel", "menú + pedidos + panel"),
    (r"servicios con citas", "locales con menú y pedidos"),
    (r"negocio de servicio", "local QSR o barra de bebidas"),
    (r"negocios de servicio", "locales QSR o barras de bebidas"),
    (r"design partner", "design partner"),  # keep
    # Entity / UI language (Spanish curriculum)
    (r"CRUD de citas/clientes/servicios", "CRUD de menú/pedidos/categorías"),
    (r"citas/clientes/servicios", "menú/pedidos/categorías"),
    (r"clientes/servicios/citas", "categorías/ítems/pedidos"),
    (r"Cliente/Servicio/Cita", "Categoría/Ítem/Pedido"),
    (r"cliente/servicio/cita", "categoría/ítem/pedido"),
    (r"Servicios, citas, clientes", "Menú, pedidos, clientes"),
    (r"servicios, citas, clientes", "menú, pedidos, clientes"),
    (r"crear cita", "crear pedido"),
    (r"Crear cita", "Crear pedido"),
    (r"detalle de cita", "detalle de pedido"),
    (r"Detalle de cita", "Detalle de pedido"),
    (r"detalle-de-cita", "detalle-de-pedido"),
    (r"lista de citas", "lista de pedidos"),
    (r"Lista de citas", "Lista de pedidos"),
    (r"lista-de-citas", "lista-de-pedidos"),
    (r"cola de citas", "cola de pedidos"),
    (r"estados de la cita", "estados del pedido"),
    (r"estados de cita", "estados de pedido"),
    (r"estado de la cita", "estado del pedido"),
    (r"reglas de cita", "reglas de pedido"),
    (r"Reglas de cita", "Reglas de pedido"),
    (r"regla de cita", "regla de pedido"),
    (r"service citas", "service pedidos"),
    (r"decorator citas", "decorator pedidos"),
    (r"tabla citas", "tabla pedidos"),
    (r"tabla `citas`", "tabla `orders`"),
    (r"`citas`", "`orders`"),
    (r"\bcitas\b", "pedidos"),
    (r"\bCitas\b", "Pedidos"),
    (r"\bcita\b", "pedido"),
    (r"\bCita\b", "Pedido"),
    (r"no-show", "pedido abandonado"),
    (r"no show", "pedido abandonado"),
    (r"1 calendario", "menú con límite bajo"),
    (r"salones, clínicas o talleres", "cafés, bobas, matcha o QSR"),
    (r"STRIDE CRM", "STRIDE Vitrina"),
    (r"STRIDE aplicado al CRM", "STRIDE aplicado a Vitrina"),
    (r"del CRM", "de Vitrina"),
    (r"al CRM", "a Vitrina"),
    (r"el CRM", "Vitrina"),
    (r"Esquema del CRM", "Esquema de Vitrina"),
    (r"esquema del CRM", "esquema de Vitrina"),
    (r"contexto Agenda Ops", "contexto Vitrina"),
    (r"stakeholders Agenda Ops", "stakeholders Vitrina"),
]

SKIP_DIR_PARTS = {
    "node_modules",
    "dist",
    ".git",
    "pagefind",
    "M01",
    "M02",
    "M03",
    "M04",
    "M05",
    "M06",
    "M07",
    "M08",
    "M27",
    "M28",
    "m01-diario",
    "m02-programacion",
    "m03-discretas",
    "m04-stats",
    "m05-como-corre",
    "m06-programacion-ii",
    "m07-estructuras",
    "m08-algoritmos",
    "m27-bajo-nivel",
}

TEXT_SUFFIXES = {".md", ".mdx", ".astro", ".ts", ".tsx", ".js", ".json", ".txt", ".yml", ".yaml"}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    # Always allow top-level curriculum docs and product projects
    if path.parts[:2] == ("curriculum",) and path.name in {
        "producto-saas.md",
        "egreso.md",
        "INDEX.md",
        "glosario.md",
        "como-estudiar.md",
        "filosofia.md",
    }:
        return True  # already rewritten carefully — script may re-touch; skip to be safe
    for p in path.parts:
        if p in SKIP_DIR_PARTS:
            # Allow M09+ under etapas
            if p.startswith("M0") and p[1:].isdigit() and int(p[1:]) <= 8:
                return True
            if p in {
                "M01",
                "M02",
                "M03",
                "M04",
                "M05",
                "M06",
                "M07",
                "M08",
                "M27",
                "M28",
            }:
                return True
            if p.startswith("m0") and not p.startswith("m09"):
                # m01-m08 project folders
                num = p[1:3]
                if num.isdigit() and int(num) < 9:
                    return True
            if p in {"node_modules", "dist", ".git", "pagefind"}:
                return True
    return False


def transform(text: str) -> str:
    out = text
    for pat, repl in REPLACEMENTS:
        out = re.sub(pat, repl, out)
    return out


def iter_files() -> list[Path]:
    files: list[Path] = []
    for base in (ROOT / "curriculum", ROOT / "projects", ROOT / "academia" / "src"):
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            rel = path.relative_to(ROOT)
            if should_skip(rel):
                continue
            files.append(path)
    return files


def main() -> None:
    changed = 0
    for path in iter_files():
        # Skip canon already hand-written
        if path.name in {
            "producto-saas.md",
            "egreso.md",
        } and "hilos" not in path.parts:
            if path.parent.name == "curriculum":
                continue
        raw = path.read_text(encoding="utf-8")
        new = transform(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"done: {changed} files")


if __name__ == "__main__":
    main()
