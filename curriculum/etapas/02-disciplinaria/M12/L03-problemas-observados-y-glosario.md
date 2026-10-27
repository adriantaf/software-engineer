---
id: L03
materia: M12
orden: 3
titulo: Problemas observados y glosario
horas: 5.0
semana: 1
lectura: problemas.md + glosario del dominio
evidencia: problemas.md y glosario.md
---

# L03 — Problemas observados y glosario

**~5.0 h · Semana 1**

Traduces la entrevista a problemas y lenguaje compartido.

## Objetivo

Publicar `problemas.md` y `glosario.md` en `projects/m12-srs/`.

## Pasos

### 1. Extrae problemas (75 min)

Tabla:

| ID | Problema observado | Evidencia (nota) | Impacto | Frecuencia |
|----|--------------------|------------------|---------|------------|
| P-01 | Doble reserva el sábado | 00:18 | pierde cliente | semanal |

Prohibido: soluciones (“app con calendario”).

### 2. Glosario (60 min)

Términos mínimos: Cliente, Servicio, Pedido, No-show, Recordatorio, Staff, Owner, Bloqueo de horario, Nota privada, Adelanto (si aplica). Definición en 1–2 frases del partner.

### 3. Commit (15 min)

```bash
git add projects/m12-srs/problemas.md projects/m12-srs/glosario.md
git commit -m "docs(m12): l03 problemas y glosario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Problema ≠ solución; glosario pedido/servicio/cliente/pedido abandonado | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `problemas.md` con ≥6 problemas observados (evidencia → impacto → frecuencia).
2. `glosario.md` con ≥8 términos del dominio alineados al partner.
3. Commit `docs(m12): l03 problemas y glosario`.

## Errores comunes

- Escribir “necesitan dashboard” como problema.
- Glosario genérico sin el lenguaje del negocio.
- Problemas sin ancla en las notas.

## Siguiente

[L04 — Stakeholders y contexto Vitrina](L04-stakeholders-y-contexto-vitrina.md)
