---
id: L12
materia: M05
orden: 12
titulo: Documental “cómo corre node” y cierre
horas: 5
semana: 3
lectura: "Repaso Stallings semana 3 + README del proyecto M05"
evidencia: "projects/m05-como-corre/README ampliado (proyecto) + checklist M05"
---

# L12 — Documental “cómo corre `node`” y cierre

**~5 h · Semana 3**

Integras arquitectura, memoria y representación en un relato técnico: de la tecla Enter al output en terminal.

## Objetivo

Ampliar `projects/m05-como-corre/README.md` (o `COMO-CORRE.md`) describiendo el camino desde `node cli.js` hasta el output, con procesos, memoria y syscalls a nivel conceptual; cerrar M05 con autoevaluación.

## Pasos

### 1. Elige un CLI real (30 min)

Usa un script tuyo de M02 (`projects/m02-habits/` o similar) o:

```bash
node -e "console.log(process.version)"
```

Debe ser un comando que puedas repetir mientras observas el SO.

### 2. Redacta el documental (120–150 min)

Estructura mínima del README del proyecto:

```markdown
# Cómo corre mi CLI

## Comando estudiado
## 1. Shell y exec
## 2. Proceso Node (V8, heap, stack)
## 3. Carga de módulos / disco
## 4. CPU durante la lógica
## 5. E/S: stdout y terminal
## 6. Límites del modelo (caché, JIT, async)
## Referencias cruzadas
(enlaces a diagrama.md, benchmark, notas L01–L11)
```

Tono: ensayo técnico breve, no lista de buzzwords.

### 3. Diagrama de secuencia (60 min)

Añade diagrama ASCII o mermaid de 8–12 pasos desde invocación hasta output.

### 4. Checklist y criterios (45 min)

Verifica evidencia P1–P3 y proyecto. Marca criterios de dominio en la ficha solo si puedes demostrarlo oralmente.

### 5. Commit final (15 min)

```bash
git add projects/m05-como-corre/
git commit -m "docs(m05): documental como corre node y cierre M05"
```

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Repaso representación + sistema |
| Ficha M05 | Criterios de dominio |

## Hecho cuando

1. README del proyecto describe el camino completo `node` → output con secciones pedidas.
2. Enlaces a evidencias L01–L11.
3. Commit final; puedes explicar RAM vs disco y por qué más hilos no siempre ayuda.

## Errores comunes

- Copiar definiciones de Wikipedia sin anclarlas a **tu** comando.
- Olvidar syscalls/E/S al hablar solo de CPU.

## Siguiente

Siguiente materia del plan: **M06 — Programación II** ([ficha](../M06-programacion-ii.md), lección [L01](../M06/L01-dominio-inicial-y-entorno.md)).
