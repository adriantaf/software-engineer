#!/usr/bin/env python3
"""Generate M01-style lesson markdown for M21–M23 (terminal / Agenda Ops ops thread)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_m10_m13_lessons as gen  # noqa: E402

gen.BASE = ROOT / "curriculum" / "etapas" / "03-terminal"

from generate_m10_m13_lessons import _lesson, write_materia  # noqa: E402

P21 = "projects/m21-proyectos"
P22 = "projects/m22-bektor"
P23 = "projects/m23-ia"
PS = "../../../producto-saas.md"
CS = "../../../como-estudiar.md"
SEC = "../../hilos/seguridad.md"


def rows(*pairs: tuple[str, str, str]) -> list[tuple[str, str, str]]:
    return list(pairs)


def m21() -> list[dict]:
    L: list[dict] = []

    def w(*a, **k):
        L.append(_lesson(*a, **k))

    w(
        "Entorno M21, Scrum de uno y Definition of Done",
        1,
        "Guía Scrum 2020 (ES) — roles y eventos",
        f"{P21}/definition-of-done.md",
        "Crear la carpeta de evidencia, leer Scrum adaptado a un solo dev-owner y redactar Definition of Done usable en issues reales de Agenda Ops.",
        "Sin DoD escrito cierras issues con ‘ya quedó’; M22 y M26 dependen de un backlog honesto del mismo repo producto.",
        ["Product Owner de uno.", "Sprint de 1–2 semanas.", "DoD con PR, test, doc.", "Backlog ≠ lista de deseos."],
        f"""```bash
mkdir -p {P21}/sprints
```

Lee la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) completa una vez.

En `{P21}/definition-of-done.md` define checklist mínima: PR revisado (o self-review documentado), tests/CI cuando aplique, doc en `projects/` si la materia lo pide, staging si es deploy. Incluye **un ítem de seguridad** (ej. no secretos en git).

Añade `{P21}/bitacora-m21.md` con párrafo: cómo mapeas roles Scrum cuando eres solo tú + mentor ocasional.""",
        rows(("Scrum Guide", "2020 ES PDF", CS), ("Plan", PS, SEC)),
        ["DoD ≥6 ítems verificables.", "bitacora-m21.md con roles adaptados.", "Commit docs(m21)."],
        ["DoD genérico ‘código limpio’.", "Ignorar ítem seguridad."],
    )
    w(
        "Milestones y cinco issues reales del producto",
        1,
        "Scrum Guide — artefactos y compromiso del backlog",
        f"{P21}/board.md borrador",
        "Crear milestones de cuatro semanas de M21 y mover cinco issues **reales** del repo Agenda Ops al backlog priorizado.",
        "El tablero ficticio no prepara trials (M22) ni FAQ (M23); hoy enlazas gestión al código que ya desplegaste.",
        ["Milestone.", "Issue vs épica.", "Etiquetas feature/security/ops.", "Prioridad vs urgencia."],
        f"""En GitHub Projects (o Linear): milestones `M21-S1` … `M21-S4` con fechas orientativas.

Mueve **5 issues** del repo producto al backlog ordenado. **Al menos uno** debe ser seguridad o `tenant_id` (cross-tenant, secretos, backup).

Escribe `{P21}/board.md` con URL del board + fecha de captura. Lista los 5 issues con enlace `#`.""",
        rows(("Scrum Guide", "Artefactos", "GitHub Projects docs")),
        ["5 issues enlazados.", "≥1 issue security/tenant.", "board.md con URL."],
        ["Issues de tutorial sin repo producto.", "Milestone sin fechas."],
    )
    w(
        "Roadmap trimestral alineado a producto-saas",
        1,
        "producto-saas.md — piloto → tenants → billing",
        f"{P21}/roadmap-trimestre.md",
        "Redactar roadmap de un trimestre con 3–5 objetivos medibles de Agenda Ops (multi-tenant, staging estable, trials, handoff M23).",
        "P1 exige un documento que un mentor pueda cuestionar; debe reflejar [producto-saas]({PS}), no features al azar.",
        ["Outcome vs output.", "Dependencia M22/M26.", "Design partner.", "Corte explícito (MoSCoW)."],
        f"""En `{P21}/roadmap-trimestre.md`:

- **Visión 90 días** (3–5 bullets).
- Tabla objetivos: **qué**, **por qué ahora**, **métrica**, **issue/milestone** enlazado.
- Sección **No haremos este trimestre** (≥3 ítems) para combatir scope creep.

Relee [producto-saas.md]({PS}) y marca qué objetivo habilita trials comerciales y qué habilita FAQ por tenant.""",
        rows(("Plan", PS, "../M21-admin-proyectos.md")),
        ["roadmap con 3–5 objetivos.", "Tabla con métricas.", "Sección ‘no haremos’."],
        ["40 features sin orden.", "Roadmap sin enlace a milestones."],
    )
    w(
        "Backlog refinado y criterios de aceptación",
        1,
        "Scrum Guide — refinamiento del Product Backlog",
        f"{P21}/roadmap-trimestre.md sección backlog",
        "Refinar las historias del backlog: criterios de aceptación testeables y tamaño ≤ un sprint para las top 5.",
        "Cierras semana 1 con P1 casi listo: el roadmap debe ser ejecutable, no aspiracional.",
        ["Historia de usuario.", "Criterio Given/When/Then.", "INVEST (selecto).", "Deuda etiquetada."],
        f"""Para las **5 issues** prioritarias añade en el issue (o anexo `{P21}/backlog-refinado.md`) criterios de aceptación numerados.

Verifica que cada criterio sea **observable** (URL, test, archivo). Etiqueta deuda técnica explícita.

