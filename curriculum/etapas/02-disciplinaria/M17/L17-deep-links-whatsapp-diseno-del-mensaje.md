---
id: L17
materia: M17
orden: 17
titulo: Deep links WhatsApp — diseño del mensaje
horas: 5
semana: 5
lectura: Docs proveedor WhatsApp
evidencia: projects/m17-vitrina/docs/integracion-whatsapp.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir plantilla mensaje recordatorio/confirmación con
      placeholders y enlace wa.me.


      - deep link

      - plantilla

      - PII mínima
  - id: s2
    tipo: ejemplo
    titulo: 1. Diseña mensaje wa.me
    xp: 10
    cuerpo: |-
      ```ts
      export function whatsappReminderUrl(phoneE164: string, text: string) {
        const n = phoneE164.replace(/\\D/g, "");
        return `https://wa.me/${n}?text=${encodeURIComponent(text)}`;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Deep links WhatsApp — diseño del mensaje" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m17-vitrina/docs/integracion-whatsapp.md
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
    pregunta: ¿Es buena práctica en esta lección? “Pegar teléfonos reales en el repo."
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
          Definir plantilla mensaje recordatorio/confirmación con placeholders y
          enlace wa.me.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Helper URL encoder
    xp: 10
    cuerpo: |-
      ```ts
      export function whatsappReminderUrl(phoneE164: string, text: string) {
        const n = phoneE164.replace(/\\D/g, "");
        return `https://wa.me/${n}?text=${encodeURIComponent(text)}`;
      }
      ```

      ```bash
      npm test -- whatsapp
      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina
      git commit -m "docs(m17): L17 deep links whatsapp mensaje"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m17-vitrina/docs/integracion-whatsapp.md` define plantilla
        wa.me + helper testeado.
      - 'Commit `docs(m17): L17 deep-links-whatsapp-diseno-del-mensaje`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — Deep links WhatsApp — diseño del mensaje

**~5.0 h · Semana 5**

Canal que el design partner ya usa.

## Objetivo

Definir plantilla mensaje recordatorio/confirmación con placeholders y enlace wa.me.

## Conceptos clave

- deep link
- plantilla
- PII mínima

## Pasos (hazlos en orden)

### 1. Diseña mensaje wa.me (50–60 min)

```bash
# plantilla (sin PII real en git):
# https://wa.me/52XXXXXXXXXX?text=Hola%20...%20cita%20...
```

Documenta en `projects/m17-vitrina/docs/integracion-whatsapp.md` campos: nombre, fecha, deep link ficha.

### 2. Helper URL encoder (40–50 min)

```ts
export function whatsappReminderUrl(phoneE164: string, text: string) {
  const n = phoneE164.replace(/\\D/g, "");
  return `https://wa.me/${n}?text=${encodeURIComponent(text)}`;
}
```

```bash
npm test -- whatsapp
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina
git commit -m "docs(m17): L17 deep links whatsapp mensaje"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Docs proveedor WhatsApp | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/integracion-whatsapp.md` define plantilla wa.me + helper testeado.
2. Commit `docs(m17): L17 deep-links-whatsapp-diseno-del-mensaje`.

## Errores comunes

- Pegar teléfonos reales en el repo.
- Texto wa.me sin `encodeURIComponent`.

## Siguiente

[L18 — Botón enviar recordatorio desde ficha pedido](L18-boton-enviar-recordatorio-desde-ficha-pedido.md)
