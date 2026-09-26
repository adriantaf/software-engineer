"""M13 — Análisis y diseño: 20 lessons at M01/M09 quality."""
from __future__ import annotations

FILENAMES = {
    1: "L01-trust-boundaries-y-adr-001.md",
    2: "L02-actores-y-casos-de-uso-prioritarios.md",
    3: "L03-escenarios-alternos-y-errores.md",
    4: "L04-cierre-p1-flujos-principales.md",
    5: "L05-diagrama-de-clases-del-dominio.md",
    6: "L06-cardinalidades-y-persistencia-futura.md",
    7: "L07-secuencia-autenticacion-y-sesion.md",
    8: "L08-secuencia-crear-cita-p2.md",
    9: "L09-arquitectura-en-capas.md",
    10: "L10-dtos-validacion-y-frontera-http.md",
    11: "L11-componentes-y-despliegue-c4-ligero.md",
    12: "L12-boundaries-actualizados-y-amenazas.md",
    13: "L13-plantilla-adr-y-decisiones-de-diseno.md",
    14: "L14-adr-persistencia-y-modelo-de-datos.md",
    15: "L15-extensibilidad-tenant-id-sin-implementar.md",
    16: "L16-adr-auth-y-sesion.md",
    17: "L17-indice-del-paquete-de-diseno.md",
    18: "L18-endpoints-y-modulos-previstos-m17.md",
    19: "L19-checklist-listo-para-scaffold.md",
    20: "L20-cierre-m13-trazabilidad-y-dominio.md",
}

LESSONS: list[dict] = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Trust boundaries y ADR 001",
        horas=5.0,
        semana=1,
        lectura="Larman: contexto de diseño + plantilla ADR M01",
        evidencia="projects/m13-diseno/diagramas/trust-boundaries.md + adr/001-monolito-modular.md",
        _lectura_corta="Límites de confianza en apps web; plantilla ADR (contexto → decisión → consecuencias)",
        _enlace_titulo="OWASP — Trust Boundaries (glosario)",
        _enlace="https://owasp.org/www-community/vulnerabilities/Trust_Boundary_Violation",
        _hecho="""1. Existe `projects/m13-diseno/diagramas/trust-boundaries.md` con Mermaid (navegador | API | DB) y datos que cruzan cada límite.
2. Existe `projects/m13-diseno/adr/001-monolito-modular.md` con contexto Agenda Ops, decisión y ≥3 consecuencias.
3. Commit `docs(m13): trust boundaries y ADR 001 monolito modular`.""",
        _errores="""- Dibujar microservicios “porque es moderno” sin problema que lo justifique.
- Boundary sin listar qué dato o credencial cruza (cookie, JSON, SQL).
- ADR genérico copiado sin mencionar citas/clientes/roles del piloto.""",
        siguiente="[L02 — Actores y casos de uso prioritarios](L02-actores-y-casos-de-uso-prioritarios.md)",
        body=r"""
# L01 — Trust boundaries y ADR 001

**~5.0 h · Semana 1**

El SRS de Agenda Ops dice *qué*; hoy marcas *dónde* deja de confiarse el sistema y decides monolito modular antes de dibujar 40 cajas.

## Objetivo

Dejar `projects/m13-diseno/` con trust boundaries dibujados y el ADR 001 (monolito modular) firmado en git.

## Por qué empieza así

Autorización no vive solo ocultando botones en el panel. Si no marcas el límite navegador→API→DB, M17 nacerá confiando en el cliente HTTP.

## Pasos (hazlos en orden)

### 1. Revisa scaffold y SRS (25–35 min)

```bash
ls projects/m13-diseno
cat projects/m13-diseno/README.md
ls projects/m12-srs
```

Si aún no tienes `projects/m12-srs/srs-v1.md`, usa `projects/m12-srs/plantilla.md` + [producto-saas.md](../../../producto-saas.md) (citas, clientes, owner/staff). Anota 3 requisitos Must que toquen auth o datos ajenos.

### 2. Crea carpetas (10 min)

```bash
mkdir -p projects/m13-diseno/diagramas projects/m13-diseno/adr
```

### 3. Dibuja trust boundaries (70–90 min)

Crea `projects/m13-diseno/diagramas/trust-boundaries.md` con título, el diagrama siguiente, tablas y notas.

Diagrama (cópialo al archivo):

```mermaid
flowchart LR
  U[Usuario / browser] -->|HTTPS + cookie sesión| API[API Node]
  API -->|SQL parametrizado| DB[(PostgreSQL)]
  API -->|opcional| Mail[Email / WhatsApp link]
```

Tabla **Qué cruza cada límite**:

| Límite | Datos / credenciales | Quién valida |
|--------|----------------------|--------------|
| Browser → API | Cookie de sesión, JSON de cita | API: sesión + rol |
| API → DB | user_id, cliente_id, slot | API + constraints DB |
| API → Mail | email, texto sin PII extra | API (no el browser) |

**Nota de amenaza (alto nivel):** cookie robada → sesión hijack (HttpOnly, Secure, SameSite); IDOR `GET /citas/:id` de otro negocio → 403 en API, no solo en UI.

Ajusta nombres a tu SRS; no inventes microservicios.

### 4. Escribe ADR 001 (60–75 min)

Crea `projects/m13-diseno/adr/001-monolito-modular.md` siguiendo la plantilla de M01:

```markdown
# ADR 001 — Monolito modular para el piloto Agenda Ops

## Contexto
Un design partner, un deploy, equipo de uno. Necesito auth + citas + clientes
sin ops de N servicios.

## Decisión
Monolito modular: un proceso API + un front, módulos internos
(auth, citas, clientes) con fronteras claras de código.

## Consecuencias
+ Deploy simple; traces end-to-end fáciles
+ Transacciones locales (crear cita) sin saga
− Riesgo de “ball of mud” si no cuidamos capas (mitigar en M13 L09+)
− Multi-tenant real llega después (tenant_id en M15/M17 path)
```

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git status
git commit -m "docs(m13): trust boundaries y ADR 001 monolito modular"
```
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="Actores y casos de uso prioritarios",
        horas=5.0,
        semana=1,
        lectura="Larman: actores y casos de uso; SRS Agenda Ops Must",
        evidencia="projects/m13-diseno/casos-de-uso.md (actores + UC prioritarios)",
        _lectura_corta="Actores, casos de uso y priorización Must del SRS",
        _enlace_titulo="UML — Use Case Diagram (resumen)",
        _enlace="https://www.uml-diagrams.org/use-case-diagrams.html",
        _hecho="""1. `casos-de-uso.md` lista actores (owner, staff, sistema) con 1 frase de responsabilidad cada uno.
