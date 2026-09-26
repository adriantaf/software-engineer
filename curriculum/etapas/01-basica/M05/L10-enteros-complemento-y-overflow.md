---
id: L10
materia: M05
orden: 10
titulo: Enteros, complemento a dos y overflow
horas: 5
semana: 3
lectura: "Stallings — enteros con signo, complemento a dos, overflow aritmético"
evidencia: "projects/m05-como-corre/enteros-overflow.ts + enteros-notas.md"
---

# L10 — Enteros, complemento a dos y overflow

**~5 h · Semana 3**

Los enteros tienen ancho fijo en hardware. El complemento a dos explica suma con signo; el overflow explica bugs silenciosos.

## Objetivo

Explicar complemento a dos a alto nivel; detectar overflow en modelos finitos; relacionar con `Number.MAX_SAFE_INTEGER` en JavaScript/TS.

## Conceptos

- **Magnitud y signo** vs **complemento a dos**.
- **Overflow** aritmético vs **wrap-around** en lenguajes de alto nivel.
- **Int32** en WASM/Node buffers vs `number` IEEE-754.

## Pasos

### 1. Lectura (75 min)

Stallings: representación de enteros con signo. Traza suma 5 + (-3) en 4 bits (toy example) en `enteros-notas.md`.

### 2. Ejemplos TS (90 min)

`enteros-overflow.ts`:

```ts
const casi = Number.MAX_SAFE_INTEGER;
console.log(casi + 1 === casi + 2);

function sumaInt32(a: number, b: number): number {
  return (a + b) | 0; // truco educativo; documenta límites
}
```

Documenta cuándo `| 0` ayuda y cuándo engaña.

### 3. Ejercicios (60 min)

Al menos 5 preguntas tipo examen (respuestas al final del archivo de notas): overflow sí/no, rango de n bits.

### 4. Enlace a P2 (15 min)

Lista qué archivos forman la evidencia **P2** hasta ahora (L09–L10).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Enteros, complemento a dos |

## Hecho cuando

1. `enteros-notas.md` con traza 4-bit y ejercicios resueltos.
2. `enteros-overflow.ts` ejecutado y comentado.
3. Explicas por qué JS no tiene enteros de 64 bits expuestos como tipo primitivo.

## Errores comunes

- Creer que TS previene overflow numérico en runtime.
- Ignorar `MAX_SAFE_INTEGER` en IDs y contadores.

## Siguiente

[L11 — Punto flotante y precisión (P2–P3)](L11-punto-flotante-y-benchmark-io.md)
