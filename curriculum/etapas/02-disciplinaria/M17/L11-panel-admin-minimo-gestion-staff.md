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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - admin

      - invitación

      - UX claro


      **Objetivo de esta lección:** Pantalla admin: listar staff, invitar o
      crear staff (según SRS), solo owner.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Ruta /admin mínima
    xp: 10
    cuerpo: >-
      ```bash

      curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff

      curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      http://localhost:3000/admin/staff

      # 403

      ```


      UI o API: listar staff, invitar/desactivar. Solo owner.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Evidencia + commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina
      git commit -m "feat(m17): L11 panel admin staff"
      ```

      Anota URL/ruta en `docs/permisos.md` o captura redactada en `docs/`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Panel admin mínimo — gestión staff», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Panel admin mínimo —
          gestión staff
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

      `curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff`
    comandoEsperado:
      - 'curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff'
      - >-
        curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
        http://localhost:3000/admin/staff
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS -b /tmp/ao.ck http://localhost:3000/admin/staff'
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
          Pantalla admin: listar staff, invitar o crear staff (según SRS), solo
          owner.
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
    enunciado: >-
      Ahora el siguiente comando de la secuencia:


      `curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      http://localhost:3000/admin/staff`
    comandoEsperado:
      - >-
        curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
        http://localhost:3000/admin/staff
    explicacionError: >-
      Esperado: curl -sS -b /tmp/staff.ck -o /dev/null -w "%{http_code}\n"
      http://localhost:3000/admin/staff
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Ruta `/admin` (o equiv.) lista/gestiona staff; staff recibe 403.
      - 'Commit `docs(m17): L11 panel-admin-minimo-gestion-staff`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