2. ≥5 casos de uso Must con id (UC-xx), actor primario y traza a historia/requisito del SRS.
3. Commit `docs(m13): actores y casos de uso prioritarios`.""",
        _errores="""- 30 casos de uso “por si acaso”; quédate en el MVP Must.
- Actor “Usuario” genérico sin distinguir owner vs staff.
- Casos sin traza al SRS (imposible saber si son inventados).""",
        siguiente="[L03 — Escenarios alternos y errores](L03-escenarios-alternos-y-errores.md)",
        body=r"""
# L02 — Actores y casos de uso prioritarios

**~5.0 h · Semana 1**

Sin actores claros, los diagramas de la semana 2 no saben *quién* habla con la API.

## Objetivo

Borrador sólido de `projects/m13-diseno/casos-de-uso.md`: actores + casos Must del piloto.

## Por qué importa

M17 implementará login, CRUD de citas/clientes y roles. Si hoy no priorizas, mañana codificas features que el design partner no usa.

## Pasos (hazlos en orden)

### 1. Extrae actores del SRS (40–50 min)

Abre `projects/m12-srs/srs-v1.md` (o plantilla) y marca quién inicia cada historia Must.

Actores mínimos esperados:

| Actor | Responsabilidad |
|-------|-----------------|
| Owner | Admin del negocio: roles, servicios, clientes |
| Staff | Opera agenda del día: crear/cancelar citas |
| Sistema | Recordatorios futuros / jobs (aunque sea stub) |

### 2. Lista casos Must (70–90 min)

Crea o amplía `projects/m13-diseno/casos-de-uso.md` con secciones **Actores** y **Casos prioritarios (Must)**.

Tabla mínima esperada:

| ID | Nombre | Actor | Traza SRS | Notas |
|----|--------|-------|-----------|-------|
| UC-01 | Iniciar sesión | Owner/Staff | H-auth-01 | cookie/sesión |
| UC-02 | Crear cliente | Owner/Staff | H-cli-01 | |
| UC-03 | Crear cita | Staff | H-cita-01 | slot + servicio |
| UC-04 | Cancelar cita | Staff | H-cita-02 | |
| UC-05 | Listar agenda del día | Staff | H-cita-03 | |

Ajusta IDs a tu SRS; no copies ciegos.

### 3. Diagrama ligero opcional (30–40 min)

Si ayuda, añade Mermaid use-case (máx. 8 elipses). Si el diagrama no cambia una decisión, bórralo.

### 4. Párrafo de alcance (20 min)

Al final del archivo: qué **queda fuera** del piloto (pagos Stripe, multi-sucursal, WhatsApp bot completo).

### 5. Commit (15 min)

```bash
git add projects/m13-diseno/casos-de-uso.md
git commit -m "docs(m13): actores y casos de uso prioritarios"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="Escenarios alternos y errores",
        horas=5.0,
        semana=1,
        lectura="Larman: escenarios alternos; códigos HTTP de auth/validación",
        evidencia="casos-de-uso.md con escenarios 401/403/409 por UC críticos",
        _lectura_corta="Flujos alternos y de error; 401 vs 403 vs 409 en APIs",
        _enlace_titulo="MDN — HTTP status codes",
        _enlace="https://developer.mozilla.org/es/docs/Web/HTTP/Status",
        _hecho="""1. Al menos 3 UC críticos tienen escenario feliz + ≥2 alternos/error documentados.
2. Cada error nombra código HTTP esperado (401/403/400/409) y mensaje *sin* filtrar datos ajenos.
3. Commit `docs(m13): escenarios alternos y errores en casos de uso`.""",
        _errores="""- Mezclar 401 (no autenticado) con 403 (autenticado sin permiso).
- Mensajes tipo “el cliente X de otro negocio no existe” (filtración).
- Solo escenario feliz: el diseño de M17 fallará en conflictos de horario.""",
        siguiente="[L04 — Cierre P1 flujos principales](L04-cierre-p1-flujos-principales.md)",
        body=r"""
# L03 — Escenarios alternos y errores

**~5.0 h · Semana 1**

El flujo feliz de “crear cita” es el 20 %. Hoy diseñas el 80 %: sin sesión, sin permiso, slot ocupado, input inválido.

## Objetivo

Extender `casos-de-uso.md` con escenarios alternos y de error alineados a códigos HTTP.

## Por qué importa

M15 pedirá tests 401/403/409. Si el diseño no nombra esos caminos, los tests inventarán comportamiento.

## Pasos (hazlos en orden)

### 1. Elige 3 UC críticos (15 min)

Típico: `UC-01` login, `UC-03` crear cita, `UC-04` cancelar (o listar agenda).

### 2. Plantilla por UC (90–110 min)

Para cada uno, añade bajo el caso:

```markdown
### UC-03 Crear cita

**Feliz:** Staff autenticado, slot libre, cliente existente → 201 + cita.

**A1 — Sin autenticación:** sin cookie → **401**. No revelar si el slot existe.

**A2 — Rol insuficiente:** si defines “solo owner cancela”, staff → **403**.

**A3 — Conflicto de horario:** mismo slot → **409** con mensaje genérico.

**A4 — Input inválido:** `fin < inicio` o servicio inexistente → **400** + campos.

