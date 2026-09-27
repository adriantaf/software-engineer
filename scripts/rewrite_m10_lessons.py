#!/usr/bin/env python3
"""Rewrite M10 lessons to M01/M09 quality (concrete timed steps, no boilerplate)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "curriculum/etapas/02-disciplinaria/M10"
BIBLIO = "../../../bibliografia.md#m10-redes"
TANENBAUM = "*Redes de computadoras* — Tanenbaum & Wetherall (ed. ES)"
MDN_HTTP = "https://developer.mozilla.org/es/docs/Web/HTTP"
MDN_OVERVIEW = "https://developer.mozilla.org/es/docs/Web/HTTP/Overview"


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


def lectura_block(que, enlace_titulo="MDN HTTP", enlace=MDN_HTTP):
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {TANENBAUM} | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10]({BIBLIO}) |
"""


def render(lesson: dict) -> str:
    pub = {
        "id": lesson["id"],
        "materia": "M10",
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
    1: "L01-modelo-de-capas-y-primer-curl.md",
    2: "L02-ip-direccionamiento-y-enrutamiento-intro.md",
    3: "L03-tcp-vs-udp-y-puertos-bien-usados.md",
    4: "L04-cierre-semana-1-bitacora-p1.md",
    5: "L05-dns-resolucion-registros-y-fallos.md",
    6: "L06-http-mensajes-metodos-y-semantica.md",
    7: "L07-status-codes-y-cabeceras-de-respuesta.md",
    8: "L08-http-2-intuicion-y-curl-avanzado.md",
    9: "L09-tls-handshake-y-que-protege-en-transito.md",
    10: "L10-certificados-x-509-y-cadena-de-confianza.md",
    11: "L11-lab-openssl-y-pinning-conceptual.md",
    12: "L12-mitm-conceptual-y-amenazas-de-enlace.md",
    13: "L13-cookies-atributos-y-modelo-de-almacenamiento.md",
    14: "L14-sesiones-tokens-y-estado-en-apis.md",
    15: "L15-cors-preflight-y-errores-tipicos.md",
    16: "L16-cabeceras-de-seguridad-http.md",
    17: "L17-superficie-de-ataque-endpoints-y-datos.md",
    18: "L18-cliente-y-servidor-tcp-minimo-p2.md",
    19: "L19-documento-de-amenazas-de-red-del-producto.md",
    20: "L20-cierre-m10-evidencias-y-dominio.md",
}

LESSONS = []

# ---------- L01 ----------
LESSONS.append(
    dict(
        id="L01",
        orden=1,
        titulo="Modelo de capas y primer curl",
        horas=5.0,
        semana=1,
        lectura="Tanenbaum: intro + capas (modelo OSI/TCP simplificado)",
        evidencia="projects/m10-redes/labs/dia1.md + curl -v log",
        _lectura_corta="Intro + encapsulación; mapa de 5 capas hacia HTTP",
        _enlace={"enlace_titulo": "MDN · Overview of HTTP", "enlace": MDN_OVERVIEW},
        _hecho="""1. `projects/m10-redes/labs/dia1.md` con diagrama ASCII de 5 capas y qué ve `curl -v`.
2. Log `labs/curl-example.log` (o fragmento anotado) con líneas de DNS/TCP/TLS/HTTP resaltadas.
3. Commit `docs(m10): l01 capas y primer curl`.""",
        _errores="""- Pegar 200 líneas de curl sin marcar qué capa es cada bloque.
- Decir “HTTPS = la app ya es segura” (XSS/IDOR siguen vivos).
- Confundir TLS con cifrado en reposo de la BD.""",
        siguiente="[L02 — IP, direccionamiento y enrutamiento intro](L02-ip-direccionamiento-y-enrutamiento-intro.md)",
        body=r"""
# L01 — Modelo de capas y primer curl

**~5.0 h · Semana 1**

Sin mapa de capas, cada error de red se vuelve “el Wi‑Fi está mal”. Hoy fijas el diagrama mental que usarás hasta M18.

## Objetivo

Dejar `projects/m10-redes/` con un lab día 1: modelo de 5 capas + evidencia de `curl -v` sobre HTTPS.

## Pasos (hazlos en orden)

### 1. Revisa el scaffold (15 min)

```bash
ls projects/m10-redes
cat projects/m10-redes/README.md
mkdir -p projects/m10-redes/{labs,tcp-echo,superficie,samples}
```

No borres la estructura; amplíala.

### 2. Modelo de 5 capas (45–60 min)

En `projects/m10-redes/labs/dia1.md` dibuja ASCII (o Mermaid) con:

1. Aplicación (HTTP)
2. Transporte (TCP/UDP + puerto)
3. Red (IP)
4. Enlace
5. Física (una línea)

Anota **encapsulación**: header de cada capa envuelve el payload de arriba.

### 3. Primer `curl -v` (60–75 min)

```bash
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/labs/curl-example.log
```

En `dia1.md`, tabla de 4 filas: línea del log → capa → qué significa. Compara también:

```bash
curl -v http://example.com -o /dev/null 2>&1 | head -40
```

¿Hay redirección a HTTPS? Anótalo.

### 4. Agenda Ops (20 min)

Párrafo: cuando el panel de Agenda Ops llame a `https://api…/citas`, ¿qué capas deben funcionar antes de que el JSON exista?

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l01 capas y primer curl"
```
""",
    )
)

