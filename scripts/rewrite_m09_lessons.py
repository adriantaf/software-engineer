#!/usr/bin/env python3
"""Rewrite M09 lessons to M01-quality (concrete steps, Agenda Ops domain)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum/etapas/02-disciplinaria/M09"
BIBLIO = "../../../bibliografia.md#m09-bases-de-datos"
PG_TUT = "https://www.postgresql.org/docs/current/tutorial.html"
ELMASRI = "*Fundamentos de BD* — Elmasri & Navathe (ed. ES)"


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


def lectura_block(que, enlace_titulo="Tutorial PostgreSQL", enlace=PG_TUT):
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {ELMASRI} | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09]({BIBLIO}) |
"""


def wrap(meta, body, siguiente):
    return f"""{fm(**meta)}

{body.strip()}

{lectura_block(meta.get("_lectura_corta", meta["lectura"]))}

## Hecho cuando

Marca la lección **solo si**:

{meta["_hecho"]}

## Errores comunes

{meta["_errores"]}

## Siguiente

{siguiente}
"""


LESSONS = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="PostgreSQL local y carpeta de evidencia",
        horas=5.0,
        semana=1,
        lectura="Elmasri: intro SGBD + tutorial PostgreSQL (Getting Started)",
        evidencia="projects/m09-bases-datos/ con Docker o PG nativo + SELECT version()",
        _lectura_corta="Intro SGBD + [tutorial PG — Getting Started](https://www.postgresql.org/docs/current/tutorial-start.html)",
        _hecho="""1. Existe `projects/m09-bases-datos/` con `.env` local (no commiteado) y `docker compose` **o** PG nativo documentado.
2. Corres `SELECT version();` y anotas el resultado en el README (sin password).
3. Commit que mencione el arranque (ej. `docs(m09): arrancar postgres local`).""",
        _errores="""- Subir `.env` con passwords.
- Usar el usuario `postgres` superuser como “la app” desde el día 1.
- Documentar “ya tengo Docker” sin un `SELECT` ejecutado.""",
        siguiente="[L02 — Entidades Cliente, Servicio, Cita](L02-entidades-cliente-servicio-cita.md)",
        body=r"""
# L01 — PostgreSQL local y carpeta de evidencia

**~5.0 h · Semana 1**

Sin una BD real, Elmasri se queda en teoría. Hoy levantas PostgreSQL y dejas evidencia en git.

## Objetivo

Dejar `projects/m09-bases-datos/` usable: Compose (o nativo), conexión documentada y un `SELECT version()` ejecutado.

## Por qué empieza así

M09 diseña el esquema de **Agenda Ops**. Cada lección siguiente asume que puedes pegarle SQL a una instancia local.

## Pasos (hazlos en orden)

### 1. Revisa el scaffold (20 min)

Desde la raíz del repo:

```bash
ls projects/m09-bases-datos
cat projects/m09-bases-datos/README.md
```

Ya hay `docker-compose.yml`, `.env.example`, `migrations/` y plantillas. No borres la estructura; amplíala.

### 2. Variables locales (15 min)

```bash
cd projects/m09-bases-datos
cp .env.example .env
# Edita POSTGRES_PASSWORD (y opcionalmente APP_DB_PASSWORD)
```

Confirma que `.env` está en `.gitignore`.

### 3. Levanta PostgreSQL (45–60 min)

**Opción A — Docker:**

```bash
docker compose up -d
docker compose ps
```

**Opción B — Nativo:** crea usuario/DB con los mismos nombres del `.env` y anota el comando de instalación en el README.

### 4. Conecta y prueba (30–40 min)

```bash
set -a && source .env && set +a
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -c 'SELECT version();'
```

Si no tienes `psql` en el host:

```bash
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c 'SELECT version();'
```

Pega la versión (una línea) en una sección `## Conexión local` del README — **sin** password.

### 5. Aplica la migración 001 (45–60 min)

```bash
psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" \
  -f migrations/001_init.sql
psql "..." -c '\dt'
```

Debes ver `clientes`, `servicios`, `citas`.

### 6. Commit (15 min)

```bash
git add projects/m09-bases-datos
git status   # .env NO debe aparecer
git commit -m "docs(m09): arrancar postgres local y migración 001"
```
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Entidades Cliente, Servicio, Cita",
        horas=5.0,
        semana=1,
        lectura="Elmasri: modelo ER — entidades y atributos",
        evidencia="er-agenda.md con 3 entidades y atributos justificados",
        _hecho="""1. `er-agenda.md` describe Cliente, Servicio y Cita con atributos y tipos.
2. El diagrama Mermaid (o equivalente) refleja esas tres entidades.
3. Commit `docs(m09): entidades cliente servicio cita`.""",
        _errores="""- Mezclar “Usuario staff” con “Cliente” del salón.
- Poner precio solo en la cita y olvidar el catálogo de servicios.
- ER bonito sin relación con las tablas de `001_init.sql`.""",
        siguiente="[L03 — Cardinalidades y reglas de negocio](L03-cardinalidades-y-reglas-de-negocio.md)",
        body=r"""
# L02 — Entidades Cliente, Servicio, Cita

**~5.0 h · Semana 1**

El producto Agenda Ops gira en torno a tres hechos: quién reserva, qué se ofrece y cuándo ocurre.

## Objetivo

Completar el borrador de `er-agenda.md` con entidades, atributos y un diagrama que puedas defender en voz alta.

## Conceptos

- **Entidad** vs **atributo** vs **relación**.
- Clave primaria estable (`uuid`) vs natural (teléfono — malo como PK).
- `tenant_id` como columna preparatoria (aún single-tenant).

## Pasos

### 1. Lectura dirigida (45–60 min)

