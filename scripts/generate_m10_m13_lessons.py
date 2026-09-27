#!/usr/bin/env python3
"""Generate M01-style lesson markdown for M10–M13."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "curriculum" / "etapas" / "02-disciplinaria"


def slugify(t: str) -> str:
    t = t.lower()
    t = (
        t.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
    )
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")


def render(
    materia: str,
    orden: int,
    titulo: str,
    semana: int,
    horas: float,
    lectura: str,
    evidencia: str,
    objetivo: str,
    porque: str,
    conceptos: list[str],
    pasos_extra: str,
    lectura_rows: list[tuple[str, str, str]],
    hecho: list[str],
    errores: list[str],
    siguiente_label: str | None,
    siguiente_href: str | None,
) -> str:
    lid = f"L{orden:02d}"
    conceptos_md = "\n".join(f"- {c}" for c in conceptos)
    lectura_table = "\n".join(
        f"| {a} | {b} | {c} |" for a, b, c in lectura_rows
    )
    hecho_md = "\n".join(f"{i + 1}. {h}" for i, h in enumerate(hecho))
    errores_md = "\n".join(f"- {e}" for e in errores)
    sig = (
        f"\n## Siguiente\n\n[{siguiente_label}]({siguiente_href})\n"
        if siguiente_label and siguiente_href
        else ""
    )

    return f"""---
id: {lid}
materia: {materia}
orden: {orden}
titulo: {titulo}
horas: {horas}
semana: {semana}
lectura: "{lectura}"
evidencia: "{evidencia}"
---

# {lid} — {titulo}

**~{horas:g} h · Semana {semana}**

## Objetivo

{objetivo}

## Por qué importa

{porque}

## Conceptos

{conceptos_md}

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

{pasos_extra}

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs({materia.lower()}): {lid.lower()} {slugify(titulo)[:40]}"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
{lectura_table}

## Hecho cuando

{hecho_md}

## Errores comunes

{errores_md}
{sig}"""


def write_materia(materia: str, lessons: list[dict]) -> int:
    out_dir = BASE / materia
    out_dir.mkdir(parents=True, exist_ok=True)
    n = len(lessons)
    for i, spec in enumerate(lessons):
        orden = i + 1
        next_label = None
        next_href = None
        if orden < n:
            nt = lessons[i + 1]["titulo"]
            next_href = f"L{orden + 1:02d}-{slugify(nt)}.md"
            next_label = f"L{orden + 1:02d} — {nt}"
        body = render(
            materia=materia,
            orden=orden,
            siguiente_label=next_label,
            siguiente_href=next_href,
            **spec,
        )
        fname = f"L{orden:02d}-{slugify(spec['titulo'])}.md"
        (out_dir / fname).write_text(body, encoding="utf-8")
    return n


# --- M10 Redes (20) ---
M10 = [
    {
        "titulo": "Modelo de capas y primer curl",
        "semana": 1,
        "horas": 5,
        "lectura": "Tanenbaum — intro y capas (modelo OSI/TCP simplificado)",
        "evidencia": "projects/m10-redes/labs/semana-01.md + dia1.md con curl -v",
        "objetivo": "Dibujar un modelo de capas de cinco niveles y capturar con `curl -v` el viaje hasta la primera respuesta HTTP de un sitio HTTPS.",
        "porque": "Sin mapa de capas, cada error de red se vuelve “el Wi‑Fi está mal”. Hoy instalas el diagrama mental que usarás hasta M18.",
        "conceptos": [
            "Encapsulación y desencapsulación entre capas.",
            "Diferencia entre **protocolo** y **servicio** expuesto.",
            "Puerto lógico vs dirección IP.",
            "Request/response en capa de aplicación (HTTP).",
        ],
        "pasos_extra": """```bash
mkdir -p projects/m10-redes/labs
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/labs/curl-example.log
```

En `projects/m10-redes/dia1.md` responde: ¿qué capas ves en la salida? (resolución, TCP, TLS, HTTP). Compara `http://example.com` vs `https://` (redirección).""",
        "lectura_rows": [
            ("Tanenbaum", "Introducción + capas", "MDN *Overview of HTTP* (vista rápida)"),
            ("Plan", "[Hilo seguridad](../../../hilos/seguridad.md) (10 min)", "—"),
        ],
        "hecho": [
            "Existe `dia1.md` con qué protege TLS y qué **no** protege.",
            "Log `curl -v` guardado en `labs/`.",
            "Diagrama ASCII de capas en la bitácora.",
        ],
        "errores": [
            "Pegar la salida entera sin resaltar líneas relevantes.",
            "Confundir TLS con “cifrado de la base de datos”.",
        ],
    },
    {
        "titulo": "IP, direccionamiento y enrutamiento intro",
        "semana": 1,
        "horas": 5,
        "lectura": "Tanenbaum — capa de red (IPv4, máscaras, routing básico)",
        "evidencia": "notas en semana-01.md: IP local, gateway, traceroute resumido",
        "objetivo": "Leer tu configuración IP local y explicar hop-by-hop qué hace un paquete hacia un host público.",
        "porque": "Timeouts y “no llega al servidor” empiezan en routing o DNS; hoy practicas observación antes de culpar al código.",
        "conceptos": ["IPv4 y CIDR a nivel ingeniero.", "Default gateway.", "MTU (idea).", "ICMP y `ping` como señal, no como prueba definitiva."],
        "pasos_extra": """```bash
ip addr show | head -40    # o ifconfig en macOS
ip route | head
ping -c 3 1.1.1.1
traceroute -m 12 example.com 2>/dev/null | head -15 || tracepath example.com | head -15
```

Documenta IP, máscara y gateway. ¿Cuántos saltos hasta `example.com`?""",
        "lectura_rows": [("Tanenbaum", "Capa de red (IP)", "Labs anteriores + apuntes")],
        "hecho": ["Tabla IP/gateway en bitácora.", "Salida resumida de traceroute.", "Explicas diferencia IP pública vs privada."],
        "errores": ["Asumir que `ping` falla implica que HTTP fallará igual.", "Publicar capturas con IPs internas de producción."],
    },
    {
        "titulo": "TCP vs UDP y puertos bien usados",
        "semana": 1,
        "horas": 5,
        "lectura": "Tanenbaum — capa de transporte (TCP, UDP, puertos)",
        "evidencia": "semana-01.md: tabla protocolo/puerto/ejemplo Agenda Ops",
        "objetivo": "Contrastar TCP y UDP con ejemplos reales (HTTP/TLS vs DNS/QUIC intuición) y listar puertos que tu stack futuro expondrá o no.",
        "porque": "Abrir el puerto de Postgres “solo en local” es un clásico de incidentes; hoy decides qué debe escuchar el host.",
        "conceptos": ["Three-way handshake (idea).", "Puerto bien conocido vs efímero.", "UDP: sin garantías de entrega ordenada.", "Backlog y `LISTEN` en servidores."],
        "pasos_extra": """```bash
ss -tuln | head -30    # o netstat -tuln
nc -zv localhost 22 2>&1 | head -3
```

