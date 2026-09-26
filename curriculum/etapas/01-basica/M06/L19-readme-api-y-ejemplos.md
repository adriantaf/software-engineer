---
id: L19
materia: M06
orden: 19
titulo: README, API pública y ejemplos
horas: 5
semana: 5
lectura: "READMEs de librerías OSS pequeñas (2 ejemplos)"
evidencia: "README con instalación, uso, API, desarrollo; examples/basic.mjs"
---

# L19 — README, API pública y ejemplos

**~5 h · Semana 5**

Un paquete sin README es código cerrado disfrazado.

## Objetivo

Redactar README profesional: instalación, ejemplo mínimo, API resumida, cómo contribuir/testear.

## Pasos

### 1. Benchmark READMEs (45 min)

Lee dos librerías pequeñas en npm. Anota estructura.

### 2. Redacción (120 min)

Secciones: Title, Install, Quick start, API, Errors/Result, Development, License.

### 3. Ejemplo ejecutable (90 min)

`examples/basic.mjs` importa desde `dist` o usa `tsx` en dev; copiable por usuario.

### 4. API reference (60 min)

Tabla métodos + tipos exportados (puede generarse a mano).

### 5. Enlace evidencia plan (15 min)

Actualiza `projects/m06-programacion-ii/README.md` checklist proyecto.

## Hecho cuando

1. README permite usar la lib sin leer todo el src.
2. Ejemplo corre en máquina limpia tras `npm run build`.
3. Checklist proyecto casi completa.

## Errores comunes

- Solo badges decorativos.
- API undocumented breaking en 0.1.0.

## Siguiente

[L20 — Librería final y cierre de etapa básica](L20-libreria-final-y-cierre.md)
