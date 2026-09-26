---
id: L02
materia: M10
orden: 2
titulo: IP, direccionamiento y enrutamiento intro
horas: 5
semana: 1
lectura: "Tanenbaum — capa de red (IPv4, máscaras, routing básico)"
evidencia: "notas en semana-01.md: IP local, gateway, traceroute resumido"
---

# L02 — IP, direccionamiento y enrutamiento intro

**~5 h · Semana 1**

## Objetivo

Leer tu configuración IP local y explicar hop-by-hop qué hace un paquete hacia un host público.

## Por qué importa

Timeouts y “no llega al servidor” empiezan en routing o DNS; hoy practicas observación antes de culpar al código.

## Conceptos

- IPv4 y CIDR a nivel ingeniero.
- Default gateway.
- MTU (idea).
- ICMP y `ping` como señal, no como prueba definitiva.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
ip addr show | head -40    # o ifconfig en macOS
ip route | head
ping -c 3 1.1.1.1
traceroute -m 12 example.com 2>/dev/null | head -15 || tracepath example.com | head -15
```

Documenta IP, máscara y gateway. ¿Cuántos saltos hasta `example.com`?

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l02 ip-direccionamiento-y-enrutamiento-intro"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Tanenbaum | Capa de red (IP) | Labs anteriores + apuntes |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Tabla IP/gateway en bitácora.
2. Salida resumida de traceroute.
3. Explicas diferencia IP pública vs privada.

## Errores comunes

- Asumir que `ping` falla implica que HTTP fallará igual.
- Publicar capturas con IPs internas de producción.

## Siguiente

[L03 — TCP vs UDP y puertos bien usados](L03-tcp-vs-udp-y-puertos-bien-usados.md)