En Elmasri, secciones de entidades/atributos/tipos de entidad. Anota 5 términos en `glosario.md` o al final de `er-agenda.md`.

### 2. Contrasta con el SQL ya aplicado (30 min)

```bash
psql "..." -c '\d clientes'
psql "..." -c '\d servicios'
psql "..." -c '\d citas'
```

Lista en `er-agenda.md` qué columnas ya existen y si faltan atributos de negocio (ej. `notas`).

### 3. Escribe atributos con justificación (90 min)

Para cada entidad: atributo → tipo → por qué lo necesitas el día 1. Ejemplo mínimo:

- Cliente: `nombre`, `telefono` (WhatsApp), `email` opcional.
- Servicio: `duracion_min`, `precio_centavos` (evita floats).
- Cita: `inicia_en`, `termina_en`, `estado`.

### 4. Diagrama (45 min)

Actualiza el bloque Mermaid de `er-agenda.md` (o exporta PNG y enlázalo). Las tres entidades deben aparecer.

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos/er-agenda.md
git commit -m "docs(m09): entidades cliente servicio cita"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Cardinalidades y reglas de negocio",
        horas=5.0,
        semana=1,
        lectura="Elmasri: relaciones, cardinalidad, participación",
        evidencia="er-agenda.md con cardinalidades + CHECK/estado documentados",
        _hecho="""1. Cardinalidades Cliente–Cita y Servicio–Cita escritas (1:N).
2. Al menos 3 reglas de negocio (estados, `termina_en > inicia_en`, una más tuya).
3. Commit descriptivo.""",
        _errores="""- Dibujar N:M Cliente–Servicio sin tabla puente cuando el MVP es cita con un servicio.
- Reglas solo en la cabeza / en el front, nunca en ER ni en CHECK.
- Olvidar no-show como estado distinto de cancelada.""",
        siguiente="[L04 — Glosario alineado al dominio](L04-glosario-alineado-al-dominio.md)",
        body=r"""
# L03 — Cardinalidades y reglas de negocio

**~5.0 h · Semana 1**

Una FK sin regla de negocio es decoración. Hoy fijas cardinalidades y constraints que el dueño del salón entendería.

## Objetivo

Dejar en `er-agenda.md` las cardinalidades 1:N y un bloque de reglas verificables (algunas ya están en `001_init.sql`).

## Pasos

### 1. Lectura (45 min)

Cardinalidad mínima/máxima y participación total/parcial en Elmasri.

### 2. Escribe cardinalidades (40 min)

En `er-agenda.md`:

- Cliente **1** — **0..N** Citas
- Servicio **1** — **0..N** Citas
- Una Cita **exactamente 1** Cliente y **exactamente 1** Servicio (MVP)

Si más adelante quieres varios servicios por cita, documenta la tabla puente como *cambio futuro*, no lo inventes ya.

### 3. Reglas de negocio (90 min)

Completa una lista numerada. Mínimo:

1. `termina_en > inicia_en` (ya hay `CHECK`).
2. `estado ∈ {programada, confirmada, completada, cancelada, no_show}`.
3. Una regla tuya (ej. no solapar dos citas del mismo staff — si aún no hay staff, anótala como pendiente M17).

Verifica en SQL:

```sql
-- Debe fallar:
INSERT INTO citas (cliente_id, servicio_id, inicia_en, termina_en, estado)
SELECT id, (SELECT id FROM servicios LIMIT 1), now(), now() - interval '1 hour', 'programada'
FROM clientes LIMIT 1;
```

### 4. Participación (30 min)

¿Puede existir un cliente sin citas? (sí — parcial). ¿Una cita sin cliente? (no — total hacia cliente). Anótalo.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): cardinalidades y reglas de negocio"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Glosario alineado al dominio",
        horas=5.0,
        semana=1,
        lectura="Elmasri: diseño conceptual — vocabulario del dominio",
        evidencia="glosario.md completo + README enlaza P1 parcial",
        _hecho="""1. `glosario.md` tiene ≥8 términos con “no confundir con”.
2. El README de m09 enlaza `er-agenda.md` y `glosario.md`.
3. Commit de cierre de semana 1.""",
        _errores="""- Usar “usuario” para todo (staff, cliente, tenant).
- Glosario copiado de Wikipedia sin el producto.
- Términos que no aparecen en el ER.""",
        siguiente="[L05 — Primera forma normal y anomalías](L05-primera-forma-normal-y-anomalias.md)",
        body=r"""
# L04 — Glosario alineado al dominio

**~5.0 h · Semana 1**

Si el equipo dice “cliente” y uno piensa en el tenant SaaS, el esquema se rompe en M17. Hoy cierras vocabulario.

## Objetivo

Dejar `glosario.md` usable por alguien que no leyó Elmasri, alineado a Agenda Ops y a tu ER.

## Pasos

### 1. Lee producto (30 min)

Revisa `curriculum/producto-saas.md` (ICP, citas, tenant). Marca 5 palabras que ya usas distinto.

### 2. Completa el glosario (90 min)

Abre `projects/m09-bases-datos/glosario.md`. Amplía a ≥8 filas. Obligatorio cubrir: Cliente, Servicio, Cita, Tenant, No-show, Migración, Seed, Least privilege.

### 3. Cruza con el ER (45 min)

Cada término de entidad del glosario debe existir en `er-agenda.md`. Si sobra un término huérfano, elimínalo o modela la entidad.

### 4. README de evidencia (30 min)

