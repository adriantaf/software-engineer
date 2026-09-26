---
id: L03
materia: M10
orden: 3
titulo: TCP vs UDP y puertos bien usados
horas: 5
semana: 1
lectura: "Tanenbaum — capa de transporte (TCP, UDP, puertos)"
evidencia: "semana-01.md: tabla protocolo/puerto/ejemplo Agenda Ops"
---

# L03 — TCP vs UDP y puertos bien usados

**~5 h · Semana 1**

## Objetivo

Contrastar TCP y UDP con ejemplos reales (HTTP/TLS vs DNS/QUIC intuición) y listar puertos que tu stack futuro expondrá o no.

## Por qué importa

Abrir el puerto de Postgres “solo en local” es un clásico de incidentes; hoy decides qué debe escuchar el host.

## Conceptos

- Three-way handshake (idea).
- Puerto bien conocido vs efímero.
- UDP: sin garantías de entrega ordenada.
- Backlog y `LISTEN` en servidores.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
ss -tuln | head -30    # o netstat -tuln
nc -zv localhost 22 2>&1 | head -3
```

Enumera servicios en escucha en tu máquina. Para Agenda Ops (futuro): 443 público, 5432 **no** público. Escribe la regla en la bitácora.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l03 tcp-vs-udp-y-puertos-bien-usados"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Tanenbaum | TCP/UDP y puertos | `ss`/`netstat` man pages |

## Hecho cuando

1. Tabla TCP vs UDP con un caso cada uno.
2. Lista de puertos que NO expondrás en piloto.
3. Captura `ss` comentada.

## Errores comunes

- Memorizar puertos sin saber el servicio.
- Exponer DB porque “compose lo publicó”.

## Siguiente

[L04 — Cierre semana 1 — bitácora P1](L04-cierre-semana-1-bitacora-p1.md)
