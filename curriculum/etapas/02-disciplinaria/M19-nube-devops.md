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

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) y el hilo [producto](../../hilos/producto.md).
- Trabaja sobre el **repo real** del piloto/SaaS; no levantes un “hello world” en Docker aparte.
- Cada cambio de infra va con commit: Dockerfile, compose, docs en `projects/m19-ops/`.
- **Nunca** pongas `DATABASE_URL`, claves de Stripe (futuro M26) ni JWT secrets en la imagen ni en git.
- Si un deploy falla, anota el error en el runbook antes de borrarlo de memoria.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Docker | 6–8 | Multi-stage, Compose, healthcheck |
| Deploy | 6–8 | Staging/prod + secrets del proveedor |
| Backup | 4–6 | Job de backup + restore real una vez |
| Retro | 1 | Runbook actualizado |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea la carpeta de evidencia: `mkdir -p projects/m19-ops`.
2. Inventaria secretos en `projects/m19-ops/secrets-inventory.md`: `DATABASE_URL`, secret de sesión/JWT, API keys futuras (Stripe test), credenciales del PaaS. Marca **dónde deben vivir** (panel del host, vault, `.env` local ignorado por git).
3. Comprueba que no filtraste secretos al historial:
   ```bash
   git ls-files | rg -i '\.env|secret|credential' || true
   ```
4. Define dos ambientes en `projects/m19-ops/ambientes.md`: **staging** (experimentos, migraciones) y **prod** (design partner / demos estables). Anota la URL objetivo de cada uno (aunque staging sea temporal).
5. Añade o verifica endpoint `GET /health` en la API (200 + versión o “ok”) y anótalo en el runbook borrador.
6. Elige dominio o subdominio para Agenda Ops (ej. `app.tudominio.com`, `staging.tudominio.com`) y regístralo en `projects/m19-ops/dominios.md`.

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

## Temario semanal

### Semana 1 — Docker y Compose (~20 h)

- Por qué contenedores: reproducibilidad, mismas versiones de Node/Postgres que en prod.
- Dockerfile multi-stage: separar build y runtime; `.dockerignore` (node_modules, `.git`, `.env`).
- `docker compose`: servicio `api`, `db` (PostgreSQL), volúmenes para datos persistentes.
- Variables de entorno vía `env_file` **local** (no commiteado) o secrets del host.
- Healthchecks en Compose y dependencias (`depends_on` + condition healthy).
- Entregable: stack local que levanta Agenda Ops con un comando documentado.

### Semana 2 — Deploy staging (~20 h)

- Elegir hosting: PaaS (Fly.io, Railway, Render, etc.) o VPS con Docker — **documenta la decisión** en `projects/m19-ops/adr-hosting.md`.
- Pipeline manual o CI: build imagen → push registry (si aplica) → deploy staging.
- HTTPS y dominio en staging; forzar redirección HTTP→HTTPS.
- Secretos en el panel del proveedor, no en el repo.
- Smoke test: login, crear cita, comprobar `/health` desde fuera.

### Semana 3 — Prod + operación diaria (~20 h)

- Promover configuración probada en staging a **prod** (misma imagen, distintas env vars).
- Logs: dónde verlos en el proveedor; qué buscar ante 5xx.
- Monitoreo mínimo: uptime del healthcheck, alerta manual (calendario) si cae el piloto.
- Documentar rollback: imagen anterior o tag git desplegado.
- Revisión [hilo seguridad](../../hilos/seguridad.md): puertos expuestos, SSH si usas VPS (clave, no password; firewall).

### Semana 4 — Backup, restore y runbook (~20 h)

- Backup automático de PostgreSQL (cron del host, `pg_dump` programado, o backup gestionado del proveedor).
- **Prueba de restore** en entorno aislado: vaciar DB de prueba → restaurar dump → verificar citas.
- Runbook completo: deploy, rollback, restore, contactos, URLs.
- Checklist pre-demo para M22: prod estable antes de enseñar el producto.

## Lecturas

Canon: documentación oficial de Docker + docs del PaaS/VPS elegido. Ver [bibliografía](../../bibliografia.md) y [producto-saas](../../producto-saas.md).

| Semana | Lectura | Alternativa |
|--------|---------|-------------|
| 1 | Docker **Get started** + Dockerfile best practices (oficial) | — |
| 2 | Docs de deploy del proveedor (HTTPS, dominio, env vars) | — |
| 3 | Secrets del proveedor + variables de entorno (nunca en imagen) | Runbook borrador |
| 4 | Backups/restore del proveedor o PostgreSQL docs + healthchecks | Prueba de restore real |

**Regla:** un restore de BD probado vale más que tres tutoriales de Kubernetes que no vas a usar en el egreso.

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