En `projects/m09-bases-datos/README.md`, sección corta “Semana 1” con enlaces a `er-agenda.md` y `glosario.md`.

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): glosario dominio agenda ops"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Primera forma normal y anomalías",
        horas=5.0,
        semana=2,
        lectura="Elmasri: 1FN, anomalías de inserción/borrado/actualización",
        evidencia="er-agenda.md sección 1FN + ejemplo de tabla mala descompuesta",
        _hecho="""1. Documentas una “tabla Excel” que viola 1FN (teléfonos múltiples o listas en una celda).
2. Muestras la descomposición a relaciones atómicas.
3. Marcas 1FN como cumplida en la tabla de normalización de `er-agenda.md`.""",
        _errores="""- Guardar `telefonos` como `'a,b,c'` en un solo `text` “porque es más fácil”.
- Declarar 1FN sin ejemplo de anomalía.
- Normalizar de oídas sin tocar el ER.""",
        siguiente="[L06 — Segunda forma normal](L06-segunda-forma-normal.md)",
        body=r"""
# L05 — Primera forma normal y anomalías

**~5.0 h · Semana 2**

1FN exige atributos atómicos. Las hojas de Excel del salón casi nunca lo cumplen.

## Objetivo

Demostrar una violación de 1FN del dominio y dejar el esquema (o el diseño) en 1FN con evidencia escrita.

## Conceptos

- Valor atómico vs lista/repetición en la misma fila.
- Anomalías de actualización (cambiar un teléfono en N filas).
- Anomalías de borrado (perder el único dato del cliente al borrar una cita).

## Pasos

### 1. Lectura (45–60 min)

Capítulo/sección de 1FN y anomalías en Elmasri. Anota definiciones con tus palabras.

### 2. Tabla mala (45 min)

En `er-agenda.md` (sección Normalización), pega algo así y **explícalo**:

| cita_id | cliente | telefonos | servicios |
|---------|---------|-----------|-----------|
| 1 | Ana | 646-111, 646-222 | Corte, Barba |

Señala qué columnas no son atómicas.

### 3. Descomposición (75 min)

Escribe las tablas resultantes (Cliente, Telefono opcional, Servicio, Cita). Compara con `001_init.sql`: ¿ya estás en 1FN? Si añadiste un campo lista, corrígelo con migración o nota de deuda.

### 4. Anomalías (40 min)

Una fila de texto por tipo: inserción / actualización / borrado, usando el ejemplo malo.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): 1FN y anomalias agenda"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Segunda forma normal",
        horas=5.0,
        semana=2,
        lectura="Elmasri: 2FN, dependencia parcial",
        evidencia="Ejemplo PK compuesta + eliminación de dependencia parcial",
        _hecho="""1. Documentas un caso con PK compuesta que viola 2FN (inventado o histórico).
2. Muestras tablas resultantes en 2FN.
3. Actualizas la fila 2FN en `er-agenda.md`.""",
        _errores="""- Decir “ya estoy en 2FN” solo porque usas UUID surrogate sin analizar dependencias.
- Meter `nombre_cliente` en una tabla con PK `(cita_id, servicio_id)` y dejarlo así.
- Confundir 2FN con “tener índices”.""",
        siguiente="[L07 — Tercera forma normal (P1)](L07-tercera-forma-normal-p1.md)",
        body=r"""
# L06 — Segunda forma normal

**~5.0 h · Semana 2**

2FN elimina dependencias parciales de una clave compuesta. Aunque uses UUID, debes saber detectar el antipatrón.

## Objetivo

Explicar 2FN con un ejemplo del dominio (líneas de cita o staff+día) y justificar por qué tu esquema actual cumple o qué cambiarías.

## Pasos

### 1. Lectura (45 min)

Dependencia funcional y 2FN en Elmasri.

### 2. Caso que viola 2FN (60 min)

Imagina tabla `cita_detalle` con PK `(cita_id, servicio_id)` y columnas `nombre_servicio`, `precio_serv`. `nombre_servicio` depende solo de `servicio_id` → viola 2FN.

Escríbelo en `er-agenda.md` con la descomposición correcta (tabla `servicios` + hechos de la cita).

### 3. Tu esquema real (60 min)

Revisa PKs de `001_init.sql`. Con surrogate keys, 2FN suele cumplirse si no repites atributos del padre. Confirma por escrito: “no hay atributos que dependan de parte de la clave porque…”.

### 4. Mini ejercicio SQL (45 min)

Inserta un servicio y una cita; actualiza el nombre del servicio; verifica que las citas históricas **siguen** viendo el nombre nuevo vía JOIN (trade-off que verás en L08 — snapshot de precio).

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): segunda forma normal"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Tercera forma normal (P1)",
        horas=5.0,
        semana=2,
        lectura="Elmasri: 3FN / intro BCNF",
        evidencia="er-agenda.md en 3FN — cierra P1",
        _hecho="""1. Documentas al menos una dependencia transitiva evitada o eliminada.
2. Tabla de normalización en `er-agenda.md` marca 1FN–3FN.
3. README indica que P1 (ER hasta 3FN) está listo.""",
        _errores="""- Guardar `ciudad` y `estado` redundantes con una tabla de códigos postales a medias.
- Declarar 3FN sin mencionar dependencias transitivas.
- Cerrar P1 sin diagrama actualizado.""",
        siguiente="[L08 — Trade-offs de desnormalización](L08-trade-offs-de-desnormalizacion.md)",
        body=r"""
# L07 — Tercera forma normal (P1)

**~5.0 h · Semana 2**

3FN elimina dependencias transitivas. Con esto cierras la práctica **P1**.

## Objetivo

Dejar `er-agenda.md` en 3FN con justificación y enlazarlo como evidencia P1 en el README.

## Pasos

### 1. Lectura (45–60 min)

3FN e intro a BCNF. Diferencia en una frase tuya: 3FN vs BCNF.

### 2. Caza transitivas (60 min)

Ejemplo a analizar: `cliente_id → codigo_postal → ciudad → estado`. Si modelaras dirección completa, ¿qué tablas salen?

Para Agenda Ops MVP: decide si dirección es necesaria día 1. Si no, escríbelo como fuera de alcance (eso también es diseño).

### 3. Congela el ER 3FN (75 min)

Actualiza diagrama + tabla de normalización. Añade fecha y una frase: “P1 lista porque…”.

### 4. Checklist P1 en README (30 min)

Marca mentalmente (y en texto) que `er-agenda.md` cumple el criterio de la ficha M09.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): er en 3FN cierra P1"
```
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="Trade-offs de desnormalización",
        horas=5.0,
        semana=2,
        lectura="Elmasri: desnormalización / diseño físico intro",
        evidencia="Nota en er-agenda.md: qué desnormalizarías y por qué",
        _hecho="""1. Escribes un trade-off concreto (ej. `precio_centavos_snapshot` en `citas`).