Retro semana 1 en `bitacora-m21.md`: estimación inicial en rangos (optimista/realista/pesimista) para la issue #1.""",
        rows(("Scrum Guide", "Refinamiento", "Ficha M21 semana 1")),
        ["5 historias con criterios.", "Retro semana 1 escrita.", "P1 roadmap revisable."],
        ["Criterios ‘funciona bien’.", "Historias gigantes multi-sprint sin split."],
    )
    w(
        "Sprint planning — meta única del sprint 1",
        2,
        "Scrum Guide — Sprint Planning",
        f"{P21}/sprints/sprint-01.md",
        "Planificar sprint 1 con **una meta** clara, WIP limitado y lista de entregables enlazados a issues.",
        "Multi-tasking sin meta única es la causa #1 de carry-over; M21 te entrena a decir no.",
        ["Meta de sprint.", "WIP.", "Compromiso realista.", "Definition of Done aplicada."],
        f"""Crea `{P21}/sprints/sprint-01.md` con plantilla de la ficha (fechas, meta, tabla Planeado/Hecho/Aprendizaje vacía).

Elige **1 meta** (ej. ‘segundo tenant en staging + 1 test cross-tenant’). Máximo **3 issues** en progreso.

Documenta estimación **24–32 h** (rango) y riesgos del sprint (1 párrafo).""",
        rows(("Scrum Guide", "Sprint Planning", "DoD local")),
        ["sprint-01.md con meta única.", "≤3 issues WIP.", "Rango horas documentado."],
        ["Meta lista de 10 verbos.", "Sin fechas de sprint."],
    )
    w(
        "Ejecutar sprint 1 y registro honesto",
        2,
        "Scrum Guide — Daily Scrum (adaptado a bitácora)",
        f"{P21}/sprints/sprint-01.md tabla hecho",
        "Trabajar el sprint 1 sobre Agenda Ops y registrar **hecho real** vs planeado sin borrar desviaciones.",
        "La retrospectiva útil exige datos honestos; inflar ‘hecho’ destruye P2.",
        ["Daily de 3 líneas.", "Bloqueo documentado.", "Carry-over explícito.", "Demo a ti mismo."],
        f"""Durante el sprint, añade notas diarias de 3 líneas en `sprint-01.md` (ayer/hoy/bloqueo).

Al cerrar parcialmente la semana, llena la tabla **Planeado | Hecho | Aprendizaje** aunque falte trabajo.

Si subestimaste migración o deploy, escribe **horas reales** aproximadas.""",
        rows(("Scrum Guide", "Daily + Review", CS)),
        ["Tabla parcialmente llena.", "≥3 notas diarias.", "Desviación explicada."],
        ["Borrar filas ‘no hecho’.", "Cerrar issues sin DoD."],
    )
    w(
        "Estimación en rangos y métricas de flujo",
        2,
        "Notas lean/kanban — throughput y carry-over",
        f"{P21}/metricas-flujo.md",
        "Documentar estimaciones en tres rangos y calcular throughput simple (issues cerrados/semana) y carry-over.",
        "Sin métricas de flujo repites el mismo error de estimación en M22 (demos) y M26 (capstone).",
        ["Optimista/realista/pesimista.", "Throughput.", "Lead time (idea).", "Carry-over."],
        f"""Crea `{P21}/metricas-flujo.md` con definiciones y **números reales** del sprint 1.

Tabla: issue, estimación (3 columnas), horas reales si las tienes, estado.

Calcula: issues cerrados esta semana / issues arrastrados. Una frase: qué cambiarás en sprint 2.""",
        rows(("Ficha", "../M21-admin-proyectos.md", "Scrum Guide DoD")),
        ["metricas-flujo.md con números.", "Rangos en ≥3 issues.", "Acción para sprint 2."],
        ["Solo horas planeadas sin real.", "Vanity ‘100% productividad’."],
    )
    w(
        "Sprint 2 documentado y avance P2",
        2,
        "Scrum Guide — Sprint Review y Retrospective",
        f"{P21}/sprints/sprint-02.md",
        "Planificar y registrar sprint 2; retrospectiva del sprint 1 con mantener/cambiar/probar.",
        "P2 pide **4 sprints**; hoy dejas dos registros distintos y accionables.",
        ["Retro formato 3 preguntas.", "Review con demo URL.", "Aprendizaje ≠ excusa."],
        f"""Cierra sprint 1: sección **Retrospectiva** (mantener / cambiar / probar).

Abre `{P21}/sprints/sprint-02.md` con nueva meta. Al final de la lección, sprint 2 debe tener plan **y** al menos una fila de progreso en la tabla.

Verifica DoD en ≥1 issue cerrado esta semana.""",
        rows(("Scrum Guide", "Retro", "../M22-emprendimiento.md handoff")),
        ["sprint-01 retro completa.", "sprint-02.md creado.", "DoD usada en cierre."],
        ["Retro vacía.", "Sprint 2 copia-pega de sprint 1."],
    )
    w(
        "Matriz de riesgos del producto y del proyecto",
        3,
        "Gestión de riesgos (notas propias) + Scrum impediments",
        f"{P21}/riesgos.md borrador",
        "Identificar ≥5 riesgos con probabilidad, impacto, mitigación, dueño y fecha de revisión.",
        "P3 y criterios de dominio exigen riesgos accionables, no lista genérica de ‘bugs’.",
        ["Probabilidad × impacto.", "Riesgo vs issue.", "Mitigación verificable.", "Dueño = tú o mentor."],
        f"""Crea `{P21}/riesgos.md` con tabla (≥5 filas): descripción, P, I, mitigación, dueño, revisión.

Incluye riesgos de **producto** (un solo design partner, scope creep) y **técnicos** (dependencia PaaS).

Enlaza issues de mitigación cuando existan.""",
        rows(("Plan", SEC, PS)),
        ["≥5 riesgos.", "Mitigación concreta cada uno.", "Fechas revisión."],
        ["Riesgos ‘hackeo’ sin vector.", "Sin dueño."],
    )
    w(
        "Riesgos de seguridad, privacidad y multi-tenant",
        3,
        "Hilo seguridad + OWASP ASVS (selecto)",
        f"{P21}/riesgos.md sección seguridad",
        "Añadir ≥2 riesgos de seguridad/privacidad (IDOR cross-tenant, secretos, backup sin restore) con mitigaciones enlazadas a M18/M25.",
        "Ignorar seguridad hasta M25 es exactamente el anti-patrón del plan.",
        ["IDOR.", "Secreto en repo.", "Restore no probado.", "Dependencia API LLM (M23)."],
        f"""Extiende `{P21}/riesgos.md` con sección **Seguridad y privacidad** (≥2 filas).

Para cada uno: **cómo sabrías que ocurrió** y **evidencia de mitigación** (test, runbook, issue).

Cross-ref [hilo seguridad]({SEC}) y issues M18 si existen.""",
        rows(("Plan", SEC, "../M18-seguridad.md")),
        ["≥2 riesgos seguridad.", "Evidencia mitigación citada.", "Issue enlazado si aplica."],
        ["Mitigación ‘confío en el framework’.", "Mezclar riesgo con bug puntual sin impacto."],
    )
    w(
        "Tablero vivo, sprints 3–4 y DoD en práctica",
        3,
        "Scrum Guide — transparencia del incremento",
        f"{P21}/sprints/sprint-03.md + sprint-04.md",
        "Actualizar board.md, esbozar sprints 3–4 y cerrar ≥3 issues con DoD completa.",
        "El proyecto de la materia es un tablero que refleja la realidad del SaaS, no un ejercicio.",
        ["Transparencia.", "Issues zombie.", "Handoff M22.", "Incremento demoable."],
        f"""Actualiza `{P21}/board.md` (fecha ≤7 días).

Crea `{P21}/sprints/sprint-03.md` y `sprint-04.md` con meta y al menos encabezado de tabla (pueden solapar semanas calendario si ya iterabas).

Añade al backlog issues etiquetados **demo-comercial** para M22. Cierra ≥3 issues con DoD.""",
        rows(("Ficha", "../M22-emprendimiento.md", PS)),
        ["board.md reciente.", "sprint-03/04 existen.", "≥3 issues con DoD.", "Issues demo M22."],
        ["Board sin URL.", "Sprints sin fechas ni meta."],
    )
    w(
        "Cierre M21 — P1–P3, dominio y handoff comercial",
        3,
        "Repaso ficha M21 criterios de dominio",
        f"{P21}/cierre-m21.md",
        "Auditar evidencias P1–P3, tablero, cuatro sprints y redactar handoff a M22 (trials) y M23 (métricas).",
        "Cierras la materia de gestión antes de vender (M22) y medir con IA (M23).",
        ["Checklist evidencia.", "Pitch interno 5 min roadmap.", "Handoff.", "Riesgo residual."],
        f"""Crea `{P21}/cierre-m21.md`: checklist P1–P3 + proyecto tablero; responde criterios dominio de la ficha.

Graba guion (texto) de **5 min** explicando roadmap a persona no técnica.

Commit `docs(m21): cierre materia`. Actualiza `{P21}/README.md` con índice L01–L12.""",
        rows(("Ficha", "../M21-admin-proyectos.md", CS)),
        ["cierre-m21.md completo.", "README índice.", "Commit cierre.", "Handoff M22/M23."],
        ["Marcar UI sin archivos.", "Roadmap desalineado del board."],
    )
    return L


