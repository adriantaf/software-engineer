---
id: L09
materia: M13
orden: 9
titulo: Arquitectura en capas
horas: 5.0
semana: 3
lectura: Capas HTTP → application → domain → infrastructure
evidencia: projects/m13-diseno/arquitectura.md (capas + responsabilidades)
---

# L09 — Arquitectura en capas

**~5.0 h · Semana 3**

El monolito modular de ADR 001 necesita fronteras internas. Hoy las escribes.

## Objetivo

`projects/m13-diseno/arquitectura.md` con capas que M14/M17 puedan respetar.

## Pasos (hazlos en orden)

### 1. Define capas (60–70 min)

```text
HTTP (controllers/routes)
  → Application (services / use cases)
    → Domain (reglas: solape, estados)
      → Infrastructure (Postgres, mail, reloj)
```

Tabla:

| Capa | Puede | No puede |
|------|-------|----------|
| HTTP | parsear DTO, status codes | reglas de solape |
| Application | orquestar | SQL crudo (mejor vía repo) |
| Domain | invariantes | conocer Express |
| Infra | SQL, SMTP | decidir autorización de negocio a solas |

### 2. Mapa de carpetas previstas (40–50 min)

```text
src/
  http/
  application/
  domain/
  infrastructure/
```

Enlaza a módulos: `orders`, `clientes`, `auth`.

### 3. Dibuja dependencias (40 min)

Mermaid `flowchart TB` de capas; flechas solo hacia abajo (o inward).

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/arquitectura.md
git commit -m "docs(m13): arquitectura en capas Vitrina"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Arquitectura en capas; dónde viven reglas vs I/O | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. `arquitectura.md` describe ≥4 capas con responsabilidad y ejemplo de archivo futuro.
2. Queda explícito que autorización/reglas de pedido no viven solo en React.
3. Commit `docs(m13): arquitectura en capas Vitrina`.

## Errores comunes

- “Arquitectura” = lista de librerías sin fronteras.
- Domain que importa SQL o Express.
- Capas de adorno (8 capas para un CRUD).

## Siguiente

[L10 — DTOs, validación y frontera HTTP](L10-dtos-validacion-y-frontera-http.md)