2. Listas costo (consistencia) vs beneficio (historial / reportes).
3. Decides para M09: ¿lo implementas en una migración o lo dejas documentado?""",
        _errores="""- Desnormalizar “por si acaso” sin query que lo pida.
- Copiar `nombre_cliente` a la cita sin decir cómo se actualiza.
- Confundir caché de lectura con modelo canónico.""",
        siguiente="[L09 — Joins inner y left](L09-joins-inner-y-left.md)",
        body=r"""
# L08 — Trade-offs de desnormalización

**~5.0 h · Semana 2**

3FN no es religión: a veces el reporte del dueño necesita un snapshot. Hoy decides con criterio.

## Objetivo

Documentar **una** desnormalización consciente (implementada o aplazada) en `er-agenda.md`.

## Pasos

### 1. Lectura corta (30 min)

Secciones de diseño físico / desnormalización. Alternativa: notas PG sobre costos de JOIN vs almacenamiento.

### 2. Caso Agenda Ops (60 min)

Si el precio del “Corte” sube mañana, las citas completadas ayer ¿deben mostrar $150 o $180?

- Opción A: siempre JOIN a `servicios` (precio actual).
- Opción B: `citas.precio_centavos_snapshot` al crear la cita.

Elige y justifica en la sección L08 de `er-agenda.md`.

### 3. (Opcional) Migración (60–90 min)

Si eliges B:

```sql
ALTER TABLE citas
  ADD COLUMN IF NOT EXISTS precio_centavos_snapshot integer;
```

Versiona en `migrations/002_…` o un archivo nuevo numerado. Rellena snapshot en seeds después.

### 4. Regla de equipo (30 min)

Una frase en README: “Desnormalizamos X; la fuente de verdad de Y sigue siendo Z”.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): trade-off desnormalizacion precio"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Joins inner y left",
        horas=5.0,
        semana=3,
        lectura="Elmasri SQL joins + PG tutorial Queries",
        evidencia="sql/joins-citas-cliente.sql ejecutado",
        _hecho="""1. Ejecutaste INNER y LEFT JOIN del archivo (o el tuyo equivalente).
2. Hay comentario con salida de ejemplo en el `.sql` o en `samples/`.
3. Commit `feat(m09): joins citas cliente`.""",
        _errores="""- Usar solo comma-join (`FROM a, b WHERE`) sin entender la diferencia.
- LEFT JOIN y filtrar la tabla derecha en `WHERE` convirtiendo el left en inner sin querer.
- No tener seeds: joins sobre tablas vacías no enseñan nada.""",
        siguiente="[L10 — Agregaciones y GROUP BY](L10-agregaciones-y-group-by.md)",
        body=r"""
# L09 — Joins inner y left

**~5.0 h · Semana 3**

Los reportes del salón son JOINs. Hoy ejecutas los dos patrones básicos contra tu BD.

## Objetivo

Completar y correr `sql/joins-citas-cliente.sql` con datos reales (aunque sean seeds mínimos).

## Pasos

### 1. Seeds mínimos (30–45 min)

Si no hay filas:

```bash
psql "..." -f seeds/001_demo.sql
psql "..." -c 'SELECT count(*) FROM citas;'
```

### 2. Lectura SQL (40 min)

Elmasri: joins. Alternativa: [PG tutorial — Queries](https://www.postgresql.org/docs/current/tutorial-select.html).

### 3. Ejecuta el scaffold (60 min)

Abre `sql/joins-citas-cliente.sql`. Corre cada query. Ajusta columnas si tu esquema diverge.

### 4. Añade un tercer join útil (45 min)

Ejemplo: citas `completada` de la última semana con teléfono del cliente (para recordatorio manual). Guárdalo en el mismo archivo o en `sql/joins-completadas-recientes.sql`.

### 5. Evidencia + commit (30 min)

Comenta al final del SQL 3–5 líneas de resultado. Commit.
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Agregaciones y GROUP BY",
        horas=5.0,
        semana=3,
        lectura="Elmasri: agregación GROUP BY; PG aggregate functions",
        evidencia="sql/agg-citas-por-servicio.sql",
        _hecho="""1. Existe y corre un SQL con `GROUP BY` + `COUNT`/`SUM`.
2. Interpretas el resultado en una frase de negocio.
3. Commit.""",
        _errores="""- Seleccionar columnas no agregadas fuera del `GROUP BY`.
- Sumar `precio` en float.
- Reportar conteos sin filtrar `cancelada` cuando la pregunta es “atendidas”.""",
        siguiente="[L11 — Subconsultas y HAVING](L11-subconsultas-y-having.md)",
        body=r"""
# L10 — Agregaciones y GROUP BY

**~5.0 h · Semana 3**

El dueño pregunta: “¿qué servicio se agenda más?”. Eso es `GROUP BY`.

## Objetivo

Entregar `sql/agg-citas-por-servicio.sql` con al menos dos agregaciones ejecutadas.