def m22() -> list[dict]:
    L: list[dict] = []

    def w(*a, **k):
        L.append(_lesson(*a, **k))

    w(
        "Lean Startup aplicado a Agenda Ops — carpeta y visión",
        1,
        "El método Lean Startup — visión, start, build-measure-learn",
        f"{P22}/demos + bitacora-m22.md",
        "Crear estructura comercial, leer visión/start/BML y escribir hipótesis de negocio SaaS (no agencia).",
        "M22 vende **suscripción** al producto que construiste; Bektor como agencia no es el modelo del plan.",
        ["Visión vs estrategia.", "Build-measure-learn.", "SaaS vertical.", "Anti-patrón agencia."],
        f"""```bash
mkdir -p {P22}/demos
```

Lee capítulos iniciales de *El método Lean Startup* (ed. ES). En `{P22}/bitacora-m22.md`: visión en 5 líneas + ciclo BML aplicado a trials de Agenda Ops.

Lista 3 supuestos que **matarían** el negocio si fueran falsos.""",
        rows(("Ries", "Lean Startup inicio", PS), ("Ficha", "../M22-emprendimiento.md", CS)),
        ["demos/ existe.", "bitacora con BML.", "3 supuestos críticos."],
        ["Volver a vender ‘páginas web’.", "Leer sin escribir acción."],
    )
    w(
        "ICP único — sub-vertical fijado por escrito",
        1,
        "Lean — segmento inicial + anti-patterns",
        f"{P22}/icp.md",
        "Elegir **un** sub-vertical (barbería, clínica dental, taller…) en Ensenada o alrededores y documentar por qué encaja con Agenda Ops.",
        "Cambiar de ICP cada semana invalida demos y pricing; la materia exige disciplina de 6 semanas.",
        ["ICP.", "Dolor operativo.", "Willingness to pay (hipótesis).", "Canal de contacto."],
        f"""En `{P22}/icp.md`: perfil del dueño, tamaño del negocio, dolor (no-shows, doble reserva), herramientas actuales, por qué **no** marketplace.

Compromiso: **no cambiar** sub-vertical hasta fin de M22 salvo pivote documentado al final.""",
        rows(("Plan", PS, "../M12-requerimientos.md design partner")),
        ["icp.md completo.", "Sub-vertical único.", "Dolor medible descrito."],
        ["ICP ‘cualquier negocio’.", "Sin geografía/canal."],
    )
    w(
        "Oferta SaaS en un párrafo",
        1,
        "Lean — propuesta de valor",
        f"{P22}/oferta-saas.md",
        "Redactar oferta de **un producto** suscripción: problema del dueño → Agenda Ops → precio orientativo → trial.",
        "P1 es un párrafo defendible, no folleto de servicios Bektor.",
        ["Problema.", "Outcome.", "Suscripción.", "Siguiente paso trial."],
        f"""Escribe `{P22}/oferta-saas.md` con **un párrafo** (≤120 palabras). Prohibido: ‘también hacemos logos/hosting’.

Añade pitch **60 segundos** en bullet (≤6 líneas) al final del archivo.""",
        rows(("Ficha", "../M22-emprendimiento.md P1", PS)),
        ["Un párrafo oferta.", "Pitch 60s.", "Menciona suscripción MXN orientativa."],
        ["Lista de servicios agencia.", "Sin CTA trial."],
    )
    w(
        "Outreach 20 contactos y guion demo 5 min",
        1,
        "Lean — experimento de contacto",
        f"{P22}/outreach-lista.md + guion-demo-5min.md",
        "Armar lista de 20 negocios ICP y guion de demo staging: login → cita → WhatsApp → cierre trial.",
        "Sin lista no hay 10 demos; sin guion las conversaciones divagan.",
        ["Outreach.", "Staging URL.", "Demo script.", "CTA trial 14 días."],
        f"""`{P22}/outreach-lista.md`: 20 filas (nombre, contacto, por qué encajan).

`{P22}/guion-demo-5min.md`: pasos cronometrados sobre **staging/prod M19**, nunca localhost.

Borrador `{P22}/pricing.md`: planes Free/Pro MXN + límites (calendarios, citas/mes).""",
        rows(("M19", "URL staging", "../M19-nube-devops.md")),
        ["20 contactos.", "Guion 5 min.", "pricing.md borrador."],
        ["Demo localhost.", "Lista sin contacto real."],
    )
    w(
        "Validated learning — hipótesis de dolor y métrica de trial",
        2,
        "Lean — validated learning",
        f"{P22}/hipotesis-trial.md",
        "Formular hipótesis: dolor, solución mínima, métrica de éxito del trial (≥1 cita en 7 días).",
        "M22 mide aprendizaje, no vanity; esta métrica alinea con M23.",
        ["Hipótesis falsable.", "Métrica activación.", "Baseline.", "Criterio de pivot."],
        f"""Crea `{P22}/hipotesis-trial.md` con plantilla: Creemos que… Mediremos… Éxito si… Fracaso si…

Enlaza a `{P22}/metricas-trials.md` (crear encabezados de columnas: negocio, trial iniciado, activación 7d, notas).""",
        rows(("Ries", "Validated learning", PS)),
        ["hipotesis-trial.md.", "metricas-trials.md esqueleto.", "Métrica activación definida."],
        ["Métrica ‘likes’.", "Hipótesis no falsable."],
    )
    w(
        "Demo 1 — conversación real documentada",
        2,
        "Lean — entrevista/solución",
        f"{P22}/demos/demo-01.md",
        "Ejecutar primera demo o intento serio con negocio ICP y documentar con plantilla de la ficha.",
        "‘No contestó’ no cuenta sin intento; ‘sí demo’ exige aprendizaje escrito el mismo día.",
        ["Objeción.", "Siguiente paso.", "Canal.", "Aprendizaje distinto."],
        f"""Crea `{P22}/demos/demo-01.md` con plantilla ficha (contacto, mostrado, objeción, respuesta, siguiente paso, aprendizaje).

Usa URL staging. Pide **trial o segunda reunión** antes de colgar.""",
        rows(("Ficha", "../M22-emprendimiento.md ejemplo demo", CS)),
        ["demo-01.md mismo día.", "URL staging.", "Siguiente paso concreto."],
        ["Demo sin producto.", "Copiar texto de blog."],
    )
    w(
        "Demo 2 — refinar guion y oferta",
        2,
        "Lean — pivot del mensaje",
        f"{P22}/demos/demo-02.md + oferta-saas.md",
        "Segunda conversación; actualizar guion u oferta según objeción #1 observada.",
        "Build-measure-learn en ventas: el mensaje es código que refactorizas.",
        ["Objeción Excel/WhatsApp.", "Iteración mensaje.", "Evidencia en git."],
        f"""Documenta `{P22}/demos/demo-02.md`. Tras la call, edita **una** sección de `guion-demo-5min.md` o `oferta-saas.md` con cambio justificado (commit separado).

Nota en bitácora: ¿la objeción es precio, tiempo o confianza?""",
        rows(("Ries", "Pivot mensaje", "../M21-admin-proyectos.md backlog")),
        ["demo-02.md.", "Cambio guion/oferta commiteado.", "Objeción clasificada."],
        ["Ignorar feedback.", "10 demos idénticas sin aprendizaje."],
    )
    w(
        "Demos 3–4 y anti-patrones agencia",
        2,
        "Lean — perseverancia vs pivot",
        f"{P22}/demos/demo-03.md + demo-04.md",
        "Completar dos demos más; registrar tentación de vender ‘proyecto a medida’ y rechazarla por escrito.",
        "El pivote Bektor→Agenda Ops es decisión de negocio; documentar qué **no** vendes.",
        ["Perseverancia.", "Pivot.", "Scope comercial.", "Trial vs proyecto."],
        f"""Crea demo-03 y demo-04. Escribe `{P22}/pivote-bektor-agenda-ops.md` borrador: qué dejaste de vender (lista) y por qué SaaS gana.

Actualiza `{P22}/README.md` con contador demos (4/10).""",
        rows(("Ficha", "../M22-emprendimiento.md proyecto", PS)),
        ["2 demos.", "pivote borrador.", "README contador."],
        ["Aceptar proyecto custom sin ADR comercial.", "Demos sin fecha."],
    )
    w(
        "Tres hipótesis de precio o sub-vertical",
        3,
        "Lean — experimentación",
        f"{P22}/pricing-experimentos.md",
        "Documentar tres experimentos de pricing o empaquetado y cómo los invalidarías con datos de demos.",
        "Semana 3 exige rigor: precio no es número mágico, es hipótesis.",
        ["Precio.", "Elasticidad (cualitativa).", "Free tier.", "Límites técnicos."],
        f"""`{P22}/pricing-experimentos.md`: 3 hipótesis (ej. Pro $499 vs $699 MXN; límite citas/mes). Para cada una: señal de éxito/fracaso en conversaciones.

Compara alternativas: libreta, Calendly genérico, WhatsApp solo — tabla 1 página.""",
        rows(("Plan", PS, "Competidores locales (observación)")),
        ["3 hipótesis.", "Tabla alternativas.", "Señales éxito/fracaso."],
        ["Precio sin justificación.", "Copiar USD sin MXN."],
    )
    w(
        "Demos 5–6 — escuchar precio en voz alta",
        3,
        "Lean — experimentos de mercado",
        f"{P22}/demos/demo-05.md + demo-06.md",
        "Dos demos donde **dices el precio** o rango Pro sin tartamudear y registras reacción.",
        "M26 integrará Stripe; hoy practicas defensa del valor en MXN.",
        ["Anclaje precio.", "Free/Pro.", "Objeción precio.", "Trial como reduce riesgo."],
        f"""Documenta demos 5–6. En cada ficha campo **Reacción precio** (verbatim si puedes).

Ajusta `{P22}/pricing.md` con límites técnicos reales del producto (no prometer IA ilimitada si M23 costea tokens).""",
        rows(("M23", "costos LLM futuros", PS)),
        ["2 demos con precio dicho.", "pricing.md actualizado.", "Reacción documentada."],
        ["Evitar nombrar precio.", "Prometer features inexistentes."],
    )
    w(
        "Refinar ICP tras objeciones recurrentes",
        3,
        "Lean — segmento y niche",
        f"{P22}/icp.md revisión",
        "Revisar ICP: ¿sigues en el sub-vertical? Ajustar **mensaje**, no segmento, salvo evidencia fuerte.",
        "Cambiar ICP cada semana es anti-patrón; aquí solo permites ajuste de mensaje o criterio de calificación.",
        ["Calificación lead.", "Disqualify.", "Mensaje.", "Evidencia 6 demos."],
        f"""Añade a `{P22}/icp.md` sección **Calificación**: 3 preguntas antes de demo.

Resume objeciones 1–6 en `{P22}/bitacora-m22.md`. Confirma por escrito: mantienes sub-vertical Sí/No + razón.""",
        rows(("Ries", "Pivot segmento", "../M21-admin-proyectos.md")),
        ["ICP revisado.", "Objeciones resumidas.", "Decisión segmento explícita."],
        ["Cambiar ICP sin 10 conversaciones.", "Mezclar verticales en outreach."],
    )
    w(
        "Pricing Free/Pro — borrador defendible",
        3,
        "producto-saas + límites técnicos",
        f"{P22}/pricing.md",
        "Cerrar borrador Free/Pro MXN con límites (calendarios, citas/mes, staff) alineados al código actual.",
        "P3 exige coherencia técnica; pricing que rompe el producto es deuda comercial.",
        ["Free tier.", "Pro tier.", "Límites.", "Upgrade path M26."],
        f"""Completa `{P22}/pricing.md`: tabla planes, límites, qué pasa al exceder, política trial 14 días.

Párrafo **Por qué estos números** (costo hosting, tiempo ahorrado, comparativa local).""",
        rows(("Plan", PS, "../M26-proyecto-integrador.md Stripe")),
        ["Free/Pro completos.", "Límites técnicos.", "Justificación breve."],
        ["Pro ‘contactar’ sin cifra.", "Free ilimitado imposible."],
    )
    w(
        "Métricas accionables — tablero de trials",
        4,
        "Lean — medir lo que importa",
        f"{P22}/metricas-trials.md datos",
        "Llenar tablero con trials iniciados, activación 7d y notas; rechazar vanity metrics.",
        "MRR ficticio sin pagos está prohibido en la ficha; mide activación y conversación.",
        ["Trial iniciado.", "Activación 7d.", "Vanity vs accionable.", "Seguimiento."],
        f"""Actualiza `{P22}/metricas-trials.md` con filas reales (≥6 negocios contactados).

Define fórmula activación en el archivo. Gráfico ASCII o tabla semanal suficiente.""",
        rows(("M23", "métricas por tenant", PS)),
        ["Tablero con datos.", "Fórmula activación.", "Sin MRR inventado."],
        ["Contar WhatsApp enviado como trial.", "Métricas sin definición."],
    )
    w(
        "Demos 7–8 — seguimiento y lotes pequeños",
        4,
        "Lean — cohortes pequeñas",
        f"{P22}/demos/demo-07.md + demo-08.md",
        "Dos demos con **seguimiento** a contactos previos; practicar lote de 5 contactos/semana.",
        "Semana 4 acelera aprendizaje acumulado, no spam.",
        ["Follow-up.", "Cadencia.", "CRM mínimo.", "Rechazo documentado."],
        f"""Demos 7–8. En bitácora: tabla follow-ups (fecha, contacto, resultado).

Marca en outreach-lista estado: pendiente / demo / trial / no.""",
        rows(("Ries", "Accelerate lotes", CS)),
        ["2 demos.", "Follow-ups registrados.", "Estados en lista."],
        ["Spam sin personalizar.", "No registrar rechazos."],
    )
    w(
        "Objeción #1 y cambio de producto o mensaje",
        4,
        "Lean — build-measure-learn en producto",
        f"{P22}/objeciones-sintesis.md",
        "Identificar objeción más frecuente y documentar cambio en mensaje **o** issue en backlog Agenda Ops.",
        "Criterio dominio: nombrar objeción #1 y qué cambiaste.",
        ["Objeción.", "Backlog producto.", "Mensaje.", "Trazabilidad M21."],
        f"""Crea `{P22}/objeciones-sintesis.md` con ranking top 3 objeciones.

Abre issue en repo producto **o** entrada en `{P21}/roadmap-trimestre.md` si el fix es producto. Enlaza en demo fichas.""",
        rows(("M21", P21, PS)),
        ["Top 3 objeciones.", "Cambio mensaje/producto enlazado.", "Issue o roadmap."],
        ["Quejarse sin acción.", "Objeción inventada sin demos."],
    )
    w(
        "Refinar pricing tras métricas semana 4",
        4,
        "Lean — aprendizaje acumulado",
        f"{P22}/pricing.md v2",
        "Ajustar pricing con nota de versión y evidencia de conversaciones (no intuición sola).",
        "Preparas P3 final en semana 6; hoy versionas cambios.",
        ["Changelog pricing.", "Anclaje.", "Límites Free.", "Trial."],
        f"""Añade `{P22}/pricing-changelog.md` con v1→v2 y razón (cita demo #).

Relee límites técnicos; alinea con plan Pro si incluirá FAQ IA (M23).""",
        rows(("M23", "../M23-ia-datos.md", PS)),
        ["pricing-changelog.", "pricing.md v2.", "Evidencia demo citada."],
        ["Cambiar precio sin razón.", "Ignorar costo IA."],
    )
    w(
        "Outreach semana 5 — lote de cinco contactos",
        5,
        "Lean — motor de crecimiento (intro)",
        f"{P22}/outreach-semana-05.md",
        "Contactar 5 negocios del ICP con secuencia (mensaje → seguimiento → demo offer).",
        "Semana 5 exige volumen disciplinado, no heroísmo aleatorio.",
        ["Secuencia.", "Personalización mínima.", "Canal.", "Tasa respuesta."],
        f"""Documenta `{P22}/outreach-semana-05.md`: 5 contactos, mensaje enviado, respuesta, siguiente paso.

Objetivo: ≥2 conversaciones sobre producto esta semana.""",
        rows(("Ries", "Motor crecimiento (lectura selecta)", CS)),
        ["5 contactos documentados.", "≥2 conversaciones producto.", "Fechas reales."],
        ["Copy-paste masivo sin nombre.", "Contar email sin respuesta como demo."],
    )
    w(
        "Demos 9–10 — cerrar P2",
        5,
        "Lean — validación comercial",
        f"{P22}/demos/demo-09.md + demo-10.md",
        "Completar demos 9 y 10 con aprendizajes **distintos**; índice en demos/README.md.",
        "P2 exige 10 fichas; copy-paste invalida criterio dominio.",
        ["Índice demos.", "Aprendizaje único.", "Trial pedido."],
        f"""Crea demo-09 y demo-10. `{P22}/demos/README.md` tabla 10 filas con enlace y aprendizaje one-liner.

Verifica contador 10/10 en README raíz.""",
        rows(("Ficha", "../M22-emprendimiento.md P2", CS)),
        ["10 demos totales.", "README índice.", "Aprendizajes distintos."],
        ["Duplicar aprendizaje.", "Demo sin producto mostrado."],
    )
    w(
        "Landing de precios y enlace en evidencia",
        5,
        "producto-saas — página precios",
        f"{P22}/landing-precios.md",
        "Publicar o enlazar landing estática de precios (repo producto o página) y documentar URL en evidencia.",
        "M26 conectará Stripe; hoy el dueño debe **ver** números fuera de un MD privado.",
        ["Landing.", "URL pública.", "Coherencia pricing.md.", "CTA trial."],
        f"""Crea `{P22}/landing-precios.md` con URL HTTPS, captura o commit del HTML/ruta.

Debe coincidir con `{P22}/pricing.md`. Anota fecha verificación.""",
        rows(("M19", "deploy estático", PS)),
        ["URL pública.", "Coherencia pricing.", "Fecha verificación."],
        ["Solo MD privado.", "Precios distintos web vs doc."],
    )
    w(
        "Pivote Bektor → Agenda Ops — narrativa completa",
        5,
        "Lean — pivot documentado",
        f"{P22}/pivote-bektor-agenda-ops.md",
        "Finalizar narrativa de pivote: qué vendía Bektor, qué vendes ahora, evidencia de conversaciones.",
        "Proyecto de materia: decisión de negocio trazable, no rebranding cosmetico.",
        ["Pivot.", "Evidencia.", "SaaS.", "Anti-agencia."],
        f"""Completa `{P22}/pivote-bektor-agenda-ops.md` (≥2 páginas markdown): timeline, métricas aprendizaje, quotes anonimizados de demos.

Actualiza `{P22}/README.md` con enlaces a oferta, pricing, pivote, métricas.""",
        rows(("Ficha", "../M22-emprendimiento.md proyecto", PS)),
        ["Pivote completo.", "README actualizado.", "Evidencia demos citada."],
        ["Pivot sin fechas.", "Volver a listar servicios agencia."],
    )
    w(
        "Pricing final para M26 y trial operativo",
        6,
        "Stripe docs (preview) + pricing.md",
        f"{P22}/pricing.md final",
        "Congelar pricing Free/Pro MXN para integración Stripe test en M26; checklist trial operativo.",
        "Semana 6 cierra comercial de la materia con números estables.",
        ["Price freeze.", "Trial 14d.", "Límites.", "Handoff M26."],
        f"""Marca `{P22}/pricing.md` sección **Final M22** con fecha congelación.

Lista checklist trial: alta tenant, credenciales, soporte WhatsApp, activación medida.""",
        rows(("M26", "../M26-proyecto-integrador.md", "Stripe test mode")),
        ["Pricing congelado fechado.", "Checklist trial.", "P3 listo para UI."],
        ["Cambiar precio post-cierre sin nota.", "Trial sin proceso."],
    )
    w(
        "Síntesis comercial para backlog M21",
        6,
        "Lean — aprendizaje → producto",
        f"{P22}/handoff-producto.md",
        "Traducir aprendizajes comerciales en ≥5 issues priorizados para Agenda Ops (M21 backlog).",
        "El hilo Ops/SaaS cierra loop gestión ↔ mercado.",
        ["Backlog.", "Prioridad.", "Issue template.", "Demo feedback."],
        f"""`{P22}/handoff-producto.md`: tabla aprendizaje → issue sugerido → prioridad.

Crea o enlaza issues reales en repo producto. Notifica en `{P21}/board.md`.""",
        rows(("M21", P21, PS)),
        ["≥5 issues sugeridos.", "Enlaces GitHub.", "board.md actualizado."],
        ["Lista deseos sin issues.", "Features sin origen demo."],
    )
    w(
        "Pitch final 60s y práctica grabada",
        6,
        "Lean — narrativa de venta",
        f"{P22}/pitch-60s.md",
        "Escribir y practicar pitch 60s SaaS; opcional audio/video ≤90s en evidencia.",
        "Criterio dominio incluye pitch fluido con precio y trial.",
        ["Pitch.", "Precio.", "Trial.", "ICP."],
        f"""`{P22}/pitch-60s.md` versión final. Graba audio o escribe transcripción cronometrada ≤65s.

Incluye nombre producto, dolor, precio Pro, CTA trial.""",
        rows(("Ficha", "../M22-emprendimiento.md dominio", CS)),
        ["pitch-60s.md.", "Transcripción cronometrada.", "Precio incluido."],
        ["Pitch agencia.", "Sin CTA."],
    )
    w(
        "Cierre M22 — P1–P3, dominio y README",
        6,
        "Repaso ficha M22",
        f"{P22}/cierre-m22.md",
        "Auditar oferta, 10 demos, pricing, pivote; responder checklist dominio; commit cierre.",
        "Cierras venta consultiva antes de IA aplicada (M23).",
        ["Evidencia.", "Dominio.", "Honestidad bitácora.", "Handoff M23."],
        f"""`{P22}/cierre-m22.md` checklist P1–P3 + proyecto. Verifica ICP único 6 semanas.

Commit `docs(m22): cierre materia`. README con índice L01–L24.""",
        rows(("Ficha", "../M22-emprendimiento.md", "../M23-ia-datos.md")),
        ["cierre-m22.md.", "Commit cierre.", "README L01–L24."],
        ["Marcar UI sin 10 demos.", "Inflar métricas."],
    )
    return L