Enumera servicios en escucha en tu máquina. Para Agenda Ops (futuro): 443 público, 5432 **no** público. Escribe la regla en la bitácora.""",
        "lectura_rows": [("Tanenbaum", "TCP/UDP y puertos", "`ss`/`netstat` man pages")],
        "hecho": ["Tabla TCP vs UDP con un caso cada uno.", "Lista de puertos que NO expondrás en piloto.", "Captura `ss` comentada."],
        "errores": ["Memorizar puertos sin saber el servicio.", "Exponer DB porque “compose lo publicó”."],
    },
    {
        "titulo": "Cierre semana 1 — bitácora P1",
        "semana": 1,
        "horas": 5,
        "lectura": "Repaso semana 1 Tanenbaum + ficha M10",
        "evidencia": "projects/m10-redes/labs/semana-01.md consolidado",
        "objetivo": "Consolidar la bitácora de labs de la semana 1 y enlazar cada experimento a una hipótesis de fallo en producción.",
        "porque": "P1 exige evidencia continua; hoy cierras la semana con criterio de auditoría, no con notas sueltas.",
        "conceptos": ["Trazabilidad comando → observación → implicación.", "Hipótesis red vs aplicación."],
        "pasos_extra": "Revisa L01–L03. Une logs en `semana-01.md` con secciones: **Comando**, **Salida clave**, **Qué aprendí**, **Riesgo Agenda Ops**. Añade un mini diagrama DNS→TCP→TLS→HTTP.",
        "lectura_rows": [("Ficha", "../M10-redes.md", "—")],
        "hecho": ["`semana-01.md` ≥4 experimentos documentados.", "Un riesgo concreto para API futura.", "Commit de cierre semana 1."],
        "errores": ["Marcar P1 sin carpeta `labs/`.", "Diagrama copiado sin explicación propia."],
    },
    {
        "titulo": "DNS: resolución, registros y fallos",
        "semana": 2,
        "horas": 5,
        "lectura": "Tanenbaum — DNS + MDN DNS",
        "evidencia": "labs/semana-02-dns.md con dig/host",
        "objetivo": "Resolver un nombre con `dig`/`host`, interpretar TTL y registrar cómo un fallo DNS se manifiesta en el navegador o en `curl`.",
        "porque": "Certificados válidos con nombre equivocado, caches viejas y subdominios mal configurados rompen deploys.",
        "conceptos": ["Registros A/AAAA, CNAME.", "TTL y caché recursiva.", "Autoritativo vs recursivo."],
        "pasos_extra": """```bash
dig example.com A +short
dig example.com AAAA +short
dig @1.1.1.1 example.com
host -t SOA example.com
```

Simula “cambio de IP”: anota qué pasaría si el TTL fuera 3600 y cambias el registro.""",
        "lectura_rows": [("Tanenbaum", "DNS", "MDN *DNS*")],
        "hecho": ["Salida `dig` comentada.", "Explicas TTL en tus palabras.", "Escenario de fallo DNS documentado."],
        "errores": ["Confundir DNS con búsqueda HTTP.", "Ignorar IPv6 (AAAA) en entornos mixtos."],
    },
    {
        "titulo": "HTTP mensajes, métodos y semántica",
        "semana": 2,
        "horas": 5,
        "lectura": "MDN HTTP methods + Tanenbaum capa aplicación",
        "evidencia": "labs/http-metodos.md",
        "objetivo": "Construir requests GET/HEAD/OPTIONS con `curl` y explicar idempotencia y seguridad de métodos comunes.",
        "porque": "REST mal diseñado mezcla verbos; hoy fijas criterio antes de modelar `/citas` en Agenda Ops.",
        "conceptos": ["Línea de petición y cabeceras.", "Cuerpo y `Content-Type`.", "Idempotencia (GET, PUT, DELETE)."],
        "pasos_extra": """```bash
curl -sI https://httpbin.org/get
curl -s -X OPTIONS -I https://httpbin.org/ 2>/dev/null | head -20
```

Escribe qué método usarías para listar citas vs cancelar una (borrador conceptual).""",
        "lectura_rows": [("MDN", "HTTP request methods", "httpbin.org para pruebas")],
        "hecho": ["Tabla método/uso/riesgo.", "Al menos tres requests documentados.", "Nota sobre idempotencia en cancelación de citas."],
        "errores": ["Usar POST para todo.", "Olvidar que HEAD no lleva cuerpo."],
    },
    {
        "titulo": "Status codes y cabeceras de respuesta",
        "semana": 2,
        "horas": 5,
        "lectura": "MDN HTTP response status + lista IANA selecta",
        "evidencia": "labs/status-codes.md",
        "objetivo": "Clasificar códigos 2xx/3xx/4xx/5xx y leer cabeceras `Cache-Control`, `Content-Type`, `Server` con ojo crítico.",
        "porque": "Un 401 mal interpretado como 500 envía horas de debug al lugar equivocado.",
        "conceptos": ["Semántica 401 vs 403.", "Redirects 301/302.", "Caching en APIs (cuándo no cachear)."],
        "pasos_extra": """```bash
curl -s -o /dev/null -w '%{http_code}\\n' https://httpbin.org/status/404
curl -sI https://httpbin.org/response-headers?freeform=%22X-Test:1%22 | head -25
```

Mapea códigos que usará Agenda Ops: login fallido, cita no encontrada, conflicto de horario.""",
        "lectura_rows": [("MDN", "HTTP status codes", "httpbin.org/status")],
        "hecho": ["Lista ≥8 códigos con ejemplo Agenda Ops.", "Captura de cabeceras anotada.", "Diferencia 401/403 escrita."],
        "errores": ["Devolver siempre 200 con `{error:true}`.", "Exponer `Server` con versión vulnerable."],
    },
    {
        "titulo": "HTTP/2 intuición y curl avanzado",
        "semana": 2,
        "horas": 5,
        "lectura": "MDN HTTP/2 + notas Tanenbaum aplicación",
        "evidencia": "labs/curl-avanzado.md",
        "objetivo": "Usar `curl` con tiempos, redirects y guardado selectivo; comparar HTTP/1.1 vs h2 cuando el servidor lo permita.",
        "porque": "Latencia percibida en el panel de citas depende de cómo multiplexas recursos; no necesitas implementar h2, sí leer evidencia.",
        "conceptos": ["Multiplexación (idea).", "ALPN en TLS.", "TTFB y tiempo total (`curl -w`)."],
        "pasos_extra": """```bash
curl -sI --http2 https://www.google.com 2>&1 | head -5
curl -w 'dns:%{time_namelookup} tcp:%{time_connect} tls:%{time_appconnect} total:%{time_total}\\n' -o /dev/null -s https://example.com
```

Guarda plantilla de timing para repetir en M19.""",
        "lectura_rows": [("MDN", "HTTP/2", "curl -w format")],
        "hecho": ["Plantilla timing en bitácora.", "Nota HTTP/2 vs 1.1 en un párrafo.", "Cierre semana 2 enlazado en P1."],
        "errores": ["Optimizar h2 antes de corregir N+1 en API.", "Confundir keep-alive con sesión de usuario."],
    },
    {
        "titulo": "TLS: handshake y qué protege en tránsito",
        "semana": 3,
        "horas": 5,
        "lectura": "Tanenbaum seguridad/TLS selecto + MDN TLS",
        "evidencia": "labs/tls-handshake.md",
        "objetivo": "Describir las fases del handshake TLS 1.2/1.3 a alto nivel y listar amenazas que TLS mitiga vs las que no.",
        "porque": "“Ya tiene HTTPS” no responde por XSS ni por logs con PII; hoy acotas el contrato de TLS.",
        "conceptos": ["Confidencialidad e integridad en tránsito.", "Certificado de servidor.", "Perfect Forward Secrecy (idea)."],
        "pasos_extra": """```bash
curl -v https://example.com -o /dev/null 2>&1 | rg -i 'TLS|SSL|subject|issuer' || true
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

Tabla: amenaza → ¿TLS ayuda? (eavesdropping, tampering, phishing de dominio).""",
        "lectura_rows": [("Tanenbaum", "TLS intro", "MDN Transport Layer Security")],
        "hecho": ["Tabla amenaza/mitigación.", "Salida openssl comentada.", "Párrafo “qué no protege TLS”."],
        "errores": ["Creer que TLS autentica al usuario.", "Mezclar TLS con hash de contraseña en DB."],
    },
    {
        "titulo": "Certificados X.509 y cadena de confianza",
        "semana": 3,
        "horas": 5,
        "lectura": "MDN certificate transparency (idea) + Tanenbaum PKI intro",
        "evidencia": "labs/certificados.md",
        "objetivo": "Leer subject, SAN, fechas de validez y cadena hasta una CA de confianza del sistema.",
        "porque": "Renovaciones fallidas y nombres mal emitidos tumban el piloto Agenda Ops en viernes por la tarde.",
        "conceptos": ["CN/SAN.", "CA intermedia.", "Revocación (CRL/OCSP, idea)."],
        "pasos_extra": """```bash