## Pasos

### 1. Lectura (40 min)

Funciones de agregación y `GROUP BY` / `WHERE` vs filtros de grupo.

### 2. Escribe y corre (90 min)

```sql
-- sql/agg-citas-por-servicio.sql
SELECT s.nombre,
       count(*) AS total_citas,
       count(*) FILTER (WHERE c.estado = 'completada') AS completadas,
       coalesce(sum(s.precio_centavos) FILTER (WHERE c.estado = 'completada'), 0) AS ingresos_centavos
FROM citas c
JOIN servicios s ON s.id = c.servicio_id
GROUP BY s.id, s.nombre
ORDER BY total_citas DESC;
```

(Ajusta si usas snapshot de precio en la cita.)

### 3. Segunda query (45 min)

Citas por día (`date_trunc('day', inicia_en)`) de los últimos 14 días.

### 4. Frase de negocio (20 min)

En comentario del SQL: “El servicio más agendado esta semana es X con N citas”.

### 5. Commit (15 min)
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Subconsultas y HAVING",
        horas=5.0,
        semana=3,
        lectura="Elmasri: subconsultas; HAVING",
        evidencia="sql/subq-clientes-frecuentes.sql",
        _hecho="""1. Una query con `HAVING` y otra con subconsulta (`IN` / `EXISTS` / escalar).
2. Ambas ejecutadas con comentario de salida.
3. Commit.""",
        _errores="""- Usar `WHERE count(*) > 1` en lugar de `HAVING`.
- Subconsulta correlacionada innecesariamente lenta sin mirar el plan (eso es L14; hoy solo correctness).
- Clientes frecuentes incluyendo solo canceladas.""",
        siguiente="[L12 — Cinco consultas P2 comentadas](L12-cinco-consultas-p2-comentadas.md)",
        body=r"""
# L11 — Subconsultas y HAVING

**~5.0 h · Semana 3**

“Clientes con más de 2 citas completadas” pide filtrar **grupos**, no filas.

## Objetivo

Crear `sql/subq-clientes-frecuentes.sql` con `HAVING` y al menos una subconsulta.

## Pasos

### 1. Lectura (40 min)

Subconsultas escalares, `IN`/`EXISTS`, y `HAVING`.

### 2. HAVING (60 min)

```sql
SELECT cl.nombre, count(*) AS completadas
FROM citas c
JOIN clientes cl ON cl.id = c.cliente_id
WHERE c.estado = 'completada'
GROUP BY cl.id, cl.nombre
HAVING count(*) >= 2
ORDER BY completadas DESC;
```

### 3. Subconsulta (60 min)

Lista servicios que **nunca** se han agendado (`NOT EXISTS` o `LEFT JOIN … IS NULL`). Prefiere `EXISTS` y explica por qué en un comentario.

### 4. Compara mentalmente con JOIN (30 min)

Reescribe una de las dos con puro JOIN. ¿Más legible? Anota preferencia.

### 5. Commit (15 min)
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Cinco consultas P2 comentadas",
        horas=5.0,
        semana=3,
        lectura="Repaso Elmasri SQL + tutorial PG",
        evidencia="sql/ con ≥5 archivos .sql comentados — avanza P2",
        _hecho="""1. Hay ≥5 archivos `.sql` en `sql/` (joins, agg, subq, +2 reportes o variantes).
2. Cada uno tiene comentario de propósito + salida ejemplo.
3. Commit de paquete P2 queries.""",
        _errores="""- Cinco archivos vacíos o idénticos.
- Queries que no corren.
- Sin relación con preguntas de negocio del salón.""",
        siguiente="[L13 — Índices B-tree intro](L13-indices-b-tree-intro.md)",
        body=r"""
# L12 — Cinco consultas P2 comentadas

**~5.0 h · Semana 3**

Cierras el paquete de consultas de la práctica **P2** (falta EXPLAIN en semana 4).

## Objetivo

Dejar ≥5 SQL comentados, ejecutables, orientados a Agenda Ops.

## Pasos

### 1. Inventario (20 min)

```bash
ls projects/m09-bases-datos/sql/*.sql
```

### 2. Completa el set (150 min)

Mínimo sugerido:

1. `joins-citas-cliente.sql` (L09)
2. `agg-citas-por-servicio.sql` (L10)
3. `subq-clientes-frecuentes.sql` (L11)
4. `reporte-no-shows.sql` — tasa o listado de no-show
5. `reporte-agenda-del-dia.sql` — citas de un día (`\set dia '''2026-09-26'''` o literal)

Cada archivo: encabezado con pregunta de negocio + comentario de salida.

### 3. Smoke test (40 min)

Corre los cinco seguidos; arregla los que fallen.

### 4. Commit (20 min)

```bash
git add projects/m09-bases-datos/sql
git commit -m "feat(m09): cinco consultas P2 comentadas"
```
""",
    )
)

# ---------- L13 ----------
LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="Índices B-tree intro",
        horas=5.0,
        semana=4,
        lectura="Elmasri: índices; PG docs Indexes / CREATE INDEX",
        evidencia="Índice nuevo documentado + \\d citas",
        _hecho="""1. Creas (o justificas) al menos un índice adicional alineado a un reporte.
2. Documentas en `explain-notas.md` o migración por qué existe.
3. Commit.""",
        _errores="""- Indexar todas las columnas.
- Índice único accidental que rompe inserts legítimos.
- No saber qué es B-tree vs “magia del motor”.""",
        siguiente="[L14 — EXPLAIN ANALYZE en consultas reales](L14-explain-analyze-en-consultas-reales.md)",
        body=r"""
# L13 — Índices B-tree intro

**~5.0 h · Semana 4**

Un índice no es un logro: es una apuesta sobre lecturas vs escrituras.

