---
id: L19
materia: M10
orden: 19
titulo: Documento de amenazas de red del producto
horas: 5.0
semana: 5
lectura: Proyecto M10 README + STRIDE lite (red)
evidencia: projects/m10-redes/amenazas-red.md actualizado
---

# L19 — Documento de amenazas de red del producto

**~5.0 h · Semana 5**

El entregable del proyecto: un doc que M18 pueda consumir sin redescubrir la red.

## Objetivo

Publicar `amenazas-red.md` completo y enlazado.

## Pasos

### 1. Fusiona fuentes (60 min)

Parte de `amenazas-enlace.md` + `superficie/endpoints.md` + labs TLS/cookies. Crea `amenazas-red.md` con secciones: activos, amenazas, mitigaciones, residual, follow-ups M18/M19.

### 2. STRIDE lite (60 min)

Al menos una fila por: Spoofing, Tampering, Repudiation (logs), Information disclosure, DoS, Elevation (si aplica a red/admin).

### 3. README (40 min)

Índice del proyecto con P1/P2/P3 y proyecto marcados.

### 4. Commit (15 min)

```bash
git add projects/m10-redes
git commit -m "docs(m10): l19 amenazas red producto"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) | STRIDE lite sobre red: spoofing, tampering, info disclosure, DoS | [MDN HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) |
| Catálogo | Entrada de esta materia | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

Marca la lección **solo si**:

1. `amenazas-red.md` integra enlace + superficie + mitigaciones hacia M18/M19.
2. README del proyecto enlaza amenazas, superficie y tcp-echo.
3. Commit `docs(m10): l19 amenazas red producto`.

## Errores comunes

- Lista genérica copiada sin Vitrina.
- Amenazas sin mitigación ni dueño (tú / M18).
- Olvidar DNS y cookies.

## Siguiente

[L20 — Cierre M10 — evidencias y dominio](L20-cierre-m10-evidencias-y-dominio.md)