**Datos que NUNCA van en el mensaje:** emails de otros clientes, IDs internos de otro negocio.
```

### 3. Tabla resumen de errores (40–50 min)

Al final de `casos-de-uso.md`:

| UC | Condición | HTTP | Mensaje (idea) |
|----|-----------|------|----------------|
| UC-03 | sin sesión | 401 | “Inicia sesión” |
| UC-03 | slot ocupado | 409 | “Horario no disponible” |

### 4. Revisa contra trust boundaries (20 min)

Abre `diagramas/trust-boundaries.md`: ¿cada error se decide en la **API**, no solo en el front?

### 5. Commit (15 min)

```bash
git add projects/m13-diseno/casos-de-uso.md
git commit -m "docs(m13): escenarios alternos y errores en casos de uso"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Cierre P1 flujos principales",
        horas=5.0,
        semana=1,
        lectura="Repaso casos de uso Must; evidencia P1 ficha M13",
        evidencia="casos-de-uso.md consolidado (P1) + bitácora semana 1",
        _lectura_corta="Cierre de flujos Must; checklist P1 de la ficha M13",
        _hecho="""1. `casos-de-uso.md` cubre historias Must del SRS con actores, UC y errores 401/403/409 donde aplica.
2. Existe `projects/m13-diseno/bitacora-semana-1.md` (qué quedó fuera + 1 decisión).
3. Commit `docs(m13): cierre P1 flujos principales`.""",
        _errores="""- Marcar P1 en la UI sin el archivo consolidado en git.
- Dejar UC “TBD” en Must.
- Bitácora vacía o solo “avancé”.""",
        siguiente="[L05 — Diagrama de clases del dominio](L05-diagrama-de-clases-del-dominio.md)",
        body=r"""
# L04 — Cierre P1 flujos principales

**~5.0 h · Semana 1**

P1 de M13 es evidencia: flujos principales del Agenda en un solo archivo legible.

## Objetivo

Consolidar `casos-de-uso.md` y dejar bitácora de semana 1 lista para marcar P1.

## Pasos (hazlos en orden)

### 1. Auditoría Must (50–60 min)

Compara `casos-de-uso.md` vs SRS:

```bash
# anota a mano o con grep mental
# ¿Cada historia Must tiene UC-xx?
```

Tabla de cobertura al inicio del archivo:

| Historia SRS | UC | ¿Errores? |
|--------------|----|-----------|
| … | UC-0x | sí/no |

### 2. Limpieza (40–50 min)

- Elimina UC duplicados o “nice to have” sin traza.
- Unifica nombres (Cliente vs Customer).
- Asegura que login y crear cita tienen alternos.

### 3. Bitácora semana 1 (40–50 min)

`projects/m13-diseno/bitacora-semana-1.md`:

```markdown
# Bitácora M13 — Semana 1

## Hecho
- Trust boundaries + ADR 001
- Casos de uso Must + errores

## Fuera de alcance (consciente)
- …

## Decisión que sostengo
Monolito modular porque …
```

### 4. Checklist P1 (20 min)

Según ficha: P1 = `casos-de-uso.md` cubriendo Must. Léelo en voz alta 5 minutos: ¿un compañero entiende el piloto?

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre P1 flujos principales"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="Diagrama de clases del dominio",
        horas=5.0,
        semana=2,
        lectura="Larman: modelo de dominio; entidades Agenda Ops",
        evidencia="projects/m13-diseno/diagramas/clases.md (Mermaid classDiagram)",
        _lectura_corta="Modelo de dominio: clases, atributos y asociaciones mínimas",
        _enlace_titulo="Mermaid — classDiagram",
        _enlace="https://mermaid.js.org/syntax/classDiagram.html",
        _hecho="""1. `diagramas/clases.md` incluye Mermaid con ≥4 clases del MVP (p. ej. Usuario, Cliente, Servicio, Cita).
2. Cada clase tiene atributos que implementarás en M17 (no “campos por estética”).
3. Commit `docs(m13): diagrama de clases del dominio`.""",
        _errores="""- 40 clases el día 1 (Factura, Inventario, CRM…).
- Modelar pantallas React como clases de dominio.
- Olvidar `negocioId`/`userId` donde el SRS implica pertenencia.""",
        siguiente="[L06 — Cardinalidades y persistencia futura](L06-cardinalidades-y-persistencia-futura.md)",
        body=r"""
# L05 — Diagrama de clases del dominio

**~5.0 h · Semana 2**

Traduces UC a cosas que existen: Cliente, Servicio, Cita, Usuario. Sin UML decorativo.

## Objetivo

`projects/m13-diseno/diagramas/clases.md` con dominio mínimo alineado al SRS y a M09.

## Pasos (hazlos en orden)

### 1. Lista entidades Must (30–40 min)

Desde `casos-de-uso.md` y, si existe, `projects/m09-bases-datos/er-agenda.md`:

- Usuario (rol owner/staff)
- Cliente
- Servicio
- Cita
- (Opcional) Negocio stub si ya pensaste single-tenant explícito

### 2. Escribe el Mermaid (70–90 min)

En `diagramas/clases.md` incluye este diagrama (ajústalo a tu SRS):

```mermaid
classDiagram
  class Usuario {
    +id: string
    +email: string
    +rol: owner|staff
  }
  class Cliente {
    +id: string
    +nombre: string
    +telefono: string
  }
  class Servicio {
    +id: string
    +nombre: string
    +duracionMin: number
    +precioBase: number
  }
  class Cita {
    +id: string
    +inicio: datetime
    +fin: datetime
    +estado: agendada|cancelada
  }
  Usuario "1" --> "*" Cita : agenda
  Cliente "1" --> "*" Cita
  Servicio "1" --> "*" Cita
```

Añade una tabla **Trazabilidad** (clase → UC / historia). Ejemplo: `Cita` → UC-03, UC-04.

### 3. Atributos honestos (40 min)

