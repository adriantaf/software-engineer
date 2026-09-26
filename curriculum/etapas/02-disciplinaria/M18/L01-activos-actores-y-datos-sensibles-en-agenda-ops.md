---
id: L01
materia: M18
orden: 1
titulo: Activos, actores y datos sensibles en Agenda Ops
horas: 5
semana: 1
lectura: "OWASP Threat Modeling (overview) + notas STRIDE"
evidencia: "projects/m18-appsec/threat-model-v0.md sección Activos"
---

# L01 — Activos, actores y datos sensibles en Agenda Ops

**~5 h · Semana 1**

## Objetivo

Inventariar actores (dueño, staff, cliente final, atacante) y activos (PII, credenciales, citas, tokens, Postgres) del piloto Agenda Ops.

## Por qué importa

Sin lista de activos, el threat model es decoración. Esta lección arranca P1 y el hilo OWASP del módulo.

## Conceptos

- Actor vs rol en el sistema.
- PII en citas (nombre, teléfono, notas).
- Superficie: panel web + API REST.
- Supuesto: solo atacas **tu** staging/local.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m18-appsec
```

En `threat-model-v0.md` crea tablas **Actores** y **Activos** (≥5 activos). Dibuja un diagrama caja-flecha: navegador → API → Postgres. Marca qué datos salen en JSON de `/api/citas`.

```bash
git ls-files | rg -i 'env|secret|credential|\.pem' || true
```

Anota el resultado en el mismo archivo (sin pegar secretos).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l01 activos-actores-y-datos-sensibles-en-age"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Threat Modeling (ES/overview) | Cheat Sheet STRIDE |
| Plan | [producto-saas.md](../../../producto-saas.md) | M13 trust boundaries |

## Hecho cuando

1. Existe `projects/m18-appsec/threat-model-v0.md` con actores y ≥5 activos.
2. Diagrama ASCII o Mermaid del piloto.
3. Comando anti-secretos ejecutado y anotado.

## Errores comunes

- Activos genéricos (“la DB”) sin tablas/campos.
- Omitir al cliente final como fuente de datos.

## Siguiente

[L02 — Trust boundaries y flujos de confianza](L02-trust-boundaries-y-flujos-de-confianza.md)
