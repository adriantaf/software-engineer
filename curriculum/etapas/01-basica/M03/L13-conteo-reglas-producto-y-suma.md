---
id: L13
materia: M03
orden: 13
titulo: Conteo — regla del producto y la suma
horas: 2.5
semana: 4
lectura: "Rosen Cap. 6.1 — reglas básicas de conteo, árbol de decisiones"
evidencia: "apuntes/conteo.md + 4 problemas resueltos (producto/suma)"
---

# L13 — Conteo: regla del producto y la suma

**~2.5 h · Semana 4**

Semana 4: contar sin listar todo. Las reglas del producto y la suma son el fundamento de complejidad combinatoria.

## Objetivo

Aplicar regla del producto y regla de la suma (casos disjuntos); modelar problemas con árboles de decisión; evitar doble conteo.

## Pasos

### 1. Apuntes (30 min)

`projects/m03-discretas/apuntes/conteo.md`:

- **Producto:** si la tarea 1 tiene `a` formas y la 2 tiene `b` formas independientes → `a·b`.
- **Suma:** si son casos **disjuntos** → `a + b`.
- Principio del palomar (mención): si `n` objetos en `k` cajas, alguna caja tiene ≥ `⌈n/k⌉`.

### 2. Problemas a mano (90 min)

Resuelve **4** problemas (enunciado + razonamiento + número):

1. Cadenas de bits de longitud `n` (producto).
2. Contraseñas con restricciones simples (producto con casos).
3. Elegir un curso de lista A **o** lista B (suma disjunta).
4. Un problema donde **falles** si aplicas producto sin disjunción — corrige el error en la solución.

### 3. Código ilustrativo (30 min)

`src/counting.ts`:

```ts
export function cadenasBinarias(n: number): number {
  if (n < 0) throw new Error("n inválido");
  return 2 ** n;
}
```

Test: `n=0` → 1 (cadena vacía). Comenta por qué es `2^n` (producto repetido).

### 4. Lectura Rosen (20 min)

Un ejercicio del 6.1 adicional en `conteo.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 6.1 |

## Hecho cuando

1. Cuatro problemas documentados con justificación de producto o suma.
2. Explicas por qué los casos del problema 3 son disjuntos.
3. `cadenasBinarias` con test para `n=0`.

## Errores comunes

- Sumar cuando los casos se solapan.
- Multiplicar cuando las etapas no son independientes.
- Olvidar la cadena vacía en conteos de cadenas.

## Siguiente

[L14 — Permutaciones y combinaciones](L14-permutaciones-y-combinaciones.md)
