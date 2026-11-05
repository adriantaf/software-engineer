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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Tabla: cada riesgo → mitigación actual o gap hacia M18.

      - OWASP
      - gap
      - mitigación
  - id: s2
    tipo: ejemplo
    titulo: 1. Mapa OWASP Top 10
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Mapa OWASP Top 10 en el piloto" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/owasp-mapa.md
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

      `git add projects/m17-vitrina/docs/owasp-mapa.md`
    comandoEsperado:
      - git add projects/m17-vitrina/docs/owasp-mapa.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m17-vitrina/docs/owasp-mapa.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Tabla: cada riesgo → mitigación actual o gap hacia M18.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/owasp-mapa.md
      git commit -m "docs(m17): L25 mapa owasp top10"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/owasp-mapa.md` cubre ≥A01–A05 con control o
        gap.
      - 'Commit `docs(m17): L25 mapa-owasp-top-10-en-el-piloto`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