Borra getters UML vacíos. Si no sabes el tipo, anótalo en una lista “decidir en L14” — no inventes 12 enums.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/clases.md
git commit -m "docs(m13): diagrama de clases del dominio"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="Cardinalidades y persistencia futura",
        horas=5.0,
        semana=2,
        lectura="Cardinalidades 1..* / *..*; FK futuras M09",
        evidencia="clases.md con cardinalidades + nota de tablas/FK",
        _lectura_corta="Multiplicidad en asociaciones; mapeo a FK en PostgreSQL",
        _hecho="""1. Cada asociación en `clases.md` tiene multiplicidad explícita (1, 0..1, 1..*, *).
2. Sección “Persistencia futura” mapea clase→tabla y FK (aunque no escribas SQL hoy).
3. Commit `docs(m13): cardinalidades y mapeo a persistencia`.""",
        _errores="""- Cita *—* Servicio sin aclarar si una cita es un solo servicio (MVP).
- Cardinalidades que contradicen el ER de M09.
- “N:N citas-servicios” sin tabla puente pensada.""",
        siguiente="[L07 — Secuencia: autenticación y sesión](L07-secuencia-autenticacion-y-sesion.md)",
        body=r"""
# L06 — Cardinalidades y persistencia futura

**~5.0 h · Semana 2**

Las flechas bonitas mienten si no dices *cuántos*. Hoy fijamos multiplicidad y el puente a tablas.

## Objetivo

Actualizar `diagramas/clases.md` con cardinalidades y un mapa clase→tabla coherente con M09.

## Pasos (hazlos en orden)

### 1. Revisa M09 si existe (25–35 min)

```bash
ls projects/m09-bases-datos/migrations 2>/dev/null
cat projects/m09-bases-datos/er-agenda.md 2>/dev/null | head -80
```

Si no hay M09 aún, asume tablas `usuarios`, `clientes`, `servicios`, `citas` como en el scaffold típico.

### 2. Anota multiplicidades (50–60 min)

Ejemplo piloto:

| Asociación | Multiplicidad | Regla |
|------------|---------------|-------|
| Cliente–Cita | 1 a * | toda cita tiene un cliente |
| Servicio–Cita | 1 a * | MVP: un servicio por cita |
| Usuario–Cita | 1 a * | quién la creó / staff asignado |

Actualiza el Mermaid (`"1" --> "*"`).

### 3. Sección persistencia (60–70 min)

Añade a `clases.md`:

```markdown
## Persistencia futura (M09 / M17)

| Clase | Tabla | FK |
|-------|-------|-----|
| Cita | citas | cliente_id, servicio_id, usuario_id |
| … | … | … |

Índices probables: (inicio), (cliente_id), unique parcial anti-doble-booking (decidir en ADR persistencia).
```

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/clases.md
git commit -m "docs(m13): cardinalidades y mapeo a persistencia"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Secuencia: autenticación y sesión",
        horas=5.0,
        semana=2,
        lectura="Larman: diagramas de secuencia; flujo login/sesión",
        evidencia="projects/m13-diseno/diagramas/secuencia-auth.md",
        _lectura_corta="Secuencia UML: login, cookie/sesión, fallo 401",
        _enlace_titulo="Mermaid — sequenceDiagram",
        _enlace="https://mermaid.js.org/syntax/sequenceDiagram.html",
        _hecho="""1. `secuencia-auth.md` muestra participantes Browser, API, Store/DB y pasos de login OK + fallo.
2. Queda explícito dónde se crea/valida la sesión (API, no solo front).
3. Commit `docs(m13): secuencia autenticacion y sesion`.""",
        _errores="""- Secuencia donde el browser “guarda el rol” y la API confía ciegamente.
- Olvidar el camino de credenciales inválidas.
- Tokens en localStorage sin justificación (si eliges cookie, dilo en el diagrama).""",
        siguiente="[L08 — Secuencia: crear cita (P2)](L08-secuencia-crear-cita-p2.md)",
        body=r"""
# L07 — Secuencia: autenticación y sesión

**~5.0 h · Semana 2**

Sin una secuencia de auth, el resto de diagramas asume magia. Hoy dibujas login y validación de sesión.

## Objetivo

`diagramas/secuencia-auth.md` con Mermaid del flujo UC-01.

## Pasos (hazlos en orden)

### 1. Decide mecanismo (20–30 min)

Piloto recomendado: **sesión server-side o cookie firmada HttpOnly**. Anótalo; el ADR formal es L16.

### 2. Secuencia feliz + fallo (80–100 min)

En `diagramas/secuencia-auth.md`:

```mermaid
sequenceDiagram
  participant U as Browser
  participant API as API
  participant DB as PostgreSQL
  U->>API: POST /auth/login {email, password}
  API->>DB: buscar usuario + verificar hash
  alt ok
    API->>API: crear sesión
    API-->>U: 200 + Set-Cookie HttpOnly
  else credenciales inválidas
    API-->>U: 401
  end
  U->>API: GET /me (Cookie)
  API->>API: validar sesión
  API-->>U: 200 {id, rol}
```

### 3. Notas de seguridad (40 min)

Lista bajo el diagrama: password hasheado (nunca en logs), rate limit futuro, no revelar “email no existe” vs “password mal” si tu amenaza lo pide (o documenta el trade-off UX).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/secuencia-auth.md
git commit -m "docs(m13): secuencia autenticacion y sesion"
```
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="Secuencia: crear cita (P2)",
        horas=5.0,
        semana=2,
        lectura="Secuencia crear cita con auth + reglas; cierre P2 UML",
        evidencia="diagramas/secuencia-crear-cita.md + clases.md (P2)",
        _lectura_corta="Secuencia crítica crear cita; authz en API",
        _hecho="""1. `secuencia-crear-cita.md` incluye validación de sesión/rol, reglas de dominio e INSERT.
2. P2 completo: `clases.md` + al menos una secuencia crítica en `diagramas/`.
3. Commit `docs(m13): secuencia crear cita y cierre P2`.""",
        _errores="""- API inserta sin chequear sesión.
- Conflicto de horario ausente en la secuencia.
- Marcar P2 sin archivo de secuencia en git.""",
        siguiente="[L09 — Arquitectura en capas](L09-arquitectura-en-capas.md)",
        body=r"""
# L08 — Secuencia: crear cita (P2)

**~5.0 h · Semana 2**

P2 pide clases + secuencia crítica. Hoy cierras con el corazón del piloto: **crear cita**.

## Objetivo

`diagramas/secuencia-crear-cita.md` alineada a UC-03 y a los errores de L03.

## Pasos (hazlos en orden)

### 1. Borrador Mermaid (80–100 min)

```mermaid
sequenceDiagram
  participant U as Browser
  participant API as API
  participant S as CitaService
  participant DB as PostgreSQL
  U->>API: POST /citas (Cookie + JSON)
  API->>API: sesión + rol
  alt sin sesión
    API-->>U: 401
  end
  API->>S: crearCita(dto, userId)
  S->>S: validar rango horario
  S->>DB: ¿slot libre?
  alt conflicto
    S-->>API: Conflict
    API-->>U: 409
  else ok
    S->>DB: INSERT cita
    S-->>API: Cita
    API-->>U: 201 + JSON
  end
