---
id: L08
materia: M20
orden: 8
titulo: 'Roles: confiar en la API, no solo en UI'
horas: 5
semana: 2
lectura: RBAC móvil
evidencia: nota rbac en demo-login-lista.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Probar cuenta staff vs owner; ocultar acciones que API niega
      con 403.


      - 403 handling

      - roles
  - id: s2
    tipo: ejemplo
    titulo: 1. Confía en API para RBAC
    xp: 10
    cuerpo: >-
      ```bash

      # staff token → acción owner debe fallar 403 aunque el botón exista

      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Roles: confiar en la API, no solo en UI" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: nota rbac en demo-login-lista.md
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"`
    comandoEsperado:
      - >-
        curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
        "$API_BASE/admin/staff"
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Probar cuenta staff vs owner; ocultar acciones que API niega con 403.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Nota rbac
    xp: 10
    cuerpo: |-
      ```bash
      cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Nota RBAC: UI puede ocultar; 403 de API verificado (staff vs owner).'
      - 'Commit `docs(m20): L08 roles-confiar-en-la-api-no-solo-en-ui`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Roles: confiar en la API, no solo en UI

**~5.0 h · Semana 2**

Doble fuente de verdad mata proyectos.

## Objetivo

Probar cuenta staff vs owner; ocultar acciones que API niega con 403.

## Conceptos clave

- 403 handling
- roles

## Pasos (hazlos en orden)

### 1. Confía en API para RBAC (50–60 min)

```bash
# staff token → acción owner debe fallar 403 aunque el botón exista
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" "$API_BASE/admin/staff"
```

### 2. Nota rbac (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## RBAC
UI puede ocultar; autorización real = API 403. Probado: …
EOF
git add projects/m20-movil/demo-login-lista.md
git commit -m "docs(m20): L08 roles confiar en api"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | RBAC móvil | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Nota RBAC: UI puede ocultar; 403 de API verificado (staff vs owner).
2. Commit `docs(m20): L08 roles-confiar-en-la-api-no-solo-en-ui`.

## Errores comunes

- Ocultar botón y creer que es seguridad.
- Ignorar 403 de la API.

## Siguiente

[L09 — Pantalla detalle de pedido](L09-pantalla-detalle-de-pedido.md)
