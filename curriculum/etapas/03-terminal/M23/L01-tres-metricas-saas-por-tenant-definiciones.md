---
id: L01
materia: M23
orden: 1
titulo: Tres métricas SaaS por tenant — definiciones
horas: 5
semana: 1
lectura: producto-saas + notas métricas M23
evidencia: projects/m23-ia/metricas/definiciones.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M23 y M22 comparten métricas accionables; sin definición clara los CSV
      mienten.


      Conceptos que debes poder explicar al cerrar:


      - Activación.

      - tenant_id.

      - Vanity vs accionable.

      - Ventana temporal.


      **Objetivo de esta lección:** Definir activación 7d, pedidos
      creadas/semana y trials activos con fórmula y fuente de datos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tres métricas SaaS por tenant — definiciones», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tres métricas SaaS por
          tenant — definic…
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

      `mkdir -p projects/m23-ia/{metricas,llm-eval,rag}`
    comandoEsperado:
      - 'mkdir -p projects/m23-ia/{metricas,llm-eval,rag}'
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m23-ia/{metricas,llm-eval,rag}'
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
          Definir activación 7d, pedidos creadas/semana y trials activos con
          fórmula y fuente de datos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: >-
      En `projects/m23-ia/metricas/definiciones.md` documenta ≥3 métricas con
      fórmula, numerador/denominador, frecuencia, anti-PII.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/metricas/definiciones.md`.'
      - definiciones.md ≥3 métricas.
      - Fórmulas explícitas.
      - Anti-PII.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Tres métricas SaaS por tenant — definiciones

**~5 h · Semana 1**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/metricas/definiciones.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Definir activación 7d, pedidos creadas/semana y trials activos con fórmula y fuente de datos.

## Por qué empieza así

M23 y M22 comparten métricas accionables; sin definición clara los CSV mienten.

Conceptos que debes poder explicar al cerrar:

- Activación.
- tenant_id.
- Vanity vs accionable.
- Ventana temporal.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _producto-saas + notas métricas M23_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

```bash
mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
```

### 3. Laboratorio principal (90–120 min)

En `projects/m23-ia/metricas/definiciones.md` documenta ≥3 métricas con fórmula, numerador/denominador, frecuencia, anti-PII.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l01 tres-m-tricas-saas-por-tenant-definicion"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | producto-saas + notas métricas M23 | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/metricas/definiciones.md`.
2. definiciones.md ≥3 métricas.
3. Fórmulas explícitas.
4. Anti-PII.
5. Commit `docs(m23): l01 …` en el historial.

## Errores comunes

- Métrica sin fórmula.
- Mezclar tenants en definición.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — Consulta agregada por tenant_id sin PII](L02-consulta-agregada-por-tenant-id-sin-pii.md)
