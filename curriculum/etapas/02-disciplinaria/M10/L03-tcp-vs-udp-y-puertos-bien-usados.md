---
id: L03
materia: M10
orden: 3
titulo: TCP vs UDP y puertos bien usados
horas: 5.0
semana: 1
lectura: "Tanenbaum: capa de transporte — TCP, UDP, puertos"
evidencia: "semana-01.md: tabla protocolo/puerto/ejemplo Agenda Ops"
---

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | TCP fiable vs UDP; sockets (IP:puerto); puertos bien conocidos | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla en `semana-01.md`: ≥6 filas protocolo/puerto/uso (incl. 443, 80, 53, 5432, 3000).
2. `ss -tuln` (o `netstat`) capturado y explicado: qué escucha en tu máquina.
3. Commit `docs(m10): l03 tcp udp puertos`.

## Errores comunes

- Decir “UDP es inseguro / TCP es seguro” (seguridad ≠ capa de transporte).
- Publicar Postgres `5432` al mundo “solo en local” y olvidarlo.
- Confundir puerto de contenedor con puerto del host.

## Siguiente

[L04 — Cierre semana 1 — bitácora P1](L04-cierre-semana-1-bitacora-p1.md)
