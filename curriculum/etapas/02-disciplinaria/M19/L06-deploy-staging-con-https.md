---
id: L06
materia: M19
orden: 6
titulo: Deploy staging con HTTPS
horas: 5
semana: 2
lectura: "Proveedor: deploy + TLS"
evidencia: "projects/m19-ops/deploy-log.md"
---

# L06 — Deploy staging con HTTPS

**~5 h · Semana 2**

## Objetivo

Desplegar staging con HTTPS forzado y variables en panel del host.

## Por qué importa

Primera URL pública del piloto.

## Conceptos

- HTTP→HTTPS
- env vars
- build remoto

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Registra URL, fecha, commit SHA en deploy-log. Secretos solo en panel.

curl -I staging URL.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l06 deploy-staging-con-https"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Proveedor | HTTPS docs | M10 TLS |

## Hecho cuando

1. URL HTTPS viva.
2. deploy-log entrada.
3. Sin secretos en repo.

## Errores comunes

- HTTP plano
- TLS solo en front

## Siguiente

[L07 — Smoke test: login, cita y health externo](L07-smoke-test-login-cita-y-health-externo.md)
