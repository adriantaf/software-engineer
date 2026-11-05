---
id: L11
materia: M10
orden: 11
titulo: Lab openssl y pinning conceptual
horas: 5
semana: 3
lectura: MDN certificate pinning (advertencias) + hilo seguridad
evidencia: labs/openssl-lab.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Huella y pinning son herramientas de **confianza extra**, no magia. Hoy
      las documentas con cuidado.


      **Objetivo de esta lección:** Calcular fingerprint y escribir cuándo el
      pinning tiene sentido (y cuándo no) para Vitrina.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Fingerprint
    xp: 10
    cuerpo: >-
      ```bash

      echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \
        | openssl x509 -fingerprint -sha256 -noout
      ```


      Guarda en `labs/openssl-lab.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Exportar PEM de estudio
    xp: 10
    cuerpo: >-
      ```bash

      echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \
        | openssl x509 -out projects/m10-redes/samples/example-leaf.pem
      openssl x509 -in projects/m10-redes/samples/example-leaf.pem -noout -text
      | head -40

      ```


      Solo cert público — **nunca** claves privadas de tu producto en git.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lab openssl y pinning conceptual», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lab openssl y pinning
          conceptual
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `echo | openssl s_client -connect example.com:443 -servername example.com
      2>/dev/null \`
    comandoEsperado:
      - >-
        echo | openssl s_client -connect example.com:443 -servername example.com
        2>/dev/null \
      - >-
        git add projects/m10-redes/labs/openssl-lab.md
        projects/m10-redes/samples
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: echo | openssl s_client -connect example.com:443 -servername
      example.com 2>/dev/null \
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
          Calcular fingerprint y escribir cuándo el pinning tiene sentido (y
          cuándo no) para Vitrina.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Pinning conceptual
    xp: 10
    cuerpo: >-
      Escribe: (a) mobile/API crítica con pin + backup pin; (b) por qué rotar
      leaf sin backup rompe clientes; (c) alternativa: Certificate Transparency
      + buena validación de cadena + HSTS.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `labs/openssl-lab.md` con fingerprint SHA256 del leaf de un sitio +
        comandos reproducibles.
      - 'Nota de pinning: beneficio vs riesgo operacional (rotación CA/leaf).'
      - 'Commit `docs(m10): l11 openssl pinning`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Lab openssl y pinning conceptual

**~5.0 h · Semana 3**

Huella y pinning son herramientas de **confianza extra**, no magia. Hoy las documentas con cuidado.

## Objetivo

Calcular fingerprint y escribir cuándo el pinning tiene sentido (y cuándo no) para Vitrina.

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

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | Huella del cert; pinning: cuándo ayuda y cómo duele en rotación | [Hilo seguridad](../../../hilos/seguridad.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `labs/openssl-lab.md` con fingerprint SHA256 del leaf de un sitio + comandos reproducibles.
2. Nota de pinning: beneficio vs riesgo operacional (rotación CA/leaf).
3. Commit `docs(m10): l11 openssl pinning`.

## Errores comunes

- Recomendar pinning ciego en una app web típica sin plan de rotación.
- Tratar pinning como sustituto de validación de cadena.
- Publicar material de “cómo hacer MITM” ofensivo — aquí solo defensa conceptual.

## Siguiente

[L12 — MITM conceptual y amenazas de enlace](L12-mitm-conceptual-y-amenazas-de-enlace.md)