```

### 2. Alinea con clases y casos (40–50 min)

- Nombres de métodos ≈ lo que pondrás en M14/M17 (`CitaService`).
- Actualiza `casos-de-uso.md` si descubriste un alterno nuevo.

### 3. Checklist P2 (20 min)

- [ ] `diagramas/clases.md`
- [ ] `diagramas/secuencia-*.md` (≥1 crítica)

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas
git commit -m "docs(m13): secuencia crear cita y cierre P2"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="Arquitectura en capas",
        horas=5.0,
        semana=3,
        lectura="Capas HTTP → application → domain → infrastructure",
        evidencia="projects/m13-diseno/arquitectura.md (capas + responsabilidades)",
        _lectura_corta="Arquitectura en capas; dónde viven reglas vs I/O",
        _hecho="""1. `arquitectura.md` describe ≥4 capas con responsabilidad y ejemplo de archivo futuro.
2. Queda explícito que autorización/reglas de cita no viven solo en React.
3. Commit `docs(m13): arquitectura en capas Agenda Ops`.""",
        _errores="""- “Arquitectura” = lista de librerías sin fronteras.
- Domain que importa SQL o Express.
- Capas de adorno (8 capas para un CRUD).""",
        siguiente="[L10 — DTOs, validación y frontera HTTP](L10-dtos-validacion-y-frontera-http.md)",
        body=r"""
# L09 — Arquitectura en capas

**~5.0 h · Semana 3**

El monolito modular de ADR 001 necesita fronteras internas. Hoy las escribes.

## Objetivo

`projects/m13-diseno/arquitectura.md` con capas que M14/M17 puedan respetar.

## Pasos (hazlos en orden)

### 1. Define capas (60–70 min)

```text
HTTP (controllers/routes)
  → Application (services / use cases)
    → Domain (reglas: solape, estados)
      → Infrastructure (Postgres, mail, reloj)
```

Tabla:

| Capa | Puede | No puede |
|------|-------|----------|
| HTTP | parsear DTO, status codes | reglas de solape |
| Application | orquestar | SQL crudo (mejor vía repo) |
| Domain | invariantes | conocer Express |
| Infra | SQL, SMTP | decidir autorización de negocio a solas |

### 2. Mapa de carpetas previstas (40–50 min)

```text
src/
  http/
  application/
  domain/
  infrastructure/
```

Enlaza a módulos: `citas`, `clientes`, `auth`.

### 3. Dibuja dependencias (40 min)

Mermaid `flowchart TB` de capas; flechas solo hacia abajo (o inward).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/arquitectura.md
git commit -m "docs(m13): arquitectura en capas Agenda Ops"
```
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="DTOs, validación y frontera HTTP",
        horas=5.0,
        semana=3,
        lectura="DTO vs entidad; validación de entrada en frontera",
        evidencia="arquitectura.md sección DTOs + ejemplo CreateCitaDto",
        _lectura_corta="DTOs de entrada/salida; validar en HTTP antes del dominio",
        _hecho="""1. Documentas al menos `CreateCitaDto` / respuesta con campos y validaciones (tipos, rangos).
2. Dejas claro: entidad de dominio ≠ JSON crudo del request.
3. Commit `docs(m13): DTOs y validacion en frontera HTTP`.""",
        _errores="""- Aceptar el body entero y pasarlo al INSERT.
- Validar solo en el front.
- Mezclar campos internos (`passwordHash`) en DTO de respuesta.""",
        siguiente="[L11 — Componentes y despliegue (C4 ligero)](L11-componentes-y-despliegue-c4-ligero.md)",
        body=r"""
# L10 — DTOs, validación y frontera HTTP

**~5.0 h · Semana 3**

La frontera HTTP es el primer filtro: basura in → 400. El dominio recibe datos ya saneados.

## Objetivo

Ampliar `arquitectura.md` (o `diagramas/dtos.md`) con contratos de entrada/salida del piloto.

## Pasos (hazlos en orden)

### 1. Inventario de endpoints que ya prevés (30 min)

De L02/L08: `POST /auth/login`, `POST /citas`, `GET /citas`, `POST /clientes`, …

### 2. Especifica CreateCitaDto (60–70 min)

```ts
// contrato documental (aún sin código M17)
type CreateCitaDto = {
  clienteId: string;   // uuid
  servicioId: string;
  inicio: string;      // ISO-8601
};
// fin se calcula con duracionMin del servicio (o viene explícito — decide y documenta)
```

Validaciones: uuid formato, `inicio` futuro (o ≥ ahora−slack), servicio existe.

### 3. Respuesta pública (40 min)

Lista campos del 201: `id`, `inicio`, `fin`, `estado`, `clienteId` — **sin** datos de otros módulos sensibles.

### 4. Regla de oro (20 min)

Un párrafo: “El controller valida forma; el service/domain valida negocio (solape, rol).”

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): DTOs y validacion en frontera HTTP"
```
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Componentes y despliegue (C4 ligero)",
        horas=5.0,
        semana=3,
        lectura="C4 niveles 1–2; contenedores del piloto",
        evidencia="diagramas/c4-contenedores.md (contexto + contenedores)",
        _lectura_corta="C4 context/container para un monolito web + DB",
        _enlace_titulo="C4 model",
        _enlace="https://c4model.com/",
        _hecho="""1. Diagrama de contexto (persona + Agenda Ops + sistemas externos).
2. Diagrama de contenedores: Web, API, PostgreSQL (± email).
3. Commit `docs(m13): C4 ligero contexto y contenedores`.""",
        _errores="""- C4 con 25 microservicios inventados.
- Olvidar al design partner / usuario del negocio como persona.
- Mezclar nivel clases con nivel contenedores en un solo dibujo ilegible.""",
        siguiente="[L12 — Boundaries actualizados y amenazas](L12-boundaries-actualizados-y-amenazas.md)",
        body=r"""
# L11 — Componentes y despliegue (C4 ligero)

**~5.0 h · Semana 3**