# ---------- L02 ----------
LESSONS.append(
    dict(
        id="L02",
        orden=2,
        titulo="IP, direccionamiento y enrutamiento intro",
        horas=5.0,
        semana=1,
        lectura="Tanenbaum: capa de red — IPv4, máscaras, routing básico",
        evidencia="labs/semana-01.md: IP local, gateway, traceroute resumido",
        _lectura_corta="IPv4, máscara/CIDR, gateway, hop-by-hop",
        _enlace={"enlace_titulo": "MDN · HTTP (contexto app)", "enlace": MDN_HTTP},
        _hecho="""1. `labs/semana-01.md` con IP local, máscara/CIDR, gateway y 3–5 hops de traceroute (o `tracepath`/`mtr`).
2. Explicas en 5 líneas qué problema resuelve IP vs qué resuelve TCP.
3. Commit `docs(m10): l02 ip y enrutamiento`.""",
        _errores="""- Confundir IP privada (`10.`, `192.168.`) con “no hay internet”.
- Pegar traceroute completo sin interpretar timeouts.
- Olvidar que el API de Agenda Ops tendrá IP pública *y* ruta interna en compose.""",
        siguiente="[L03 — TCP vs UDP y puertos bien usados](L03-tcp-vs-udp-y-puertos-bien-usados.md)",
        body=r"""
# L02 — IP, direccionamiento y enrutamiento intro

**~5.0 h · Semana 1**

HTTP no “viaja solo”: alguien elige el siguiente hop. Hoy lees tu propia mesa de enrutamiento.

## Objetivo

Documentar dirección local, gateway y un traceroute resumido hacia un host público.

## Pasos

### 1. Inventario de interfaces (40 min)

```bash
ip -br addr
ip route
```

En `projects/m10-redes/labs/semana-01.md` anota: interfaz, IPv4/CIDR, default gateway. Si usas macOS: `ifconfig` + `netstat -rn`.

### 2. Lectura dirigida (45 min)

Tanenbaum (capa de red): qué es una máscara, por qué existe NAT en casa, diferencia host vs red. Escribe 6 viñetas propias — no copies el libro.

### 3. Traceroute (60–75 min)

```bash
# Linux:
traceroute -n example.com | head -20
# o
tracepath example.com | head -20
```

Tabla: hop | RTT aprox | nota (timeout / ISP / destino). Relaciona “salto” con “router que decide”.

### 4. Hipótesis Agenda Ops (25 min)

Si el panel no alcanza la API: ¿fallo DNS, IP inalcanzable, o app? Criterio de triage en 4 bullets.

### 5. Commit (15 min)

```bash
git add projects/m10-redes/labs/semana-01.md
git commit -m "docs(m10): l02 ip y enrutamiento"
```
""",
    )
)

# ---------- L03 ----------
LESSONS.append(
    dict(
        id="L03",
        orden=3,
        titulo="TCP vs UDP y puertos bien usados",
        horas=5.0,
        semana=1,
        lectura="Tanenbaum: capa de transporte — TCP, UDP, puertos",
        evidencia="semana-01.md: tabla protocolo/puerto/ejemplo Agenda Ops",
        _lectura_corta="TCP fiable vs UDP; sockets (IP:puerto); puertos bien conocidos",
        _hecho="""1. Tabla en `semana-01.md`: ≥6 filas protocolo/puerto/uso (incl. 443, 80, 53, 5432, 3000).
2. `ss -tuln` (o `netstat`) capturado y explicado: qué escucha en tu máquina.
3. Commit `docs(m10): l03 tcp udp puertos`.""",
        _errores="""- Decir “UDP es inseguro / TCP es seguro” (seguridad ≠ capa de transporte).
- Publicar Postgres `5432` al mundo “solo en local” y olvidarlo.
- Confundir puerto de contenedor con puerto del host.""",
        siguiente="[L04 — Cierre semana 1 — bitácora P1](L04-cierre-semana-1-bitacora-p1.md)",
        body=r"""
# L03 — TCP vs UDP y puertos bien usados

**~5.0 h · Semana 1**

Agenda Ops hablará HTTP sobre TCP/443. DNS suele ir por UDP/53. Hoy dejas la tabla que evita confusiones en M11/M19.

## Objetivo

Contrastar TCP vs UDP y mapear puertos al stack del producto.

## Pasos

### 1. Conceptos en 10 líneas (40 min)

En `semana-01.md`: handshake/estado vs datagrama; qué significa “puerto”; diferencia cliente efímero vs servidor bien conocido.

### 2. Escucha local (45 min)

```bash
ss -tuln | head -40
# alternativa: netstat -tuln
```

Marca 3 sockets que reconozcas (ssh, docker, node, postgres…). Si no hay nada interesante, arranca algo de M09 y vuelve a listar.

### 3. Tabla Agenda Ops (60 min)

| Protocolo | Puerto | Quién | Notas |
|-----------|--------|-------|-------|
| TCP | 443 | API/HTTPS | tránsito cifrado |
| TCP | 80 | redirect | idealmente solo → 443 |
| UDP/TCP | 53 | DNS | fallo = “no resuelve” |
| TCP | 5432 | Postgres | **no** exponer a 0.0.0.0 en prod |
| TCP | 3000 | API dev | solo localhost o red compose |

Añade una fila más (Redis, mail, etc. si aplica).

### 4. Experimento mental tcpdump (30 min)

Sin capturar tráfico ajeno: escribe qué *verías* en un `tcpdump port 443` conceptual (SYN, TLS ClientHello, Application Data). Guarda en la bitácora — el lab real de captura queda para tu máquina con permiso.

### 5. Commit (15 min)

```bash
git add projects/m10-redes/labs/semana-01.md
git commit -m "docs(m10): l03 tcp udp puertos"
```
""",
    )
)

