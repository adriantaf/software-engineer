---
id: L11
materia: M15
orden: 11
titulo: npm audit y política de dependencias
horas: 5
semana: 3
lectura: "npm audit docs"
evidencia: "ci.yml audit step"
---

# L11 — npm audit y política de dependencias

**~5 h · Semana 3**

## Objetivo

Añadir `npm audit --audit-level=high` (o documentar excepción con ticket).

## Por qué importa

Supply chain importa aunque seas piloto.

## Conceptos

- audit.
- dependencias.
- CVE.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Paso audit en CI. Si falla, `SECURITY-EXCEPTIONS.md` con razón y fecha revisión.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l11 npm-audit-y-politica-de-dependencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| npm | audit | OWASP dep check |
| Catálogo | Entrada M15 | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

1. Audit en CI.
2. Política escrita.
3. Verde o excepción documentada.

## Errores comunes

- Ignorar audit.
- Excepciones sin fecha.

## Siguiente

[L12 — Badge README y artefacto de test](L12-badge-readme-y-artefacto-de-test.md)