Zoom out: no clases, sino cajas desplegables. Suficiente para M19 sin teatro enterprise.

## Objetivo

`diagramas/c4-contenedores.md` con contexto + contenedores del piloto.

## Pasos (hazlos en orden)

### 1. Contexto (40–50 min)

Personas: Owner/Staff. Sistema: Agenda Ops. Externos: Email o WhatsApp link, (luego) Stripe.

### 2. Contenedores (60–70 min)

```mermaid
flowchart LR
  Person[Staff/Owner] --> Web[Web app]
  Web --> API[API monolito]
  API --> DB[(PostgreSQL)]
  API --> Mail[Email provider]
```

Notas de deploy tentativas: un VPS o PaaS, un proceso Node, un Postgres (Docker ok en local).

### 3. Qué NO dibujas (20 min)

Sin service mesh, sin cola Kafka “por si acaso”. Si el SRS no lo pide, fuera.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/c4-contenedores.md
git commit -m "docs(m13): C4 ligero contexto y contenedores"
```
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="Boundaries actualizados y amenazas",
        horas=5.0,
        semana=3,
        lectura="Trust boundaries + amenazas alto nivel; cierre P3",
        evidencia="trust-boundaries.md actualizado (P3) + notas de amenaza",
        _lectura_corta="Amenazas en límites; IDOR, sesión, validación",
        _hecho="""1. `trust-boundaries.md` actualizado con capas/C4 y ≥3 amenazas con mitigación de diseño.
2. P3 cumplido: boundaries con límites y notas de amenaza.
3. Commit `docs(m13): boundaries actualizados y amenazas P3`.""",
        _errores="""- Lista OWASP Top 10 pegada sin relación a tus cajas.
- Mitigaciones solo “usaremos HTTPS” sin authz en API.
- P3 marcado con el archivo de L01 sin actualizar.""",
        siguiente="[L13 — Plantilla ADR y decisiones de diseño](L13-plantilla-adr-y-decisiones-de-diseno.md)",
        body=r"""
# L12 — Boundaries actualizados y amenazas

**~5.0 h · Semana 3**

Cierras P3: el diagrama de L01 ahora refleja capas, DTOs y contenedores reales.

## Objetivo

Actualizar `diagramas/trust-boundaries.md` y dejar P3 evidenciable.

## Pasos (hazlos en orden)

### 1. Relee L01 + arquitectura (30 min)

Marca desactualizaciones (¿apareció el mail? ¿sesión?).

### 2. Tabla de amenazas (70–90 min)

| Amenaza | Límite | Mitigación de diseño |
|---------|--------|----------------------|
| IDOR cita | API→DB | filtro por dueño/negocio en queries |
| Session hijack | Browser→API | Cookie Secure/HttpOnly; logout |
| Mass assignment | Browser→API | DTO allowlist |
| SQLi | API→DB | parametrized queries / ORM |

### 3. Checklist P3 (20 min)

Ficha: `trust-boundaries.md` con límites y notas de amenaza.

### 4. Bitácora semana 3 (30 min)

`bitacora-semana-3.md`: capas + amenaza que más te preocupa.

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): boundaries actualizados y amenazas P3"
```
""",
    )
)

# ---------- L13 ----------
LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="Plantilla ADR y decisiones de diseño",
        horas=5.0,
        semana=4,
        lectura="Plantilla ADR M01; índice de decisiones pendientes",
        evidencia="adr/README.md índice + plantilla reutilizable",
        _lectura_corta="ADR: contexto, decisión, consecuencias; índice vivo",
        _hecho="""1. `adr/README.md` lista ADR 001 y placeholders 002–004 con estado.
2. Existe `adr/PLANTILLA.md` (o equivalente) copiable.
3. Commit `docs(m13): indice ADR y plantilla`.""",
        _errores="""- ADRs de 3 líneas sin consecuencias.
- Decisiones en chats/Discord sin archivo.
- Índice que no enlaza archivos reales.""",
        siguiente="[L14 — ADR persistencia y modelo de datos](L14-adr-persistencia-y-modelo-de-datos.md)",
        body=r"""
# L13 — Plantilla ADR y decisiones de diseño

**~5.0 h · Semana 4**

Semana de decisiones. Hoy ordenas el proceso para no improvisar en M17.

## Objetivo

Índice de ADRs + plantilla; lista de decisiones que faltan (persistencia, auth, tenant).

## Pasos (hazlos en orden)

### 1. Plantilla (30–40 min)

`projects/m13-diseno/adr/PLANTILLA.md` con secciones Contexto / Decisión / Consecuencias / Alternativas rechazadas.

### 2. Índice (40–50 min)

`adr/README.md`:

| ADR | Título | Estado |
|-----|--------|--------|
| 001 | Monolito modular | Aceptado |
| 002 | Persistencia | Borrador L14 |
| 003 | Auth/sesión | Borrador L16 |
| 004 | Extensibilidad tenant | Nota L15 |

### 3. Backlog de decisiones (50–60 min)

Lista 5 preguntas abiertas (¿ORM?, ¿calcula fin el server?, ¿soft-delete citas?).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/adr
git commit -m "docs(m13): indice ADR y plantilla"
```
""",
    )
)

# ---------- L14 ----------
LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="ADR persistencia y modelo de datos",
        horas=5.0,
        semana=4,
        lectura="Elección Postgres + acceso a datos; modelo MVP",
        evidencia="adr/002-persistencia.md",
        _lectura_corta="Decisión de persistencia: Postgres, migraciones, acceso",
        _hecho="""1. ADR 002 elige Postgres (o justifica excepción) y cómo migrarás (SQL files / herramienta).
2. Alternativas rechazadas (p. ej. Mongo “porque JSON”) con motivo.
3. Commit `docs(m13): ADR 002 persistencia`.""",
        _errores="""- Elegir DB por moda sin relación al reporte de citas.
- “Usaremos un ORM” sin decir cuál ni migración.
- Contradecir cardinalidades de L06 sin actualizar clases.""",
        siguiente="[L15 — Extensibilidad tenant_id sin implementar](L15-extensibilidad-tenant-id-sin-implementar.md)",
        body=r"""
# L14 — ADR persistencia y modelo de datos

**~5.0 h · Semana 4**

Agenda Ops vive de consultas de agenda y FKs. Hoy firmas cómo persistir.

## Objetivo

`adr/002-persistencia.md` alineado a M09 y al diagrama de clases.

## Pasos (hazlos en orden)

### 1. Escribe el ADR (90–110 min)

```markdown
# ADR 002 — PostgreSQL + migraciones versionadas

