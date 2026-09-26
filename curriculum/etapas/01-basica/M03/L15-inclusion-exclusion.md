---
id: L15
materia: M03
orden: 15
titulo: Principio de inclusión-exclusión
horas: 2.5
semana: 4
lectura: "Rosen Cap. 6.2 — inclusión-exclusión para dos y tres conjuntos"
evidencia: "conteo.md problema |A∪B| + demo o cálculo verificado"
---

# L15 — Principio de inclusión-exclusión

**~2.5 h · Semana 4**

Cuando los casos **no** son disjuntos, la regla de la suma falla; inclusion-exclusión corrige el doble conteo.

## Objetivo

Aplicar `|A ∪ B| = |A| + |B| − |A ∩ B|` y la versión de tres conjuntos; resolver un problema de conteo con intersección no vacía.

## Pasos

### 1. Fórmulas (30 min)

En `conteo.md`, escribe las fórmulas para 2 y 3 conjuntos y un diagrama de Venn comentado.

### 2. Problema tipo encuesta (60–70 min)

Ejemplo clásico: estudiantes que estudian idioma A, idioma B, ambos — calcula solo A, solo B, ninguno si te dan totales. Adapta números propios; muestra cada región del Venn.

### 3. Con conjuntos en código (40 min)

Usa `sets.ts` con universo finito etiquetado:

```ts
export function cardinalidad<T>(a: Set<T>): number {
  return a.size;
}

export function unionSize<T>(a: Set<T>, b: Set<T>): number {
  return union(a, b).size;
}
```

Verifica numéricamente tu problema del paso 2.

### 4. Rosen (30 min)

Un ejercicio 6.2 adicional.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 6.2 |

## Hecho cuando

1. Problema resuelto con fórmula 2 o 3 conjuntos y Venn.
2. Verificación con `Set` en TS coincide con el cálculo a mano.
3. Explicas qué se “resta dos veces” sin inclusion-exclusión.

## Errores comunes

- Sumar `|A|` y `|B|` sin restar intersección.
- Tres conjuntos: olvidar términos `+|A∩B∩C|` o signos alternos.
- Universo no acotado en problemas de “al menos uno”.

## Siguiente

[L16 — Binomial, Pascal y Big-O de funciones propias](L16-binomial-y-complejidad.md)
