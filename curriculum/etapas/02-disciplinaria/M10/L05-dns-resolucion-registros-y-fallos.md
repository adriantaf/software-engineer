---
id: L05
materia: M10
orden: 5
titulo: DNS: resolución, registros y fallos
horas: 5
semana: 2
lectura: "Tanenbaum — DNS + MDN DNS"
evidencia: "labs/semana-02-dns.md con dig/host"
---

# L05 — DNS: resolución, registros y fallos

**~5 h · Semana 2**

## Objetivo

Resolver un nombre con `dig`/`host`, interpretar TTL y registrar cómo un fallo DNS se manifiesta en el navegador o en `curl`.

## Por qué importa

Certificados válidos con nombre equivocado, caches viejas y subdominios mal configurados rompen deploys.

## Conceptos

- Registros A/AAAA, CNAME.
- TTL y caché recursiva.
- Autoritativo vs recursivo.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
dig example.com A +short
dig example.com AAAA +short
dig @1.1.1.1 example.com
host -t SOA example.com
```

Simula “cambio de IP”: anota qué pasaría si el TTL fuera 3600 y cambias el registro.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l05 dns-resolucion-registros-y-fallos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Tanenbaum | DNS | MDN *DNS* |

## Hecho cuando

1. Salida `dig` comentada.
2. Explicas TTL en tus palabras.
3. Escenario de fallo DNS documentado.

## Errores comunes

- Confundir DNS con búsqueda HTTP.
- Ignorar IPv6 (AAAA) en entornos mixtos.

## Siguiente

[L06 — HTTP mensajes, métodos y semántica](L06-http-mensajes-metodos-y-semantica.md)