## Contexto
Citas con rangos de tiempo, FKs, reportes simples, posible tenant_id luego.

## Decisión
PostgreSQL; migraciones SQL (o Prisma migrate — elige una) en repo.

## Consecuencias
+ Constraints e índices reales
+ Coincide con M09
− Ops de backups (M19)
```

Incluye acceso: Repository en infra (M14), no SQL en controllers.

### 2. Actualiza índice ADR (15 min)

### 3. Commit (15 min)

```bash
git add projects/m13-diseno/adr
git commit -m "docs(m13): ADR 002 persistencia"
```
""",
    )
)

# ---------- L15 ----------
LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="Extensibilidad tenant_id sin implementar",
        horas=5.0,
        semana=4,
        lectura="producto-saas.md multi-tenant; nota de extensibilidad",
        evidencia="adr/004-extensibilidad-tenant.md o seccion en arquitectura.md",
        _lectura_corta="Single-tenant ahora; dónde encajará tenant_id después",
        _enlace_titulo="Producto SaaS — evolución técnica",
        _enlace="../../../producto-saas.md",
        _hecho="""1. Documento que explica single-tenant del piloto y *dónde* se añadirá `tenant_id` (tablas/capas).
2. Lista explícita de lo que NO implementas aún (billing, onboarding multi-negocio).
3. Commit `docs(m13): nota extensibilidad tenant_id`.""",
        _errores="""- Implementar multi-tenant completo en diseño día 1.
- Ignorar tenant y luego reescribir todo el esquema.
- Poner tenant_id solo en el front.""",
        siguiente="[L16 — ADR auth y sesión](L16-adr-auth-y-sesion.md)",
        body=r"""
# L15 — Extensibilidad tenant_id sin implementar

**~5.0 h · Semana 4**

El camino a SaaS pide `tenant_id` después. Hoy dejas el gancho **sin** construir el edificio.

## Objetivo

Nota de extensibilidad legible por el yo-de-M17/M19.

## Pasos (hazlos en orden)

### 1. Lee producto-saas (25 min)

Sección evolución técnica: piloto single-tenant → tenants.

### 2. Escribe la nota (80–100 min)

`adr/004-extensibilidad-tenant.md`:

```markdown
# Nota — Extensibilidad multi-tenant

## Ahora (piloto)
Un negocio design partner. `negocioId` implícito o constante de config.

## Después
Columna `tenant_id` en clientes, servicios, citas, usuarios.
Queries siempre filtran por tenant. Tests IDOR cross-tenant en M15/M18.

## Qué no hacemos hoy
Stripe, onboarding self-serve, N esquemas Postgres.
```

### 3. Marca en clases.md (30 min)

Comentario: “candidato a tenant_id” en entidades de negocio.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): nota extensibilidad tenant_id"
```
""",
    )
)

# ---------- L16 ----------
LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="ADR auth y sesión",
        horas=5.0,
        semana=4,
        lectura="Sesión vs JWT; cookie HttpOnly; roles owner/staff",
        evidencia="adr/003-auth-sesion.md",
        _lectura_corta="Decisión de autenticación/sesión y roles del piloto",
        _hecho="""1. ADR 003 elige mecanismo (p. ej. cookie de sesión) con consecuencias.
2. Roles owner/staff y dónde se autorizan (API) quedan escritos.
3. Commit `docs(m13): ADR 003 auth y sesion`.""",
        _errores="""- JWT en localStorage “porque tutorial” sin amenazas.
- Roles solo en el front.
- ADR que contradice secuencia-auth sin actualizarla.""",
        siguiente="[L17 — Índice del paquete de diseño](L17-indice-del-paquete-de-diseno.md)",
        body=r"""
# L16 — ADR auth y sesión

**~5.0 h · Semana 4**

Cierras la decisión que L07 dibujó: cómo autenticamos el piloto.

## Objetivo

`adr/003-auth-sesion.md` coherente con `secuencia-auth.md` y boundaries.

## Pasos (hazlos en orden)

### 1. Alternativas (40 min)

Tabla: sesión servidor / JWT cookie / JWT bearer. Elige una para el piloto.

### 2. ADR (70–90 min)

Incluye: hash de passwords, expiración, logout, roles, rechazo de “rol en query string”.

### 3. Sincroniza diagrama (30 min)

Si cambió el mecanismo, actualiza `secuencia-auth.md`.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): ADR 003 auth y sesion"
```
""",
    )
)

# ---------- L17 ----------
LESSONS.append(
    dict(
        id="L17",
        orden=17,
        titulo="Índice del paquete de diseño",
        horas=5.0,
        semana=5,
        lectura="Empaquetar evidencias; README como mapa M17",
        evidencia="projects/m13-diseno/README.md índice enlazando SRS/diagramas/ADRs",
        _lectura_corta="README índice del paquete de diseño Agenda Ops",
        _hecho="""1. README M13 enlaza SRS, casos-de-uso, diagramas, arquitectura y ADRs.
2. Un extraño puede navegar el paquete en ≤10 minutos.
3. Commit `docs(m13): indice del paquete de diseno`.""",
        _errores="""- README genérico de la plantilla sin enlaces.
- Enlaces rotos a archivos que no existen.
- Diagramas huérfanos fuera del índice.""",
        siguiente="[L18 — Endpoints y módulos previstos M17](L18-endpoints-y-modulos-previstos-m17.md)",
        body=r"""
# L17 — Índice del paquete de diseño

**~5.0 h · Semana 5**

El proyecto de M13 es el paquete. Hoy el README se vuelve el mapa.

## Objetivo

Reescribir `projects/m13-diseno/README.md` como índice navegable.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

```bash
find projects/m13-diseno -type f -name '*.md' | sort
```

### 2. README índice (80–100 min)

Secciones: En resumen · Enlace SRS · Flujos · Diagramas · Arquitectura · ADRs · Checklist evidencias P1–P3 · Cómo empezar M17.

### 3. Rompe enlaces (20 min)

Haz clic mental: cada ruta relativa debe existir.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/README.md
git commit -m "docs(m13): indice del paquete de diseno"
```
""",
    )
)

# ---------- L18 ----------
LESSONS.append(
    dict(
        id="L18",
        orden=18,
        titulo="Endpoints y módulos previstos M17",
        horas=5.0,
        semana=5,
        lectura="Lista de rutas API y módulos de código previstos",
        evidencia="projects/m13-diseno/endpoints-m17.md",
        _lectura_corta="Contrato tentativo de API y módulos para el scaffold M17",
        _hecho="""1. `endpoints-m17.md` lista métodos/rutas Must con DTO/status resumidos.
