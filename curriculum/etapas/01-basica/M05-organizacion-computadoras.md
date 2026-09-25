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

**En cristiano:** entiendes qué pasa cuando corres `node`: CPU, RAM, disco. Dejas de tratar la máquina como magia.

## Análogos

- UABC: Organización de Computadoras

## Objetivos

1. Modelo von Neumann a alto nivel.
2. Memoria, CPU, bus, almacenamiento.
3. Representación de datos.
4. Relacionar el modelo con programas reales.

## Cómo estudiar esta materia

- Dibuja más de lo que subrayas.
- Cada concepto → “¿dónde lo veo cuando corro `node cli.js`?”.
- No memorizes ciclos de reloj: entiende el flujo de datos.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Arquitectura | 6–8 | Diagrama + lectura Stallings |
| Memoria / I/O | 6–8 | Labs de medición |
| Documento | 4–6 | `projects/m05-como-corre/` |
| Retro | 1 | RAM vs disco en tus palabras |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)

1. Lee un capítulo corto de arquitectura (Stallings/Tanenbaum ES, intro).
2. En papel, dibuja: CPU, RAM, disco, teclado/pantalla y flechas de datos.
3. Escribe en `projects/m05-como-corre/diagrama.md` la explicación en tus palabras (máx. 1 página).
4. Ejecuta en terminal:
   ```bash
   free -h   # o el equivalente en tu SO
   df -h
   ```
5. Anota qué es “memoria usada” vs “disco usado”.

## Ejemplo — overflow de enteros (intuición)

```ts
// En JS los Number son flotantes; igual sirve para pensar límites
const casi = Number.MAX_SAFE_INTEGER;
console.log(casi + 1 === casi + 2); // true → perdiste precisión
```

Reflexión: la representación finita siempre tiene límites.

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Arquitectura básica, ciclo de instrucción |
| 2 | Memoria jerárquica, disco vs RAM |
| 3 | Representación + proyecto |

## Lecturas

Canon: *Organización y arquitectura de computadoras* — William Stallings (ed. ES). Alternativa: Tanenbaum *Estructura y organización…* (mismos temas). Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos (Stallings, por título) | Alternativa |
|--------|-----------------------------------|-------------|
| 1 | Intro + **estructura/función del computador** + ciclo de instrucción (caps. de introducción y buses/CPU según tu ed.) | Explicación M05 + diagrama propio CPU–RAM–I/O |
| 2 | **Memoria**: jerarquía, caché, interna y externa/disco | Apuntes M05 + benchmark RAM vs disco de la práctica |
| 3 | **Representación de datos** + aritmética / overflow (caps. de número y ALU) + proyecto “cómo corre `node`” | Misma ficha M05 + conversiones en código |

**Regla:** un diagrama por semana en `projects/m05-como-corre/`.

## Prácticas

1. **P1:** Diagrama + explicación de 1 página.
2. **P2:** Conversiones y overflow; ejemplos en código.
3. **P3:** Benchmark ingenuo: loop vs I/O de archivo; escribe por qué difieren.

## Proyecto útil

Documento `projects/m05-como-corre/README.md`: desde que escribes `node cli.js` hasta que ves output — procesos, memoria, syscalls a nivel conceptual.

## Errores comunes

- Decir “la nube es magia” sin ubicar CPU/RAM/disco.
- Confundir almacenamiento (SSD) con memoria principal (RAM).
- Medir rendimiento una sola vez sin repetir.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Diagrama:** 1 página CPU–RAM–I/O en Markdown/imagen.
- **P2 — Binario:** Ejercicios de overflow/conversión en código + notas.
- **P3 — Benchmark:** Loop vs I/O medido ≥3 veces; explicación.
- **Proyecto — Cómo corre:** README desde `node cli.js` hasta el output.

## Criterios de dominio

- [ ] Explicas RAM vs disco a un principiante.
- [ ] Sabes por qué “más hilos” no siempre = más rápido.
