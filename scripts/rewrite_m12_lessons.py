#!/usr/bin/env python3
"""Rewrite M12 lessons to M01/M09 quality (concrete timed steps, no boilerplate)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum/etapas/02-disciplinaria/M12"
BIBLIO = "../../../bibliografia.md#m12-requerimientos"
PLANTILLA = "../../../../projects/m12-srs/plantilla.md"
PRODUCTO = "../../../producto-saas.md"


def fm(**kw):
    lines = ["---"]
    for k, v in kw.items():
        if isinstance(v, str) and (":" in v or v.startswith("*") or '"' in v or "'" in v):
            safe = v.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{k}: "{safe}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def lectura_block(que, enlace_titulo="plantilla SRS", enlace=PLANTILLA):
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12]({BIBLIO}) |
"""


def render(lesson: dict) -> str:
    pub = {
        "id": lesson["id"],
        "materia": "M12",
        "orden": lesson["orden"],
        "titulo": lesson["titulo"],
        "horas": lesson["horas"],
        "semana": lesson["semana"],
        "lectura": lesson["lectura"],
        "evidencia": lesson["evidencia"],
    }
    enlace = lesson.get("_enlace", {})
    return f"""{fm(**pub)}

{lesson["body"].strip()}

{lectura_block(lesson.get("_lectura_corta", lesson["lectura"]), **enlace)}

## Hecho cuando

Marca la lección **solo si**:

{lesson["_hecho"].strip()}

## Errores comunes

{lesson["_errores"].strip()}

## Siguiente

{lesson["siguiente"]}
"""


FILENAMES = {
    1: "L01-design-partner-y-guion-de-entrevista.md",
    2: "L02-entrevista-y-notas-timestamp.md",
    3: "L03-problemas-observados-y-glosario.md",
    4: "L04-stakeholders-y-contexto-agenda-ops.md",
    5: "L05-formato-user-story-y-trazabilidad.md",
    6: "L06-criterios-de-aceptacion-verificables.md",
    7: "L07-historias-de-vacio-duplicados-y-conflicto.md",
    8: "L08-rnf-seguridad-privacidad-y-p2.md",
    9: "L09-alcance-mvp-y-moscow.md",
    10: "L10-requisitos-funcionales-en-srs.md",
    11: "L11-srs-v1-freeze-y-p3.md",
    12: "L12-revision-m13-y-cierre-m12.md",
}

LESSONS = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Design partner y guion de entrevista",
        horas=5.0,
        semana=1,
        lectura="plantilla.md + producto-saas.md",
        evidencia="entrevistas/guion-v1.md",
        _lectura_corta="ICP, design partner, alcance piloto single-tenant Agenda Ops",
        _enlace={"enlace_titulo": "producto-saas.md", "enlace": PRODUCTO},
        _hecho="""1. Sub-vertical elegido y escrito (no se cambia en M12).
2. `entrevistas/guion-v1.md` con ≥10 preguntas abiertas (flujo citas, no-shows, datos sensibles).
3. Commit `docs(m12): l01 guion entrevista`.""",
        _errores="""- Empezar por pantallas UI.
- Preguntas cerradas tipo “¿te gustaría una app?”.
- Cambiar de barbería a clínica a mitad de semana.""",
        siguiente="[L02 — Entrevista y notas timestamp](L02-entrevista-y-notas-timestamp.md)",
        body=r"""
# L01 — Design partner y guion de entrevista

**~5.0 h · Semana 1**

Agenda Ops empieza con un problema real, no con Figma. Hoy eliges partner y guion.

## Objetivo

Fijar sub-vertical + `guion-v1.md` listo para una entrevista real o simulada seria.

## Pasos (hazlos en orden)

### 1. Scaffold (15 min)

```bash
mkdir -p projects/m12-srs/entrevistas
cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
cat projects/m12-srs/README.md
```

### 2. Producto e ICP (45–60 min)

Lee [producto-saas.md](../../../producto-saas.md). En `entrevistas/guion-v1.md` escribe:

- Sub-vertical (ej. barbería / consultorio / taller) — **uno**
- Ciudad/contexto
- Nombre o rol del design partner (puede ser anónimo)
- Qué herramientas usa hoy (WhatsApp, libreta, Excel…)

### 3. Guion ≥10 preguntas (75–90 min)

Categorías obligatorias:

1. Flujo de una cita de punta a punta
2. No-shows y recordatorios
3. Datos de clientes que guardan (PII)
4. Quién agenda (dueño vs staff)
5. Dolores de cobro / adelantos (sin diseñar pagos aún)
6. Qué **no** quieren automatizar

Regla: preguntas abiertas (“cuéntame…”, “¿qué pasa cuando…?”).

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l01 guion entrevista"
```
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Entrevista y notas timestamp",
        horas=5.0,
        semana=1,
        lectura="Técnicas elicitación (plantilla + tu guion)",
        evidencia="entrevistas/notas-YYYY-MM-DD.md",
        _lectura_corta="Notas con timestamp; separar cita textual vs interpretación",
        _hecho="""1. Archivo `entrevistas/notas-YYYY-MM-DD.md` con ≥30 min de sesión (real o roleplay serio).
