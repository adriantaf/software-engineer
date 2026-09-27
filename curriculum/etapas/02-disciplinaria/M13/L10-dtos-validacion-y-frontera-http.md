---
id: L10
materia: M13
orden: 10
titulo: DTOs, validación y frontera HTTP
horas: 5.0
semana: 3
lectura: DTO vs entidad; validación de entrada en frontera
evidencia: arquitectura.md sección DTOs + ejemplo CreateCitaDto
---

# L10 — DTOs, validación y frontera HTTP

**~5.0 h · Semana 3**

La frontera HTTP es el primer filtro: basura in → 400. El dominio recibe datos ya saneados.

## Objetivo

Ampliar `arquitectura.md` (o `diagramas/dtos.md`) con contratos de entrada/salida del piloto.

## Pasos (hazlos en orden)

### 1. Inventario de endpoints que ya prevés (30 min)

De L02/L08: `POST /auth/login`, `POST /pedidos`, `GET /pedidos`, `POST /clientes`, …

### 2. Especifica CreateCitaDto (60–70 min)

```ts
// contrato documental (aún sin código M17)
type CreateCitaDto = {
  clienteId: string;   // uuid
  servicioId: string;
  inicio: string;      // ISO-8601
};
// fin se calcula con duracionMin del servicio (o viene explícito — decide y documenta)
```

Validaciones: uuid formato, `inicio` futuro (o ≥ ahora−slack), servicio existe.

### 3. Respuesta pública (40 min)

Lista campos del 201: `id`, `inicio`, `fin`, `estado`, `clienteId` — **sin** datos de otros módulos sensibles.

### 4. Regla de oro (20 min)

Un párrafo: “El controller valida forma; el service/domain valida negocio (solape, rol).”

### 5. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): DTOs y validacion en frontera HTTP"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | DTOs de entrada/salida; validar en HTTP antes del dominio | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas al menos `CreateCitaDto` / respuesta con campos y validaciones (tipos, rangos).
2. Dejas claro: entidad de dominio ≠ JSON crudo del request.
3. Commit `docs(m13): DTOs y validacion en frontera HTTP`.

## Errores comunes

- Aceptar el body entero y pasarlo al INSERT.
- Validar solo en el front.
- Mezclar campos internos (`passwordHash`) en DTO de respuesta.

## Siguiente

[L11 — Componentes y despliegue (C4 ligero)](L11-componentes-y-despliegue-c4-ligero.md)