echo | openssl s_client -showcerts -connect example.com:443 2>/dev/null | openssl x509 -noout -text | head -40
```

Anota algoritmo de firma y fechas. ¿Qué pasa si expira mañana?""",
        "lectura_rows": [("MDN", "Digital certificates", "openssl x509 man")],
        "hecho": ["Campos del cert explicados.", "Plan de renovación (Let's Encrypt u otro) esbozado.", "Riesgo nombre incorrecto documentado."],
        "errores": ["Aceptar certificados autofirmados en prod sin proceso.", "Olvidar SAN al emitir para subdominio API."],
    },
    {
        "titulo": "Lab openssl y pinning conceptual",
        "semana": 3,
        "horas": 5,
        "lectura": "MDN certificate pinning (advertencias) + hilo seguridad",
        "evidencia": "labs/openssl-lab.md",
        "objetivo": "Verificar manualmente un certificado contra el hostname y discutir por qué el pinning raramente se hace a mano en web apps.",
        "porque": "Entender confianza del SO vs pinning evita modas peligrosas en apps móviles y APIs.",
        "conceptos": ["Hostname verification.", "Pinning vs CA store.", "MITM en redes captive portal."],
        "pasos_extra": "Prueba `curl` contra un host con SNI correcto e incorrecto (`--resolve` si hace falta). Documenta error esperado.",
        "lectura_rows": [("Plan", "[Hilo seguridad](../../../hilos/seguridad.md)", "OWASP Transport Layer Protection (vista rápida)")],
        "hecho": ["Experimento SNI/hostname documentado.", "Opinión fundamentada sobre pinning.", "Entrada P1 semana 3."],
        "errores": ["Deshabilitar verificación TLS en prod “temporalmente”.", "Pinning sin plan de rotación."],
    },
    {
        "titulo": "MITM conceptual y amenazas de enlace",
        "semana": 3,
        "horas": 5,
        "lectura": "Tanenbaum ataques en red (selecto)",
        "evidencia": "amenazas-enlace.md en m10-redes",
        "objetivo": "Explicar MITM, downgrade y rogue AP a nivel ingeniero y enlazarlos a controles (TLS, HSTS, no HTTP plano).",
        "porque": "Esta lección alimenta el documento de amenazas del proyecto y M18.",
        "conceptos": ["MITM.", "Downgrade TLS.", "HSTS (intro)."],
        "pasos_extra": "Redacta tres escenarios: café Wi‑Fi, DNS comprometido, proxy corporativo. Mitigación por escenario.",
        "lectura_rows": [("Tanenbaum", "Seguridad en redes", "MDN HSTS")],
        "hecho": ["Tres escenarios + mitigación.", "Enlace a hilo seguridad.", "Cierre semana 3 en bitácora."],
        "errores": ["Asumir VPN sustituye TLS end-to-end.", "Mezclar contenido activo HTTP en página HTTPS."],
    },
    {
        "titulo": "Cookies: atributos y modelo de almacenamiento",
        "semana": 4,
        "horas": 5,
        "lectura": "MDN Cookies (ES)",
        "evidencia": "labs/cookies.md",
        "objetivo": "Documentar `Set-Cookie` con `Secure`, `HttpOnly`, `SameSite` y cuándo usar cookie vs header Authorization.",
        "porque": "La sesión del dueño de Agenda Ops no puede robarse por XSS ni enviarse en HTTP plano.",
        "conceptos": ["Cookie de sesión vs token en memoria.", "SameSite=Lax/Strict.", "Path y Domain."],
        "pasos_extra": """```bash
curl -sI https://httpbin.org/cookies/set/session/abc | rg -i set-cookie || true
```

Diseña (en texto) la cookie de sesión del piloto: atributos obligatorios.""",
        "lectura_rows": [("MDN", "HTTP cookies", "OWASP Session Management cheat sheet (selecto)")],
        "hecho": ["Diseño de cookie de sesión escrito.", "Tabla atributo/propósito.", "Riesgo XSS ligado a HttpOnly."],
        "errores": ["SameSite=None sin Secure.", "Guardar JWT enorme en cookie sin necesidad."],
    },
    {
        "titulo": "Sesiones, tokens y estado en APIs",
        "semana": 4,
        "horas": 5,
        "lectura": "MDN Web Storage vs cookies + notas OAuth2 (vista alta)",
        "evidencia": "labs/sesiones.md",
        "objetivo": "Comparar sesión server-side, JWT stateless y refresh tokens; elegir borrador para piloto single-tenant.",
        "porque": "M12/M13 fijarán auth; hoy entiendes trade-offs de red y superficie.",
        "conceptos": ["Stateful session store.", "JWT en header vs cookie.", "Rotación de refresh."],
        "pasos_extra": "Tabla comparativa con columnas: revocación, tamaño, CSRF, XSS. Recomendación provisional para Agenda Ops.",
        "lectura_rows": [("MDN", "Web Storage API", "OAuth 2.0 overview (no implementar aún)")],
        "hecho": ["Tabla comparativa completa.", "Recomendación con justificación.", "Riesgos CSRF mencionados."],
        "errores": ["JWT en localStorage “porque es fácil”.", "Sesiones sin expiración."],
    },
    {
        "titulo": "CORS, preflight y errores típicos",
        "semana": 4,
        "horas": 5,
        "lectura": "MDN CORS",
        "evidencia": "labs/cors.md",
        "objetivo": "Explicar por qué el navegador aplica CORS y qué cabeceras configura el servidor API para un front en otro origen.",
        "porque": "En M17 separarás front y API; hoy evitas “arreglar CORS con `*`”.",
        "conceptos": ["Same-origin policy.", "Preflight OPTIONS.", "Credentials y `Access-Control-Allow-Credentials`."],
        "pasos_extra": "Esboza política CORS para piloto: orígenes permitidos, métodos, headers. Prohíbe `*` con credenciales.",
        "lectura_rows": [("MDN", "CORS", "Fetch API")],
        "hecho": ["Política CORS borrador.", "Explicas preflight en 5 frases.", "Error común documentado."],
        "errores": ["`Access-Control-Allow-Origin: *` con cookies.", "Confundir CORS con autorización en API."],
    },
    {
        "titulo": "Cabeceras de seguridad HTTP",
        "semana": 4,
        "horas": 5,
        "lectura": "MDN CSP, HSTS, X-Frame-Options",
        "evidencia": "labs/security-headers.md",
        "objetivo": "Inspeccionar un sitio real y redactar lista de cabeceras que aplicarás en Agenda Ops (aunque aún no exista código).",
        "porque": "P3 y el proyecto M10 piden inventario honesto de superficie.",
        "conceptos": ["CSP (idea).", "HSTS.", "X-Content-Type-Options."],
        "pasos_extra": """```bash