2. Cada bloque marca tiempo + texto; al final: 5 insights y 5 preguntas abiertas.
3. Commit `docs(m12): l02 notas entrevista`.""",
        _errores="""- Notas que solo dicen “quiere una app”.
- Mezclar lo que dijo con lo que tú inventaste.
- Grabar sin consentimiento si es persona real.""",
        siguiente="[L03 — Problemas observados y glosario](L03-problemas-observados-y-glosario.md)",
        body=r"""
# L02 — Entrevista y notas timestamp

**~5.0 h · Semana 1**

P1 exige evidencia de entrevista. Hoy la corres y dejas notas auditables.

## Objetivo

Completar una sesión con notas timestamp en `entrevistas/`.

## Pasos

### 1. Prep (20 min)

Imprime o ten abierto `guion-v1.md`. Acuerda duración (~45 min). Si es simulación: briefing escrito del personaje (dueño de X).

### 2. Sesión (45–60 min)

Formato de notas:

```markdown
# Entrevista — 2026-09-26 — Partner A
## 00:00–00:05 Rapport
…
## 00:05–00:20 Flujo actual
> cita textual breve
Interpretación: …
```

### 3. Debrief (45 min)

Al final del archivo: insights, dolores rankeados, datos sensibles mencionados, contradicciones, follow-ups.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/entrevistas
git commit -m "docs(m12): l02 notas entrevista"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Problemas observados y glosario",
        horas=5.0,
        semana=1,
        lectura="problemas.md + glosario del dominio",
        evidencia="problemas.md y glosario.md",
        _lectura_corta="Problema ≠ solución; glosario cita/servicio/cliente/no-show",
        _hecho="""1. `problemas.md` con ≥6 problemas observados (evidencia → impacto → frecuencia).
2. `glosario.md` con ≥8 términos del dominio alineados al partner.
3. Commit `docs(m12): l03 problemas y glosario`.""",
        _errores="""- Escribir “necesitan dashboard” como problema.
- Glosario genérico sin el lenguaje del negocio.
- Problemas sin ancla en las notas.""",
        siguiente="[L04 — Stakeholders y contexto Agenda Ops](L04-stakeholders-y-contexto-agenda-ops.md)",
        body=r"""
# L03 — Problemas observados y glosario

**~5.0 h · Semana 1**

Traduces la entrevista a problemas y lenguaje compartido.

## Objetivo

Publicar `problemas.md` y `glosario.md` en `projects/m12-srs/`.

## Pasos

### 1. Extrae problemas (75 min)

Tabla:

| ID | Problema observado | Evidencia (nota) | Impacto | Frecuencia |
|----|--------------------|------------------|---------|------------|
| P-01 | Doble reserva el sábado | 00:18 | pierde cliente | semanal |

Prohibido: soluciones (“app con calendario”).

### 2. Glosario (60 min)

Términos mínimos: Cliente, Servicio, Cita, No-show, Recordatorio, Staff, Owner, Bloqueo de horario, Nota privada, Adelanto (si aplica). Definición en 1–2 frases del partner.

### 3. Commit (15 min)

```bash
git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
git commit -m "docs(m12): l03 problemas y glosario"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Stakeholders y contexto Agenda Ops",
        horas=5.0,
        semana=1,
        lectura="SRS plantilla — stakeholders y descripción general",
        evidencia="srs-borrador.md sección contexto",
        _lectura_corta="Stakeholders owner/staff/cliente; perspectiva del producto piloto",
        _hecho="""1. `srs-borrador.md` secciones 1–2 rellenadas (propósito, alcance borrador, stakeholders).
