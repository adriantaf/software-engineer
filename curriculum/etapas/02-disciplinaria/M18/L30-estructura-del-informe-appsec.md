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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El entregable del proyecto es el informe: ejecutivo, alcance, hallazgos,
      mitigaciones, residual.


      **Objetivo de esta lección:** Borrador
      `projects/m18-appsec/informe-appsec.md` enlazando PoCs y commits (sin PII
      de partner).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Plantilla
    xp: 10
    cuerpo: >-
      ```bash cat > projects/m18-appsec/informe-appsec.md <<'EOF' # Informe
      AppSec — Vitrina
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Estructura del informe AppSec», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Estructura del informe
          AppSec
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “Informe sin hallazgos reales."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
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
          Borrador `projects/m18-appsec/informe-appsec.md` enlazando PoCs y
          commits (sin PII de partner).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Copiar OWASP sin contexto."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
