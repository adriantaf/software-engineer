---
id: L05
materia: M19
orden: 5
titulo: ADR hosting: PaaS vs VPS
horas: 5
semana: 2
lectura: "Docs Fly/Railway/Render o VPS"
evidencia: "projects/m19-ops/adr-hosting.md"
---

# L05 — ADR hosting: PaaS vs VPS

**~5 h · Semana 2**

## Objetivo

Documentar decisión de hosting para Agenda Ops con criterios costo, TLS, Postgres gestionado, DX.

## Por qué importa

Evitas re-decidir cada semana.

## Conceptos

- PaaS
- VPS+Docker
- egress y region

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ADR con alternativas y consecuencias operativas (logs, secrets panel).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l05 adr-hosting-paas-vs-vps"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M19 semana 2 | — |

## Hecho cuando

1. ADR firmada.
2. Proveedor elegido.
3. Riesgos listados.

## Errores comunes

- Sin ADR
- Elegir solo por tutorial viejo

## Siguiente

[L06 — Deploy staging con HTTPS](L06-deploy-staging-con-https.md)