2. Diagrama de contexto (Mermaid o ASCII): actores ↔ Agenda Ops.
3. Commit `docs(m12): l04 contexto stakeholders`.""",
        _errores="""- Olvidar al cliente final (aunque no tenga login en MVP).
- Alcance infinito en la intro.
- Stakeholders sin metas.""",
        siguiente="[L05 — Formato user story y trazabilidad](L05-formato-user-story-y-trazabilidad.md)",
        body=r"""
# L04 — Stakeholders y contexto Agenda Ops

**~5.0 h · Semana 1**

Cierras elicitación metiendo contexto en el SRS borrador.

## Objetivo

Rellenar introducción + descripción general del `srs-borrador.md`.

## Pasos

### 1. Lee la plantilla (30 min)

```bash
sed -n '1,80p' projects/m12-srs/plantilla.md
```

### 2. Stakeholders (60 min)

Para Owner, Staff, Cliente final (indirecto): metas, dolores, acceso a datos. Incluye supuesto single-tenant del piloto.

### 3. Contexto (60 min)

Secciones 1.1–1.3 y 2.1–2.3 del borrador. Diagrama:

```mermaid
flowchart LR
  Owner --> Panel
  Staff --> Panel
  Panel --> API
  API --> DB
  Cliente -. WhatsApp .-> Owner
```

### 4. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md
git commit -m "docs(m12): l04 contexto stakeholders"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Formato user story y trazabilidad",
        horas=5.0,
        semana=2,
        lectura="Plantilla + historias INVEST",
        evidencia="stories.md inicio",
        _lectura_corta="Como/quiero/para; INVEST; trazabilidad story→problema→SRS",
        _hecho="""1. `stories.md` con ≥4 stories en formato estándar + ID (US-01…).
2. Cada story enlaza a un problema P-xx o insight de entrevista.
3. Commit `docs(m12): l05 user stories base`.""",
        _errores="""- Stories técnicas (“como desarrollador quiero Postgres”).
- Sin ID ni trazabilidad.
- Épicas enormes sin partir.""",
        siguiente="[L06 — Criterios de aceptación verificables](L06-criterios-de-aceptacion-verificables.md)",
        body=r"""
# L05 — Formato user story y trazabilidad

**~5.0 h · Semana 2**

Las stories son el puente entrevista → SRS → tests (M15/M17).

## Objetivo

Arrancar `stories.md` con historias trazables.

## Pasos

### 1. Plantilla de story (30 min)

```markdown
## US-01 — …
**Como** owner **quiero** … **para** …
**Problema:** P-01
**Prioridad:** (luego MoSCoW)
```

### 2. Escribe ≥4 (90 min)

Cobertura mínima: agendar cita, ver agenda del día, alta de cliente, cancelar/reagendar. Lenguaje del glosario.

### 3. Mapa (30 min)

Tabla `US-xx → P-xx → sección SRS futura`.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l05 user stories base"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Criterios de aceptación verificables",
        horas=5.0,
        semana=2,
        lectura="Given/When/Then intro",
        evidencia="stories.md criterios",
        _lectura_corta="Criterios testeables; happy path + error; nada de “se ve bien”",
        _hecho="""1. Cada story existente tiene ≥3 criterios verificables (Given/When/Then o lista numerada).