# ---------- L04 ----------
LESSONS.append(
    dict(
        id="L04",
        orden=4,
        titulo="Cierre semana 1 — bitácora P1",
        horas=5.0,
        semana=1,
        lectura="Repaso semana 1 Tanenbaum + ficha M10",
        evidencia="projects/m10-redes/labs/semana-01.md consolidado (P1)",
        _lectura_corta="Síntesis capas + IP + transporte; checklist P1 parcial",
        _hecho="""1. `labs/semana-01.md` unifica L01–L03 con índice y enlaces a logs.
2. README de m10 marca “Semana 1 / P1 parcial” con checklist.
3. Commit `docs(m10): l04 cierre semana 1 bitacora`.""",
        _errores="""- Tres archivos sueltos sin índice.
- Checklist vacía (“luego documento”).
- Commit sin `labs/`.""",
        siguiente="[L05 — DNS: resolución, registros y fallos](L05-dns-resolucion-registros-y-fallos.md)",
        body=r"""
# L04 — Cierre semana 1 — bitácora P1

**~5.0 h · Semana 1**

P1 es bitácora reproducible. Hoy la dejas legible para tu yo de la semana 5.

## Objetivo

Consolidar evidencia de capas/IP/TCP y actualizar el README del proyecto.

## Pasos

### 1. Auditoría de archivos (30 min)

```bash
find projects/m10-redes -type f | sort
```

Mueve notas sueltas a `labs/` si hace falta.

### 2. Consolida `semana-01.md` (90–120 min)

Estructura mínima:

```markdown
# Semana 1 — Capas, IP, TCP/UDP
## Índice
## Capas + curl (L01)
## IP / ruta (L02)
## Puertos Agenda Ops (L03)
## Pendientes
```

Copia fragmentos **anotados** (no dumps enteros).

### 3. README (45 min)

En `projects/m10-redes/README.md`, sección “Semana 1”:

- [x] dia1 + curl log
- [x] IP/gateway/traceroute
- [x] tabla puertos

### 4. Auto-quiz (30 min)

Responde por escrito (5–8 líneas c/u): (a) qué protege TLS vs qué no; (b) por qué 5432 no va a internet; (c) triage timeout.

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l04 cierre semana 1 bitacora"
```
""",
    )
)

# ---------- L05 ----------
LESSONS.append(
    dict(
        id="L05",
        orden=5,
        titulo="DNS: resolución, registros y fallos",
        horas=5.0,
        semana=2,
        lectura="Tanenbaum DNS + MDN DNS overview",
        evidencia="labs/semana-02-dns.md con dig/host",
        _lectura_corta="Resolución recursiva, A/AAAA/CNAME/MX/TXT, TTL y fallos típicos",
        _enlace={
            "enlace_titulo": "MDN · DNS (concepto)",
            "enlace": "https://developer.mozilla.org/es/docs/Glossary/DNS",
        },
        _hecho="""1. `labs/semana-02-dns.md` con salida anotada de `dig`/`host` (A/AAAA/CNAME al menos).
2. Escenario escrito: “DNS falla pero ping a IP funciona” — cómo lo detectas.
3. Commit `docs(m10): l05 dns dig`.""",
        _errores="""- Confundir “no resuelve” con “el servidor HTTP está caído”.
- Ignorar TTL cuando “ya cambié el DNS y no veo el cambio”.
- Pegar dig sin decir qué registro buscabas.""",
        siguiente="[L06 — HTTP mensajes, métodos y semántica](L06-http-mensajes-metodos-y-semantica.md)",
        body=r"""
# L05 — DNS: resolución, registros y fallos

**~5.0 h · Semana 2**

Antes de TCP hay un nombre. Si DNS miente o tarda, Agenda Ops “no carga” aunque la API esté viva.

## Objetivo

Usar `dig`/`host` y documentar registros y modos de fallo.

## Pasos

### 1. Herramientas (20 min)

```bash
which dig host getent || true
dig -v 2>&1 | head -1
```

Si no hay `dig`: `sudo apt install dnsutils` (o equivalente).

### 2. Labs de registros (75–90 min)

```bash
dig example.com A +noall +answer
dig example.com AAAA +short
dig www.github.com CNAME +short
host -a example.com | head -30
```

En `projects/m10-redes/labs/semana-02-dns.md`: qué es A vs CNAME; qué harías con un TXT de verificación.

### 3. Fallos (45 min)

Escribe tres síntomas y la primera prueba:

1. NXDOMAIN
2. SERVFAIL / timeout al resolver
3. Respuesta correcta pero IP bloqueada/firewall

Comando de contraste:

```bash
getent hosts example.com
ping -c 1 $(dig +short example.com A | head -1)
```

### 4. Producto (25 min)

Cuando publiques `api.tu-dominio`, lista registros mínimos (A/AAAA o CNAME) y por qué el panel y la API pueden ser hosts distintos.

### 5. Commit (15 min)

```bash
git add projects/m10-redes/labs/semana-02-dns.md
git commit -m "docs(m10): l05 dns dig"
```
""",
    )
)

# ---------- L06 ----------
LESSONS.append(
    dict(
        id="L06",
        orden=6,
        titulo="HTTP mensajes, métodos y semántica",
        horas=5.0,
        semana=2,
        lectura="MDN HTTP methods + Tanenbaum capa aplicación",
        evidencia="labs/http-metodos.md",
        _lectura_corta="Request-line, headers, body; GET/POST/PUT/PATCH/DELETE e idempotencia",
        _enlace={
            "enlace_titulo": "MDN · Métodos HTTP",
            "enlace": "https://developer.mozilla.org/es/docs/Web/HTTP/Methods",
        },
        _hecho="""1. `labs/http-metodos.md` con tabla método → semántica → ejemplo Agenda Ops (`/citas`, `/clientes`).
2. Al menos dos capturas `curl -v` (GET y POST de ejemplo a httpbin o similar).
3. Commit `docs(m10): l06 http metodos`.""",
        _errores="""- Usar GET con body para “crear cita”.
- Confundir PUT y PATCH.
- Llamar “REST” a cualquier JSON sin mirar semántica del método.""",
        siguiente="[L07 — Status codes y cabeceras de respuesta](L07-status-codes-y-cabeceras-de-respuesta.md)",
        body=r"""
# L06 — HTTP mensajes, métodos y semántica

**~5.0 h · Semana 2**

La API de Agenda Ops será una conversación de mensajes. Hoy fijas métodos e idempotencia.

## Objetivo

Documentar la anatomía de un mensaje HTTP y mapear métodos al dominio de citas.

## Pasos

### 1. Anatomía (40 min)

En `labs/http-metodos.md` dibuja request y response: start-line, headers, body vacío vs JSON.

### 2. Labs curl (75 min)

```bash
curl -v https://httpbin.org/get
curl -v -X POST https://httpbin.org/post \
  -H 'Content-Type: application/json' \
  -d '{"cliente":"Ana","servicio":"corte"}'
```

Guarda fragmentos en `samples/` (sin tokens). Anota `Host`, `User-Agent`, `Content-Type`.

### 3. Mapa Agenda Ops (60 min)

| Método | Recurso (borrador) | Idempotente? | Notas |
|--------|-------------------|--------------|-------|
| GET | `/api/citas?fecha=` | sí | listar |
| POST | `/api/citas` | no | crear |
| PATCH | `/api/citas/:id` | sí* | remarcar |
| DELETE | `/api/citas/:id` | sí | cancelar |

\*Documenta tu interpretación.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/http-metodos.md projects/m10-redes/samples
git commit -m "docs(m10): l06 http metodos"
```
""",
    )
)

