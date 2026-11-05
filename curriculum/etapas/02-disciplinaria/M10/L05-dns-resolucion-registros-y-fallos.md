---
id: L05
materia: M10
orden: 5
titulo: 'DNS: resolución, registros y fallos'
horas: 5
semana: 2
lectura: Tanenbaum DNS + MDN DNS overview
evidencia: labs/semana-02-dns.md con dig/host
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Usar `dig`/`host` y documentar registros y modos de fallo.


      Antes de TCP hay un nombre. Si DNS miente o tarda, Vitrina “no carga”
      aunque la API esté viva.
  - id: s2
    tipo: ejemplo
    titulo: 1. Herramientas
    xp: 10
    cuerpo: |-
      ```bash
      which dig host getent || true
      dig -v 2>&1 | head -1
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "DNS: resolución, registros y fallos" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: labs/semana-02-dns.md con dig/host
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/m10-redes/labs/semana-02-dns.md`
    comandoEsperado:
      - git add projects/m10-redes/labs/semana-02-dns.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m10-redes/labs/semana-02-dns.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Usar `dig`/`host` y documentar registros y modos de fallo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Labs de registros
    xp: 10
    cuerpo: >-
      ```bash

      dig example.com A +noall +answer

      dig example.com AAAA +short

      dig www.github.com CNAME +short

      host -a example.com | head -30

      ```


      En `projects/m10-redes/labs/semana-02-dns.md`: qué es A vs CNAME; qué
      harías con un TXT de verificación.
  - id: s7
    tipo: ejemplo
    titulo: 3. Fallos
    xp: 10
    cuerpo: |-
      ```bash
      getent hosts example.com
      ping -c 1 $(dig +short example.com A | head -1)
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/semana-02-dns.md` con salida anotada de `dig`/`host` (A/AAAA/CNAME
        al menos).
      - >-
        Escenario escrito: “DNS falla pero ping a IP funciona” — cómo lo
        detectas.
      - 'Commit `docs(m10): l05 dns dig`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — DNS: resolución, registros y fallos

**~5.0 h · Semana 2**

Antes de TCP hay un nombre. Si DNS miente o tarda, Vitrina “no carga” aunque la API esté viva.

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Resolución recursiva, A/AAAA/CNAME/MX/TXT, TTL y fallos típicos | [MDN · DNS (concepto)](https://developer.mozilla.org/es/docs/Glossary/DNS) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/semana-02-dns.md` con salida anotada de `dig`/`host` (A/AAAA/CNAME al menos).
2. Escenario escrito: “DNS falla pero ping a IP funciona” — cómo lo detectas.
3. Commit `docs(m10): l05 dns dig`.

## Errores comunes

- Confundir “no resuelve” con “el servidor HTTP está caído”.
- Ignorar TTL cuando “ya cambié el DNS y no veo el cambio”.
- Pegar dig sin decir qué registro buscabas.

## Siguiente

[L06 — HTTP mensajes, métodos y semántica](L06-http-mensajes-metodos-y-semantica.md)
