---
id: L02
materia: M10
orden: 2
titulo: 'IP, direccionamiento y enrutamiento intro'
horas: 5
semana: 1
lectura: 'Tanenbaum: capa de red — IPv4, máscaras, routing básico'
evidencia: 'labs/semana-01.md: IP local, gateway, traceroute resumido'
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      HTTP no “viaja solo”: alguien elige el siguiente hop. Hoy lees tu propia
      mesa de enrutamiento.


      **Objetivo de esta lección:** Documentar dirección local, gateway y un
      traceroute resumido hacia un host público.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario de interfaces
    xp: 10
    cuerpo: >-
      ```bash

      ip -br addr

      ip route

      ```


      En `projects/m10-redes/labs/semana-01.md` anota: interfaz, IPv4/CIDR,
      default gateway. Si usas macOS: `ifconfig` + `netstat -rn`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Lectura dirigida
    xp: 10
    cuerpo: |-
      ```bash
      # Linux:
      traceroute -n example.com | head -20
      # o
      tracepath example.com | head -20
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «IP, direccionamiento y enrutamiento intro», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de IP, direccionamiento y
          enrutamiento int…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git add projects/m10-redes/labs/semana-01.md`
    comandoEsperado:
      - git add projects/m10-redes/labs/semana-01.md
      - 'git commit -m "docs(m10): l02 ip y enrutamiento"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m10-redes/labs/semana-01.md'
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Documentar dirección local, gateway y un traceroute resumido hacia un
          host público.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Traceroute
    xp: 10
    cuerpo: >-
      Tabla: hop | RTT aprox | nota (timeout / ISP / destino). Relaciona “salto”
      con “router que decide”.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/semana-01.md` con IP local, máscara/CIDR, gateway y 3–5 hops de
        traceroute (o `tracepath`/`mtr`).
      - Explicas en 5 líneas qué problema resuelve IP vs qué resuelve TCP.
      - 'Commit `docs(m10): l02 ip y enrutamiento`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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

### 4. Hipótesis Vitrina (25 min)

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
- Olvidar que el API de Vitrina tendrá IP pública *y* ruta interna en compose.

## Siguiente

[L03 — TCP vs UDP y puertos bien usados](L03-tcp-vs-udp-y-puertos-bien-usados.md)