2. Mapa módulo → carpeta (`auth`, `citas`, `clientes`).
3. Commit `docs(m13): endpoints y modulos previstos M17`.""",
        _errores="""- OpenAPI de 80 rutas para el MVP.
- Endpoints sin auth marcada.
- Módulos que no coinciden con arquitectura.md.""",
        siguiente="[L19 — Checklist listo para scaffold](L19-checklist-listo-para-scaffold.md)",
        body=r"""
# L18 — Endpoints y módulos previstos M17

**~5.0 h · Semana 5**

Puente explícito al scaffold: qué rutas y carpetas nacerán en M17.

## Objetivo

`endpoints-m17.md` breve y accionable.

## Pasos (hazlos en orden)

### 1. Tabla de endpoints (70–90 min)

| Método | Ruta | Auth | Éxito | Errores |
|--------|------|------|-------|---------|
| POST | /auth/login | no | 200 | 401 |
| POST | /citas | sí | 201 | 400/401/403/409 |
| GET | /citas | sí | 200 | 401 |
| … | … | … | … | … |

### 2. Módulos (40 min)

```text
auth/  clientes/  servicios/  citas/
```

Relación con capas de L09.

### 3. Enlaza desde README (20 min)

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): endpoints y modulos previstos M17"
```
""",
    )
)

# ---------- L19 ----------
LESSONS.append(
    dict(
        id="L19",
        orden=19,
        titulo="Checklist listo para scaffold",
        horas=5.0,
        semana=5,
        lectura="Checklist de salida hacia M17",
        evidencia="checklist-scaffold.md marcado con evidencia enlazada",
        _lectura_corta="Definition of Ready del paquete de diseño",
        _hecho="""1. `checklist-scaffold.md` con ítems marcados y enlaces a archivos del paquete.
2. Cero ítems Must en “TBD” sin justificación.
3. Commit `docs(m13): checklist listo para scaffold`.""",
        _errores="""- Checklist todo ✓ sin enlaces.
- Dejar P2/P3 incompletos y seguir igual.
- Incluir nice-to-have como bloqueantes.""",
        siguiente="[L20 — Cierre M13 — trazabilidad y dominio](L20-cierre-m13-trazabilidad-y-dominio.md)",
        body=r"""
# L19 — Checklist listo para scaffold

**~5.0 h · Semana 5**

Definition of Ready: si falta algo Must, hoy se arregla o se documenta el riesgo.

## Objetivo

`checklist-scaffold.md` que un yo futuro use el día 1 de M17.

## Pasos (hazlos en orden)

### 1. Escribe el checklist (60–70 min)

```markdown
# Checklist — listo para scaffold M17

- [ ] SRS enlazado
- [ ] casos-de-uso.md (P1)
- [ ] clases + secuencia (P2)
- [ ] trust-boundaries (P3)
- [ ] arquitectura.md + DTOs
- [ ] ADR 001–003
- [ ] endpoints-m17.md
- [ ] nota tenant_id
```

### 2. Marca con enlaces (50–60 min)

Cada ítem: ruta relativa al archivo.

### 3. Deuda consciente (30 min)

Sección “Aceptamos no tener X porque…”.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/checklist-scaffold.md
git commit -m "docs(m13): checklist listo para scaffold"
```
""",
    )
)

# ---------- L20 ----------
LESSONS.append(
    dict(
        id="L20",
        orden=20,
        titulo="Cierre M13 — trazabilidad y dominio",
        horas=5.0,
        semana=5,
        lectura="Criterios de dominio ficha M13; trazabilidad SRS↔diagramas",
        evidencia="trazabilidad.md + README final; criterios de dominio autoevaluados",
        _lectura_corta="Trazabilidad requisito→diseño; autoevaluación criterios de dominio",
        _hecho="""1. `trazabilidad.md` mapea historias Must → UC → diagramas/ADRs.
2. Autoevaluación de criterios de dominio en bitácora o README (honesta).
3. Commit `docs(m13): cierre trazabilidad y criterios de dominio`.""",
        _errores="""- Diagramas sin fila en la matriz de trazabilidad.
- Autoevaluación todo ✓ sin evidencia.
- Microservicios reintroducidos en el cierre.""",
        siguiente="Materia siguiente: [M14 — Patrones](../M14-patrones.md) · L01 en `../M14/`.",
        body=r"""
# L20 — Cierre M13 — trazabilidad y dominio

**~5.0 h · Semana 5**

Cierras la materia demostrando que cada diagrama sirve a un requisito — y que puedes defender el monolito modular.

## Objetivo

Matriz de trazabilidad + autoevaluación de criterios de dominio de la ficha.

## Pasos (hazlos en orden)

### 1. Matriz (70–90 min)

`trazabilidad.md`:

| Historia SRS | UC | Diagrama / ADR |
|--------------|----|----------------|
| H-cita-01 | UC-03 | secuencia-crear-cita, ADR 002 |

Borra artefactos huérfanos o enlázalos.

### 2. Criterios de dominio (40–50 min)

De la ficha M13 — responde en `bitacora-cierre.md`:

- ¿Defiendes monolito modular con trade-offs?
- ¿Sabes dónde se valida el rol?
- ¿Un compañero puede empezar M17 con SRS + este paquete?

### 3. Pulido README (30 min)

Estado: “Paquete listo para M17” + fecha.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): cierre trazabilidad y criterios de dominio"
```
""",
    )
)
