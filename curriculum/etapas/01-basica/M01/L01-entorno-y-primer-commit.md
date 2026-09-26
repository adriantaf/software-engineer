---
id: L01
materia: M01
orden: 1
titulo: Entorno y primer commit
horas: 2.5
semana: 1
lectura: "Pro Git cap. 1 (Introducción) — instalación solo si falta Git"
evidencia: "projects/m01-diario/entorno.md + commit docs(m01): registrar entorno"
---

# L01 — Entorno y primer commit

**~2.5 h · Semana 1**

Esta es tu primera lección del plan. Al terminar tendrás terminal lista, evidencia en `projects/` y un commit limpio en **este** repo.

## Objetivo

Configurar el entorno mínimo (Git + Node + editor) y dejar constancia en git de que existes aquí.

## Por qué empieza así

Sin entorno y sin hábito de commit, el resto del plan se diluye en “luego lo configuro”. Hoy instalas poco y **demuestras** con un archivo + un commit.

## Pasos (hazlos en orden)

### 1. Terminal y versiones (15–20 min)

Abre la terminal. En Windows, preferible **WSL2** (Ubuntu). Comprueba:

```bash
git --version
node --version
```

- Si falta **Git**: instálalo ([git-scm.com](https://git-scm.com/) o `sudo apt install git` en Linux/WSL).
- Si falta **Node**: instala **LTS** desde [nodejs.org](https://nodejs.org/) (no uses una versión random de un tutorial viejo).

Anota las versiones; las vas a pegar en el siguiente paso.

### 2. Repo y carpeta de evidencia (20–30 min)

Clona o abre este repositorio. Desde la raíz:

```bash
mkdir -p projects/m01-diario
pwd
ls projects/m01-diario
```

Si aún no tienes el repo local: clónalo desde GitHub y entra a la carpeta antes de seguir.

### 3. Escribe `entorno.md` (30–40 min)

Crea `projects/m01-diario/entorno.md` con al menos:

```markdown
# Entorno — M01

- SO:
- Git:
- Node:
- Editor:
- Fecha:
- Notas (WSL / rutas / lo que te costó):
```

Sé concreto. “Windows” no basta: indica edición y si usas WSL.

### 4. Primer commit atómico (20–30 min)

```bash
git status
git add projects/m01-diario/entorno.md
git commit -m "docs(m01): registrar entorno de desarrollo"
git log -1 --oneline
```

Si Git pide nombre/email la primera vez:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### 5. Lectura corta (30–40 min)

Lee *Pro Git* **capítulo 1** (Introducción). No te pierdas en servidores remotos todavía.

Anota **5 comandos o ideas nuevas** al final de `entorno.md` (o en una sección `## Notas Pro Git`).

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| *Pro Git* | Cap. 1 | Misma [URL en español](https://git-scm.com/book/es/v2) |
| Este plan | [Cómo estudiar](../../../como-estudiar.md) (una pasada) | — |
| Catálogo | Entrada M01 | [Bibliografía · M01](../../../bibliografia.md#m01-metodo-git) |


## Hecho cuando

Marca la lección **solo si**:

1. Existen `git` y `node` en tu PATH (versiones anotadas).
2. Existe `projects/m01-diario/entorno.md` con SO / Git / Node / editor.
3. Hay un commit cuyo mensaje menciona el entorno (ideal: `docs(m01): registrar entorno de desarrollo`).

Esto alimenta la **P1** de la materia. No marques P1 en la ficha hasta que la evidencia exista.

## Errores comunes

- Instalar 15 herramientas y no hacer el commit.
- Escribir `entorno.md` pero dejarlo sin `git add`.
- Usar solo la GUI y no saber qué hizo `commit`.

## Siguiente

[L02 — Método y práctica deliberada](L02-metodo-y-practica-deliberada.md)
