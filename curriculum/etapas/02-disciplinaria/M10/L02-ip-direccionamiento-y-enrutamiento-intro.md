---
id: L02
materia: M10
orden: 2
titulo: IP, direccionamiento y enrutamiento intro
horas: 5.0
semana: 1
lectura: "Tanenbaum: capa de red — IPv4, máscaras, routing básico"
evidencia: "labs/semana-01.md: IP local, gateway, traceroute resumido"
---

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | IPv4, máscara/CIDR, gateway, hop-by-hop | [MDN · HTTP (contexto app)](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-01.md` con IP local, máscara/CIDR, gateway y 3–5 hops de traceroute (o `tracepath`/`mtr`).
2. Explicas en 5 líneas qué problema resuelve IP vs qué resuelve TCP.
3. Commit `docs(m10): l02 ip y enrutamiento`.

## Errores comunes

- Confundir IP privada (`10.`, `192.168.`) con “no hay internet”.
- Pegar traceroute completo sin interpretar timeouts.
- Olvidar que el API de Agenda Ops tendrá IP pública *y* ruta interna en compose.

## Siguiente

[L03 — TCP vs UDP y puertos bien usados](L03-tcp-vs-udp-y-puertos-bien-usados.md)
