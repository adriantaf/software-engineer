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

## Análogos

- UABC: Organización de Computadoras

## Objetivos

1. Modelo von Neumann a alto nivel.
2. Memoria, CPU, bus, almacenamiento.
3. Representación de datos.
4. Relacionar el modelo con programas reales.

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Arquitectura básica, ciclo de instrucción |
| 2 | Memoria jerárquica, disco vs RAM |
| 3 | Representación + proyecto |

## Libros (español)

- Capítulos selectos de *Organización y arquitectura de computadoras* (Stallings, ed. ES) **o**
- *Estructura y organización de computadores* (Tanenbaum, ed. ES) — solo lo esencial.

## Prácticas

1. **P1:** Diagrama + explicación de 1 página.
2. **P2:** Conversiones y overflow; ejemplos en código.
3. **P3:** Benchmark ingenuo: loop vs I/O de archivo; escribe por qué difieren.

## Proyecto útil

Documento `projects/m05-como-corre/README.md`: desde que escribes `node cli.js` hasta que ves output — procesos, memoria, syscalls a nivel conceptual.

## Criterios de dominio

- [ ] Explicas RAM vs disco a un principiante.
- [ ] Sabes por qué “más hilos” no siempre = más rápido.
