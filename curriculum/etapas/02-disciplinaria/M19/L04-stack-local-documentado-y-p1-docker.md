---
id: L04
materia: M19
orden: 4
titulo: Stack local documentado y P1 Docker
horas: 5
semana: 1
lectura: "Repaso semana 1"
evidencia: "projects/m19-ops/docker.md completo"
---

# L04 — Stack local documentado y P1 Docker

**~5 h · Semana 1**

## Objetivo

Consolidar instrucciones un comando, troubleshooting y evidencia de login/cita en contenedores.

## Por qué importa

Cierra semana 1 con P1 listo para marcar.

## Conceptos

- reproducibilidad
- logs compose

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Añade sección Troubleshooting a docker.md. Captura `docker compose ps` y respuesta `/health`.

Smoke: crear cita desde UI contra stack dockerizado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l04 stack-local-documentado-y-p1-docker"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M19 P1 | — |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. docker.md completo.
2. Smoke test anotado.
3. Commit P1.

## Errores comunes

- Solo README vacío
- Imagen sin healthcheck

## Siguiente

[L05 — ADR hosting: PaaS vs VPS](L05-adr-hosting-paas-vs-vps.md)
