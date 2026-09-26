---
id: L20
materia: M06
orden: 20
titulo: Librería final y cierre de etapa básica
horas: 5
semana: 5
lectura: "Ficha M06 criterios; repaso M02 código para 5 mejoras"
evidencia: "npm pack final + cierre-etapa.md con 5 mejoras M02"
---

# L20 — Librería final y cierre de etapa básica

**~5 h · Semana 5**

Cierras M06 y la **Etapa Básica**: librería empaquetada, evidencias completas, reflexión sobre M02.

## Objetivo

Entregar paquete local (`npm pack` o GitHub package si tienes remoto); completar checklist; redactar `cierre-etapa.md` con 5 mejoras concretas al código M02.

## Pasos

### 1. Auditoría final (60 min)

| Ítem | OK |
|------|-----|
| P1 dominio TS | |
| P2 refactor | |
| P3 bordes | |
| Proyecto README/semver/tests | |

### 2. Build y pack (45 min)

```bash
npm run test
npm run build
npm pack
```

Guarda nombre del `.tgz` en bitácora.

### 3. Prueba de consumo (60 min)

Proyecto vacío temporal importa tu paquete; ejecuta ejemplo.

### 4. Revisión M02 (90 min)

Abre `projects/m02-habits/` (o tu CLI M02). Escribe `cierre-etapa.md`:

```markdown
# Cierre etapa básica — M06

## Librería
- Paquete:
- Versión:

## Cinco mejoras concretas para M02
1. (archivo:línea — qué cambiar — principio)
...
```

Debe ser específico, no “usar mejores nombres”.

### 5. Criterios de dominio (30 min)

Autoevalúa checkboxes de la ficha M06. Graba commit final:

```bash
git add .
git commit -m "feat(m06): libreria final y cierre etapa basica"
```

### 6. Retro (15 min)

¿Cuándo no usar herencia? Respuesta escrita en `cierre-etapa.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Ficha M06 | Criterios de dominio |
| Tu M02 | Código real a mejorar |
| Catálogo | [Bibliografía · M06](../../../bibliografia.md#m06-programacion-ii) |


## Hecho cuando

1. Tarball generado y probado.
2. `cierre-etapa.md` con 5 mejoras M02 accionables.
3. Evidencia proyecto completa; puedes enseñar la librería en 3 minutos.

## Errores comunes

- Marcar proyecto sin tarball.
- Mejoras M02 vagas.

## Siguiente

Siguiente etapa del plan: **Etapa Disciplinaria** (M07 en adelante). Revisa [README etapa básica](../README.md).
