---
id: M19
titulo: Cómputo en la nube y DevOps
etapa: disciplinaria
orden: 19
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Docker multi-stage + Compose prod-like
  - id: p2
    titulo: Deploy reproducible con secretos en el hosting (staging/prod)
  - id: p3
    titulo: Backup automático de BD + restore probado
proyecto:
  id: proj
  titulo: Runbook de producción del SaaS Agenda Ops
---

# M19 — Cómputo en la nube y DevOps

## Por qué existe

El piloto de [Agenda Ops](../../producto-saas.md) que construiste en M17–M18 no es producto mientras solo corre en tu laptop. Un SaaS real necesita **ambientes separados**, **secretos fuera del código**, **HTTPS**, **dominio estable** y la certeza de que puedes **recuperar la base de datos** si algo falla. Esta materia es el puente entre “demo que funciona” y “servicio que otro dueño de negocio puede usar sin llamarte a las 11 p.m.”.

También prepara el camino multi-tenant: staging es donde pruebas `tenant_id` y migraciones sin tocar clientes; prod es donde vive el design partner y, después, los trials de M22.

**En resumen:** el piloto sobrevive fuera de tu laptop: Docker, secretos, HTTPS, backup con restore probado.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Empaquetar la API y el front de Agenda Ops en imágenes Docker **multi-stage** (imagen final pequeña, sin toolchain de build).
2. Orquestar servicios con Compose (app + PostgreSQL + volúmenes) de forma reproducible en tu máquina y en el hosting.
3. Diferenciar **staging** y **prod** (URLs, variables, credenciales) sin duplicar lógica de negocio.
4. Configurar TLS y dominio en un PaaS o VPS siguiendo la documentación del proveedor.
5. Automatizar backup de PostgreSQL y **restaurar** una copia en un entorno de prueba, con pasos documentados.
6. Mantener un runbook operativo que otra persona (o tú en seis meses) pueda seguir sin adivinar.

## Cómo estudiar esta materia (lecciones)

M19 lleva **Agenda Ops** fuera de tu laptop: L01–L16 con evidencia en `projects/m19-ops/` y en el repo del producto.