# ---------- L07 ----------
LESSONS.append(
    dict(
        id="L07",
        orden=7,
        titulo="Status codes y cabeceras de respuesta",
        horas=5.0,
        semana=2,
        lectura="MDN HTTP response status + cabeceras selectas",
        evidencia="labs/status-codes.md",
        _lectura_corta="Clases 2xx/3xx/4xx/5xx; Cache-Control, Content-Type, Location",
        _enlace={
            "enlace_titulo": "MDN · Códigos de estado",
            "enlace": "https://developer.mozilla.org/es/docs/Web/HTTP/Status",
        },
        _hecho="""1. `labs/status-codes.md` con ≥8 códigos y cuándo los usaría Agenda Ops (401/403/404/409/422/429…).
2. Labs `curl -sI` anotando status + 3 cabeceras relevantes.
3. Commit `docs(m10): l07 status codes`.""",
        _errores="""- Devolver 200 con `{error:…}` en el body y llamarlo API.
- Confundir 401 (no autenticado) con 403 (no autorizado).
- Usar 500 para validación de input del cliente.""",
        siguiente="[L08 — HTTP/2 intuición y curl avanzado](L08-http-2-intuicion-y-curl-avanzado.md)",
        body=r"""
# L07 — Status codes y cabeceras de respuesta

**~5.0 h · Semana 2**

El cliente (y tú en soporte) leen el status antes que el JSON. Hoy eliges códigos con criterio.

## Objetivo

Tabla de status para Agenda Ops + inspección de cabeceras con `curl -sI`.

## Pasos

### 1. Inventario de códigos (60 min)

En `labs/status-codes.md` documenta al menos: 200, 201, 204, 301/302, 400, 401, 403, 404, 409, 422, 429, 500, 502/503. Una frase de cuándo aplica a citas/clientes.

### 2. Labs cabeceras (60 min)

```bash
curl -sI https://example.com | tee projects/m10-redes/samples/headers-example.txt
curl -sI https://httpbin.org/status/404
curl -sI https://httpbin.org/status/301
```

Marca `Content-Type`, `Location`, `Cache-Control` / `Age` si aparecen.

### 3. Matriz producto (45 min)

Escenarios: cita duplicada en mismo slot → ¿409?; token ausente → 401; staff sin permiso a notas privadas → 403; validación de horario → 422.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/status-codes.md projects/m10-redes/samples
git commit -m "docs(m10): l07 status codes"
```
""",
    )
)

# ---------- L08 ----------
LESSONS.append(
    dict(
        id="L08",
        orden=8,
        titulo="HTTP/2 intuición y curl avanzado",
        horas=5.0,
        semana=2,
        lectura="MDN HTTP/2 + notas Tanenbaum aplicación",
        evidencia="labs/curl-avanzado.md",
        _lectura_corta="Multiplexión HTTP/2; curl -w timings; --http1.1 vs --http2",
        _enlace={
            "enlace_titulo": "MDN · HTTP/2",
            "enlace": "https://developer.mozilla.org/es/docs/Glossary/HTTP_2",
        },
        _hecho="""1. `labs/curl-avanzado.md` con timings (`curl -w`) y comparación HTTP/1.1 vs HTTP/2 si el servidor lo ofrece.
2. Semana 2 consolidada en README (DNS + HTTP).
3. Commit `docs(m10): l08 curl avanzado`.""",
        _errores="""- Asumir que HTTP/2 “cifra” (sigue necesitando TLS en la práctica web).
- Optimizar micro-timings sin hipótesis.
- Olvidar `-o /dev/null` y llenar el repo de HTML.""",
        siguiente="[L09 — TLS: handshake y qué protege en tránsito](L09-tls-handshake-y-que-protege-en-transito.md)",
        body=r"""
# L08 — HTTP/2 intuición y curl avanzado

**~5.0 h · Semana 2**

Mides antes de opinar. Hoy `curl` deja de ser solo `-v`.

## Objetivo

Documentar timings y, si aplica, que el servidor habla HTTP/2.

## Pasos

### 1. Formato de timing (45 min)

```bash
curl -o /dev/null -s -w 'dns:%{time_namelookup} connect:%{time_connect} tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total} code:%{http_code}\n' \
  https://example.com
```

Copia 3 corridas a `labs/curl-avanzado.md` e interpreta cada campo.

### 2. HTTP versión (45 min)

```bash
curl --http1.1 -sI https://example.com | head -5
curl --http2 -sI https://example.com | head -5
```

¿Aparece `HTTP/2`? Anota. Si no, documenta el límite del servidor — no inventes.

### 3. Flags útiles (40 min)

Practica y anota: `-H`, `-d`, `-X`, `-L` (follow redirect), `--fail-with-body` (si tu curl lo tiene), `-A` User-Agent.

### 4. Cierre semana 2 (40 min)

Índice en README: L05–L08 hechos. Checklist P1 sigue abierta hasta TLS.

### 5. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l08 curl avanzado"
```
""",
    )
)

