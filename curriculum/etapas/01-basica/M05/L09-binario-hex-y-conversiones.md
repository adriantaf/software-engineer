---
id: L09
materia: M05
orden: 9
titulo: Binario, hex y conversiones
horas: 5
semana: 3
lectura: "Stallings — representación de datos, sistemas numéricos"
evidencia: "projects/m05-como-corre/conversiones.ts + notas-conversiones.md"
---

# L09 — Binario, hex y conversiones

**~5 h · Semana 3**

Todo en la máquina es bits. Dominar conversiones evita errores en flags, permisos y protocolos.

## Objetivo

Convertir entre decimal, binario y hexadecimal; interpretar bytes como datos; implementar conversiones en TypeScript con tests manuales claros.

## Pasos

### 1. Lectura (60–75 min)

Stallings: representación numérica (bases 2, 10, 16). Haz **10 conversiones a mano** antes de codear.

### 2. `notas-conversiones.md` (45 min)

Tabla de ejercicios resueltos (incluye permisos Unix `rwx` como ejemplo de bits).

### 3. Código `conversiones.ts` (120 min)

En `projects/m05-como-corre/` (configura `tsx` si hace falta, como en M02):

```ts
export function decToBin(n: number): string { /* solo enteros ≥0 razonables */ }
export function decToHex(n: number): string { /* mayúsculas opcional, consistente */ }
export function binToDec(s: string): number { /* validar entrada */ }
```

Añade al menos **8 casos de prueba** documentados al final del archivo o en comentarios.

### 4. Puente con permisos (30 min)

Explica `chmod 644` en binario (6 = rw-, etc.) en las notas.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Sistemas numéricos, representación |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Notas con 10 conversiones manuales + explicación chmod.
2. `conversiones.ts` con funciones y casos de prueba ejecutables.
3. Entiendes por qué hex agrupa bits de a 4.

## Errores comunes

- Usar `parseInt` sin validar strings inválidos.
- Confundir string binario con número JS.

## Siguiente

[L10 — Enteros, complemento a dos y overflow](L10-enteros-complemento-y-overflow.md)
