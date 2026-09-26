---
id: M05
titulo: Organización de computadoras
etapa: basica
orden: 5
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Diagrama CPU–memoria–I/O con tus palabras
  - id: p2
    titulo: Ejercicios de representación binaria / enteros / floats (intro)
  - id: p3
    titulo: Medir tiempo de un programa y relacionarlo con caché/IO
proyecto:
  id: proj
  titulo: Mini-documental técnico (escrito) de cómo corre tu CLI
---

# M05 — Organización de computadoras

## Por qué existe

Entender qué hace el hardware evita magia negra con rendimiento, memoria y sistemas operativos.

**En resumen:** entiendes qué pasa cuando corres `node`: CPU, RAM, disco. Dejas de tratar la máquina como magia.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Explicar el modelo von Neumann y el flujo CPU–memoria–E/S a alto nivel.
2. Describir jerarquía de memoria, caché y la diferencia RAM vs almacenamiento.
3. Representar datos (binario, enteros, punto flotante) y reconocer overflow y pérdida de precisión.
4. Relacionar el modelo con un programa real (`node`, syscalls, I/O) y medir comportamiento básico.

## Cómo estudiar esta materia (lecciones)

M05 sigue el formato de lecciones cortas y completas (como M01): marcas una a una cuando cumples “Hecho cuando”.

1. Abre las lecciones **en orden** (L01 → L12).
2. Cada lección trae objetivo, pasos, lectura de libro y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. Las **prácticas / proyecto** siguen exigiendo evidencia en `projects/m05-como-corre/`.
5. **Dibuja más de lo que subrayas.** Cada concepto → “¿dónde lo veo cuando corro `node cli.js`?”.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Arquitectura / memoria | 6–8 | L01–L08, Stallings, diagramas |
| Representación + medición | 6–8 | L09–L11, código y benchmarks |
| Proyecto documental | 4–6 | `projects/m05-como-corre/` (L12) |
| Retro | 1 | RAM vs disco en tus palabras |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Arquitectura y ciclo de instrucción (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Modelo von Neumann e introducción](M05/L01-modelo-von-neumann-e-introduccion.md) | 5 |
| L02 | [CPU, registros y ciclo de instrucción](M05/L02-cpu-registros-y-ciclo-instruccion.md) | 5 |
| L03 | [Buses, E/S y periféricos](M05/L03-buses-es-y-perifericos.md) | 5 |
| L04 | [Diagrama CPU–RAM–I/O (P1)](M05/L04-diagrama-cpu-ram-io-p1.md) | 5 |

### Semana 2 — Memoria jerárquica y almacenamiento (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Memoria principal y direccionamiento](M05/L05-memoria-principal-y-direccionamiento.md) | 5 |
| L06 | [Jerarquía de memoria y caché](M05/L06-jerarquia-memoria-y-cache.md) | 5 |
| L07 | [Disco vs RAM y persistencia](M05/L07-disco-vs-ram-y-persistencia.md) | 5 |
| L08 | [Medición: `free`, `df` y observación del SO](M05/L08-medicion-free-df-y-so.md) | 5 |

### Semana 3 — Representación de datos y proyecto (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Binario, hex y conversiones](M05/L09-binario-hex-y-conversiones.md) | 5 |
| L10 | [Enteros, complemento a dos y overflow](M05/L10-enteros-complemento-y-overflow.md) | 5 |
| L11 | [Punto flotante y precisión (P2–P3)](M05/L11-punto-flotante-y-benchmark-io.md) | 5 |
| L12 | [Documental “cómo corre `node`” y cierre](M05/L12-documental-como-corre-node-y-cierre.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Organización y arquitectura de computadoras* — William Stallings (ed. ES). Alternativa: Tanenbaum *Estructura y organización…* (mismos temas). Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / foco (Stallings, por título) |
|--------|-----------|-------------------------------------------|
| 1 | L01–L04 | Intro + **estructura/función del computador** + ciclo de instrucción + buses/E/S |
| 2 | L05–L08 | **Memoria**: jerarquía, caché, interna y externa/disco + medición en terminal |
| 3 | L09–L12 | **Representación de datos** + aritmética / overflow + proyecto “cómo corre `node`” |

**Regla:** un diagrama actualizado por semana en `projects/m05-como-corre/`.

## Ejemplo — overflow de enteros (intuición)

```ts
// En JS los Number son flotantes; igual sirve para pensar límites
const casi = Number.MAX_SAFE_INTEGER;
console.log(casi + 1 === casi + 2); // true → perdiste precisión
```

Reflexión: la representación finita siempre tiene límites.

## Prácticas

1. **P1:** Diagrama + explicación de 1 página (L04).
2. **P2:** Conversiones y overflow; ejemplos en código (L09–L11).
3. **P3:** Benchmark ingenuo: loop vs I/O de archivo; escribe por qué difieren (L11).

## Proyecto útil

Documento en `projects/m05-como-corre/`: desde que escribes `node cli.js` hasta que ves output — procesos, memoria, syscalls a nivel conceptual (L12).

## Errores comunes

- Decir “la nube es magia” sin ubicar CPU/RAM/disco.
- Confundir almacenamiento (SSD) con memoria principal (RAM).
- Medir rendimiento una sola vez sin repetir.
- Marcar lecciones sin cumplir “Hecho cuando”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Diagrama:** 1 página CPU–RAM–I/O en Markdown/imagen.
- **P2 — Binario:** Ejercicios de overflow/conversión en código + notas.
- **P3 — Benchmark:** Loop vs I/O medido ≥3 veces; explicación.
- **Proyecto — Cómo corre:** README desde `node cli.js` hasta el output.

## Criterios de dominio

- [ ] Explicas RAM vs disco a un principiante.
- [ ] Sabes por qué “más hilos” no siempre = más rápido.
- [ ] Ubicas representación finita detrás de bugs de precisión numérica.