# ---------- L09 ----------
LESSONS.append(
    dict(
        id="L09",
        orden=9,
        titulo="TLS: handshake y qué protege en tránsito",
        horas=5.0,
        semana=3,
        lectura="Tanenbaum seguridad/TLS selecto + MDN TLS",
        evidencia="labs/tls-handshake.md",
        _lectura_corta="Handshake TLS; confidencialidad e integridad en tránsito; qué NO cubre",
        _enlace={
            "enlace_titulo": "MDN · TLS",
            "enlace": "https://developer.mozilla.org/es/docs/Glossary/TLS",
        },
        _hecho="""1. `labs/tls-handshake.md` explica handshake en lenguaje ingeniero + captura `curl -v` con líneas TLS.
2. Lista explícita: 3 cosas que TLS protege y 3 que **no** (XSS, IDOR, BD robada…).
3. Commit `docs(m10): l09 tls handshake`.""",
        _errores="""- “HTTPS = seguro contra todo”.
- Pensar que el body JSON ya no necesita authz.
- Confundir certificado inválido con “firewall”.""",
        siguiente="[L10 — Certificados X.509 y cadena de confianza](L10-certificados-x-509-y-cadena-de-confianza.md)",
        body=r"""
# L09 — TLS: handshake y qué protege en tránsito

**~5.0 h · Semana 3**

Sin TLS, cookies de sesión de Agenda Ops viajan en claro. Con TLS mal entendido, crees que ya terminaste AppSec.

## Objetivo

Describir el handshake y delimitar el alcance de protección en tránsito.

## Pasos

### 1. Lectura + esquema (60 min)

En `labs/tls-handshake.md`: ClientHello → ServerHello/cert → claves → Application Data. Una figura ASCII basta.

### 2. Ver en curl (45 min)

```bash
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/samples/tls-curl.txt
```

Resalta: ALPN, versión TLS, “SSL certificate verify ok” (o error).

### 3. Alcance (45 min)

Tabla “protege / no protege” con ejemplos del producto (eavesdropping en café Wi‑Fi vs XSS en el panel).

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/tls-handshake.md projects/m10-redes/samples
git commit -m "docs(m10): l09 tls handshake"
```
""",
    )
)

# ---------- L10 ----------
LESSONS.append(
    dict(
        id="L10",
        orden=10,
        titulo="Certificados X.509 y cadena de confianza",
        horas=5.0,
        semana=3,
        lectura="Tanenbaum PKI intro + MDN certificados",
        evidencia="labs/certificados.md",
        _lectura_corta="X.509, CA intermedia, leaf, validez y CN/SAN",
        _hecho="""1. `labs/certificados.md` con cadena leaf→intermedia→root explicada para un sitio real.
2. Salida `openssl s_client` o `curl -v` anotando fechas y SAN.
3. Commit `docs(m10): l10 certificados x509`.""",
        _errores="""- Confiar en un cert autofirmado en prod “porque es mío”.
- Ignorar SAN y mirar solo CN legacy.
- Subir claves privadas al repo.""",
        siguiente="[L11 — Lab openssl y pinning conceptual](L11-lab-openssl-y-pinning-conceptual.md)",
        body=r"""
# L10 — Certificados X.509 y cadena de confianza

**~5.0 h · Semana 3**

El navegador no “confía en example.com”: confía en una CA que firmó un leaf con SAN correcto.

## Objetivo

Inspeccionar un certificado real y explicar la cadena.

## Pasos

### 1. openssl s_client (60–75 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
```

Pega resultado anotado en `labs/certificados.md`.

### 2. Cadena (45 min)

```bash
echo | openssl s_client -connect example.com:443 -showcerts 2>/dev/null | head -80
```

Diagrama: leaf → intermediate → root del almacén local.

### 3. Fallos (30 min)

Escribe: cert expirado, hostname mismatch, CA desconocida — síntoma en el cliente y qué harías en staging de Agenda Ops.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/certificados.md
git commit -m "docs(m10): l10 certificados x509"
```
""",
    )
)

# ---------- L11 ----------
LESSONS.append(
    dict(
        id="L11",
        orden=11,
        titulo="Lab openssl y pinning conceptual",
        horas=5.0,
        semana=3,
        lectura="MDN certificate pinning (advertencias) + hilo seguridad",
        evidencia="labs/openssl-lab.md",
        _lectura_corta="Huella del cert; pinning: cuándo ayuda y cómo duele en rotación",
        _enlace={
            "enlace_titulo": "Hilo seguridad",
            "enlace": "../../../hilos/seguridad.md",
        },
        _hecho="""1. `labs/openssl-lab.md` con fingerprint SHA256 del leaf de un sitio + comandos reproducibles.
2. Nota de pinning: beneficio vs riesgo operacional (rotación CA/leaf).
3. Commit `docs(m10): l11 openssl pinning`.""",
        _errores="""- Recomendar pinning ciego en una app web típica sin plan de rotación.
- Tratar pinning como sustituto de validación de cadena.
- Publicar material de “cómo hacer MITM” ofensivo — aquí solo defensa conceptual.""",
        siguiente="[L12 — MITM conceptual y amenazas de enlace](L12-mitm-conceptual-y-amenazas-de-enlace.md)",
        body=r"""
# L11 — Lab openssl y pinning conceptual

**~5.0 h · Semana 3**

Huella y pinning son herramientas de **confianza extra**, no magia. Hoy las documentas con cuidado.

## Objetivo

Calcular fingerprint y escribir cuándo el pinning tiene sentido (y cuándo no) para Agenda Ops.

## Pasos

### 1. Fingerprint (45 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -fingerprint -sha256 -noout
```

Guarda en `labs/openssl-lab.md`.

### 2. Exportar PEM de estudio (30 min)

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -out projects/m10-redes/samples/example-leaf.pem
openssl x509 -in projects/m10-redes/samples/example-leaf.pem -noout -text | head -40
```

Solo cert público — **nunca** claves privadas de tu producto en git.

### 3. Pinning conceptual (60 min)

Escribe: (a) mobile/API crítica con pin + backup pin; (b) por qué rotar leaf sin backup rompe clientes; (c) alternativa: Certificate Transparency + buena validación de cadena + HSTS.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/openssl-lab.md projects/m10-redes/samples
git commit -m "docs(m10): l11 openssl pinning"
```
""",
    )
)