curl -sI https://securityheaders.com 2>/dev/null | head -30
# o cualquier sitio de referencia que elijas
```

Lista cabeceras presentes/ausentes y prioridad para MVP.""",
        "lectura_rows": [("MDN", "Content-Security-Policy", "securityheaders.com como inspiración")],
        "hecho": ["Lista priorizada para MVP.", "Captura curl comentada.", "Cierre semana 4."],
        "errores": ["CSP `unsafe-inline` sin plan de quitarlo.", "HSTS sin HTTPS estable."],
    },
    {
        "titulo": "Superficie de ataque: endpoints y datos",
        "semana": 5,
        "horas": 5,
        "lectura": "Hilo seguridad + ficha M10 proyecto",
        "evidencia": "superficie/endpoints.md (P3 inicio)",
        "objetivo": "Inventariar endpoints previstos, datos sensibles y vectores de red para el piloto web.",
        "porque": "El mapa de superficie es entregable P3 y entrada a M18.",
        "conceptos": ["Superficie de ataque.", "PII en tránsito y en reposo (intro).", "Trust boundary navegador/API."],
        "pasos_extra": "Tabla: endpoint, auth, datos, riesgo red (robo sesión, sniffing, CSRF). Incluye admin y staff.",
        "lectura_rows": [("Plan", "[Hilo seguridad](../../../hilos/seguridad.md)", "Ficha M10")],
        "hecho": ["Tabla ≥10 filas (borrador API).", "Datos PII marcados.", "Riesgos numerados."],
        "errores": ["Inventario solo del happy path.", "Olvidar webhooks o health checks."],
    },
    {
        "titulo": "Cliente y servidor TCP mínimo (P2)",
        "semana": 5,
        "horas": 5,
        "lectura": "Node net module docs + Tanenbaum transporte",
        "evidencia": "projects/m10-redes/tcp-echo/ con código y diagrama",
        "objetivo": "Implementar echo TCP en Node/TypeScript y dibujar bytes desde cliente hasta socket servidor.",
        "porque": "HTTP vive sobre TCP; ver sockets quita miedo a timeouts y backpressure.",
        "conceptos": ["Socket.", "listen/connect.", "Buffer y encoding."],
        "pasos_extra": """Crea `projects/m10-redes/tcp-echo/` con servidor y cliente mínimos (`net.createServer`, `net.connect`). Añade `diagrama-request.md` comparando capas con HTTP.""",
        "lectura_rows": [("Node.js", "net module", "Tanenbaum TCP")],
        "hecho": ["Echo funciona en local.", "Diagrama capas guardado.", "Commit código + doc."],
        "errores": ["Dejar servidor escuchando en 0.0.0.0 sin nota.", "No cerrar sockets en error."],
    },
    {
        "titulo": "Documento de amenazas de red del producto",
        "semana": 5,
        "horas": 5,
        "lectura": "Proyecto M10 README + STRIDE lite (red)",
        "evidencia": "projects/m10-redes/amenazas-red.md actualizado",
        "objetivo": "Redactar amenazas de red (eavesdropping, session theft, DNS spoofing) con mitigaciones enlazadas a M18/M19.",
        "porque": "Es el entregable proyecto de la materia y debe ser usable por tu yo de M17.",
        "conceptos": ["STRIDE a nivel red.", "Mitigación vs aceptación de riesgo.", "Dependencias (CDN, hosting)."],
        "pasos_extra": "Estructura: activo, amenaza, impacto, mitigación, estado. Mínimo 8 entradas.",
        "lectura_rows": [("Plan", "Proyecto m10-redes README", "Hilo seguridad")],
        "hecho": ["`amenazas-red.md` ≥8 entradas.", "Mitigaciones realistas.", "README enlaza doc."],
        "errores": ["Mitigación “usar HTTPS” sin detalle.", "No priorizar por impacto."],
    },
    {
        "titulo": "Cierre M10 — evidencias y dominio",
        "semana": 5,
        "horas": 5,
        "lectura": "Ficha M10 completa",
        "evidencia": "checklist P1–P3 + proyecto verificados",
        "objetivo": "Auditar P1–P3 y proyecto; autoevaluar criterios de dominio y preparar M11.",
        "porque": "Marcar sin evidencia rompe el contrato del plan.",
        "conceptos": ["Auditoría de evidencia.", "Handoff a operación (M11)."],
        "pasos_extra": "Tabla checklist ficha M10 con enlaces a archivos. Bitácora cierre: qué depurarías primero ante timeout.",
        "lectura_rows": [("Ficha", "../M10-redes.md", "—")],
        "hecho": ["Checklist P1–P3 verificada.", "Criterios dominio respondidos.", "Commit cierre M10."],
        "errores": ["Marcar lecciones sin labs.", "Perder diagrama TCP del P2."],
    },
]


def _lesson(
    titulo: str,
    semana: int,
    lectura: str,
    evidencia: str,
    objetivo: str,
    porque: str,
    conceptos: list[str],
    pasos_extra: str,
    lectura_rows: list[tuple[str, str, str]],
    hecho: list[str],
    errores: list[str],
    horas: float = 5,
) -> dict:
    return {
        "titulo": titulo,
        "semana": semana,
        "horas": horas,
        "lectura": lectura,
        "evidencia": evidencia,
        "objetivo": objetivo,
        "porque": porque,
        "conceptos": conceptos,
        "pasos_extra": pasos_extra,
        "lectura_rows": lectura_rows,
        "hecho": hecho,
        "errores": errores,
    }


M11 = [
    _lesson(
        "Procesos, permisos y bitácora día 1",
        1,
        "Silberschatz — procesos (intro)",
        "projects/m11-so/labs/dia1-comandos.md",
        "Documentar procesos en ejecución, identidad (`id`, `umask`) y permisos mínimos en un archivo de prueba.",
        "El piloto Agenda Ops correrá en un VPS o contenedor; sin lectura de procesos no diagnosticas incidentes.",
        ["PID, PPID.", "Usuario efectivo vs real.", "Permisos rwx.", "umask."],
        """```bash
mkdir -p projects/m11-so/labs
ps aux | head
id; umask
echo secreto > /tmp/m11-test-$USER.txt && chmod 600 /tmp/m11-test-$USER.txt && ls -la /tmp/m11-test-$USER.txt
```
Explica por qué `chmod 777` es mala idea en datos de clientes.""",
        [("Silberschatz", "Procesos", "man ps, chmod")],
        ["`dia1-comandos.md` ≥10 líneas con salida.", "Archivo 600 creado.", "Párrafo anti-777."],
        ["Correr todo como root por comodidad.", "Subir secretos en la bitácora."],
    ),
    _lesson(
        "Proceso vs hilo y el runtime Node",
        1,
        "Silberschatz — hilos + documentación Node event loop",
        "labs/semana-01-procesos.md sección hilos",
        "Contrastar proceso OS con el modelo de concurrencia de Node (event loop, workers opcionales).",
        "Confundir “Node es single-thread” con “una sola CPU” genera bugs de CPU y bloqueos.",
        ["Proceso pesado vs hilo ligero.", "Event loop.", "Worker threads (mención)."],
        "Diagrama: proceso `node` → un hilo principal → cola de callbacks. ¿Qué pasa con `fs.readFile`?",
        [("Silberschatz", "Hilos", "Node.js event loop guide")],
        ["Diagrama en bitácora.", "Ejemplo I/O no bloqueante explicado.", "Pregunta abierta para L03."],
        ["Usar `while(true)` en handler HTTP.", "Confundir cluster con hilos OS."],
    ),
    _lesson(
        "Señales SIGTERM y apagado graceful",
        1,
        "Silberschatz — señales + Node process signals",
        "labs/sigterm-node.md",
        "Manejar `SIGTERM` en un script Node para cerrar servidor HTTP sin cortar requests a mitad.",
        "En deploy (M19) el orquestador envía SIGTERM; ignorarla corrompe citas a medias.",
        ["SIGTERM vs SIGKILL.", "Graceful shutdown.", "Timeouts de cierre."],
        "Script mínimo `http.createServer` + handler SIGTERM que cierra con timeout 10s. Prueba con `kill -TERM`.",
        [("Silberschatz", "Señales", "Node process.on('SIGTERM')")],
        ["Servidor cierra ordenadamente.", "Log de señal guardado.", "Diferencia TERM/KILL escrita."],
        ["Solo SIGKILL en producción.", "No cerrar pool DB en shutdown."],
    ),
    _lesson(
        "Cierre semana 1 — práctica P1",
        1,
        "Repaso Silberschatz procesos",
        "labs/semana-01-procesos.md consolidado",
        "Consolidar labs de procesos/señales/permisos para P1.",
        "P1 exige comandos reproducibles, no capturas sueltas.",
        ["Trazabilidad comando → efecto."],
        "Une L01–L03 en un solo archivo con índice. Verifica que otro pueda reproducir.",
        [("Ficha", "../M11-sistemas-operativos.md", "—")],
        ["P1 semana 1 completa.", "Commit consolidado.", "Checklist permisos."],
        ["Mezclar logs de distintas máquinas sin fecha.", "Olvidar umask en explicación."],
    ),
    _lesson(
        "Memoria virtual y paginación (intuición)",
        2,
        "Silberschatz — memoria virtual",
        "labs/semana-02-memoria.md",
        "Explicar espacio de direcciones virtual, paginación y por qué un proceso cree tener memoria contigua.",
        "OOM y swapping en un VPS pequeño tumbarán el piloto si no observas RSS.",
        ["MMU.", "Page fault (idea).", "Swap."],
        "Lee capítulo y dibuja proceso → tablas de páginas → RAM. Relaciona con contenedor (L08).",
        [("Silberschatz", "Memoria virtual", "Artículos OS notes")],
        ["Diagrama virtual→físico.", "Glosario 5 términos.", "Hipótesis OOM."],
        ["Pensar que `free` miente siempre igual.", "Ignorar swap lleno."],
    ),
    _lesson(
        "Observar RSS y CPU de Node",
        2,
        "man ps, top/htop",
        "labs/rss-node.md",
        "Medir RSS/CPU de un proceso Node bajo carga ligera (script bucle + servidor).",
        "Sin baseline no sabes si un leak es real.",
        ["RSS vs VSZ.", "%CPU.", "Carga sintética."],
        """```bash
