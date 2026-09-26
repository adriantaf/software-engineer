---
id: M24
titulo: Tecnologías emergentes
etapa: terminal
orden: 24
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Research notes de 3 tecnologías candidatas
  - id: p2
    titulo: Criterios de adopción (costo, riesgo, valor, seguridad)
  - id: p3
    titulo: Spike de 1 semana
proyecto:
  id: proj
  titulo: PoC justificado (IoT, edge, realtime, etc.)
---

# M24 — Tecnologías emergentes (electiva dirigida)

## Por qué existe

Agenda Ops no necesita adoptar cada moda (blockchain, “serverless por moda”, IoT sin caso de uso). Un ingeniero senior **evalúa** antes de meter una dependencia en producción: costo, riesgo operativo, superficie de ataque y encaje con el producto. M24 es esa disciplina aplicada a **tres candidatos** y un **spike** de una semana con decisión go/no-go escrita — por ejemplo recordatorios por WhatsApp Business API, cola realtime para disponibilidad de citas, o edge para latencia en Baja California.

No es obligatorio llevar el spike a M26; es obligatorio **pensar** antes de acumular deuda.

**En resumen:** separas hype de utilidad: research, criterios (incluye seguridad) y un spike go/no-go.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Investigar tres tecnologías con **fuentes primarias** (docs oficiales) y al menos una crítica o limitación conocida.
2. Construir una matriz de adopción con costo, riesgo, valor para Agenda Ops, fit y **seguridad**.
3. Ejecutar un spike acotado (≤1 semana de esfuerzo documentado) con alcance explícito.
4. Redactar go/no-go con criterios medibles, no intuición.
5. Descartar candidatos con argumentos sólidos (tanto vale un “no” bien fundado).
6. Relacionar el spike con el backlog M21 sin prometer features no validadas.

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md): el spike debe resolver una duda **del producto**, no un tutorial ajeno.
- Sin fuente primaria (docs oficiales del vendor o RFC estándar) el candidato no entra a la matriz.
- El spike vive en rama corta o carpeta `projects/m24-emergentes/spike/`; no merges código experimental a prod sin go explícito.
- Incluye en la matriz: ¿nuevos secretos?, ¿datos de clientes salen del perímetro?, ¿vendor lock-in?

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Research | 6–8 | 3 candidatos |
| Criterios | 6–8 | Matriz adopción |
| Spike | 4–6 | PoC + decisión |
| Retro | 1 | Qué descartaste y por qué |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. `mkdir -p projects/m24-emergentes/research projects/m24-emergentes/spike`.
2. Elige **tres** candidatos alineados a Agenda Ops (ej. WhatsApp Cloud API, WebSockets/SSE para calendario, cola managed para recordatorios). Anótalo en `projects/m24-emergentes/candidatos.md`.
3. Por cada uno, abre la doc oficial y guarda enlaces + 5 bullets en `projects/m24-emergentes/research/candidato-1.md` (y 2, 3).
4. Borrador de `projects/m24-emergentes/matriz-adopcion.md` con filas vacías para puntuar después.
5. Elige **uno** para el spike de la semana 3; escribe hipótesis en `projects/m24-emergentes/spike/hipotesis.md` (“Si X, entonces reducimos no-shows / latencia / costo soporte”).
6. Define alcance **fuera** del spike (qué no harás) para no inflar la semana.

## Ejemplo — filas de matriz (extracto)

| Criterio | Candidato A (WhatsApp API) | Candidato B (SSE) | Candidato C (…) |
|----------|---------------------------|-------------------|-----------------|
| Valor ICP | Recordatorios donde ya están | Calendario vivo en panel | … |
| Costo mensual est. | Por conversación + dev time | Hosting + conexiones | … |
| Riesgo seguridad | Tokens Meta, webhooks firmados | Auth en canal largo | … |
| Fit M26 | Alto si trial pide WhatsApp | Medio | … |
| Decisión spike | **Go** | No esta fase | Descartado: … |

## Temario semanal

### Semana 1 — Research (~20 h)

- Tres tecnologías; por cada una: problema que resuelve, límites, licencia/precio, madurez.
- Una fuente crítica o limitación (issues conocidos, rate limits, regiones no soportadas).
- Comparación preliminar sin spike aún.
- Entregable: `research/candidato-*.md` completos.

### Semana 2 — Criterios y selección (~20 h)

- Matriz ponderada (define pesos: seguridad y valor ICP ≥ hype).
- Análisis de dependencia: ¿qué pasa si el vendor cambia precios?
- Threat sketch del candidato elegido (1 página en `spike/threat-sketch.md`).
- Plan del spike: entradas, salidas, tiempo máximo, criterio de éxito.

### Semana 3 — Spike y go/no-go (~20 h)

- PoC mínimo: un flujo demostrable (ej. webhook recibido, evento en UI, mensaje de prueba).
- Medición contra hipótesis (aunque falle).
- `projects/m24-emergentes/go-no-go.md`: decisión, próximos pasos si go, qué archivar si no.
- Actualizar backlog M21 con issue derivado o comentario “descartado hasta …”.

## Lecturas

Canon: research notes + docs oficiales citadas en la matriz. Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Entrega |
|--------|---------|---------|
| 1 | 3 fuentes primarias por candidato + 1 crítica/limitación cada una | `research/candidato-1.md` … `3.md` |
| 2 | Criterios de adopción + threat model ligero del elegido | `matriz-adopcion.md` + `spike/threat-sketch.md` |
| 3 | Docs del spike + changelog/seguridad de la dependencia | `spike/` + `go-no-go.md` |

**Regla:** sin fuente primaria (docs oficiales) no entra a la matriz.

## Prácticas

1. **P1 — Research:** tres archivos en `projects/m24-emergentes/research/` con enlaces y resumen honesto.
2. **P2 — Matriz:** `projects/m24-emergentes/matriz-adopcion.md` con costo, riesgo, valor, seguridad y fit.
3. **P3 — Spike:** código o script en `projects/m24-emergentes/spike/` + nota de cómo ejecutar la demo.

## Proyecto útil

**PoC justificado** documentado en `projects/m24-emergentes/go-no-go.md`, enlazando al spike. Un “no” bien argumentado cumple el proyecto si el spike demostró que el costo o riesgo supera el valor.

## Errores comunes

- Elegir tecnología por Twitter sin leer límites de la API.
- Spike sin hipótesis medible (“jugué con X” no basta).
- Meter el PoC directo en prod de Agenda Ops.
- Ignorar seguridad de webhooks (firma, replay) en integraciones messaging.
- Adoptar tres cosas a la vez en lugar de un spike enfocado.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Notes:** `projects/m24-emergentes/research/candidato-1.md`, `candidato-2.md`, `candidato-3.md`.
- **P2 — Matriz:** `projects/m24-emergentes/matriz-adopcion.md`.
- **P3 — Spike:** `projects/m24-emergentes/spike/` (README con comando demo) + commits o tag.
- **Proyecto — Go/no-go:** `projects/m24-emergentes/go-no-go.md`.

## Criterios de dominio

- [ ] PoC con decisión go/no-go argumentada y criterios explícitos.
- [ ] Matriz incluye columna de seguridad no vacía.
- [ ] Puedes explicar por qué descartaste al menos un candidato.
- [ ] Spike acotado en tiempo; alcance documentado.
- [ ] Fuentes primarias citadas en cada research note.