# ---------- L12 ----------
LESSONS.append(
    dict(
        id="L12",
        orden=12,
        titulo="MITM conceptual y amenazas de enlace",
        horas=5.0,
        semana=3,
        lectura="Tanenbaum ataques en red (selecto) + hilo seguridad",
        evidencia="amenazas-enlace.md en m10-redes",
        _lectura_corta="Amenazas en tránsito: eavesdropping, MITM, DNS spoofing (alto nivel)",
        _hecho="""1. `projects/m10-redes/amenazas-enlace.md` con ≥4 amenazas y mitigaciones (TLS, HSTS, DNS confiable…).
2. Semana 3 enlazada en README; P1 labs TLS cerrados.
3. Commit `docs(m10): l12 amenazas enlace`.""",
        _errores="""- Tutorial ofensivo de MITM — aquí solo modelo de amenaza y defensa.
- Pensar que HTTP “solo en la LAN” es inocuo.
- Olvidar captive portals / Wi‑Fi públicas en el modelo.""",
        siguiente="[L13 — Cookies: atributos y modelo de almacenamiento](L13-cookies-atributos-y-modelo-de-almacenamiento.md)",
        body=r"""
# L12 — MITM conceptual y amenazas de enlace

**~5.0 h · Semana 3**

Cierras la semana TLS con un documento de amenazas **defensivo**: qué temes y qué mitigación aplica.

## Objetivo

Redactar `amenazas-enlace.md` usable como input de M18.

## Pasos

### 1. Modelo (45 min)

Actores: usuario del panel, red del café, ISP, DNS resolver, tu API. Dibuja trust boundaries.

### 2. Catálogo (75 min)

Para cada amenaza (eavesdropping HTTP, MITM con cert falso si el cliente no valida, DNS spoofing, session theft en tránsito):

- Impacto en citas/PII
- Mitigación (TLS bien validado, HSTS, no mixed content, DNS provider serio…)
- Residual risk

### 3. Checklist P1 (40 min)

README: labs semana 1–3 listos. Enlace a `amenazas-enlace.md`.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l12 amenazas enlace"
```
""",
    )
)

# ---------- L13 ----------
LESSONS.append(
    dict(
        id="L13",
        orden=13,
        titulo="Cookies: atributos y modelo de almacenamiento",
        horas=5.0,
        semana=4,
        lectura="MDN Cookies (ES)",
        evidencia="labs/cookies.md",
        _lectura_corta="Set-Cookie; Secure, HttpOnly, SameSite, Path, Domain, Max-Age",
        _enlace={
            "enlace_titulo": "MDN · HTTP cookies",
            "enlace": "https://developer.mozilla.org/es/docs/Web/HTTP/Cookies",
        },
        _hecho="""1. `labs/cookies.md` tabla de atributos con decisión recomendada para sesión Agenda Ops.
2. Ejemplo `Set-Cookie` redactado (valores ficticios).
3. Commit `docs(m10): l13 cookies`.""",
        _errores="""- Cookie de sesión sin `Secure`/`HttpOnly` en prod.
- `SameSite=None` sin entender CSRF.
- Guardar access tokens de larga vida en `localStorage` “porque es más fácil”.""",
        siguiente="[L14 — Sesiones, tokens y estado en APIs](L14-sesiones-tokens-y-estado-en-apis.md)",
        body=r"""
# L13 — Cookies: atributos y modelo de almacenamiento

**~5.0 h · Semana 4**

La sesión del dueño del salón vivirá en cookies o en headers. Hoy eliges atributos a conciencia.

## Objetivo

Documentar el modelo de cookie de sesión para Agenda Ops.

## Pasos

### 1. Lectura MDN (50 min)

Subraya Secure, HttpOnly, SameSite=Lax/Strict/None, Domain, Path, Max-Age vs Expires.

### 2. Lab observación (40 min)

```bash
curl -sI https://example.com | grep -i set-cookie || true
```

Si no hay cookies, inventa un ejemplo realista en la bitácora y analiza cada flag.

### 3. Decisión producto (60 min)

En `labs/cookies.md`:

```text
Set-Cookie: session=…; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=…
```

Justifica cada flag para owner/staff. Contrasta con token en `Authorization` header.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/cookies.md
git commit -m "docs(m10): l13 cookies"
```
""",
    )
)

# ---------- L14 ----------
LESSONS.append(
    dict(
        id="L14",
        orden=14,
        titulo="Sesiones, tokens y estado en APIs",
        horas=5.0,
        semana=4,
        lectura="MDN Web Storage vs cookies + OAuth2 vista alta",
        evidencia="labs/sesiones.md",
        _lectura_corta="Sesión server-side vs JWT/opaque token; dónde vive el estado",
        _hecho="""1. `labs/sesiones.md` compara sesión+cookie vs Bearer token para Agenda Ops (pros/contras).
2. Diagrama: browser → API → store de sesión/Redis/PG.
3. Commit `docs(m10): l14 sesiones tokens`.""",
        _errores="""- JWT eterno en localStorage sin rotación ni revoke.
- Mezclar “stateless” con “sin authz”.
- Olvidar logout / invalidación.""",
        siguiente="[L15 — CORS, preflight y errores típicos](L15-cors-preflight-y-errores-tipicos.md)",
        body=r"""
# L14 — Sesiones, tokens y estado en APIs

**~5.0 h · Semana 4**

El panel (origen A) hablará con la API (origen B). Hoy eliges cómo viaja la identidad.

## Objetivo

Dejar una decisión documentada sesión vs token para el piloto single-tenant.

## Pasos

### 1. Modelos (50 min)

En `labs/sesiones.md`: (1) session id opaco en cookie HttpOnly; (2) access token Bearer; (3) híbrido access corto + refresh.

### 2. Amenazas (40 min)

XSS → robo de token en JS vs cookie HttpOnly; CSRF → SameSite + anti-CSRF; replay → TTL corto.

### 3. Decisión piloto (50 min)

Elige **un** modelo para M17 y escribe “por qué”. Anota qué cambia cuando llegue multi-tenant (M19+).

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/sesiones.md
git commit -m "docs(m10): l14 sesiones tokens"
```
""",
    )
)

