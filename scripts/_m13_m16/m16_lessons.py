"""M16 — IHC: 12 lessons at M01/M09 quality."""
from __future__ import annotations

FILENAMES = {
    1: "L01-recorrido-persona-nueva-y-fricciones-dia-1.md",
    2: "L02-auditoria-nielsen-tres-heuristicas-profundas.md",
    3: "L03-estados-vacio-carga-y-error-en-agenda.md",
    4: "L04-auditoria-v1-y-cierre-p1-heuristicas.md",
    5: "L05-prototipo-navegable-y-tareas-del-srs.md",
    6: "L06-guion-de-test-de-usabilidad-15-30-min.md",
    7: "L07-sesiones-1-3-notas-de-participantes.md",
    8: "L08-sesiones-4-5-y-resumen-agregado-p2.md",
    9: "L09-priorizar-top-5-hallazgos.md",
    10: "L10-iteracion-ui-antes-y-despues.md",
    11: "L11-informe-de-usabilidad-para-stakeholders.md",
    12: "L12-cierre-m16-handoff-m17-y-criterios-dominio.md",
}

LESSONS: list[dict] = []

LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Recorrido persona nueva y fricciones día 1",
        horas=5.0,
        semana=1,
        lectura="Krug: no me hagas pensar; primer recorrido Agenda Ops",
        evidencia="projects/m16-ihc/fricciones-dia-1.md",
        _lectura_corta="Escaneo y fricción en el primer uso del panel de citas",
        _enlace_titulo="Heurísticas Nielsen (NN/g)",
        _enlace="https://www.nngroup.com/articles/ten-usability-heuristics/",
        _hecho="""1. Carpeta `projects/m16-ihc/` con `fricciones-dia-1.md` (≥8 fricciones concretas del flujo agendar/ver agenda).
2. Cada fricción nombra pantalla/paso y quién sufre (owner vs staff nuevo).
3. Commit `docs(m16): fricciones dia 1 persona nueva`.""",
        _errores="""- “La UI está fea” sin paso reproducible.
- Evaluar solo como desarrollador con datos seed perfectos.
- Ignorar login y estados vacíos.""",
        siguiente="[L02 — Auditoría Nielsen — tres heurísticas profundas](L02-auditoria-nielsen-tres-heuristicas-profundas.md)",
        body=r"""
# L01 — Recorrido persona nueva y fricciones día 1

**~5.0 h · Semana 1**

El design partner no es tú. Hoy recorres Agenda Ops (prototipo o UI parcial) como persona nueva.

## Objetivo

Lista de fricciones en `fricciones-dia-1.md` y carpetas base de evidencia.

## Por qué empieza así

Sin fricciones observadas, la auditoría Nielsen se vuelve checklist vacío.

## Pasos (hazlos en orden)

### 1. Prepara carpeta (15 min)

```bash
mkdir -p projects/m16-ihc/{heuristicas,sesiones,iteracion,prototipo}
cat projects/m16-ihc/README.md
```

### 2. Elige superficie (20 min)

Prototipo HTML en `prototipo/`, Figma export, o UI M17 si existe. Si no hay nada: crea 2–3 HTML estáticos de login + agenda + nueva cita (L05 lo endurece).

### 3. Recorrido cronometrado (60–80 min)

Cronómetro: “Agendar cita para cliente nuevo”. Anota cada duda, click engañoso, label confuso.

### 4. Escribe fricciones-dia-1.md (70–90 min)

| ID | Paso | Fricción | Impacto percibido |
|----|------|----------|-------------------|
| F01 | Login | … | alto/medio/bajo |

### 5. Commit

`docs(m16): fricciones dia 1 persona nueva`
""",
    )
)

LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Auditoría Nielsen — tres heurísticas profundas",
        horas=5.0,
        semana=1,
        lectura="Tres heurísticas Nielsen a fondo sobre el piloto",
        evidencia="heuristicas/parcial-3.md",
        _lectura_corta="Visibilidad de estado, match mundo real, prevención de errores",
        _hecho="""1. Documento con 3 heurísticas profundas y ≥2 hallazgos cada una (severidad 1–3 o baja/media/alta).
2. Hallazgos trazan a pantallas del piloto (agenda/cita/login).
3. Commit `docs(m16): auditoria parcial tres heuristicas`.""",
        _errores="""- Las 10 heurísticas en una línea cada una.
- Severidad inflada en todo.
- Hallazgos genéricos (“mejorar UX”).""",
        siguiente="[L03 — Estados vacío, carga y error en agenda](L03-estados-vacio-carga-y-error-en-agenda.md)",
        body=r"""
# L02 — Auditoría Nielsen — tres heurísticas profundas

**~5.0 h · Semana 1**

Profundizas tres heurísticas que más duelen en scheduling: estado del sistema, lenguaje del negocio, prevención de errores.

## Objetivo

`heuristicas/parcial-3.md` con hallazgos severizados.

## Pasos (hazlos en orden)

### 1. Elige tres (20 min)

Recomendadas: (#1) visibilidad de estado, (#2) match con el mundo real (jerga del salón/clínica), (#5) prevención de errores.

### 2. Audita con capturas o URLs (90–110 min)

Tabla como en la ficha M16 (ID, heurística, hallazgo, severidad, fix).

### 3. Cruza con fricciones L01 (30 min)

### 4. Commit

`docs(m16): auditoria parcial tres heuristicas`
""",
    )
)

LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Estados vacío, carga y error en agenda",
        horas=5.0,
        semana=1,
        lectura="Estados UI; mensajes sin filtrar datos ajenos",
        evidencia="heuristicas/estados-agenda.md (+ mocks en prototipo)",
        _lectura_corta="Empty/loading/error en agenda; seguridad en mensajes",
        _hecho="""1. Documento de estados vacío/carga/error para agenda y crear cita.
2. Al menos un mensaje de error revisado para no filtrar datos de otros usuarios.
3. Commit `docs(m16): estados vacio carga error agenda`.""",
        _errores="""- Solo mockup del estado feliz con datos densos.
- Spinner eterno sin timeout/mensaje.
- Error “cita #4821 del tenant X” visible.""",
        siguiente="[L04 — auditoria-v1 y cierre P1 heurísticas](L04-auditoria-v1-y-cierre-p1-heuristicas.md)",
        body=r"""
# L03 — Estados vacío, carga y error en agenda

**~5.0 h · Semana 1**

La agenda vacía del lunes es el primer contacto real. Hoy diseñas empty/loading/error.

## Objetivo

Especificación (y si puedes, HTML) de los tres estados.

## Pasos (hazlos en orden)

### 1. Inventario de vistas (30 min)

Lista del día, detalle cita, formulario nueva cita.

### 2. Especifica estados (80–100 min)

Copy sugerido, CTA (“Crear primera cita”), error recuperable vs bloqueante.

### 3. Nota de seguridad UX (30 min)

Qué no decir en 403/404.

### 4. Commit

`docs(m16): estados vacio carga error agenda`
""",
    )
)

LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="auditoria-v1 y cierre P1 heurísticas",
        horas=5.0,
        semana=1,
        lectura="Consolidar auditoría v1; evidencia P1",
        evidencia="heuristicas/auditoria-v1.md (P1)",
        _lectura_corta="Cierre P1: auditoria-v1 con severidad",
        _hecho="""1. `heuristicas/auditoria-v1.md` consolida hallazgos (incl. estados) con severidad y fix propuesto.
2. README enlaza P1.
3. Commit `docs(m16): auditoria-v1 cierre P1`.""",
        _errores="""- Archivo parcial renombrado sin consolidar.
- Sin severidades.
- P1 marcado con fricciones sueltas únicamente.""",
        siguiente="[L05 — Prototipo navegable y tareas del SRS](L05-prototipo-navegable-y-tareas-del-srs.md)",
        body=r"""
# L04 — auditoria-v1 y cierre P1 heurísticas

**~5.0 h · Semana 1**

P1 = auditoría con severidad. Hoy empaquetas.

## Objetivo

`auditoria-v1.md` listo para marcar P1.

## Pasos (hazlos en orden)

### 1. Merge L01–L03 (70–90 min)

Una tabla maestra de hallazgos + apéndice de método.

### 2. Top riesgos (40 min)

### 3. Commit

`docs(m16): auditoria-v1 cierre P1`
""",
    )
)

LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Prototipo navegable y tareas del SRS",
        horas=5.0,
        semana=2,
        lectura="Prototipo clicable; tareas Must del SRS",
        evidencia="prototipo/ navegable + mapa de tareas",
        _lectura_corta="Prototipo para test de pasillo alineado al SRS",
        _hecho="""1. Prototipo navegable (HTML/Figma) cubriendo login → agenda → crear cita (mínimo).
2. `prototipo/tareas-srs.md` mapea tareas de test a historias Must.
3. Commit `feat(m16): prototipo navegable y tareas SRS`.""",
        _errores="""- Prototipo de marketing no usable en test.
- Tareas que no existen en el SRS.
- Dependencias rotas (links muertos entre pantallas).""",
        siguiente="[L06 — Guion de test de usabilidad 15–30 min](L06-guion-de-test-de-usabilidad-15-30-min.md)",
        body=r"""
# L05 — Prototipo navegable y tareas del SRS

**~5.0 h · Semana 2**

Sin prototipo, las sesiones inventan la UI. Hoy lo dejas clicable.

## Objetivo

`projects/m16-ihc/prototipo/` usable en test de 15–30 min.

## Pasos (hazlos en orden)

### 1. Pantallas mínimas (90–120 min)

HTML estático o Figma prototype: Login, Agenda del día, Nueva cita, Confirmación/error.

### 2. tareas-srs.md (40 min)

| Tarea test | Historia SRS |
|------------|--------------|
| Agendar cita cliente nuevo | H-cita-01 |
| Cancelar cita de hoy | H-cita-02 |

### 3. Commit

`feat(m16): prototipo navegable y tareas SRS`
""",
    )
)

LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Guion de test de usabilidad 15–30 min",
        horas=5.0,
        semana=2,
        lectura="Krug: test de pasillo; consentimiento básico",
        evidencia="guion-usabilidad.md",
        _lectura_corta="Guion 15–30 min + consentimiento y think-aloud",
        _hecho="""1. `guion-usabilidad.md` con intro, tareas, preguntas de cierre y tiempo.
2. Incluye consentimiento básico y anonimización de notas.
3. Commit `docs(m16): guion de usabilidad`.""",
        _errores="""- Guion que defiende el diseño (“es fácil ¿verdad?”).
- Sesiones de 2 horas.
- Sin espacio para think-aloud.""",
        siguiente="[L07 — Sesiones 1–3 — notas de participantes](L07-sesiones-1-3-notas-de-participantes.md)",
        body=r"""
# L06 — Guion de test de usabilidad 15–30 min

**~5.0 h · Semana 2**

El guion evita sesiones anécdota. Hoy lo escribes antes de citar gente.

## Objetivo

`guion-usabilidad.md` listo para leer en voz alta.

## Pasos (hazlos en orden)

### 1. Estructura (60–70 min)

Contexto → consentimiento → tareas (del L05) → debrief.

Usa el extracto de la ficha M16 como base y adáptalo a tu sub-vertical.

### 2. Criterios de éxito por tarea (40 min)

Observable: “creó la cita sin ayuda del facilitador”.

### 3. Piloto contigo mismo (30 min) — cronometra

### 4. Commit

`docs(m16): guion de usabilidad`
""",
    )
)

LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Sesiones 1–3 — notas de participantes",
        horas=5.0,
        semana=2,
        lectura="Facilitación; notas estructuradas",
        evidencia="sesiones/participante-1..3.md",
        _lectura_corta="Tres sesiones reales con notas por participante",
        _hecho="""1. Tres archivos de sesión con consentimiento anotado, tareas y citas textuales relevantes.
2. Sin PII innecesaria (usa P1/P2/P3).
3. Commit `docs(m16): sesiones 1-3 usabilidad`.""",
        _errores="""- Sesiones inventadas.
- Facilitador que interrumpe y “enseña” la UI.
- Notas solo “le fue bien”.""",
        siguiente="[L08 — Sesiones 4–5 y resumen agregado P2](L08-sesiones-4-5-y-resumen-agregado-p2.md)",
        body=r"""
# L07 — Sesiones 1–3 — notas de participantes

**~5.0 h · Semana 2**

Personas reales (design partner, conocidos del rubro, compañeros). No auto-test.

## Objetivo

`sesiones/participante-1.md` … `participante-3.md`.

## Pasos (hazlos en orden)

### 1. Agenda 3 sesiones (ya deberías haber citado)

### 2. Facilita y anota (3×15–30 min + buffer)

Plantilla:

```markdown
# Participante P1
Consentimiento: sí
Perfil: staff de … (anónimo)
Tarea 1: …
Obstáculos:
Citas textuales:
```

### 3. Commit parcial el mismo día

`docs(m16): sesiones 1-3 usabilidad`
""",
    )
)

LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="Sesiones 4–5 y resumen agregado P2",
        horas=5.0,
        semana=2,
        lectura="Síntesis de patrones; cierre P2",
        evidencia="participante-4..5 + resumen-5-usuarios.md (P2)",
        _lectura_corta="Cinco sesiones + resumen agregado de patrones",
        _hecho="""1. Cinco sesiones documentadas.
2. `sesiones/resumen-5-usuarios.md` con patrones (no solo anécdotas) — P2.
3. Commit `docs(m16): resumen 5 usuarios cierre P2`.""",
        _errores="""- Cinco clones de la misma nota.
- Resumen sin frecuencias.
- Ignorar hallazgos que contradicen tu ego de diseño.""",
        siguiente="[L09 — Priorizar top 5 hallazgos](L09-priorizar-top-5-hallazgos.md)",
        body=r"""
# L08 — Sesiones 4–5 y resumen agregado P2

**~5.0 h · Semana 2**

P2 exige 5 personas + síntesis.

## Objetivo

Cerrar sesiones y `resumen-5-usuarios.md`.

## Pasos (hazlos en orden)

### 1. Sesiones 4–5 (60–90 min netos)

### 2. Matriz de patrones (60–70 min)

| Hallazgo | # participantes | Severidad |
|----------|-----------------|-----------|
| No encuentra “Nueva cita” | 4/5 | alta |

### 3. Commit

`docs(m16): resumen 5 usuarios cierre P2`
""",
    )
)

LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Priorizar top 5 hallazgos",
        horas=5.0,
        semana=3,
        lectura="Impacto × frecuencia; backlog UX",
        evidencia="iteracion/backlog-top5.md",
        _lectura_corta="Priorizar top 5 para iterar en M16/M17",
        _hecho="""1. `backlog-top5.md` con score impacto×frecuencia y dueño (M16 fix vs M17).
2. Al menos 1 hallazgo de severidad alta en el top.
3. Commit `docs(m16): backlog top 5 hallazgos`.""",
        _errores="""- Priorizar solo lo fácil de arreglar.
- Top 5 sin relación a P1/P2.
- Mezclar bugs de backend sin etiquetar.""",
        siguiente="[L10 — Iteración UI — antes y después](L10-iteracion-ui-antes-y-despues.md)",
        body=r"""
# L09 — Priorizar top 5 hallazgos

**~5.0 h · Semana 3**

No puedes arreglar 40 cosas. Hoy eliges cinco con criterio.

## Objetivo

Backlog priorizado para la iteración.

## Pasos (hazlos en orden)

### 1. Scoring (50–60 min)

### 2. Define “hecho” por ítem (40 min)

### 3. Commit

`docs(m16): backlog top 5 hallazgos`
""",
    )
)

LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Iteración UI — antes y después",
        horas=5.0,
        semana=3,
        lectura="Implementar o wireframear fixes; evidencia visual",
        evidencia="iteracion/ antes-despues (P3)",
        _lectura_corta="Cambios concretos con evidencia antes/después",
        _hecho="""1. `iteracion/` con antes/después (capturas, HTML diff o Figma frames) de ≥1 hallazgo alto.
2. Notas de qué cambió y por qué.
3. Commit `feat(m16): iteracion UI antes-despues P3`.""",
        _errores="""- Solo promesas (“lo haremos en M17”) sin artefacto.
- Rediseño total sin trazabilidad al hallazgo.
- Después igual al antes.""",
        siguiente="[L11 — Informe de usabilidad para stakeholders](L11-informe-de-usabilidad-para-stakeholders.md)",
        body=r"""
# L10 — Iteración UI — antes y después

**~5.0 h · Semana 3**

P3: iteración documentada. Arreglas al menos lo más doloroso.

## Objetivo

Evidencia visual/código en `iteracion/`.

## Pasos (hazlos en orden)

### 1. Implementa o wireframea top hallazgos (120–150 min)

### 2. Capturas antes/después (30 min)

### 3. Commit

`feat(m16): iteracion UI antes-despues P3`
""",
    )
)

LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Informe de usabilidad para stakeholders",
        horas=5.0,
        semana=3,
        lectura="Informe ejecutivo; riesgos UX→seguridad",
        evidencia="informe-usabilidad.md (proyecto)",
        _lectura_corta="Informe para design partner: método, hallazgos, cambios",
        _hecho="""1. `informe-usabilidad.md` con resumen ejecutivo (1 pág), método, top hallazgos, cambios hechos/planificados.
2. Sección de riesgos UX que pueden virar a bugs de seguridad.
3. Commit `docs(m16): informe de usabilidad`.""",
        _errores="""- Informe solo técnico para ti.
- Sin prioridades.
- Ocultar hallazgos incómodos.""",
        siguiente="[L12 — Cierre M16 — handoff M17 y criterios dominio](L12-cierre-m16-handoff-m17-y-criterios-dominio.md)",
        body=r"""
# L11 — Informe de usabilidad para stakeholders

**~5.0 h · Semana 3**

El proyecto de M16 es el informe que el design partner entiende.

## Objetivo

`informe-usabilidad.md` completo.

## Pasos (hazlos en orden)

### 1. Resumen ejecutivo (40 min)

### 2. Cuerpo (80–100 min)

Método, participantes (anónimos), tareas, hallazgos, iteración, backlog residual.

### 3. Riesgos seguridad UX (30 min)

### 4. Commit

`docs(m16): informe de usabilidad`
""",
    )
)

LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Cierre M16 — handoff M17 y criterios dominio",
        horas=5.0,
        semana=3,
        lectura="Handoff UX→implementación M17; criterios dominio",
        evidencia="README índice + handoff-m17.md + autoevaluación",
        _lectura_corta="Handoff a M17 y criterios de dominio de la ficha",
        _hecho="""1. README M16 índice P1–P3 + informe.
2. `handoff-m17.md` con cambios UX a implementar en el front real.
3. Commit `docs(m16): cierre handoff M17 y dominio`.""",
        _errores="""- Handoff sin rutas a prototipo/informe.
- Criterios de dominio todos ✓ sin evidencia.
- Guion no reutilizable.""",
        siguiente="Materia siguiente: [M17 — Aplicaciones web](../M17-aplicaciones-web.md).",
        body=r"""
# L12 — Cierre M16 — handoff M17 y criterios dominio

**~5.0 h · Semana 3**

Cierras IHC dejando al yo-de-M17 una lista accionable, no un PDF de adorno.

## Objetivo

Handoff + autoevaluación de criterios de dominio.

## Pasos (hazlos en orden)

### 1. handoff-m17.md (50–60 min)

Tickets UX → pantallas/endpoints M13.

### 2. README final (40 min)

### 3. Criterios de dominio (40 min)

Informe con prioridades; hallazgo alto abordado; guion reutilizable; mensajes sin filtrar datos ajenos.

### 4. Commit

`docs(m16): cierre handoff M17 y dominio`
""",
    )
)
