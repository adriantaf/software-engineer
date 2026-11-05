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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir activación 7d, pedidos creadas/semana y trials
      activos con fórmula y fuente de datos.


      M23 y M22 comparten métricas accionables; sin definición clara los CSV
      mienten.


      Conceptos que debes poder explicar al cerrar:


      - Activación.

      - tenant_id.

      - Vanity vs accionable.

      - Ventana temporal.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tres métricas SaaS por tenant — definiciones" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m23-ia/metricas/definiciones.md
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

      `mkdir -p projects/m23-ia/{metricas,llm-eval,rag}`
    comandoEsperado:
      - 'mkdir -p projects/m23-ia/{metricas,llm-eval,rag}'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m23-ia/{metricas,llm-eval,rag}'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Definir activación 7d, pedidos creadas/semana y trials activos con
          fórmula y fuente de datos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m23-ia/{metricas,llm-eval,rag}
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