# ---------- L15 ----------
LESSONS.append(
    dict(
        id="L15",
        orden=15,
        titulo="CORS, preflight y errores típicos",
        horas=5.0,
        semana=4,
        lectura="MDN CORS",
        evidencia="labs/cors.md",
        _lectura_corta="Same-origin policy; ACAO; preflight OPTIONS; credenciales",
        _enlace={
            "enlace_titulo": "MDN · CORS",
            "enlace": "https://developer.mozilla.org/es/docs/Web/HTTP/CORS",
        },
        _hecho="""1. `labs/cors.md` explica preflight y configuración segura (sin `*` + credentials).
2. Ejemplo de error de consola típico y cómo lo depurarías con curl OPTIONS.
3. Commit `docs(m10): l15 cors`.""",
        _errores="""- `Access-Control-Allow-Origin: *` con cookies.
- Desactivar CORS en el navegador “para desarrollar”.
- Confundir CORS con authz de negocio.""",
        siguiente="[L16 — Cabeceras de seguridad HTTP](L16-cabeceras-de-seguridad-http.md)",
        body=r"""
# L15 — CORS, preflight y errores típicos

**~5.0 h · Semana 4**

CORS no autentica usuarios: solo relaja same-origin en el browser. Hoy lo configuras sin abrirlo todo.

## Objetivo

Documentar preflight y una política CORS para panel+API de Agenda Ops.

## Pasos

### 1. Lectura MDN (45 min)

Same-origin; simple request vs preflight; `Access-Control-Allow-Credentials`.

### 2. Simula preflight (45 min)

```bash
curl -v -X OPTIONS https://httpbin.org/anything \
  -H 'Origin: https://app.agenda.local' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: content-type,authorization'
```

Anota qué respondería **tu** API (orígenes permitidos, métodos, headers).

### 3. Política producto (45 min)

En `labs/cors.md`: allowlist de orígenes staging/prod; nunca `*` con credentials; cómo fallar cerrado.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/labs/cors.md
git commit -m "docs(m10): l15 cors"
```
""",
    )
)

# ---------- L16 ----------
LESSONS.append(
    dict(
        id="L16",
        orden=16,
        titulo="Cabeceras de seguridad HTTP",
        horas=5.0,
        semana=4,
        lectura="MDN CSP, HSTS, X-Frame-Options / frame-ancestors",
        evidencia="labs/security-headers.md",
        _lectura_corta="HSTS, CSP, X-Content-Type-Options, Referrer-Policy, frame-ancestors",
        _enlace={
            "enlace_titulo": "MDN · Strict-Transport-Security",
            "enlace": "https://developer.mozilla.org/es/docs/Web/HTTP/Headers/Strict-Transport-Security",
        },
        _hecho="""1. `labs/security-headers.md` con checklist de headers y valores iniciales para Agenda Ops.
2. `curl -sI` contra un sitio real anotando cuáles faltan.
3. Commit `docs(m10): l16 security headers`.""",
        _errores="""- CSP `unsafe-inline` eterno “para que cargue”.
- HSTS en localhost de desarrollo sin saber cómo deshacerlo.
- Creer que headers reemplazan authz.""",
        siguiente="[L17 — Superficie de ataque: endpoints y datos](L17-superficie-de-ataque-endpoints-y-datos.md)",
        body=r"""
# L16 — Cabeceras de seguridad HTTP

**~5.0 h · Semana 4**

Capa barata y visible. Hoy inventarias headers y dejas una checklist para M17/M18.

## Objetivo

Escribir la política inicial de security headers del producto.

## Pasos

### 1. Escaneo (40 min)

```bash
curl -sI https://example.com | sed -n '1,40p'
```

Busca: `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`.

### 2. Checklist Agenda Ops (75 min)

En `labs/security-headers.md`, para cada header: valor propuesto + riesgo si falta. CSP en modo report-only primero está bien — documéntalo.

### 3. Cierre semana 4 (30 min)

README: L13–L16 hechos; enlace a cookies/CORS/headers.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l16 security headers"
```
""",
    )
)

# ---------- L17 ----------
LESSONS.append(
    dict(
        id="L17",
        orden=17,
        titulo="Superficie de ataque: endpoints y datos",
        horas=5.0,
        semana=5,
        lectura="Hilo seguridad + ficha M10 proyecto",
        evidencia="superficie/endpoints.md (P3 inicio)",
        _lectura_corta="Inventario de endpoints, auth, datos sensibles y trust boundaries",
        _enlace={"enlace_titulo": "Hilo seguridad", "enlace": "../../../hilos/seguridad.md"},
        _hecho="""1. `superficie/endpoints.md` lista endpoints previstos (citas/clientes/auth) + auth + PII.
2. Diagrama trust boundary: browser / API / DB / backups.
3. Commit `docs(m10): l17 superficie endpoints`.""",
        _errores="""- Inventario vacío “porque aún no hay código”.
- Olvidar admin, healthchecks, webhooks.
- Marcar todo como “público”.""",
        siguiente="[L18 — Cliente y servidor TCP mínimo (P2)](L18-cliente-y-servidor-tcp-minimo-p2.md)",
        body=r"""
# L17 — Superficie de ataque: endpoints y datos

**~5.0 h · Semana 5**

P3 empieza aquí: inventarias antes de endurecer (M18).

## Objetivo

Completar el mapa de superficie del piloto Agenda Ops (aunque sea diseño).

## Pasos

### 1. Plantilla (30 min)

```bash
mkdir -p projects/m10-redes/superficie
```

Crea `endpoints.md` con columnas: método, path, auth, roles, datos, notas.

### 2. Inventario (90 min)

Incluye al menos: login/logout, CRUD clientes, CRUD citas, listados, health `/health`, estáticos del panel. Marca PII (teléfono, notas privadas).

### 3. Trust boundaries (40 min)

Mermaid o ASCII: User Agent → TLS → API → PG; backups; logs. Qué cruza cada frontera.

### 4. Commit (15 min)

```bash
git add projects/m10-redes/superficie
git commit -m "docs(m10): l17 superficie endpoints"
```
""",
    )
)

