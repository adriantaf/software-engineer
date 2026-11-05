---
id: L30
materia: M18
orden: 30
titulo: Estructura del informe AppSec
horas: 5
semana: 8
lectura: Reporting + risk rating
evidencia: projects/m18-appsec/informe-appsec.md (borrador)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Borrador `projects/m18-appsec/informe-appsec.md` enlazando
      PoCs y commits (sin PII de partner).


      El entregable del proyecto es el informe: ejecutivo, alcance, hallazgos,
      mitigaciones, residual.
  - id: s2
    tipo: ejemplo
    titulo: 1. Plantilla
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m18-appsec/informe-appsec.md <<'EOF'
      Informe AppSec — Vitrina
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Estructura del informe AppSec" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/informe-appsec.md (borrador)
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “Informe sin hallazgos reales."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Borrador `projects/m18-appsec/informe-appsec.md` enlazando PoCs y
          commits (sin PII de partner).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Borrador ≥4 secciones (artefacto: `projects/m18-appsec/informe-appsec.md
        (borrador)`).
      - >-
        Enlaces internos (artefacto: `projects/m18-appsec/informe-appsec.md
        (borrador)`).
      - 'Commit `docs(m18): L30 estructura-del-informe-appsec`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L30 — Estructura del informe AppSec

**~5.0 h · Semana 8**

El entregable del proyecto es el informe: ejecutivo, alcance, hallazgos, mitigaciones, residual.

## Objetivo

Borrador `projects/m18-appsec/informe-appsec.md` enlazando PoCs y commits (sin PII de partner).

## Pasos

### 1. Plantilla (25–35 min)

```bash
cat > projects/m18-appsec/informe-appsec.md <<'EOF'
# Informe AppSec — Vitrina

## 1. Ejecutivo
- …

## 2. Alcance y supuestos
- Solo staging/local propio
- Fuera de alcance: …

## 3. Metodología
STRIDE + OWASP Top 10 + PoC en API propia

## 4. Hallazgos
Tabla → ver findings-table.md (severidad, estado)

## 5. Mitigaciones
Commits / PRs: …

## 6. Riesgo residual
Top 3 con dueño/fecha

## 7. Anexos
- threat-model-v1.md
- docs/auth-inventario.md
- ci/
EOF
```
### 2. Redacción con enlaces (90–110 min)

Rellena §§1–6 con datos reales de tu P2/P3. Verifica que no hay secretos ni teléfonos reales.

```bash
rg -n 'password|Bearer |postgresql://|@gmail' projects/m18-appsec/informe-appsec.md || echo "sin secretos obvios"
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/informe-appsec.md
git commit -m "docs(m18): l30 informe appsec"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Reporting + risk rating | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Borrador ≥4 secciones (artefacto: `projects/m18-appsec/informe-appsec.md (borrador)`).
2. Enlaces internos (artefacto: `projects/m18-appsec/informe-appsec.md (borrador)`).
3. Commit `docs(m18): L30 estructura-del-informe-appsec`.

## Errores comunes

- Informe sin hallazgos reales.
- Copiar OWASP sin contexto.

## Siguiente

[L31 — Tests de regresión de seguridad (≥3)](L31-tests-de-regresion-de-seguridad-3.md)
