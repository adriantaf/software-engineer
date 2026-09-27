---
id: L04
materia: M03
orden: 4
titulo: Métodos de demostración (intro)
horas: 3
semana: 1
lectura: "Rosen Cap. 1.6–1.7 — directa, contrapositiva, contradicción, casos (intro)"
evidencia: "demos.md con 3 demostraciones numeradas (directa, contrapositiva, casos)"
---

# L04 — Métodos de demostración (intro)

**~3 h · Semana 1**

Cierras la semana de lógica escribiendo **pruebas** legibles. Esto alimenta **P1** del resto del módulo.

## Objetivo

Redactar tres demostraciones cortas con estructura clara (hipótesis → conclusiones); elegir directa, contrapositiva o por casos según el enunciado.

## Estructura de una prueba

1. **Enunciado** (lo que se demuestra).
2. **Prueba:** frases que justifican cada paso (no solo “obvio”).
3. **QED** o cierre explícito.

## Pasos

### 1. Plantilla (15 min)

Crea `projects/m03-discretas/demos.md`:

```markdown
# Demostraciones — M03

## Demo 1 — (título)
**Enunciado:**
**Prueba:**

## Demo 2 — …
```

### 2. Demostración directa (45–50 min)

Ejemplo tipo (o equivalente del Rosen):

- Si `n` es entero par, entonces `n²` es par.

O: si `a | b` y `b | c`, entonces `a | c` (divisibilidad).

Escribe la prueba completa en `demos.md` como **Demo 1**.

### 3. Contrapositiva (45–50 min)

Demuestra un enunciado del estilo “si `n²` es impar, entonces `n` es impar” usando **contrapositiva** explícita (“supongamos que `n` es par…”). **Demo 2**.

Relaciona con L02: `(P → Q) ↔ (¬Q → ¬P)`.

### 4. Por casos (40–50 min)

Enunciado finito de casos, p. ej. restos módulo 3, o “entero `n` no es divisible por 2 ni por 3” (casos pequeños). **Demo 3**.

### 5. Autocrítica (20 min)

Al final de `demos.md`, sección `## Retro semana 1`: qué método te costó más y un error que casi cometes (ej. confundir conversa con contrapositiva).

Commit:

```bash
git add projects/m03-discretas/demos.md projects/m03-discretas/apuntes
git commit -m "docs(m03): tres demostraciones introductorias"
```

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 1.6–1.7 (métodos de prueba) |
| Apuntes | `leyes-logicas.md` (contrapositiva) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `demos.md` contiene **3** demostraciones completas con métodos distintos (directa, contrapositiva, casos).
2. Cada prueba cita hipótesis al inicio del párrafo de prueba.
3. Puedes señalar en una demostración dónde se usa una implicación.

## Errores comunes

- “Prueba” de una línea sin justificar pasos.
- Demostrar la conversa en lugar del teorema.
- Saltar casos en una prueba por casos.

## Siguiente

[L05 — Conjuntos: notación y membresía](L05-conjuntos-notacion-y-membresia.md)