2. Al menos un criterio de error/permiso en 2 stories.
3. Commit `docs(m12): l06 criterios aceptacion`.""",
        _errores="""- “Que sea intuitivo”.
- Criterios solo de UI visual.
- Sin casos de error.""",
        siguiente="[L07 — Historias de vacío, duplicados y conflicto](L07-historias-de-vacio-duplicados-y-conflicto.md)",
        body=r"""
# L06 — Criterios de aceptación verificables

**~5.0 h · Semana 2**

Si no puedes convertirlo en test, no es criterio.

## Objetivo

Endurecer `stories.md` con aceptación verificable.

## Pasos

### 1. Reglas (20 min)

Cada criterio: sujeto observable + condición + resultado. Preferible Given/When/Then.

### 2. Reescribe (90–110 min)

Ejemplo:

```text
Given un owner autenticado
When crea una cita en un slot libre
Then la cita aparece en GET /api/citas?fecha=… con status 201 al crear
```

Incluye 401/403 donde aplique (aunque el RNF formal llegue en L08).

### 3. Revisión cruzada (30 min)

Marca en amarillo (comentario) criterios vagos y corrígelos.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l06 criterios aceptacion"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Historias de vacío, duplicados y conflicto",
        horas=5.0,
        semana=2,
        lectura="Casos borde negocio citas",
        evidencia="stories.md ampliado",
        _lectura_corta="Agenda vacía, cliente duplicado, conflicto de horario, no-show",
        _hecho="""1. ≥3 stories nuevas de borde (vacío/duplicado/conflicto/no-show).
2. Total de stories camino a ≥8 (completa faltantes si hace falta).
3. Commit `docs(m12): l07 stories borde`.""",
        _errores="""- Solo happy path.
- Conflicto de horario sin regla explícita.
- Duplicados de cliente sin criterio de match (teléfono/nombre).""",
        siguiente="[L08 — RNF seguridad, privacidad y P2](L08-rnf-seguridad-privacidad-y-p2.md)",
        body=r"""
# L07 — Historias de vacío, duplicados y conflicto

**~5.0 h · Semana 2**

El piloto se rompe en los bordes. Hoy los conviertes en stories.

## Objetivo

Ampliar `stories.md` hacia ≥8 con casos de borde del dominio.

## Pasos

### 1. Brainstorm bordes (40 min)

Lista: agenda vacía, slot ocupado, cliente duplicado por teléfono, cancelación tardía, no-show, nota privada, staff sin permiso.

### 2. Escribe stories (90 min)

Cada una con criterios. Ejemplo conflicto:

```text
When intento crear cita que solapa servicio+recurso
Then API responde 409 y no persiste
```

### 3. Conteo P2 (20 min)

Cuenta stories con criterios; anota cuántas faltan para ≥8.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l07 stories borde"
```
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="RNF seguridad, privacidad y P2",
        horas=5.0,
        semana=2,
        lectura="Plantilla RNF + hilo seguridad",
        evidencia="stories.md + srs-borrador RNF (≥8 stories)",
        _lectura_corta="RNF seguridad/privacidad trazables; single-tenant; 401/403",
        _enlace={"enlace_titulo": "Hilo seguridad", "enlace": "../../../hilos/seguridad.md"},
        _hecho="""1. `stories.md` tiene ≥8 stories con criterios (P2).
2. `srs-borrador.md` incluye ≥3 RNF-SEC/PRIV numerados y enlazados a stories.
3. Commit `docs(m12): l08 rnf seguridad p2`.""",
        _errores="""- “Seguridad luego en M18” sin RNF.
- RNF no medibles (“máxima seguridad”).
- Stories sin permisos.""",
        siguiente="[L09 — Alcance MVP y MoSCoW](L09-alcance-mvp-y-moscow.md)",
        body=r"""
