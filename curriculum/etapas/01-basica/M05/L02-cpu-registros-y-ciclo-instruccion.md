---
id: L02
materia: M05
orden: 2
titulo: CPU, registros y ciclo de instrucción
horas: 5
semana: 1
lectura: "Stallings — ciclo de instrucción, registros, ALU (cap. CPU según ed.)"
evidencia: "projects/m05-como-corre/ciclo-instruccion.md con diagrama fetch-decode-execute"
---

# L02 — CPU, registros y ciclo de instrucción

**~5 h · Semana 1**

La CPU no “piensa”: repite un ciclo. Entender fetch–decode–execute desmitifica optimizadores y bugs extraños.

## Objetivo

Describir registros clave (PC, IR, acumuladores/general-purpose a alto nivel) y el ciclo de instrucción en una máquina típica.

## Conceptos

- **Registros** vs **memoria**: velocidad, tamaño, propósito.
- **PC (program counter)**: dirección de la siguiente instrucción.
- **Fetch → decode → execute → (memory access) → writeback**.
- **Conjunto de instrucciones (ISA)**: lo que el compilador/interpreter targetea.

## Pasos

### 1. Lectura (60–90 min)

Stallings (o Tanenbaum): sección de **ciclo de instrucción**. Traza a mano **tres instrucciones ficticias** (load, add, store) anotando qué registro cambia en cada fase.

### 2. Documento `ciclo-instruccion.md` (90 min)

Crea `projects/m05-como-corre/ciclo-instruccion.md`:

```markdown
# Ciclo de instrucción — M05 L02

## Registros (alto nivel)
| Registro | Rol |
|----------|-----|

## Ciclo (una instrucción)
1. Fetch:
2. Decode:
3. Execute:
...

## Ejemplo trazado (3 instrucciones)
(pseudocódigo ensamblador o tabla paso a paso)
```

Incluye un diagrama de flujo ASCII del ciclo.

### 3. Puente con alto nivel (60 min)

Elige una función TS trivial:

```ts
function suma(a: number, b: number): number {
  return a + b;
}
```

En el mismo archivo, sección **“¿Qué podría hacer la CPU?”**: no traduzcas a ensamblador real; lista **tipos de operaciones** (cargar constantes, sumar, saltar, llamar). Objetivo: intuición, no disassembly perfecto.

### 4. Preguntas de comprensión (30 min)

Responde al final del archivo:

- ¿Qué pasa si el PC apunta a una dirección inválida?
- ¿Por qué más registros no siempre acelera todo?
- ¿Cómo se relaciona el ciclo con “un hilo de ejecución”?

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | CPU, ciclo de instrucción, registros |
| Opcional | Video corto de simulador educativo (solo si cierras con tu diagrama) |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Existe `ciclo-instruccion.md` con tabla de registros, diagrama del ciclo y traza de 3 instrucciones.
2. Explicas fetch–decode–execute sin usar solo inglés técnico suelto (traduce conceptos).
3. Relacionaste el ciclo con la ejecución de una función de alto nivel.

## Errores comunes

- Memorizar nombres de registros x86 sin entender roles.
- Olvidar que algunas instrucciones acceden memoria **dentro** del ciclo.
- Diagrama del ciclo sin flechas de retroalimentación al PC.

## Siguiente

[L03 — Buses, E/S y periféricos](L03-buses-es-y-perifericos.md)