node -e "setInterval(()=>{},1000)"
# en otra terminal: ps -o pid,rss,cmd -p <pid>
```""",
        [("Silberschatz", "Memoria", "htop tutorial")],
        ["Captura antes/después carga.", "Números con unidades.", "Interpretación honesta."],
        ["Un solo snapshot.", "Confundir heap JS con RSS total."],
    ),
    _lesson(
        "OOM, ulimit y síntomas",
        2,
        "Silberschatz OOM + ulimit man",
        "labs/oom-ulimit.md",
        "Describir qué hace el kernel ante OOM y cómo `ulimit -v` puede limitar (lab opcional controlado).",
        "Agenda Ops en VPS 1GB necesita límites y alertas.",
        ["OOM killer.", "ulimit.", "cgroup memory (preview)."],
        "Documenta señales de OOM en logs (sin forzar en prod). Plan: reinicio, límites compose.",
        [("Silberschatz", "Memoria", "Docker memory limits doc")],
        ["Síntomas OOM listados.", "Plan mitigación piloto.", "No ejecutar fork bomb."],
        ["Probar fork bomb en máquina compartida.", "Ignorar límites de contenedor."],
    ),
    _lesson(
        "cgroups y memoria en contenedores",
        2,
        "Docker docs memory + Silberschatz resumen",
        "labs/cgroups-nota.md",
        "Relacionar cgroups con límites de memoria en Docker y qué ve el proceso dentro del contenedor.",
        "M11 semana 4 dockeriza el stack; hoy entiendes por qué el contenedor muere “sin razón”.",
        ["cgroup v2 (idea).", "Límite memoria Docker.", "OOM en contenedor."],
        "Esboza `deploy.resources.limits.memory` en compose futuro. Nota para playbook.",
        [("Docker", "Resource constraints", "Silberschatz")],
        ["Nota cgroups en bitácora.", "Enlace a playbook futuro.", "Cierre semana 2."],
        ["Sin límite memoria en compose.", "Asumir host ilimitado."],
    ),
    _lesson(
        "Sistema de archivos: inodos y espacio",
        3,
        "Silberschatz sistema de archivos",
        "labs/semana-03-fs.md",
        "Usar `df` y `du` para localizar consumo; explicar inodo y nombre.",
        "Logs de API y backups llenan disco antes que CPU.",
        ["inodo.", "df vs du.", "Enlaces duros/simbólicos (idea)."],
        """```bash
