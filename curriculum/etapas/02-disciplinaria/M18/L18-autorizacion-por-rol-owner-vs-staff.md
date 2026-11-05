---
id: L18
materia: M18
orden: 18
titulo: Autorización por rol owner vs staff
horas: 5
semana: 5
lectura: Access Control Cheat Sheet
evidencia: projects/m18-appsec/docs/rbac-matrix.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Vitrina distingue dueño y staff; la API debe hacerlo explícito.


      **Objetivo de esta lección:** Matriz rol×recurso×acción en
      `projects/m18-appsec/docs/rbac-matrix.md` + ≥1 prueba manual de gap.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Matriz RBAC
    xp: 10
    cuerpo: >-
      ```bash cat > projects/m18-appsec/docs/rbac-matrix.md <<'EOF' # RBAC —
      Vitrina | Recurso / acción | Owner | Staff | Anónimo |
      |------------------|-------|-------|---------| | Listar pedidos | ✓ | ✓
      (alcance) | ✗ | | Crear pedido | ✓ | ✓ | ✗ | | Borrar cualquier pedido | ✓
      | ? | ✗ | | Configuración negocio | ✓ | ✗ | ✗ | | Gestionar usuarios | ✓ |
      ✗ | ✗ |
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Autorización por rol owner vs staff», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Autorización por rol
          owner vs staff
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
    pregunta: ¿Es recomendable en esta lección? “Un solo rol ‘admin’."
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
          Matriz rol×recurso×acción en `projects/m18-appsec/docs/rbac-matrix.md`
          + ≥1 prueba manual de gap.
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
    pregunta: ¿Debes hacer esto? “404 para esconder sin authz."
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
      - 'Matriz completa (artefacto: `projects/m18-appsec/docs/rbac-matrix.md`).'
      - >-
        ≥1 prueba manual rol (artefacto:
        `projects/m18-appsec/docs/rbac-matrix.md`).
      - 'Commit `docs(m18): L18 autorizacion-por-rol-owner-vs-staff`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Autorización por rol owner vs staff

**~5.0 h · Semana 5**

Vitrina distingue dueño y staff; la API debe hacerlo explícito.

## Objetivo

Matriz rol×recurso×acción en `projects/m18-appsec/docs/rbac-matrix.md` + ≥1 prueba manual de gap.

## Pasos

### 1. Matriz RBAC (50–60 min)

```bash
cat > projects/m18-appsec/docs/rbac-matrix.md <<'EOF'
# RBAC — Vitrina
| Recurso / acción | Owner | Staff | Anónimo |
|------------------|-------|-------|---------|
| Listar pedidos | ✓ | ✓ (alcance) | ✗ |
| Crear pedido | ✓ | ✓ | ✗ |
| Borrar cualquier pedido | ✓ | ? | ✗ |
| Configuración negocio | ✓ | ✗ | ✗ |
| Gestionar usuarios | ✓ | ✗ | ✗ |

## Gaps código vs SRS
- …
## Prueba manual
- Actor: staff · Acción: … · Resultado HTTP: …
EOF
```
### 2. Prueba staff vs owner (50–70 min)

```bash
curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-staff \
  -X PATCH localhost:3000/api/settings -H 'content-type: application/json' -d '{"tz":"UTC"}'
# esperado: 403
```

```ts
// guard ilustrativo
if (req.user.role !== "owner") return res.status(403).json({ error: "forbidden" });
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/rbac-matrix.md
git commit -m "docs(m18): l18 rbac matrix"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Access Control Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Matriz completa (artefacto: `projects/m18-appsec/docs/rbac-matrix.md`).
2. ≥1 prueba manual rol (artefacto: `projects/m18-appsec/docs/rbac-matrix.md`).
3. Commit `docs(m18): L18 autorizacion-por-rol-owner-vs-staff`.

## Errores comunes

- Un solo rol ‘admin’.
- 404 para esconder sin authz.

## Siguiente

[L19 — Rate limiting en login y endpoints sensibles](L19-rate-limiting-en-login-y-endpoints-sensibles.md)
