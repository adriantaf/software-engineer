---
id: L25
materia: M17
orden: 25
titulo: Mapa OWASP Top 10 en el piloto
horas: 5
semana: 7
lectura: OWASP Top 10 overview
evidencia: projects/m17-vitrina/docs/owasp-mapa.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - OWASP

      - gap

      - mitigación


      **Objetivo de esta lección:** Tabla: cada riesgo → mitigación actual o gap
      hacia M18.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Mapa OWASP Top 10
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m17-vitrina/docs/owasp-mapa.md << 'EOF'
      # OWASP Top 10 → Vitrina
      | Riesgo | ¿Aplica? | Control en piloto | Gap |
      |--------|----------|-------------------|-----|
      | A01 Broken Access Control | sí | authorize()+tests 403 | |
      | A02 Cryptographic Failures | sí | bcrypt + HTTPS | |
      EOF
      ```

      Cubre al menos A01–A05 con evidencia (ruta de test o doc).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/owasp-mapa.md
      git commit -m "docs(m17): L25 mapa owasp top10"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Mapa OWASP Top 10 en el piloto», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Mapa OWASP Top 10 en el
          piloto
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

      `git add projects/m17-vitrina/docs/owasp-mapa.md`
    comandoEsperado:
      - git add projects/m17-vitrina/docs/owasp-mapa.md
      - 'git commit -m "docs(m17): L25 mapa owasp top10"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m17-vitrina/docs/owasp-mapa.md'
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
        texto: 'Tabla: cada riesgo → mitigación actual o gap hacia M18.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git commit -m "docs(m17): L25 mapa owasp top10"`
    comandoEsperado:
      - 'git commit -m "docs(m17): L25 mapa owasp top10"'
    explicacionError: 'Esperado: git commit -m "docs(m17): L25 mapa owasp top10"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/owasp-mapa.md` cubre ≥A01–A05 con control o
        gap.
      - 'Commit `docs(m17): L25 mapa-owasp-top-10-en-el-piloto`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L25 — Mapa OWASP Top 10 en el piloto

**~5.0 h · Semana 7**

M18 profundiza; hoy ubicas huecos.

## Objetivo

Tabla: cada riesgo → mitigación actual o gap hacia M18.

## Conceptos clave

- OWASP
- gap
- mitigación

## Pasos (hazlos en orden)

### 1. Mapa OWASP Top 10 (80–100 min)

```bash
cat > projects/m17-vitrina/docs/owasp-mapa.md << 'EOF'
# OWASP Top 10 → Vitrina
| Riesgo | ¿Aplica? | Control en piloto | Gap |
|--------|----------|-------------------|-----|
| A01 Broken Access Control | sí | authorize()+tests 403 | |
| A02 Cryptographic Failures | sí | bcrypt + HTTPS | |
EOF
```

Cubre al menos A01–A05 con evidencia (ruta de test o doc).

### 2. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/owasp-mapa.md
git commit -m "docs(m17): L25 mapa owasp top10"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP Top 10 overview | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/owasp-mapa.md` cubre ≥A01–A05 con control o gap.
2. Commit `docs(m17): L25 mapa-owasp-top-10-en-el-piloto`.

## Errores comunes

- Tabla OWASP vacía o copy-paste sin controles del repo.
- Ignorar Broken Access Control.

## Siguiente

[L26 — Headers de seguridad y CORS prod](L26-headers-de-seguridad-y-cors-prod.md)