# L08 — RNF seguridad, privacidad y P2

**~5.0 h · Semana 2**

Cierras P2 y metes seguridad en el SRS desde ya ([hilo](../../../hilos/seguridad.md)).

## Objetivo

≥8 stories + ≥3 RNF de seguridad/privacidad trazables.

## Pasos

### 1. Completa stories (45 min)

Llega a ≥8 con criterios. Índice al inicio de `stories.md`.

### 2. RNF (75 min)

En `srs-borrador.md` §3.2, ejemplos:

| ID | Tipo | Descripción |
|----|------|-------------|
| RNF-SEC-01 | Seguridad | Toda ruta de negocio exige sesión; sin token → 401 |
| RNF-SEC-02 | Autorización | Staff no lee notas privadas → 403 + log |
| RNF-PRIV-01 | Privacidad | PII mínimo; single-tenant documentado |

Enlaza cada RNF a US-xx.

### 3. README P2 (20 min)

Marca P2 listo.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l08 rnf seguridad p2"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Alcance MVP y MoSCoW",
        horas=5.0,
        semana=3,
        lectura="producto-saas fases + priorización",
        evidencia="srs-borrador alcance MoSCoW",
        _lectura_corta="MVP 4 semanas build; Must/Should/Could/Won't",
        _enlace={"enlace_titulo": "producto-saas.md", "enlace": PRODUCTO},
        _hecho="""1. Tabla MoSCoW de todas las US + lista explícita Won't (multi-tenant, billing, IA…).
2. Párrafo: por qué el Must cabe en ~4 semanas de build hacia M17.
3. Commit `docs(m12): l09 moscow mvp`.""",
        _errores="""- Todo es Must.
- Won't vacío.
- MVP que incluye pagos + IA + multi-sucursal.""",
        siguiente="[L10 — Requisitos funcionales en SRS](L10-requisitos-funcionales-en-srs.md)",
        body=r"""
# L09 — Alcance MVP y MoSCoW

**~5.0 h · Semana 3**

Decir “no” es un entregable. Hoy priorizas.

## Objetivo

Congelar alcance MVP con MoSCoW en el borrador SRS.

## Pasos

### 1. Inventario (30 min)

Lista US-xx existentes.

### 2. MoSCoW (75 min)

| US | MoSCoW | Justificación 1 línea |
|----|--------|----------------------|

Must típicos: auth owner, clientes, citas CRUD básico, agenda del día. Won't: multi-tenant, Stripe, IA, app móvil nativa.

### 3. Capacidad (40 min)

Escribe supuestos de velocidad (1 dev) y qué cae si algo Must se atrasa.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md projects/m12-srs/stories.md
git commit -m "docs(m12): l09 moscow mvp"
```
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Requisitos funcionales en SRS",
        horas=5.0,
        semana=3,
        lectura="plantilla.md — requisitos funcionales",
        evidencia="srs-borrador.md funcionales",
        _lectura_corta="RF-xx con prioridad y criterio; trazabilidad a US",
        _hecho="""1. Tabla §3.1 con ≥8 RF derivados de Must/Should.
2. Cada RF tiene criterio de aceptación o enlace a US.
3. Commit `docs(m12): l10 requisitos funcionales`.""",
        _errores="""- Copiar stories verbatim sin IDs RF.
- RF sin prioridad.
- Mezclar RNF en la tabla funcional.""",
        siguiente="[L11 — SRS v1, freeze y P3](L11-srs-v1-freeze-y-p3.md)",
        body=r"""
# L10 — Requisitos funcionales en SRS

**~5.0 h · Semana 3**

El SRS habla RF-xx; las stories alimentan pero no sustituyen.

## Objetivo

Completar §3.1 Requisitos funcionales del borrador.

## Pasos

### 1. Deriva RF (90–110 min)

| ID | Descripción | Prioridad | Criterio / US |
|----|-------------|-----------|---------------|
| RF-01 | Owner autenticado gestiona clientes | Alta | US-0x |

