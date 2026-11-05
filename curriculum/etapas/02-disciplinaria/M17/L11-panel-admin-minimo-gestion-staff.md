---
id: L11
materia: M17
orden: 11
titulo: Panel admin mínimo — gestión staff
horas: 5
semana: 3
lectura: UI admin sin adornos
evidencia: ruta /admin o equivalente
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Pantalla admin: listar staff, invitar o crear staff (según
      SRS), solo owner.


      - admin

      - invitación

      - UX claro
  - id: s2
    tipo: ejemplo
    titulo: 1. Ruta /admin mínima
    xp: 10
    cuerpo: >-
      ```bash

      curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff

      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      http://localhost:3000/admin/staff

      # 403

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Panel admin mínimo — gestión staff" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: ruta /admin o equivalente
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

      `curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff`
    comandoEsperado:
      - 'curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Pantalla admin: listar staff, invitar o crear staff (según SRS), solo
          owner.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Evidencia + commit
    xp: 10
    cuerpo: |-
      Anota URL/ruta en `docs/permisos.md` o captura redactada en `docs/`.

      ```bash
      git add projects/m17-vitrina
      git commit -m "feat(m17): L11 panel admin staff"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Ruta `/admin` (o equiv.) lista/gestiona staff; staff recibe 403.
      - 'Commit `docs(m17): L11 panel-admin-minimo-gestion-staff`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Panel admin mínimo — gestión staff

**~5.0 h · Semana 3**

El dueño del negocio administra su equipo aquí.

## Objetivo

Pantalla admin: listar staff, invitar o crear staff (según SRS), solo owner.

## Conceptos clave

- admin
- invitación
- UX claro

## Pasos (hazlos en orden)

### 1. Ruta /admin mínima (70–90 min)

UI o API: listar staff, invitar/desactivar. Solo owner.

```bash
curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff
curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n" http://localhost:3000/admin/staff
# 403
```

### 2. Evidencia + commit (40 min)

Anota URL/ruta en `docs/permisos.md` o captura redactada en `docs/`.

```bash
git add projects/m17-vitrina
git commit -m "feat(m17): L11 panel admin staff"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | UI admin sin adornos | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Ruta `/admin` (o equiv.) lista/gestiona staff; staff recibe 403.
2. Commit `docs(m17): L11 panel-admin-minimo-gestion-staff`.

## Errores comunes

- Admin usable por staff.
- Invitar staff sin audit/nota.

## Siguiente

[L12 — Demo roles y inicio P3 WhatsApp](L12-demo-roles-y-inicio-p3-whatsapp.md)
