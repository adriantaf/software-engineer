---
id: M03
titulo: Matemáticas discretas
etapa: basica
orden: 3
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: Cuaderno de demostraciones (10 pruebas cortas)
  - id: p2
    titulo: Implementar conjuntos, relaciones y grafos simples en TS
  - id: p3
    titulo: Contar complejidad de 5 algoritmos propios
proyecto:
  id: proj
  titulo: Bitácora matemática + visualizador de grafos CLI
---

# M03 — Matemáticas discretas

## Por qué existe

Es el lenguaje de estructuras de datos, criptografía ligera, bases de datos y algoritmos. UABC y Tec la exigen; aquí la haces **aplicada a código**.

## Análogos

- UABC / Tec: Matemáticas discretas

## Objetivos

1. Lógica proposicional y predicados básicos.
2. Conjuntos, relaciones, funciones.
3. Inducción y conteo.
4. Grafos introductorios.
5. Conectar ideas con código TypeScript.

## Temario

| Semana | Temas |
|--------|-------|
| 1 | Lógica, tablas de verdad, equivalencias |
| 2 | Conjuntos, operaciones, leyes |
| 3 | Relaciones, funciones, inducción |
| 4 | Combinatoria básica |
| 5 | Grafos: representación, BFS/DFS intro |

## Libros (español)

- *Matemáticas discretas y sus aplicaciones* — Kenneth Rosen (ed. ES) **o**
- Texto universitario ES de matemáticas discretas (cualquier facultad de ingeniería).
- Complemento: apuntes propios en `projects/m03-discretas/`.

## Prácticas

1. **P1:** 10 demostraciones cortas a mano (escaneadas o Markdown).
2. **P2:** Implementar `Set` ops, matriz de relación, lista de adyacencia.
3. **P3:** Para 5 funciones tuyas, escribir Big-O y justificar.

## Proyecto útil

CLI que lea un grafo (JSON) e imprima BFS/DFS y grado de nodos. Documenta la teoría detrás.

## Criterios de dominio

- [ ] Pruebas por inducción de un sumatorio simple.
- [ ] Explicas por qué un grafo se representa de dos formas.
- [ ] No confundes O(n) con “rápido en mi laptop”.
