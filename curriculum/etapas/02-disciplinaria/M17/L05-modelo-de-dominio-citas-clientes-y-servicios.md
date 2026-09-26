---
id: L05
materia: M17
orden: 5
titulo: Modelo de dominio citas, clientes y servicios
horas: 5.0
semana: 2
lectura: m13 diagrama clases + srs-v1
evidencia: migraciones / entidades
---

# L05 — Modelo de dominio citas, clientes y servicios

**~5.0 h · Semana 2**

CRUD sin dominio coherente genera IDOR y huérfanos. Hoy alineas entidades a M13/M09.

## Objetivo

Migraciones + carpeta `domain/` (o equivalente) con reglas puras sin ORM.

## Pasos (hazlos en orden)

### 1. Contrasta diseño (30 min)

Abre diagrama M13 y migraciones M09. Lista diferencias a resolver hoy.

### 2. Migraciones (70–90 min)

Asegura tablas `clientes`, `servicios`, `citas` con FKs, estados, duración/precio base. Aplica y `\dt`.

### 3. Reglas de dominio (50–60 min)

Funciones puras: `fin > inicio`, solapamiento, cancelación permitida. Tests unitarios sin DB si puedes.

### 4. Commit

`feat(m17): l05 dominio citas clientes servicios`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m13 diagrama clases + srs-v1 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Migraciones (artefacto: `migraciones / entidades`).
2. domain/ con reglas (artefacto: `migraciones / entidades`).
3. Commit (artefacto: `migraciones / entidades`).

## Errores comunes

- Lógica solo en controllers.
- Sin FK.

## Siguiente

[L06 — API citas — crear y listar con reglas](L06-api-citas-crear-y-listar-con-reglas.md)
