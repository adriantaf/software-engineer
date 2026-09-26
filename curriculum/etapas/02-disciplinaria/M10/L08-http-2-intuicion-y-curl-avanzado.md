---
id: L08
materia: M10
orden: 8
titulo: HTTP/2 intuición y curl avanzado
horas: 5
semana: 2
lectura: "MDN HTTP/2 + notas Tanenbaum aplicación"
evidencia: "labs/curl-avanzado.md"
---

# L08 — HTTP/2 intuición y curl avanzado

**~5 h · Semana 2**

## Objetivo

Usar `curl` con tiempos, redirects y guardado selectivo; comparar HTTP/1.1 vs h2 cuando el servidor lo permita.

## Por qué importa

Latencia percibida en el panel de citas depende de cómo multiplexas recursos; no necesitas implementar h2, sí leer evidencia.

## Conceptos

- Multiplexación (idea).
- ALPN en TLS.
- TTFB y tiempo total (`curl -w`).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
curl -sI --http2 https://www.google.com 2>&1 | head -5
curl -w 'dns:%{time_namelookup} tcp:%{time_connect} tls:%{time_appconnect} total:%{time_total}\n' -o /dev/null -s https://example.com
```

Guarda plantilla de timing para repetir en M19.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l08 http-2-intuicion-y-curl-avanzado"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| MDN | HTTP/2 | curl -w format |

## Hecho cuando

1. Plantilla timing en bitácora.
2. Nota HTTP/2 vs 1.1 en un párrafo.
3. Cierre semana 2 enlazado en P1.

## Errores comunes

- Optimizar h2 antes de corregir N+1 en API.
- Confundir keep-alive con sesión de usuario.

## Siguiente

[L09 — TLS: handshake y qué protege en tránsito](L09-tls-handshake-y-que-protege-en-transito.md)
