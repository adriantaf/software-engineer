---
id: L04
materia: M01
orden: 4
titulo: Shell — pipes, permisos y docs
horas: 3
semana: 1
lectura: "man grep, chmod; ojear cómo están estructuradas docs MDN o Node"
evidencia: "Ejercicio de pipe documentado + aliases útiles (opcional) en entorno.md o shell-notas.md"
---

# L04 — Shell: pipes, permisos y docs

**~3 h · Semana 1**

Cierras la parte Linux/método de la semana 1: combinar comandos, entender permisos básicos y leer documentación oficial sin ahogarte.

## Objetivo

Usar redirecciones y pipes con `grep`, leer permisos en `ls -l`, y extraer algo útil de una página de docs oficiales.

## Conceptos

- **stdout / stderr** y redirección (`>`, `>>`, `2>`).
- **Pipe** `|`: la salida de un comando alimenta al siguiente.
- Permisos `rwx` y `chmod` a nivel práctico (no memorices octal sin usarlo).
- Docs oficiales > hilos random de 2017.

## Pasos

### 1. Redirecciones (25–30 min)

Desde la raíz del repo:

```bash
ls projects > /tmp/lista-projects.txt
cat /tmp/lista-projects.txt
echo "segunda linea" >> /tmp/lista-projects.txt
cat /tmp/lista-projects.txt
```

### 2. Pipes + grep (40–50 min)

```bash
ls -la projects/m01-diario | grep -i md
git log --oneline | head -n 5
# Buscar en archivos (ejemplo):
grep -R "entorno" projects/m01-diario --include="*.md" || true
```

Documenta **un** pipeline propio en `shell-notas.md` (comando completo + qué esperabas + qué salió).

### 3. Permisos (30–40 min)

```bash
ls -l projects/m01-diario/entorno.md
# Ejemplo seguro: quitar/poner escritura al dueño (ajusta si tu SO se queja)
chmod u+w projects/m01-diario/entorno.md
ls -l projects/m01-diario/entorno.md
```

Escribe en notas qué significan las primeras columnas de `ls -l` (tipo + rwx del dueño/grupo/otros) con tus palabras.

### 4. Aliases útiles (opcional, 20 min) — hacia P1

Si quieres cerrar la parte “aliases” de P1, añade a tu shell config (`~/.bashrc` o `~/.zshrc`) algo mínimo, por ejemplo:

```bash
alias ll='ls -la'
alias gs='git status'
```

Luego `source ~/.bashrc` (o abre una terminal nueva) y verifica. Anota en `entorno.md` qué aliases añadiste.

### 5. Leer docs oficiales (40–50 min)

Elige **una**:

- [MDN — Getting started](https://developer.mozilla.org/es/docs/Learn) (solo la idea de cómo navegan las docs), o
- [Node.js docs](https://nodejs.org/docs/latest/api/) (mira el índice; no leas todo), o
- Docs de tu editor (Cursor / VS Code) sobre la terminal integrada.

En `shell-notas.md` escribe: URL + 3 hallazgos (atajos, secciones, cómo buscar).

## Lectura de esta lección

| Fuente | Qué |
|--------|-----|
| Sistema | `man grep`, `man chmod` o `--help` |
| Oficiales | MDN / Node / editor (una sola, con notas) |
| Catálogo | [Bibliografía · M01](../../../bibliografia.md#m01-metodo-git) |


## Hecho cuando

1. Tienes un pipeline `|` documentado que tú corriste.
2. Explicas `ls -l` a grandes rasgos (permisos).
3. Dejaste notas de una página de documentación oficial.
4. (Bonus P1) Aliases listados en `entorno.md`.

## Cierre de semana 1

Actualiza `semana-0001.md` → sección “Al cierre”. Si P1 ya tiene evidencia completa, puedes marcarla en la ficha de M01.

## Siguiente

[L05 — Git fundamentos](L05-git-fundamentos.md)
