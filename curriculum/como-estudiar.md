# Cómo estudiar en este plan

Esta guía es el manual metodológico del plan. Léala una vez y consúltela cuando el avance se detenga.

## Flujo rápido (cada materia)

1. **Primera lección (L01)** — sesión inicial de 2–3 h.
2. **Semana tipo (20 h)** — distribuya la semana; no improvise el bloque completo.
3. **Lecciones L01…Ln** en orden, más las **lecturas** indicadas en cada lección (solo esos capítulos).
4. **Práctica y proyecto** — márquelos en la interfaz solo si cumplen la **evidencia de hecho**.
5. Sigla en azul → [glosario](glosario.md).

En cada ficha encontrará también **En resumen** (qué se realizará, en términos claros).

### Lecciones por materia

Cada materia se divide en lecciones **L01…Ln** (aproximadamente 4 por semana). Cada una se marca como completada de forma independiente (objetivo, pasos, lectura y «Hecho cuando»). Las prácticas y el proyecto de la ficha siguen exigiendo evidencia en `projects/`.

### Criterio de calidad de una lección

Una lección de calidad (estándar del plan) incluye:

1. Objetivo medible y pasos **con tiempos** (comandos o archivos concretos).
2. Tabla **Lectura de esta lección** (fuente → qué leer → enlace a [bibliografía](bibliografia.md)).
3. **Hecho cuando** (verificaciones concretas) y **Errores frecuentes**.
4. Evidencia en `projects/…` cuando el paso lo requiera.

No cuenta como estudio: marcar la lección tras solo leer el Markdown, o pasos genéricos del tipo «lea la ficha / carpeta / commit» sin laboratorio del tema del día.

### Buscar en el plan

En la interfaz: **Buscar**. Permite localizar fichas, lecciones y guías.

## Una semana de 20 horas (modelo)

| Bloque | Horas | Actividad |
|--------|-------|-----------|
| Teoría / libro | 6–8 | Lectura activa: anote dudas; no subraye todo |
| Práctica deliberada | 6–8 | Ejercicios, katas y laboratorios de la materia |
| Proyecto | 4–6 | Avance medible del proyecto de la materia |
| Retrospectiva | 1 | Bitácora: qué se aprendió, qué falta, qué sigue |

Si un día solo dispone de 2 h: **1 h de práctica + 1 h de proyecto**. Evite consumir videos sin escribir código.

## Cómo leer una materia (orden fijo)

1. **Por qué existe** — contexto y utilidad.
2. **Objetivos** — qué debe poder hacer al terminar.
3. **Lecciones** — comience por L01 sin omitir pasos.
4. **Lecciones siguientes** — avance en orden (L02…Ln).
5. **Lecturas** — siga la tabla **semana → capítulos** o la lectura de cada lección (ver [bibliografía](bibliografia.md)). No elija capítulos al azar. Si aparece una sigla en azul, ábrala en el [glosario](glosario.md).
6. **Prácticas** — márquelas en la interfaz solo cuando existan archivos o evidencia.
7. **Proyecto** — cierre de la materia.
8. **Criterios de dominio** — autoevaluación rigurosa.

Consulte también la [filosofía](filosofia.md), el [glosario](glosario.md) y el [hilo de seguridad](hilos/seguridad.md).

## Qué cuenta como terminado

Una materia **no** está terminada por haber leído el Markdown. Está terminada cuando:

- Las prácticas tienen evidencia en `projects/` o en un repositorio enlazado.
- El proyecto cumple los requisitos mínimos de la ficha.
- Puede explicar los criterios de dominio **sin consultar el tutorial**.

Después marque la casilla en el plan. Cada semana: **registro semanal** en la página Progreso (horas reales + hecho / bloqueo / siguiente), exporte el JSON a `progress.json` y realice un commit.

## Cuando no comprenda algo

1. Intente 25–40 minutos por su cuenta (documentación y prueba y error).
2. Documente: qué intentó, qué error observó, qué esperaba.
3. Consulte al mentor (Cursor) con: **materia + enlace o código + duda concreta**.
4. Evite peticiones amplias («explíqueme todo TypeScript»); formule dudas localizadas («no comprendo por qué este `await` falla aquí»).

## Errores de método (evitar)

- Consumir muchos tutoriales sin un proyecto propio.
- Marcar prácticas sin evidencia.
- Omitir M01/M02 porque «ya se programa» (el hueco suele estar en profundidad).
- Dedicar la semana entera solo a teoría.
- Compararse con perfiles de LinkedIn en lugar de con la bitácora de hace 30 días.

## Inglés y la universidad

- Inglés: continúe su curso; aquí se usan libros en español hasta alcanzar lectura técnica de nivel B1.
- Si cursa una carrera en paralelo: este plan **adelanta y profundiza**. Cuando la universidad aborde «Bases de datos», aquí ya se construye el esquema de **Vitrina** (menú y pedidos).

## Siguiente paso

El curriculum y la academia están listos para estudiar. Ejecute el plan:

1. En la interfaz: **Continuar** (o [M01 · L01](etapas/01-basica/M01/L01-entorno-y-primer-commit.md) si comienza de cero).
2. Cumpla el **Hecho cuando** de esa lección con evidencia en `projects/`.
3. Cada semana: **registro** en **Progreso** → exporte a `progress.json` → commit.

Opcional: use **Buscar** en la interfaz para localizar lecturas y lecciones.
