---
id: L05
materia: M23
orden: 5
titulo: Política de datos LLM antes de prompts
horas: 5
semana: 2
lectura: Ética/datos + vendor LLM terms
evidencia: projects/m23-ia/politica-datos-llm.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar política: qué nunca enviar a LLM, retención logs,
      filtro tenant, incidentes.


      Regla M23: política **antes** de pegar datos en ChatGPT ‘solo probar’.


      Conceptos que debes poder explicar al cerrar:


      - PII.

      - Retención.

      - Tenant scope.

      - Incident response.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l05 pol-tica-de-datos-llm-antes-de-prompts"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Política de datos LLM antes de prompts" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m23-ia/politica-datos-llm.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Redactar política: qué nunca enviar a LLM, retención logs, filtro
          tenant, incidentes.
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
    cuerpo: >-
      Confirma rutas bajo `projects/m23-ia`.


      Completa `projects/m23-ia/politica-datos-llm.md` (≥1 página): prohibidos,
      permitidos anonimizados, logs, borrado, responsable.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Enlaza [hilo seguridad](../../hilos/seguridad.md). Commit antes de
      cualquier script que llame API.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/politica-datos-llm.md`.'
      - Política completa.
      - Commit previo a scripts.
      - Enlace seguridad.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Política de datos LLM antes de prompts

**~5 h · Semana 2**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/politica-datos-llm.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Redactar política: qué nunca enviar a LLM, retención logs, filtro tenant, incidentes.

## Por qué empieza así

Regla M23: política **antes** de pegar datos en ChatGPT ‘solo probar’.

Conceptos que debes poder explicar al cerrar:

- PII.
- Retención.
- Tenant scope.
- Incident response.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Ética/datos + vendor LLM terms_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia`.

Completa `projects/m23-ia/politica-datos-llm.md` (≥1 página): prohibidos, permitidos anonimizados, logs, borrado, responsable.

### 3. Laboratorio principal (90–120 min)

Enlaza [hilo seguridad](../../hilos/seguridad.md). Commit antes de cualquier script que llame API.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l05 pol-tica-de-datos-llm-antes-de-prompts"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Ética/datos + vendor LLM terms | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/politica-datos-llm.md`.
2. Política completa.
3. Commit previo a scripts.
4. Enlace seguridad.

## Errores comunes

- Política post-hoc.
- Permitir dumps BD.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Set gold de 10 preguntas FAQ del ICP](L06-set-gold-de-10-preguntas-faq-del-icp.md)