## Objetivo

Entender B-tree en la práctica y dejar un índice justificado por una query tuya.

## Pasos

### 1. Lectura (50 min)

Elmasri (índices) + [PG CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) (solo B-tree por ahora).

### 2. Inventario actual (30 min)

```sql
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'citas';
```

Compara con lo que ya creó `001_init.sql`.

### 3. Elige una query lenta potencial (60 min)

Ej. filtrar por `estado` + rango de `inicia_en`. Diseña:

```sql
CREATE INDEX IF NOT EXISTS idx_citas_estado_inicia
  ON citas (estado, inicia_en);
```

Ponlo en `migrations/002_auditoria_y_indices.sql` (o archivo nuevo) si aún no está.

### 4. Aplica y verifica (40 min)

```bash
psql "..." -f migrations/002_auditoria_y_indices.sql
psql "..." -c '\d citas'
```

### 5. Commit (15 min)
""",
    )
)

# ---------- L14 ----------
LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="EXPLAIN ANALYZE en consultas reales",
        horas=5.0,
        semana=4,
        lectura="PG: EXPLAIN / Using EXPLAIN",
        evidencia="explain-notas.md con plan ANTES pegado",
        _hecho="""1. Corres `EXPLAIN (ANALYZE, BUFFERS)` sobre una query de reporte.
2. Pegas el plan en `explain-notas.md` (sección antes).
3. Explicas en llano Seq Scan vs Index Scan.""",
        _errores="""- Solo `EXPLAIN` sin `ANALYZE` y hablar de tiempos reales.
- Pegar el plan sin interpretar una sola línea.
- Medir con tabla vacía.""",
        siguiente="[L15 — Optimizar query lenta de reporte](L15-optimizar-query-lenta-de-reporte.md)",
        body=r"""
# L14 — EXPLAIN ANALYZE en consultas reales

**~5.0 h · Semana 4**

El plan de ejecución es la radiografía. Hoy lees una de **tu** query.

## Objetivo

Llenar la sección “Plan (antes…)” de `explain-notas.md`.

## Pasos

### 1. Lectura (45 min)

[Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — enfócate en nodos Seq Scan, Index Scan, cost, rows, actual time.

### 2. Elige query (20 min)

Copia tu reporte diario o agg a `sql/explain-reporte-diario.sql`.

### 3. Corre EXPLAIN (60 min)

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT …;
```

Pega salida completa en `explain-notas.md`.

### 4. Traducción al español (60 min)

Escribe 5–8 líneas: qué nodo domina, estimaciones vs reality (`rows` vs `actual rows`), buffers.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): explain analyze reporte diario"
```
""",
    )
)

# ---------- L15 ----------
LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="Optimizar query lenta de reporte",
        horas=5.0,
        semana=4,
        lectura="Elmasri selectividad / PG Index-Only Scans intro",
        evidencia="Plan DESPUÉS + cambio (índice o reescritura)",
        _hecho="""1. Aplicas un cambio (índice, filtro, reescritura).
2. Vuelves a correr EXPLAIN ANALYZE.
3. Documentas comparación antes/después.""",
        _errores="""- Declarar victoria sin segunda medición.
- Índice que no se usa (tipo de dato / función sobre columna).
- Optimizar una query que nadie corre.""",
        siguiente="[L16 — Documentar planes de ejecución](L16-documentar-planes-de-ejecucion.md)",
        body=r"""
# L15 — Optimizar query lenta de reporte

**~5.0 h · Semana 4**

Una pasada de EXPLAIN no basta: cambias algo y vuelves a medir.

## Objetivo

Completar “Plan (después)” y la conclusión en `explain-notas.md`.

## Pasos

### 1. Hipótesis (30 min)

Ejemplos: falta índice en `(tenant_id, inicia_en)`; `WHERE date(inicia_en) = …` impide uso de índice; SELECT * innecesario.

### 2. Cambia una sola cosa (60–90 min)

Índice **o** reescritura (mejor `inicia_en >= @start AND inicia_en < @end` que casteos).

### 3. Remide (45 min)

Mismo `EXPLAIN (ANALYZE, BUFFERS)`. Pega en la sección después.

### 4. Criterio de éxito (30 min)

Si con seeds pequeños no hay diferencia, dilo honestamente y explica qué pasaríacon 100k citas (orden de magnitud).

### 5. Commit (15 min)
""",
    )
)

# ---------- L16 ----------
LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Documentar planes de ejecución",
        horas=5.0,
        semana=4,
        lectura="Repaso EXPLAIN + tu explain-notas.md",
        evidencia="explain-notas.md completo — cierra P2",
        _hecho="""1. `explain-notas.md` tiene pregunta, SQL, antes, cambio, después, conclusión.
2. README marca P2 (sql/ + explain) como listo.
3. Commit de cierre P2.""",
        _errores="""- Notas solo con screenshots ilegibles.
- No enlazar el archivo SQL del reporte.
- Cerrar P2 sin ≥5 queries de L12.""",
        siguiente="[L17 — Transacciones ACID](L17-transacciones-acid.md)",
        body=r"""
# L16 — Documentar planes de ejecución

**~5.0 h · Semana 4**

La evidencia de P2 es legible por otro humano (tú en tres meses).

## Objetivo

Cerrar `explain-notas.md` y la checklist P2 en el README.

## Pasos

### 1. Pulido del documento (90 min)

Relee `explain-notas.md`. Añade:

- Link relativo al `.sql`
- Pregunta de negocio en una línea
- Conclusión binaria: ¿mantenemos el índice? sí/no + cuándo revisarlo

### 2. Índice de sql/ (40 min)

Tabla corta en README: archivo → pregunta.

### 3. Autorevisión P2 (40 min)

Checklist ficha M09: joins/agregaciones + EXPLAIN comentado. Lista gaps si los hay (y ciérralos).

### 4. Commit (20 min)

```bash
git commit -am "docs(m09): cierra P2 explain y sql"
```
""",
    )
)

# ---------- L17 ----------
LESSONS.append(
    dict(
        id="L17",
        orden=17,
        titulo="Transacciones ACID",
        horas=5.0,
        semana=5,
        lectura="Elmasri: transacciones ACID; PG BEGIN/COMMIT/ROLLBACK",
        evidencia="sql/transaccion-cita.sql",
        _hecho="""1. Script con `BEGIN` que inserta cita + fila de auditoría y `COMMIT`.
2. Demuestras un `ROLLBACK` (error forzado) dejando la BD consistente.
3. Commit del SQL.""",
        _errores="""- Dos statements sueltos sin transacción cuando deben ser atómicos.
- Auditar en la app “más tarde” y perder el enlace.
- Dejar transacciones abiertas en `psql`.""",
        siguiente="[L18 — Migraciones versionadas](L18-migraciones-versionadas.md)",
        body=r"""
# L17 — Transacciones ACID

**~5.0 h · Semana 5**

Crear cita sin auditoría (o al revés) es un bug de integridad. ACID lo evita.

## Objetivo

Entregar `sql/transaccion-cita.sql` que inserta cita + `cita_auditoria` atómicamente.

## Pasos

### 1. Lectura (45 min)

Propiedades ACID en Elmasri. Traduce cada letra con un ejemplo de citas.

### 2. Asegura tabla auditoría (30 min)

Aplica `migrations/002_auditoria_y_indices.sql` si no lo hiciste.

### 3. Script feliz (75 min)

```sql
BEGIN;
WITH nueva AS (
  INSERT INTO citas (cliente_id, servicio_id, inicia_en, termina_en, estado)
  VALUES (…, …, now() + interval '3 days', now() + interval '3 days 30 min', 'programada')
  RETURNING id
)
INSERT INTO cita_auditoria (cita_id, accion, detalle)
SELECT id, 'crear', jsonb_build_object('via', 'm09-l17') FROM nueva;
COMMIT;
```

### 4. Script de fallo (45 min)

Fuerza un error (FK inválida) dentro de `BEGIN` y verifica que no quedó basura (`ROLLBACK` implícito/ explícito).

### 5. Commit (15 min)

```bash
git add projects/m09-bases-datos/sql/transaccion-cita.sql
git commit -m "feat(m09): transaccion cita + auditoria"
```
""",
    )
)

# ---------- L18 ----------
LESSONS.append(
    dict(
        id="L18",
        orden=18,
        titulo="Migraciones versionadas",
        horas=5.0,
        semana=5,
        lectura="Práctica: migraciones en git; opcional herramienta (dbmate/flyway/prisma)",
        evidencia="migrations/ 001+002 aplicadas y documentadas",
        _hecho="""1. Al menos dos migraciones numeradas en git.
2. README explica cómo aplicarlas en orden en máquina limpia.
3. Commit si faltaba documentación.""",
        _errores="""- Cambiar `001_init.sql` ya aplicado en prod/compañero sin nueva migración.
- Migraciones solo en la cabeza / en un GUI.
- Orden no determinista de archivos.""",
        siguiente="[L19 — Least privilege (P3)](L19-least-privilege-p3.md)",
        body=r"""
# L18 — Migraciones versionadas

**~5.0 h · Semana 5**

El esquema es código. Si no está en git con orden, no existe.

## Objetivo

Dejar `migrations/` reproducible: 001 + 002 (y notas de 003 para L19).

## Pasos

### 1. Elige convención (30 min)

Ya tienes numeración `001_`, `002_`. Documenta en `migrations/README.md` si más adelante usarás dbmate/flyway/prisma — **no hace falta migrar la herramienta hoy**.

### 2. Verifica idempotencia razonable (60 min)

Reaplicar `001` no debe destruir datos (usamos `IF NOT EXISTS`). Prueba en una DB temporal o anota el riesgo.

### 3. Simula máquina limpia (90 min)

```bash
docker compose down -v   # ¡borra volumen local de evidencia!
docker compose up -d
# aplicar 001, 002, seeds
```

Solo si puedes recrear seeds después. Si no quieres borrar, usa otro `POSTGRES_DB` / compose project name.

### 4. README “desde cero” (45 min)

Lista ordenada de comandos en el README principal.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): migraciones versionadas reproducibles"
```
""",
    )
)

# ---------- L19 ----------
LESSONS.append(
    dict(
        id="L19",
        orden=19,
        titulo="Least privilege (P3)",
        horas=5.0,
        semana=5,
        lectura="PG: roles / GRANT; Elmasri seguridad intro",
        evidencia="roles.md + 003_roles_app.sql — cierra P3",
        _hecho="""1. Existe rol `agenda_app` (o equivalente) sin superuser.
2. Demuestras SELECT/INSERT OK y DDL denegado (error pegado en `roles.md`).
3. README marca P3 listo.""",
        _errores="""- App y migraciones con el mismo superuser.
- GRANT ALL TABLES TO PUBLIC.
- Password del rol app en el README.""",
        siguiente="[L20 — Reportes, seeds y cierre M09](L20-reportes-seeds-y-cierre-m09.md)",
        body=r"""
# L19 — Least privilege (P3)

**~5.0 h · Semana 5**

El hilo de seguridad empieza aquí: la app no es dueña del clúster.

## Objetivo

Aplicar `migrations/003_roles_app.sql` (ajustando password local) y completar `roles.md`.

## Pasos

### 1. Lectura (40 min)

[PG privileges](https://www.postgresql.org/docs/current/ddl-priv.html) — GRANT/REVOKE básicos.

### 2. Ajusta y aplica 003 (45 min)

Edita la password del `CREATE ROLE` con tu `APP_DB_PASSWORD` **local**. Aplica el SQL.

### 3. Prueba positiva (40 min)

```bash
psql "postgresql://agenda_app:${APP_DB_PASSWORD}@localhost:5432/agenda_ops" \
  -c 'SELECT count(*) FROM citas;'
