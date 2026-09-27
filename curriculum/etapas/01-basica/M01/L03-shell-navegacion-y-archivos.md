---
id: L03
materia: M01
orden: 3
titulo: Shell — navegación y archivos
horas: 3
semana: 1
lectura: "man / --help de cd, ls, pwd, mkdir, cp, mv, rm"
evidencia: "Sección Shell en bitácora o archivo projects/m01-diario/shell-notas.md con 8 comandos usados"
---

# L03 — Shell: navegación y archivos

**~3 h · Semana 1**

La terminal no es un adorno: es el suelo donde viven Git, Node y casi todo lo que sigue.

## Objetivo

Moverte por el filesystem, crear/copiar/mover/borrar con intención, y no tener miedo de `pwd` / `ls`.

## Conceptos

- **Ruta absoluta** vs **relativa** (desde dónde estás).
- El directorio de trabajo actual (`pwd`).
- Listar con detalle (`ls -la`).
- Crear y organizar carpetas de evidencia.

## Pasos (práctica en este repo)

Trabaja **dentro** del clon de este plan. No copies comandos a ciegas en `/`.

### 1. Orientación (20 min)

```bash
pwd
ls
ls -la
cd projects
pwd
cd m01-diario
pwd
cd ../..
pwd
```

Explica en voz alta (o en notas) qué cambió en cada `cd`.

### 2. Crear y organizar (40–50 min)

```bash
mkdir -p projects/m01-diario/sandbox
cd projects/m01-diario/sandbox
echo "hola shell" > nota.txt
cp nota.txt nota-copia.txt
mv nota-copia.txt nota-renombrada.txt
ls -la
```

Luego limpia el sandbox cuando termines la lección (o déjalo y documéntalo; no subas basura infinita).

### 3. Borrado consciente (20 min)

```bash
# Desde sandbox:
rm nota-renombrada.txt
# Carpetas vacías:
rmdir carpeta-vacia   # solo si existe y está vacía
# Carpetas con contenido (cuidado):
# rm -r carpeta   # úsalo solo cuando sepas qué borras
```

Regla: **nunca** `rm -rf /` ni rutas que no hayas listado justo antes.

### 4. Notas de dominio (40–50 min)

Crea `projects/m01-diario/shell-notas.md` (o una sección en la bitácora) con:

- Tabla de 8 comandos: comando → qué hace → ejemplo que corriste.
- Una duda que te quedó (si no tienes, escribe “ninguna” y un truco que descubriste).

### 5. Lectura de ayuda nativa (30–40 min)

```bash
man ls          # q para salir; o
ls --help | less
cd --help
mkdir --help
```

Acostúmbrate a `--help` / `man` antes de Stack Overflow.

## Lectura de esta lección

No hay capítulo de libro obligatorio aquí: la “lectura” es `man`/`--help` y tu propia práctica.

## Hecho cuando

1. Puedes ir de la raíz del repo a `projects/m01-diario` y volver sin el ratón.
2. Creaste y renombraste al menos un archivo por terminal.
3. Existe evidencia escrita (notas) con ≥8 comandos que **tú** corriste.

## Errores comunes

- Trabajar siempre en el home (`~`) y no saber en qué repo estás.
- Borrar con `rm -rf` “por si acaso”.
- Depender solo del explorador de archivos del editor.

## Siguiente

[L04 — Shell: pipes, permisos y docs](L04-shell-pipes-permisos-y-docs.md)