Cubre clientes, citas, agenda, auth, roles básicos.

### 2. Fuera de alcance (30 min)

§4 con bullets concretos (no “todo lo demás”).

### 3. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md
git commit -m "docs(m12): l10 requisitos funcionales"
```
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="SRS v1, freeze y P3",
        horas=5.0,
        semana=3,
        lectura="plantilla completa",
        evidencia="projects/m12-srs/srs-v1.md",
        _lectura_corta="Freeze: copiar borrador → srs-v1.md; RNF seguridad ≥3",
        _hecho="""1. `srs-v1.md` completo (intro, contexto, RF, RNF≥3 seguridad/privacidad, fuera de alcance, glosario).
2. Fecha de freeze y versión v1 anotadas.
3. Commit `docs(m12): l11 srs-v1 freeze p3`.""",
        _errores="""- Seguir editando “borrador eterno” sin v1.
- RNF de seguridad ausentes.
- Glosario desalineado con M09/M17.""",
        siguiente="[L12 — Revisión M13 y cierre M12](L12-revision-m13-y-cierre-m12.md)",
        body=r"""
# L11 — SRS v1, freeze y P3

**~5.0 h · Semana 3**

P3 y proyecto: el documento que M13/M17 consumen.

## Objetivo

Publicar `srs-v1.md` congelado.

## Pasos

### 1. Copiar y pulir (90–120 min)

```bash
cp projects/m12-srs/srs-borrador.md projects/m12-srs/srs-v1.md
```

Completa huecos: referencias, supuestos, dependencias (Node, Postgres), RNF ≥3, glosario, MoSCoW resumido.

### 2. Freeze banner (20 min)

Al inicio:

```markdown
> **Freeze v1 — YYYY-MM-DD**  
> Cambios post-freeze → ADR o srs-v1.1 con diff explícito.
```

### 3. Checklist P3 (30 min)

README: P1 entrevistas, P2 stories≥8, P3 srs-v1 con RNF.

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): l11 srs-v1 freeze p3"
```
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Revisión M13 y cierre M12",
        horas=5.0,
        semana=3,
        lectura="Ficha M12 + handoff diseño",
        evidencia="nota-handoff-m13.md",
        _lectura_corta="Handoff a análisis/diseño: entidades, casos de uso, riesgos",
        _hecho="""1. `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas y riesgos.
2. README m12 con checklist P1–P3 y proyecto cerrados.
3. Commit `docs(m12): cierre handoff m13`.""",
        _errores="""- Handoff vacío “lee el SRS”.
- Reabrir alcance Must sin versión.
- No enlazar stories/SRS desde README.""",
        siguiente="Cierra la [ficha M12](../M12-requerimientos.md). Siguiente: [M13 — Análisis y diseño](../M13-analisis-y-diseno.md).",
        body=r"""
# L12 — Revisión M13 y cierre M12

**~5.0 h · Semana 3**

Dejas el testigo listo para diseño (Larman/UML en M13).

## Objetivo

Handoff explícito + cierre de evidencias.

## Pasos

### 1. Relectura SRS (40 min)

Lee `srs-v1.md` como si fueras M13: marca ambigüedades.

### 2. Handoff (75 min)

`nota-handoff-m13.md`:

- Entidades candidatas (Cliente, Servicio, Cita, Usuario…)
- Casos de uso Must
- Reglas de conflicto de horario
- Preguntas abiertas
- Riesgos (alcance, datos, auth)

### 3. Dominio (30 min)

Auto-check de la ficha: ¿puedes decir “no” con alternativa escrita? ¿3 RNF? ¿Must con criterios?

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): cierre handoff m13"
```
""",
    )
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(LESSONS) == 12, len(LESSONS)
    for lesson in LESSONS:
        path = OUT / FILENAMES[lesson["orden"]]
        text = render(lesson)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print("total", len(LESSONS))


if __name__ == "__main__":
    main()