# ---------- L18 ----------
LESSONS.append(
    dict(
        id="L18",
        orden=18,
        titulo="Cliente y servidor TCP mínimo (P2)",
        horas=5.0,
        semana=5,
        lectura="Node net module + Tanenbaum transporte",
        evidencia="projects/m10-redes/tcp-echo/ con código y diagrama",
        _lectura_corta="Sockets TCP en Node: listen, connect, stream de bytes",
        _enlace={
            "enlace_titulo": "Node.js net",
            "enlace": "https://nodejs.org/api/net.html",
        },
        _hecho="""1. `tcp-echo/server.js` + `client.js` (o TS) funcionan en localhost.
2. `diagrama-request.md` compara echo TCP vs request HTTP/TLS.
3. Commit `feat(m10): l18 tcp echo p2`.""",
        _errores="""- Servidor que no hace `.end()` / deja sockets colgados.
- Confundir “eco TCP” con HTTP.
- Bind en `0.0.0.0` expuesto sin firewall en una red no confiable.""",
        siguiente="[L19 — Documento de amenazas de red del producto](L19-documento-de-amenazas-de-red-del-producto.md)",
        body=r"""
# L18 — Cliente y servidor TCP mínimo (P2)

**~5.0 h · Semana 5**

Bajas una capa: bytes sobre TCP sin HTTP. P2 exige código que corre.

## Objetivo

Implementar echo TCP mínimo y un diagrama de una request real del producto.

## Pasos

### 1. Scaffold (20 min)

```bash
mkdir -p projects/m10-redes/tcp-echo
cd projects/m10-redes/tcp-echo
```

### 2. Servidor (60 min)

`server.js`:

```js
import net from "node:net";
const port = Number(process.env.PORT || 9000);
const server = net.createServer((socket) => {
  socket.on("data", (buf) => {
    socket.write(buf);
  });
});
server.listen(port, "127.0.0.1", () => {
  console.log(`echo on 127.0.0.1:${port}`);
});
```

### 3. Cliente (45 min)

`client.js` conecta, envía una línea, imprime eco, cierra. Prueba:

```bash
node server.js &
node client.js
kill %1
```

### 4. Diagrama (45 min)

`diagrama-request.md`: eco TCP (L18) vs `GET /api/citas` (DNS→TCP→TLS→HTTP). Relaciona puertos.

### 5. Commit (15 min)

```bash
git add projects/m10-redes/tcp-echo
git commit -m "feat(m10): l18 tcp echo p2"
```
""",
    )
)

# ---------- L19 ----------
LESSONS.append(
    dict(
        id="L19",
        orden=19,
        titulo="Documento de amenazas de red del producto",
        horas=5.0,
        semana=5,
        lectura="Proyecto M10 README + STRIDE lite (red)",
        evidencia="projects/m10-redes/amenazas-red.md actualizado",
        _lectura_corta="STRIDE lite sobre red: spoofing, tampering, info disclosure, DoS",
        _hecho="""1. `amenazas-red.md` integra enlace + superficie + mitigaciones hacia M18/M19.
2. README del proyecto enlaza amenazas, superficie y tcp-echo.
3. Commit `docs(m10): l19 amenazas red producto`.""",
        _errores="""- Lista genérica copiada sin Agenda Ops.
- Amenazas sin mitigación ni dueño (tú / M18).
- Olvidar DNS y cookies.""",
        siguiente="[L20 — Cierre M10 — evidencias y dominio](L20-cierre-m10-evidencias-y-dominio.md)",
        body=r"""
# L19 — Documento de amenazas de red del producto

**~5.0 h · Semana 5**

El entregable del proyecto: un doc que M18 pueda consumir sin redescubrir la red.

## Objetivo

Publicar `amenazas-red.md` completo y enlazado.

## Pasos

### 1. Fusiona fuentes (60 min)

Parte de `amenazas-enlace.md` + `superficie/endpoints.md` + labs TLS/cookies. Crea `amenazas-red.md` con secciones: activos, amenazas, mitigaciones, residual, follow-ups M18/M19.

### 2. STRIDE lite (60 min)

Al menos una fila por: Spoofing, Tampering, Repudiation (logs), Information disclosure, DoS, Elevation (si aplica a red/admin).

### 3. README (40 min)

Índice del proyecto con P1/P2/P3 y proyecto marcados.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l19 amenazas red producto"
```
""",
    )
)

# ---------- L20 ----------
LESSONS.append(
    dict(
        id="L20",
        orden=20,
        titulo="Cierre M10 — evidencias y dominio",
        horas=5.0,
        semana=5,
        lectura="Ficha M10 completa",
        evidencia="checklist P1–P3 + proyecto verificados",
        _lectura_corta="Auditoría de evidencia y criterios de dominio de la ficha",
        _hecho="""1. Checklist P1 labs, P2 tcp-echo, P3 superficie, proyecto amenazas — todo enlazado en README.
2. Auto-respuesta escrita a los 3 criterios de dominio de la ficha M10.
3. Commit `docs(m10): cierre materia`.""",
        _errores="""- Marcar dominio sin poder explicar TLS en voz alta.
- Evidencia solo en la cabeza / Discord.
- Dejar `tcp-echo` sin README de uso.""",
        siguiente="Cierra la [ficha M10](../M10-redes.md). Siguiente: [M11 — Sistemas operativos](../M11-sistemas-operativos.md).",
        body=r"""
# L20 — Cierre M10 — evidencias y dominio

**~5.0 h · Semana 5**

Cierras la materia como ingeniero: evidencia en git + dominio oral.

## Objetivo

Auditar P1–P3/proyecto y dejar el README listo para revisión.

## Pasos

### 1. Auditoría (60 min)

```bash
find projects/m10-redes -type f | sort
```

Verifica: labs semana 1–4, tls/certs, cookies/cors/headers, `tcp-echo/`, `superficie/`, `amenazas-red.md`.

### 2. Criterios de dominio (60 min)

Escribe en `projects/m10-redes/dominio-oral.md` respuestas a:

1. Depurar un timeout (red vs app)
2. Explicar TLS sin “magia”
3. Defender tu mapa de superficie

### 3. README final (40 min)

Checklist con casillas marcadas y rutas exactas.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): cierre materia"
```
""",
    )
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(LESSONS) == 20, len(LESSONS)
    for lesson in LESSONS:
        path = OUT / FILENAMES[lesson["orden"]]
        text = render(lesson)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print("total", len(LESSONS))


if __name__ == "__main__":
    main()