df -h
du -sh projects/* 2>/dev/null | sort -h | tail
```""",
        [("Silberschatz", "Sistema de archivos", "man df/du")],
        ["Salida df/du comentada.", "Riesgo logs Agenda Ops.", "Plan rotación (L11)."],
        ["Borrar datos sin backup.", "Ignorar inodos agotados."],
    ),
    _lesson(
        "Permisos, usuarios y mínimo privilegio",
        3,
        "Silberschatz protección",
        "labs/permisos.md",
        "Practicar `chmod`/`chown` en directorio de datos simulado con roles owner/staff (carpetas).",
        "Datos de clientes no deben ser legibles por cualquier usuario del host.",
        ["rwx para user/group/other.", "750 vs 700.", "Principio least privilege."],
        "Crea árbol `data/owner` y `data/staff` con permisos distintos; documenta matriz.",
        [("Silberschatz", "Protección", "Ficha M11")],
        ["Matriz rol/carpeta/permiso.", "Experimento reproducido.", "Sin 777."],
        ["chmod 777 en volumen Docker.", "Correr Postgres como root innecesario."],
    ),
    _lesson(
        "Script de backup automatizado (P2)",
        3,
        "Silberschatz I/O + bash strict",
        "projects/m11-so/scripts/backup.sh",
        "Escribir backup con `set -euo pipefail` y variables de entorno (sin secretos en repo).",
        "Sin backup probado, el piloto no es serio.",
        ["pipefail.", "RETENTION.", "pg_dump o equivalente simulado."],
        "Implementa `scripts/backup.sh` y doc de variables. Simula dump a archivo si no hay DB.",
        [("Silberschatz", "I/O", "bash manual")],
        ["Script versionado.", "Ejecución exitosa logueada.", "Secretos fuera del repo."],
        ["Hardcode DATABASE_URL.", "Backup en mismo disco sin copia offsite (anótalo)."],
    ),
    _lesson(
        "Rotación de logs y restore de prueba",
        3,
        "logrotate concept + tu script",
        "restore-prueba.md + rotación",
        "Añadir rotación por tamaño/fecha y documentar **un** restore de prueba.",
        "P2 no cuenta sin restore documentado.",
        ["rotación.", "restore.", "RPO/RTO (intro)."],
        "Rotación en script o logrotate config. Restore a carpeta/DB vacía; fecha en `restore-prueba.md`.",
        [("Ficha", "M11 P2", "—")],
        ["`restore-prueba.md` con fecha.", "Rotación funciona.", "P2 lista para auditoría."],
        ["Restore nunca probado.", "Sobrescribir único backup."],
    ),
    _lesson(
        "Imágenes, contenedores y volúmenes",
        4,
        "Docker docs + Silberschatz síntesis",
        "labs/docker-intro.md",
        "Diferenciar imagen, contenedor, volumen; levantar `hello-world` y un contenedor Node efímero.",
        "Agenda Ops usará Postgres persistente; hoy separas datos de imagen.",
        ["capa de imagen.", "volumen nombrado.", "ephemeral container."],
        """```bash
docker run --rm hello-world
docker volume create m11-pgdata
```""",
        [("Docker", "Volumes overview", "Silberschatz")],
        ["Glosario imagen/contenedor/volumen.", "Volumen creado.", "Notas para compose."],
        ["Datos en capa writable sin volumen.", "docker system prune sin pensar."],
    ),
    _lesson(
        "Dockerfile Node sin root (P3)",
        4,
        "Dockerfile reference USER",
        "projects/m11-so/Dockerfile",
        "Escribir Dockerfile Node con usuario no-root y dependencias `npm ci`.",
        "Root en contenedor amplifica escape y escritura indebida.",
        ["USER.", "COPY --chown.", "slim images."],
        "Dockerfile según ejemplo ficha M11; `docker build` y `docker run` verificando `whoami` dentro.",
        [("Docker", "Dockerfile best practices", "Ficha M11")],
        ["Imagen construye.", "Proceso no es root.", "Nota en README."],
        ["Secretos en ARG/ENV de build.", "latest sin pin."],
    ),
    _lesson(
        "docker compose: API y base de datos",
        4,
        "Compose file reference",
        "docker-compose.yml documentado",
        "Definir compose mínimo API+Postgres: red interna, volumen DB, puerto API solo.",
        "Playbook M11 debe levantar stack reproducible.",
        ["service network.", "depends_on.", "ports mapping."],
        "Compose con Postgres no publicado a 0.0.0.0 salvo necesidad documentada. `.env.example`.",
        [("Docker", "Compose", "Postgres image doc")],
        ["`docker compose up` funciona.", "DB no expuesta públicamente.", ".env.example sin secretos."],
        ["Puerto 5432 publicado “temporal”.", "Contraseña en git."],
    ),
    _lesson(
        "Playbook local y cierre M11",
        4,
        "Ficha M11 proyecto",
        "playbook.md + README",
        "Completar `playbook.md` (up/down/backup/restore) y auditar P1–P3.",
        "Otro dev debe levantar Agenda Ops local solo con el playbook.",
        ["runbook.", "handoff M19."],
        "Diagrama Mermaid host→contenedores→volumen. Checklist ficha. Bitácora cierre.",
        [("Ficha", "../M11-sistemas-operativos.md", "producto-saas.md")],
        ["Playbook completo.", "P1–P3 verificados.", "Commit cierre M11."],
        ["Playbook sin restore.", "Olvidar usuario no-root en doc."],
    ),
]

M12 = [
    _lesson(
        "Design partner y guion de entrevista",
        1,
        "plantilla.md + producto-saas.md",
        "entrevistas/guion-v1.md",
        "Elegir sub-vertical estable y redactar ≥10 preguntas abiertas sobre flujo de citas y dolores actuales.",
        "Agenda Ops empieza con problema real, no con pantallas.",
        ["ICP.", "design partner.", "preguntas abiertas."],
        """```bash
mkdir -p projects/m12-srs/entrevistas
cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
```
Guion: roles, herramientas actuales (WhatsApp/libreta), no-shows, datos sensibles.""",
        [("Plan", "producto-saas.md", "plantilla SRS")],
        ["Sub-vertical elegido.", "Guion ≥10 preguntas.", "Sin cambiar vertical en 3 semanas."],
        ["Preguntas cerradas sí/no.", "Saltar roles staff."],
    ),
    _lesson(
        "Entrevista y notas timestamp",
        1,
        "Técnicas elicitación (plantilla)",
        "entrevistas/notas-YYYY-MM-DD.md",
        "Realizar entrevista (real o simulación seria) y capturar citas, dolores y reglas de negocio.",
        "Sin notas crudas no hay trazabilidad al SRS.",
        ["semiestructurada.", "problema vs solución.", "timestamp."],
        "Sesión ≥30 min. Notas con timestamp cada 10–15 min. Commit notas.",
        [("Plantilla", "secciones contexto", "—")],
        ["Notas con fecha.", "≥5 citas o paráfrasis.", "Problemas sin UI aún."],
        ["Inventar respuestas sin marcar simulación.", "Mezclar dos negocios."],
    ),
    _lesson(
        "Problemas observados y glosario",
        1,
        "problemas.md + glosario",
        "problemas.md y glosario.md",
        "Listar ≥5 problemas observados y glosario dominio (cita, servicio, no-show, staff).",
        "El glosario evita ambigüedad en stories y SRS.",
        ["problema observado.", "término dominio.", "supuesto."],
        "Cada problema: evidencia de entrevista. Glosario ≥8 términos.",
        [("Plan", "producto-saas.md", "—")],
        ["≥5 problemas.", "Glosario enlazado.", "Supuestos marcados."],
        ["Problemas = features deseadas.", "Sin fuente en notas."],
    ),
    _lesson(
        "Stakeholders y contexto Agenda Ops",
        1,
        "SRS plantilla stakeholders",
        "srs-borrador.md sección contexto",
        "Documentar actores owner/staff/cliente final y objetivos del piloto single-tenant.",
        "M13 y M17 heredan actores; cambiarlos tarde cuesta caro.",
        ["stakeholder.", "single-tenant.", "MVP 4 semanas."],
        "Completa contexto y alcance preliminar en borrador. MoSCoW preview.",
        [("Plantilla", "introducción", "hilo seguridad")],
        ["Actores definidos.", "Objetivo piloto escrito.", "Cierre semana 1 P1."],
        ["Omitir cliente final indirecto.", "Multi-tenant en MVP."],
    ),
    _lesson(
        "Formato user story y trazabilidad",
        2,
        "Plantilla + historias INVEST",
        "stories.md inicio",
        "Escribir primeras stories con rol, necesidad y beneficio; enlazar a problemas.md.",
        "Stories son puente a tests en M15/M17.",
        ["INVEST.", "trazabilidad.", "rol."],
        "≥4 stories iniciales en `stories.md` con ID (US-01…).",
        [("Plantilla", "req funcionales", "—")],
        ["≥4 stories.", "Enlace a problema.", "IDs estables."],
        ["Stories técnicas (“crear tabla”).", "Sin rol."],
    ),
    _lesson(
        "Criterios de aceptación verificables",
        2,
        "Given/When/Then intro",
        "stories.md criterios",
        "Añadir criterios numerados o GWT a cada story; incluir 401/403 donde aplique.",
        "Seguridad entra aquí, no “luego en M18”.",
        ["criterio verificable.", "error path.", "permisos."],
        "Al menos 2 stories con criterios de error. Ejemplo notas privadas staff vs owner.",
        [("Plan", "hilo seguridad", "ejemplo ficha M12")],
        ["Criterios en todas las stories nuevas.", "≥2 con error/permiso.", "Sin “se ve bien”."],
        ["Criterios subjetivos.", "Omitir 403 en datos sensibles."],
    ),
    _lesson(
        "Historias de vacío, duplicados y conflicto",
        2,
        "Casos borde negocio citas",
        "stories.md ampliado",
        "Cubrir sin citas, cliente duplicado, horario inválido, doble reserva.",
        "El MVP falla en borde si solo happy path.",
        ["caso borde.", "idempotencia.", "mensaje usuario."],
        "≥4 stories adicionales (total acumulado ≥8). Prioriza Must.",
        [("Plantilla", "reglas negocio", "—")],
        ["≥8 stories total.", "Bordes cubiertos.", "Mapa story→SRS."],
        ["Duplicar stories sin criterio.", "Ignorar zona horaria."],
    ),
    _lesson(
        "RNF seguridad, privacidad y P2",
        2,
        "Plantilla RNF + hilo seguridad",
        "stories.md + srs-borrador RNF",
        "Definir ≥3 RNF numerados (SEC/PRIV) trazables a stories.",
        "P2 y P3 dependen de RNF explícitos.",
        ["RNF.", "PII mínimo.", "auditoría."],
        "RNF-SEC/PRIV en borrador SRS. Cada RNF enlaza a ≥1 story.",
        [("Hilo", "seguridad.md", "plantilla")],
        ["≥3 RNF seguridad/privacidad.", "Trazabilidad.", "P2 listo."],
        ["RNF genéricos.", "Sin criterio de prueba futuro."],
    ),
    _lesson(
        "Alcance MVP y MoSCoW",
        3,
        "producto-saas fases",
        "srs-borrador alcance",
        "Priorizar Must/Should/Could/Won't para build de 4 semanas (auth, citas, clientes, admin).",
        "Freeze evita MVP infinito.",
        ["MoSCoW.", "freeze.", "fuera de alcance."],
        "Tabla MoSCoW. Lista explícita: multi-tenant, billing, IA = Won't ahora.",
        [("Plan", "producto-saas.md", "—")],
        ["MoSCoW completo.", "Won't documentado.", "Fecha freeze propuesta."],
        ["Todo es Must.", "Cambiar vertical."],
    ),
    _lesson(
        "Requisitos funcionales en SRS",
        3,
        "plantilla.md funcionales",
        "srs-borrador.md funcionales",
        "Completar sección funcional numerada alineada a stories Must.",
        "El SRS es contrato para M13/M17.",
        ["RF numerado.", "consistencia.", "dependencias."],
        "Cada Must tiene RF. Revisa duplicados y conflictos.",
        [("Plantilla", "funcionales", "stories.md")],
        ["RF cubren Must.", "Sin contradicciones.", "Referencias US-XX."],
        ["RF vagos.", "Desalineación con stories."],
    ),
    _lesson(
        "SRS v1, freeze y P3",
        3,
        "plantilla completa",
        "projects/m12-srs/srs-v1.md",
        "Promover borrador a `srs-v1.md` con fecha de freeze y firma (tu nombre/fecha).",
        "Entregable proyecto Agenda Ops para diseño e implementación.",
        ["srs-v1.", "freeze.", "supuestos."],
        "Copia/revisa → srs-v1.md. README m12 actualizado. Checklist P1–P3.",
        [("Plantilla", "completa", "Ficha M12")],
        ["srs-v1.md existe.", "≥3 RNF SEC/PRIV.", "Freeze fechado."],
        ["Dejar borrador sin v1.", "Sin supuestos single-tenant."],
    ),
    _lesson(
        "Revisión M13 y cierre M12",
        3,
        "Ficha M12 + handoff diseño",
        "nota-handoff-m13.md",
        "Auto revisión: coherencia, preguntas abiertas para diseño, criterios dominio.",
        "M13 empieza leyendo tu SRS; hoy reduces fricción.",
        ["handoff.", "preguntas abiertas.", "auditoría."],
        "Lista preguntas para M13 (auth, modelo cita). Bitácora cierre. Commit final M12.",
        [("Ficha", "../M12-requerimientos.md", "m13-diseno README")],
        ["Handoff escrito.", "P1–P3 auditados.", "Cierre M12 commit."],
        ["SRS sin fecha.", "Stories sin criterios."],
    ),
]

M13 = [
    _lesson(
        "Trust boundaries y ADR 001",
        1,
        "Larman + ADR M01",
        "diagramas/trust-boundaries.md + adr/001",
        "Marcar límites navegador|API|DB y registrar ADR monolito modular.",
        "Autorización no vive solo en el front del panel de citas.",
        ["trust boundary.", "ADR.", "monolito modular."],
        """```bash
mkdir -p projects/m13-diseno/diagramas projects/m13-diseno/adr
```
Lee `projects/m12-srs/srs-v1.md` (o borrador) y dibuja tres zonas.""",
        [("Plan", "hilo seguridad", "plantilla ADR M01")],
        ["trust-boundaries.md.", "ADR 001.", "Commit docs(m13)."],
        ["Microservicios día 1.", "Boundary sin datos que cruzan."],
    ),
    _lesson(
        "Actores y casos de uso prioritarios",
        1,
        "Larman casos de uso",
        "casos-de-uso.md borrador",
        "Derivar casos de uso Must del SRS: login, CRUD citas/clientes, admin roles.",
        "Casos de uso son guía de pruebas y API.",
        ["actor.", "caso de uso.", "precondición."],
        "≥6 casos con ID CU-XX. Enlaza a US del SRS.",
        [("Larman", "casos de uso", "srs-v1")],
        ["≥6 casos.", "Trazabilidad SRS.", "Actores correctos."],
        ["Casos decorativos.", "Olvidar staff."],
    ),
    _lesson(
        "Escenarios alternos y errores",
        1,
        "Escenarios excepción",
        "casos-de-uso.md escenarios",
        "Documentar alternos 401/403, conflicto horario, validación.",
        "M17 implementará estos caminos; hoy los nombras.",
        ["flujo alterno.", "postcondición error.", "mensaje."],
        "Cada caso Must tiene ≥1 alterno de error.",
        [("Larman", "escenarios", "stories errores")],
        ["Alternos documentados.", "Códigos HTTP previstos.", "Sin happy path único."],
        ["Errores genéricos 500.", "Ignorar 403 en notas privadas."],
    ),
    _lesson(
        "Cierre P1 flujos principales",
        1,
        "Ficha M13 P1",
        "casos-de-uso.md consolidado",
        "Consolidar `casos-de-uso.md` cubriendo historias Must.",
        "P1 exige flujos completos, no lista suelta.",
        ["consolidación.", "revisión SRS."],
        "Índice, revisión coherencia con srs-v1. Commit P1.",
        [("Ficha", "../M13-analisis-y-diseno.md", "—")],
        ["P1 completo.", "Must cubiertos.", "Semana 1 cerrada."],
        ["Casos huérfanos.", "Desalineación SRS."],
    ),
    _lesson(
        "Diagrama de clases del dominio",
        2,
        "Larman modelo dominio",
        "diagramas/clases.md",
        "Modelar entidades MVP: Usuario, Cliente, Cita, Servicio (ajusta a SRS).",
        "Clases deben caber en 4 semanas de build.",
        ["entidad.", "agregado (idea).", "relación."],
        "Mermaid classDiagram en clases.md. Solo Must.",
        [("Larman", "modelo conceptual", "M09 FK preview")],
        ["clases.md con Mermaid.", "≤8 entidades.", "Nombres alineados SRS."],
        ["40 entidades día 1.", "UML sin atributos útiles."],
    ),
    _lesson(
        "Cardinalidades y persistencia futura",
        2,
        "Elmasri relaciones (repaso)",
        "clases.md cardinalidades",
        "Anotar cardinalidades y FKs futuras coherentes con M09.",
        "Evita modelo que no se puede implementar en SQL.",
        ["1:N.", "nullable.", "índice (nota)."],
        "Tabla entidad-relación texto. Marca PII.",
        [("M09", "ficha repaso", "srs-v1 datos")],
        ["Cardinalidades en diagrama.", "PII marcada.", "Notas FK."],
        ["Many-to-many sin tabla intermedia.", "Mezclar staff y owner en una clase."],
    ),
    _lesson(
        "Secuencia: autenticación y sesión",
        2,
        "Mermaid sequence",
        "diagramas/secuencia-auth.md",
        "Diagrama de secuencia login + cookie/sesión según SRS.",
        "Auth es secuencia crítica para seguridad.",
        ["secuencia.", "sesión.", "validación API."],
        "Mermaid: browser→API→DB. Marca validación rol en API.",
        [("MDN", "cookies/sesión", "srs auth")],
        ["secuencia-auth.md.", "Validación en API.", "Errores 401."],
        ["Auth solo en front.", "Omitir logout."],
    ),
    _lesson(
        "Secuencia: crear cita (P2)",
        2,
        "Secuencia negocio",
        "diagramas/secuencia-crear-cita.md",
        "Secuencia crear cita con chequeo conflicto horario.",
        "P2 exige clase + secuencia crítica.",
        ["transacción (idea).", "conflicto.", "201/409."],
        "Secuencia con rama conflicto. Enlaza CU y US.",
        [("Larman", "secuencia", "stories citas")],
        ["P2 secuencia lista.", "Conflicto modelado.", "Commit semana 2."],
        ["Happy path solo.", "Sin rol staff."],
    ),
    _lesson(
        "Arquitectura en capas",
        3,
        "Capas + Clean idea",
        "arquitectura.md borrador",
        "Definir capas HTTP → aplicación → dominio → infraestructura.",
        "Evita mezclar SQL en controllers.",
        ["controller.", "service.", "repository."],
        "Diagrama capas + regla: autorización en aplicación/dominio.",
        [("Larman", "capas", "Código limpio módulos")],
        ["arquitectura.md.", "Regla autorización.", "Nombres de capas."],
        ["Anémico sin comportamiento.", "Lógica en React."],
    ),
    _lesson(
        "DTOs, validación y frontera HTTP",
        3,
        "Validación entrada",
        "arquitectura.md DTO",
        "Listar DTOs de entrada/salida y dónde validas (no confiar en cliente).",
        "Agenda Ops recibe JSON malicioso desde el primer día.",
        ["DTO.", "validación.", "sanitización (idea)."],
        "Tabla endpoint→DTO→reglas. Enlaza RNF.",
        [("OWASP", "input validation intro", "srs")],
        ["Tabla DTOs.", "Validación server-side.", "Sin confiar en front."],
        ["Tipos TS = validación.", "Omitir límites tamaño."],
    ),
    _lesson(
        "Componentes y despliegue (C4 ligero)",
        3,
        "C4 nivel 1-2",
        "diagramas/componentes.md",
        "Diagrama contenedores: browser, API, Postgres, (futuro) worker.",
        "Prepara M11 playbook y M19 deploy.",
        ["contenedor C4.", "dependencia.", "puerto."],
        "Mermaid o texto. Postgres solo red interna.",
        [("C4", "modelo contenedor", "m11 playbook")],
        ["componentes.md.", "DB interna.", "Enlace arquitectura."],
        ["DB pública en diagrama.", "Falta API."],
    ),
    _lesson(
        "Boundaries actualizados y amenazas",
        3,
        "trust boundaries + STRIDE lite",
        "trust-boundaries.md v2",
        "Actualizar boundaries con endpoints y amenazas por zona.",
        "P3 requiere límites y notas de amenaza.",
        ["zona desconfianza.", "amenaza.", "control."],
        "Cada límite: datos, protocolo, control. Al menos 3 amenazas.",
        [("Hilo", "seguridad", "M10 amenazas")],
        ["P3 actualizado.", "Amenazas por zona.", "Semana 3 cerrada."],
        ["Boundary estático sin API.", "Sin control en API."],
    ),
    _lesson(
        "Plantilla ADR y decisiones de diseño",
        4,
        "ADR M01",
        "adr/README o 002",
        "Fijar plantilla ADR y abrir ADR 002 (stack o persistencia).",
        "Decisiones explícitas evitan debate infinito en M17.",
        ["contexto.", "decisión.", "consecuencias."],
        "ADR 002: p.ej. Postgres + ORM/query builder. Alternativas rechazadas.",
        [("M01", "ADR ejemplo", "srs RNF")],
        ["ADR 002 completo.", "Plantilla documentada.", "Commit."],
        ["ADR sin alternativas.", "Copiar texto genérico."],
    ),
    _lesson(
        "ADR persistencia y modelo de datos",
        4,
        "Elmasri + ADR",
        "adr/003-persistencia.md",
        "ADR sobre esquema relacional, migraciones y soft-delete si aplica.",
        "M09 y M17 dependen de esta decisión.",
        ["migración.", "esquema.", "soft delete."],
        "ADR 003 enlaza clases.md y cardinalidades.",
        [("M09", "ficha", "srs")],
        ["ADR 003.", "Enlace diagrama clases.", "Migraciones mencionadas."],
        ["JSON files en prod.", "Sin plan migraciones."],
    ),
    _lesson(
        "Extensibilidad tenant_id sin implementar",
        4,
        "producto-saas evolución",
        "adr/004-tenant-future.md",
        "Documentar dónde vivirá `tenant_id` en modelo y API sin implementarlo en piloto.",
        "Camino a SaaS sin reescribir todo en M21.",
        ["single-tenant ahora.", "tenant_id futuro.", "riesgo mezcla datos."],
        "ADR 004: supuestos, columnas futuras, no exponer multi-tenant en MVP.",
        [("Plan", "producto-saas.md", "srs supuestos")],
        ["ADR 004.", "Riesgo cross-tenant nombrado.", "No implementar aún."],
        ["Implementar multi-tenant en piloto.", "Ignorar extensión."],
    ),
    _lesson(
        "ADR auth y sesión",
        4,
        "SRS seguridad",
        "adr/005-auth.md",
        "ADR alineada a RNF: sesión server-side vs JWT según M10/M12.",
        "Auth unificada en diseño antes del código.",
        ["sesión.", "CSRF.", "rotación."],
        "ADR 005 con consecuencias operativas (redis/DB sessions).",
        [("M12", "RNF SEC", "M10 cookies")],
        ["ADR 005.", "Alineado SRS.", "≥2 ADRs semana 4."],
        ["Auth indefinida en M17.", "Omitir CSRF."],
    ),
    _lesson(
        "Índice del paquete de diseño",
        5,
        "README proyecto",
        "projects/m13-diseno/README.md",
        "Crear índice enlazando SRS, diagramas, ADRs, arquitectura.",
        "El paquete debe ser navegable en 2 minutos.",
        ["índice.", "trazabilidad.", "onboarding."],
        "README con checklist enlaces. Verifica rutas relativas.",
        [("Ficha", "proyecto M13", "srs-v1")],
        ["README índice.", "Todos los artefactos enlazados.", "Sin enlaces rotos."],
        ["README vacío.", "Diagramas huérfanos."],
    ),
    _lesson(
        "Endpoints y módulos previstos M17",
        5,
        "OpenAPI borrador opcional",
        "endpoints.md",
        "Listar rutas REST previstas con método, auth, DTO (texto).",
        "Scaffold M17 usa esta lista.",
        ["ruta.", "método.", "rol."],
        "Tabla ≥12 rutas Must. Coherente con casos de uso.",
        [("srs-v1", "RF", "arquitectura")],
        ["endpoints.md.", "Auth por ruta.", "Coherencia CU."],
        ["Rutas no en SRS.", "Falta POST citas."],
    ),
    _lesson(
        "Checklist listo para scaffold",
        5,
        "Ficha M13 cierre",
        "checklist-scaffold.md",
        "Verificar modelo, secuencias, ADRs, boundaries antes de código.",
        "Evita empezar M17 sin mapa.",
        ["checklist.", "riesgo residual.", "preguntas."],
        "Checklist binaria Sí/No por ítem. Preguntas abiertas a M17.",
        [("Ficha", "../M13-analisis-y-diseno.md", "M17 ficha")],
        ["checklist-scaffold.md.", "Sin ítems No críticos.", "Preguntas listadas."],
        ["Marcar sí sin artefacto.", "Diagramas sin SRS."],
    ),
    _lesson(
        "Cierre M13 — trazabilidad y dominio",
        5,
        "Auditoría completa",
        "nota-cierre-m13.md",
        "Auditar P1–P3, criterios dominio, eliminar diagramas huérfanos.",
        "Cierras diseño antes de implementación.",
        ["trazabilidad.", "limpieza.", "handoff M17."],
        "Matriz requisito→artefacto. Borra o enlaza diagramas sin uso. Commit cierre.",
        [("Ficha", "../M13-analisis-y-diseno.md", "—")],
        ["P1–P3 verificados.", "Sin huérfanos.", "Handoff M17 escrito."],
        ["Microservicios en doc.", "SRS no enlazado."],
    ),
]


def main() -> None:
    counts = {}
    for mid, lessons in [("M10", M10), ("M11", M11), ("M12", M12), ("M13", M13)]:
        counts[mid] = write_materia(mid, lessons)
    print("Generated:", counts)


if __name__ == "__main__":
    main()