1. Orden **L01 → L16**; cada lección termina en commit de infra o doc ops.
2. Trabaja sobre el **repo real** del piloto; no un hello-world Docker aparte.
3. **Nunca** secretos en imagen ni en git; inventario sin valores.
4. Staging para experimentos; prod para design partner y demos M22.
5. [Cómo estudiar](../../como-estudiar.md) y [hilo producto](../../hilos/producto.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Docker / deploy | 10–12 | 4 lecciones (~5 h) |
| Operación y backup | 6–8 | Restore real, runbook |
| Retro | 1 | Runbook actualizado |

Si un día solo tienes 2 h: **una lección** (Dockerfile, deploy-log o restore). No saltes healthcheck ni smoke test.

## Lecciones

### Semana 1 — Docker multi-stage y Compose prod-like (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Inventario de secretos y ambientes staging/prod](M19/L01-inventario-de-secretos-y-ambientes-staging-prod.md) | 5 |
| L02 | [Dockerfile multi-stage para la API](M19/L02-dockerfile-multi-stage-para-la-api.md) | 5 |
| L03 | [Compose prod-like: API + Postgres + volúmenes](M19/L03-compose-prod-like-api-postgres-volumenes.md) | 5 |
| L04 | [Stack local documentado y P1 Docker](M19/L04-stack-local-documentado-y-p1-docker.md) | 5 |

### Semana 2 — Deploy staging HTTPS y dominios (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [ADR hosting: PaaS vs VPS](M19/L05-adr-hosting-paas-vs-vps.md) | 5 |
| L06 | [Deploy staging con HTTPS](M19/L06-deploy-staging-con-https.md) | 5 |
| L07 | [Smoke test: login, cita y health externo](M19/L07-smoke-test-login-cita-y-health-externo.md) | 5 |
| L08 | [Dominios y deploy-log semana 2](M19/L08-dominios-y-deploy-log-semana-2.md) | 5 |

### Semana 3 — Producción, logs y rollback (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Promover configuración a producción](M19/L09-promover-configuracion-a-produccion.md) | 5 |
| L10 | [Logs, rollback y versión desplegada](M19/L10-logs-rollback-y-version-desplegada.md) | 5 |
| L11 | [Monitoreo mínimo y alertas manuales](M19/L11-monitoreo-minimo-y-alertas-manuales.md) | 5 |
| L12 | [Revisión seguridad: puertos, SSH y firewall](M19/L12-revision-seguridad-puertos-ssh-y-firewall.md) | 5 |

### Semana 4 — Backup, restore y runbook (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L13 | [Backup automático PostgreSQL](M19/L13-backup-automatico-postgresql.md) | 5 |
| L14 | [Prueba de restore en entorno aislado](M19/L14-prueba-de-restore-en-entorno-aislado.md) | 5 |
| L15 | [Runbook completo de producción](M19/L15-runbook-completo-de-produccion.md) | 5 |
| L16 | [Cierre M19 — checklist pre-demo M22](M19/L16-cierre-m19-checklist-pre-demo-m22.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: documentación oficial **Docker** + docs del PaaS/VPS elegido. Ver [bibliografía](../../bibliografia.md) y [producto-saas](../../producto-saas.md).

| Semana | Lecciones | Lectura | Entrega |
|--------|-----------|---------|---------|
| 1 | L01–L04 | Docker Get started + Dockerfile best practices | P1 Compose + `docker.md` |
| 2 | L05–L08 | Deploy proveedor (HTTPS, dominio, env) | `deploy-log.md`, staging URL |
| 3 | L09–L12 | Logs, rollback, postura host | `runbook.md` borrador, prod |
| 4 | L13–L16 | PostgreSQL backup/restore | P3 `restore-test.md`, runbook final |

**Regla:** un restore de BD probado vale más que tutoriales de Kubernetes que no usarás en el egreso.



## Ejemplo — Dockerfile multi-stage (idea)

```dockerfile
# stage build
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# stage runtime — sin devDependencies ni fuentes TS
FROM node:22-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
HEALTHCHECK CMD wget -qO- http://localhost:3000/health || exit 1
CMD ["node", "dist/server.js"]
```

La imagen final no debe contener `.env` ni claves: solo variables inyectadas al arrancar el contenedor.



## Prácticas

1. **P1 — Docker multi-stage + Compose:** Dockerfile multi-stage en el repo del producto (o enlace en `projects/m19-ops/docker.md`); `compose.yml` prod-like con API + Postgres + volúmenes; instrucciones `docker compose up` en evidencia.
2. **P2 — Deploy reproducible:** URL HTTPS estable en staging y prod (o staging + prod en hosts distintos); captura o anotación en `projects/m19-ops/deploy-log.md`; secretos solo en el hosting.
3. **P3 — Backup + restore:** Script o procedimiento en `projects/m19-ops/backup.md`; registro de la prueba en `projects/m19-ops/restore-test.md` (fecha, tamaño dump, tiempo, resultado).

## Proyecto útil

**Runbook de producción de Agenda Ops** en `projects/m19-ops/runbook.md` (puede enlazar archivos del repo del app):

- URLs staging/prod, versiones desplegadas.
- Cómo desplegar, rollback y rotar secretos.
- Backup/restore paso a paso.
- Healthcheck y contacto si cae el servicio durante un trial.

## Errores comunes

- Secretos baked en la imagen Docker o commiteados en `compose.yml`.
- Un solo ambiente “prod” donde experimentas migraciones peligrosas.
- Backup configurado pero **nunca** restaurado (descubres que el dump estaba corrupto el día de la demo).
- Abrir SSH al mundo con contraseña en un VPS.
- Confundir “el contenedor arranca” con “la app sirve tráfico HTTPS correctamente”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Imágenes:** Dockerfile multi-stage + `compose.yml` (repo producto o `projects/m19-ops/docker.md` con enlaces); commit visible.
- **P2 — Deploy:** `projects/m19-ops/ambientes.md` + URL HTTPS en `projects/m19-ops/deploy-log.md`; inventario de secretos sin valores en git.
- **P3 — Restore:** `projects/m19-ops/restore-test.md` con fecha y resultado de restore real.
- **Proyecto — Runbook:** `projects/m19-ops/runbook.md` completo y enlazado desde el README del proyecto.

## Criterios de dominio

- [ ] Explicas por qué multi-stage y qué va en `.dockerignore`.
- [ ] Staging y prod tienen secretos y URLs distintas documentadas.
- [ ] Restauraste la BD al menos una vez y puedes repetir los pasos sin improvisar.
- [ ] `/health` responde en prod y lo usas antes de decir “está arriba”.
- [ ] Otro dev podría desplegar siguiendo solo tu runbook.
