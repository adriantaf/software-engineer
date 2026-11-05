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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - 403 handling

      - roles


      **Objetivo de esta lección:** Probar cuenta staff vs owner; ocultar
      acciones que API niega con 403.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Confía en API para RBAC
    xp: 10
    cuerpo: >-
      ```bash

      # staff token → acción owner debe fallar 403 aunque el botón exista

      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Nota rbac
    xp: 10
    cuerpo: >-
      ```bash

      # staff token → acción owner debe fallar 403 aunque el botón exista

      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Roles: confiar en la API, no solo en UI», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Roles: confiar en la
          API, no solo en UI
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


      `curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"`
    comandoEsperado:
      - >-
        curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
        "$API_BASE/admin/staff"
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      "$API_BASE/admin/staff"
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
        texto: Probar cuenta staff vs owner; ocultar acciones que API niega con 403.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Ignorar 403 de la API."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Nota RBAC: UI puede ocultar; 403 de API verificado (staff vs owner).'
      - 'Commit `docs(m20): L08 roles-confiar-en-la-api-no-solo-en-ui`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