```

### 4. Prueba negativa (40 min)

```sql
DROP TABLE citas;          -- debe fallar
CREATE TABLE hack(x int);  -- debe fallar
```

Pega el error en `roles.md`.

### 5. Commit (20 min) — sin secretos

```bash
git add projects/m09-bases-datos/roles.md projects/m09-bases-datos/migrations/003_roles_app.sql
git commit -m "feat(m09): rol agenda_app least privilege"
```
""",
    )
)

# ---------- L20 ----------
LESSONS.append(
    dict(
        id="L20",
        orden=20,
        titulo="Reportes, seeds y cierre M09",
        horas=5.0,
        semana=5,
        lectura="Cierre: seeds + reportes de negocio",
        evidencia="seeds + reportes.md + README — cierra proyecto M09",
        _hecho="""1. `seeds/001_demo.sql` (o ampliado) aplica limpio.
2. `reportes.md` tiene ≥2 reportes con SQL + salida.
3. Otro dev podría recrear la BD solo con tu README (lo simulas tú).""",
        _errores="""- Reportes sin pregunta de negocio.
- Seeds con datos personales reales.
- Marcar el proyecto en la UI sin `reportes.md`.""",
        siguiente="Cierra la [ficha M09](../M09-bases-de-datos.md). Siguiente materia disciplinaria según tu plan.",
        body=r"""
# L20 — Reportes, seeds y cierre M09

**~5.0 h · Semana 5**

Cierras el **proyecto** de la materia: esquema reproducible, seeds y reportes útiles.

## Objetivo

Dejar `seeds/`, `reportes.md` y README en estado “otro humano levanta esto”.

## Pasos

### 1. Seeds realistas (75 min)

Amplía `seeds/001_demo.sql`: ≥5 clientes, ≥3 servicios, citas en varios estados (`programada`, `completada`, `no_show`, `cancelada`). Reaplica en DB limpia o tras truncate controlado.

### 2. Dos reportes (75 min)

Completa `reportes.md`. Ideas:

1. No-shows de los últimos 30 días por cliente.
2. Ingresos estimados (centavos) por servicio en citas `completada`.

Cada uno: pregunta → archivo SQL → salida → uso para el dueño.

### 3. Checklist total (45 min)

P1 `er-agenda.md` · P2 `sql/` + `explain-notas.md` · P3 `migrations/` + `roles.md` · Proyecto seeds + reportes.

### 4. Simulación máquina limpia (45 min)

Sigue solo tu README (sin mirar las lecciones). Anota fricciones y arréglalas.

### 5. Commit de cierre (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): cierre materia seeds y reportes"
```
""",
    )
)


def render(lesson: dict) -> str:
    meta = {
        "id": lesson["id"],
        "materia": "M09",
        "orden": lesson["orden"],
        "titulo": lesson["titulo"],
        "horas": lesson["horas"],
        "semana": lesson["semana"],
        "lectura": lesson["lectura"],
        "evidencia": lesson["evidencia"],
        "_hecho": lesson["_hecho"],
        "_errores": lesson["_errores"],
        "_lectura_corta": lesson.get("_lectura_corta", lesson["lectura"]),
    }
    # strip private keys from frontmatter
    pub = {k: v for k, v in meta.items() if not k.startswith("_")}
    body = lesson["body"].strip() + "\n\n" + lectura_block(
        lesson.get("_lectura_corta", lesson["lectura"])
    )
    errores = lesson["_errores"].strip()
    hecho = lesson["_hecho"].strip()
    return f"""{fm(**pub)}

{lesson["body"].strip()}

{lectura_block(lesson.get("_lectura_corta", lesson["lectura"]))}

## Hecho cuando

Marca la lección **solo si**:

{hecho}

## Errores comunes

{errores}

## Siguiente

{lesson["siguiente"]}
"""


def filename(lesson: dict) -> str:
    # keep existing kebab names
    mapping = {
        1: "L01-postgresql-local-y-carpeta-de-evidencia.md",
        2: "L02-entidades-cliente-servicio-cita.md",
        3: "L03-cardinalidades-y-reglas-de-negocio.md",
        4: "L04-glosario-alineado-al-dominio.md",
        5: "L05-primera-forma-normal-y-anomalias.md",
        6: "L06-segunda-forma-normal.md",
        7: "L07-tercera-forma-normal-p1.md",
        8: "L08-trade-offs-de-desnormalizacion.md",
        9: "L09-joins-inner-y-left.md",
        10: "L10-agregaciones-y-group-by.md",
        11: "L11-subconsultas-y-having.md",
        12: "L12-cinco-consultas-p2-comentadas.md",
        13: "L13-indices-b-tree-intro.md",
        14: "L14-explain-analyze-en-consultas-reales.md",
        15: "L15-optimizar-query-lenta-de-reporte.md",
        16: "L16-documentar-planes-de-ejecucion.md",
        17: "L17-transacciones-acid.md",
        18: "L18-migraciones-versionadas.md",
        19: "L19-least-privilege-p3.md",
        20: "L20-reportes-seeds-y-cierre-m09.md",
    }
    return mapping[lesson["orden"]]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lesson in LESSONS:
        path = OUT / filename(lesson)
        text = render(lesson)
        # ensure single trailing newline
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print("total", len(LESSONS))


if __name__ == "__main__":
    main()