def m23() -> list[dict]:
    L: list[dict] = []

    def w(*a, **k):
        L.append(_lesson(*a, **k))

    w(
        "Tres métricas SaaS por tenant — definiciones",
        1,
        "producto-saas + notas métricas M23",
        f"{P23}/metricas/definiciones.md",
        "Definir activación 7d, citas creadas/semana y trials activos con fórmula y fuente de datos.",
        "M23 y M22 comparten métricas accionables; sin definición clara los CSV mienten.",
        ["Activación.", "tenant_id.", "Vanity vs accionable.", "Ventana temporal."],
        f"""```bash
mkdir -p {P23}/{{metricas,llm-eval,rag}}
```

En `{P23}/metricas/definiciones.md` documenta ≥3 métricas con fórmula, numerador/denominador, frecuencia, anti-PII.""",
        rows(("Plan", PS, "../M22-emprendimiento.md metricas")),
        ["definiciones.md ≥3 métricas.", "Fórmulas explícitas.", "Anti-PII."],
        ["Métrica sin fórmula.", "Mezclar tenants en definición."],
    )
    w(
        "Consulta agregada por tenant_id sin PII",
        1,
        "SQL agregaciones + minimización datos",
        f"{P23}/metricas/query-agregada.sql",
        "Escribir SQL o script que agrupe por `tenant_id` sin columnas de PII en SELECT.",
        "El pipeline P1 debe ser reproducible y seguro para compartir export de ejemplo.",
        ["GROUP BY tenant_id.", "Minimización.", "Vistas.", "Anonimización."],
        f"""Crea `{P23}/metricas/query-agregada.sql` (o `.ts` script) contra schema Agenda Ops o fixture documentado.

Prohibido SELECT de teléfono, nombre, notas clínicas. Comentario en archivo explica fuente tablas.""",
        rows(("M09", "modelo datos", SEC)),
        ["Query/script existe.", "Sin PII en output.", "Comentario fuente."],
        ["Dump crudo clientes.", "tenant_id del cliente HTTP."],
    )
    w(
        "Export de ejemplo y borrador pipeline",
        1,
        "Reproducibilidad jobs métricas",
        f"{P23}/metricas/export-ejemplo.csv + pipeline.md",
        "Generar CSV de ejemplo (ficticio o anonimizado) y documentar pipeline extracción → agregación → export.",
        "P1 entrega artefactos que M26 puede operar; hoy es diseño ejecutable.",
        ["Pipeline.", "CSV.", "Job schedule (idea).", "Idempotencia."],
        f"""Exporta muestra a `{P23}/metricas/export-ejemplo.csv` (≥5 filas, columnas tenant_id + métricas).

Borrador `{P23}/metricas/pipeline.md`: pasos, herramienta, frecuencia, owner, enlace script.""",
        rows(("M19", "cron/job", PS)),
        ["CSV ejemplo.", "pipeline.md borrador.", "Script ejecutable o instrucción clara."],
        ["CSV con nombres.", "Pipeline ‘manual cuando quiera’."],
    )
    w(
        "Cierre semana 1 métricas — P1 avance",
        1,
        "Repaso definiciones + privacidad",
        f"{P23}/metricas/semana-01.md",
        "Consolidar semana métricas; revisar que export cumple política futura LLM.",
        "Semana 1 cierra base numérica antes de tocar APIs externas.",
        ["Revisión pares (mentor).", "Checklist P1.", "Documentación."],
        f"""`{P23}/metricas/semana-01.md`: checklist P1 parcial + preguntas abiertas.

Anticipa `{P23}/politica-datos-llm.md` con 3 bullets qué **nunca** sale a LLM.""",
        rows(("Ficha", "../M23-ia-datos.md", SEC)),
        ["semana-01.md.", "Checklist P1.", "Bullets política LLM."],
        ["Marcar P1 completo sin pipeline.", "Export sin revisar PII."],
    )
    w(
        "Política de datos LLM antes de prompts",
        2,
        "Ética/datos + vendor LLM terms",
        f"{P23}/politica-datos-llm.md",
        "Redactar política: qué nunca enviar a LLM, retención logs, filtro tenant, incidentes.",
        "Regla M23: política **antes** de pegar datos en ChatGPT ‘solo probar’.",
        ["PII.", "Retención.", "Tenant scope.", "Incident response."],
        f"""Completa `{P23}/politica-datos-llm.md` (≥1 página): prohibidos, permitidos anonimizados, logs, borrado, responsable.

Enlaza [hilo seguridad]({SEC}). Commit antes de cualquier script que llame API.""",
        rows(("Plan", SEC, "Términos API LLM elegida")),
        ["Política completa.", "Commit previo a scripts.", "Enlace seguridad."],
        ["Política post-hoc.", "Permitir dumps BD."],
    )
    w(
        "Set gold de 10 preguntas FAQ del ICP",
        2,
        "FAQ realistas barbería/clínica/taller",
        f"{P23}/llm-eval/preguntas-gold.json",
        "Listar 10 preguntas con respuesta esperada corta basada en docs ficticios de un tenant demo.",
        "Evaluación sin gold set es opinión; M22 ICP informa el tono.",
        ["Gold set.", "JSON.", "Respuesta esperada.", "Tenant demo."],
        f"""Crea `{P23}/llm-eval/preguntas-gold.json` array de {{id, pregunta, respuesta_esperada, tenant_id_demo}}.

Preguntas tipo política cancelación, horario, servicios, no-show.""",
        rows(("M22", P22, PS)),
        ["10 preguntas.", "JSON válido.", "Respuesta esperada cada una."],
        ["Preguntas genéricas Wikipedia.", "Sin tenant_id_demo."],
    )
    w(
        "Proveedor LLM — auth, modelo y costos",
        2,
        "Docs API LLM oficiales",
        f"{P23}/llm-eval/proveedor.md",
        "Elegir proveedor, anotar modelo, límites rate, precio por 1k tokens, variables entorno.",
        "Costos ignorados hasta factura es error común del plan.",
        ["API key.", "Modelo.", "Rate limit.", "Costo estimado."],
        f"""`{P23}/llm-eval/proveedor.md`: tabla comparativa si dudaste; decisión final con razón.

Plantilla `.env.example` sin secretos; claves solo en entorno local/staging.""",
        rows(("Vendor", "Pricing + limits docs", CS)),
        ["proveedor.md.", ".env.example.", "Sin secretos en git."],
        ["Key en repo.", "Modelo sin límite tokens."],
    )
    w(
        "Primer script LLM y logs sin PII",
        2,
        "Prompt sistema + usuario",
        f"{P23}/llm-eval/prompt-v1.txt + logs/",
        "Implementar CLI o script que llame API con prompt v1 y registre latencia/tokens sin PII.",
        "P2 empieza con versión explícita de prompt, no ‘el que funcionó ayer’.",
        ["Prompt versionado.", "Tokens.", "Latencia.", "Redacción logs."],
        f"""Guarda `{P23}/llm-eval/prompt-v1.txt`. Script en `{P23}/llm-eval/run-eval.ts` o `.py` (documenta comando).

Log en `{P23}/llm-eval/logs/` con timestamp, tokens, modelo — **sin** texto de cliente.""",
        rows(("Vendor", "Quickstart API", "../M23-ia-datos.md semana 2")),
        ["prompt-v1.txt.", "Script ejecutable.", "Log sin PII."],
        ["Log con teléfonos.", "Prompt en código sin archivo."],
    )
    w(
        "Rúbrica de evaluación FAQ",
        3,
        "Evaluación LLM — correcto/parcial/incorrecto/alucinación",
        f"{P23}/llm-eval/rubrica.md",
        "Definir rúbrica con ejemplos anclados para calificar respuestas del asistente.",
        "Calidad medible habilita comparar prompt v1 vs v2 objetivamente.",
        ["Rúbrica.", "Anclas.", "Alucinación.", "Parcial aceptable."],
        f"""`{P23}/llm-eval/rubrica.md`: 4 categorías, definición, ejemplo bueno/malo por categoría.

Acuerda umbral (ej. ≥80% correcto+parcial aceptable) en el mismo archivo.""",
        rows(("Vendor", "Eval guides", CS)),
        ["Rúbrica 4 niveles.", "Ejemplos anclados.", "Umbral numérico."],
        ["‘Se ve bien’.", "Sin definir alucinación."],
    )
    w(
        "Correr evaluación v1 sobre gold set",
        3,
        "Batch eval reproducible",
        f"{P23}/llm-eval/resultados-v1.csv",
        "Ejecutar evaluación completa v1; tabular pregunta, respuesta modelo, score rúbrica.",
        "Resultados versionados permiten auditoría y mejora.",
        ["Batch.", "CSV resultados.", "Reproducibilidad.", "Version tag."],
        f"""Genera `{P23}/llm-eval/resultados-v1.csv`. Documenta comando exacto en `{P23}/llm-eval/README.md`.

No pegues API key en README.""",
        rows(("Ficha", "../M23-ia-datos.md semana 3", "preguntas-gold.json")),
        ["resultados-v1.csv 10 filas.", "README comando.", "prompt-v1 referenciado."],
        ["Eval parcial sin commit.", "Editar gold para ‘pasar’."],
    )
    w(
        "Prompt v2 — iteración medida",
        3,
        "Error analysis sobre v1",
        f"{P23}/llm-eval/prompt-v2.txt + notas",
        "Analizar fallos v1, ajustar prompt v2, documentar hipótesis de mejora.",
        "Iteración sin análisis es adivinar; registra **por qué** cambiaste cada frase.",
        ["Error analysis.", "Changelog prompt.", "Temperatura.", "Grounding."],
        f"""`{P23}/llm-eval/prompt-v2-changelog.md`: fallos v1 → cambio v2.

Archivo `prompt-v2.txt`. Re-ejecuta eval → `resultados-v2.csv`.""",
        rows(("Vendor", "Prompt engineering tips", SEC)),
        ["prompt-v2 + changelog.", "resultados-v2.csv.", "Hipótesis por cambio."],
        ["v2 sin comparar v1.", "Subir temperatura sin razón."],
    )
    w(
        "Umbral de calidad y cierre P2 parcial",
        3,
        "Quality gate FAQ",
        f"{P23}/llm-eval/resumen-evaluacion.md",
        "Comparar v1 vs v2; decidir si cumples umbral o documentas deuda para semana 5–6.",
        "P2 exige rúbrica + resultados tabulados; hoy cierras el gate numérico.",
        ["Umbral.", "Deuda.", "Costo por eval.", "Go/no-go RAG."],
        f"""`{P23}/llm-eval/resumen-evaluacion.md`: tabla versiones, % correcto, costo tokens estimado, decisión.

Si no alcanzas umbral, lista 3 acciones (más docs tenant, RAG, bajar temperatura).""",
        rows(("Ficha", "../M23-ia-datos.md P2", PS)),
        ["Resumen v1/v2.", "Umbral evaluado.", "Decisión documentada."],
        ["Declarar éxito sin CSV.", "Ignorar costos."],
    )
    w(
        "Diseño RAG por tenant — chunking y almacén",
        4,
        "Vendor RAG docs + pgvector/sqlite-vss",
        f"{P23}/rag/diseno.md",
        "Documentar arquitectura RAG: ingesta, chunking, embeddings, store, filtro tenant_id **antes** de retrieval.",
        "RAG global con filtro ‘después’ en prompt es vulnerabilidad explícita del plan.",
        ["Chunking.", "Embeddings.", "tenant_id en WHERE.", "Amenaza injection."],
        f"""`{P23}/rag/diseno.md`: diagrama, elección store, tamaño chunk, metadata obligatoria tenant_id.

Sección amenazas: prompt injection en PDF del dueño, metadatos mal filtrados.""",
        rows(("Vendor", "RAG guide", SEC)),
        ["diseno.md completo.", "Filtro tenant antes retrieval.", "Amenazas listadas."],
        ["Filtro solo en prompt.", "Store sin tenant_id."],
    )
    w(
        "Ingesta corpus tenant A (demo)",
        4,
        "Docs markdown políticas negocio",
        f"{P23}/rag/corpus/tenant-a/",
        "Ingestar ≥3 documentos markdown de políticas ficticias del tenant A demo.",
        "Necesitas corpus separado antes de probar cross-tenant.",
        ["Corpus.", "Markdown.", "Metadatos.", "Sin PII real."],
        f"""Crea `{P23}/rag/corpus/tenant-a/*.md` (horarios, cancelación, servicios). Script ingesta documentado o manual con hashes.

Registra versión corpus en `{P23}/rag/corpus/README.md`.""",
        rows(("M12", "SRS políticas", PS)),
        ["≥3 docs tenant A.", "README corpus.", "Sin PII real."],
        ["PDF escaneado sin OCR plan.", "Mezclar A y B en carpeta."],
    )
    w(
        "Ingesta corpus tenant B y contraste",
        4,
        "Aislamiento datos desde diseño",
        f"{P23}/rag/corpus/tenant-b/",
        "Segundo corpus claramente distinto (tenant B) para pruebas cross-tenant.",
        "Demo obligatoria A no ve B empieza con datos separados.",
        ["Separación física.", "IDs distintos.", "Políticas opuestas (test)."],
        f"""Corpus `{P23}/rag/corpus/tenant-b/` con política cancelación **distinta** a A (facilita detectar fuga).

Tabla comparación A vs B en `{P23}/rag/corpus/README.md`.""",
        rows(("Ficha", "../M23-ia-datos.md regla demo", SEC)),
        ["Corpus B ≥3 docs.", "Política distinta.", "README comparativo."],
        ["Mismo texto A/B.", "tenant_id solo en comentario."],
    )
    w(
        "Implementación retrieval con WHERE tenant_id",
        4,
        "Pseudocódigo SQL/ORM del plan",
        f"{P23}/rag/implementacion.md",
        "Describir o implementar retrieval donde tenant_id viene de sesión autenticada, no del cliente.",
        "Confiar en parámetro `tenantId` del JSON es IDOR waiting to happen.",
        ["Sesión server-side.", "WHERE obligatorio.", "Tests unit retrieval."],
        f"""`{P23}/rag/implementacion.md`: código en repo producto **o** pseudocódigo con enlaces commit.

Incluye snippet SQL estilo ficha (ORDER BY dist LIMIT 5 **con tenant**).""",
        rows(("M18", "IDOR", SEC)),
        ["implementacion.md.", "tenant de sesión.", "Snippet SQL correcto."],
        ["tenant_id query param.", "Búsqueda global k-NN."],
    )
    w(
        "Endpoint faq-preview protegido",
        5,
        "API interna admin",
        f"{P23}/faq-asistente/endpoint.md",
        "Diseñar o implementar POST interno faq-preview auth owner/staff con rate limit.",
        "Semana 5 entrega superficie controlada antes de UI pulida.",
        ["AuthZ.", "Rate limit.", "Preview vs prod.", "Logging redacted."],
        f"""Documenta en `{P23}/faq-asistente/endpoint.md` ruta, roles, body, respuesta, errores.

Enlaza PR repo producto si existe. Sin endpoint público anónimo.""",
        rows(("M18", "authZ", "../M17-aplicaciones-web.md")),
        ["endpoint.md.", "Roles definidos.", "Rate limit mencionado."],
        ["Endpoint público.", "Sin auth."],
    )
    w(
        "UI o CLI asistente para owner",
        5,
        "UX mínima FAQ",
        f"{P23}/faq-asistente/README.md borrador",
        "Exponer asistente mínimo: owner pregunta política cancelación → respuesta grounded.",
        "Proyecto materia: asistente scoped por tenant en staging.",
        ["UI mínima.", "CLI alternativa.", "Citas fuente.", "Fallback sin alucinar."],
        f"""Amplía `{P23}/faq-asistente/README.md`: cómo probar, credenciales test, ejemplo pregunta/respuesta.

Captura o log de sesión **redactado**.""",
        rows(("Plan", PS, "../M16-ihc.md estados UI")),
        ["README uso.", "Ejemplo Q&A.", "Staging URL."],
        ["Prometer auto-agenda.", "Respuesta sin fuente."],
    )
    w(
        "Casos tests-cross-tenant manuales",
        5,
        "QA seguridad producto",
        f"{P23}/rag/tests-cross-tenant.md",
        "Documentar casos: tenant A pregunta política B → no chunks B en contexto/respuesta.",
        "P3 y criterio egreso: evidencia reproducible de aislamiento.",
        ["Cross-tenant.", "Context dump.", "Assertion.", "Evidencia log."],
        f"""`{P23}/rag/tests-cross-tenant.md`: ≥4 casos, pasos, resultado esperado, evidencia (log CI o captura redacted).

Pregunta A sobre ‘política cancelación’ debe citar solo A.""",
        rows(("SEC", SEC, "../M18-seguridad.md")),
        ["≥4 casos.", "Evidencia adjunta/enlace.", "Pasos reproducibles."],
        ["Solo ‘parece ok’.", "Test sin tenant B ingestado."],
    )
    w(
        "Test automatizado cross-tenant en CI",
        5,
        "Vitest/Jest en repo producto",
        f"{P23}/rag/ci-evidencia.md",
        "Automatizar al menos un test que falle si retrieval devuelve chunk de otro tenant.",
        "Manual no escala; CI evita regresión antes de M26.",
        ["Test auto.", "Fixture dos tenants.", "CI verde.", "Regression."],
        f"""`{P23}/rag/ci-evidencia.md`: enlace workflow o comando local, commit SHA, salida test PASS.

Si aún no hay CI, script `npm test -- rag-isolation` documentado.""",
        rows(("M15", "../M15-vv-calidad.md", "GitHub Actions")),
        ["Test automatizado.", "ci-evidencia.md.", "Enlace commit."],
        ["Solo test manual.", "Skip en CI."],
    )
    w(
        "Feature flag IA y alineación pricing M22",
        6,
        "Plan Pro limits + cost control",
        f"{P23}/faq-asistente/plan-pro-ia.md",
        "Documentar flag o límite IA por plan Free/Pro coherente con pricing M22.",
        "Vender IA ilimitada en Pro sin costeo tumba margen.",
        ["Feature flag.", "Cuota mensual.", "Upgrade.", "Free sin RAG."],
        f"""`{P23}/faq-asistente/plan-pro-ia.md`: tabla plan → cuotas tokens/preguntas.

Enlaza `{P22}/pricing.md` con nota cruzada.""",
        rows(("M22", P22, PS)),
        ["plan-pro-ia.md.", "Enlace pricing.", "Cuotas numéricas."],
        ["IA gratis ilimitada.", "Flag sin default seguro."],
    )
    w(
        "Costo mensual estimado por tenant activo",
        6,
        "Unit economics IA",
        f"{P23}/llm-eval/costos-mensuales.md",
        "Estimar costo API + storage embeddings por tenant/mes con supuestos explícitos.",
        "Dueño y tú deben entender bill antes de activar Pro.",
        ["Costo variable.", "Supuestos.", "Preguntas/mes.", "Margen."],
        f"""`{P23}/llm-eval/costos-mensuales.md`: escenario bajo/medio/alto uso; fórmula; en MXN aproximado.

Actualiza `{P23}/politica-datos-llm.md` sección costos/retención.""",
        rows(("Vendor", "Pricing calculator", PS)),
        ["costos-mensuales.md.", "3 escenarios.", "Política actualizada."],
        ["Ignorar embedding cost.", "Sin supuestos."],
    )
    w(
        "README asistente FAQ y límites producto",
        6,
        "Soporte y expectativas",
        f"{P23}/faq-asistente/README.md final",
        "Finalizar README: qué hace, qué no hace, escalación humana, privacidad.",
        "Proyecto P3 FAQ integrado; soporte necesita límites claros.",
        ["Scope.", "No-go.", "Soporte.", "Privacidad."],
        f"""README final en `{P23}/faq-asistente/`: secciones Scope, Limits, Privacy, Runbook incidencia.

Enlaza código/endpoint staging.""",
        rows(("Ficha", "../M23-ia-datos.md proyecto", SEC)),
        ["README final.", "Limits claros.", "Enlace código."],
        ["‘IA mágica’.", "Sin escalación humana."],
    )
    w(
        "Cierre M23 — P1–P3, dominio y handoff M26",
        6,
        "Repaso ficha M23",
        f"{P23}/cierre-m23.md",
        "Auditar pipeline, eval LLM, RAG aislado, FAQ; commit cierre; README L01–L24.",
        "Cierras hilo IA/datos antes de emergentes (M24) y capstone (M26).",
        ["Checklist.", "Cross-tenant demo.", "Dominio.", "Handoff."],
        f"""`{P23}/cierre-m23.md` responde criterios dominio. Verifica política LLM respetada en scripts.

Commit `docs(m23): cierre materia`. Actualiza `{P23}/README.md` índice lecciones.""",
        rows(("Ficha", "../M23-ia-datos.md", "../M26-proyecto-integrador.md")),
        ["cierre-m23.md.", "Commit cierre.", "README índice.", "P1–P3 verificados."],
        ["Marcar UI sin test cross-tenant.", "PII en logs eval."],
    )
    return L


def main() -> None:
    counts = {
        "M21": write_materia("M21", m21()),
        "M22": write_materia("M22", m22()),
        "M23": write_materia("M23", m23()),
    }
    print("Generated:", counts, "total:", sum(counts.values()))


if __name__ == "__main__":
    main()
