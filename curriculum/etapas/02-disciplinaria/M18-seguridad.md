---
id: M18
titulo: Seguridad del software (AppSec)
etapa: disciplinaria
orden: 18
semanas: 8
horas: 160
practicas:
  - id: p1
    titulo: Threat model STRIDE del CRM (documento)
  - id: p2
    titulo: Reproducir y corregir ≥5 hallazgos OWASP en tu app
  - id: p3
    titulo: Checklist Secure SDLC en CI (audit, secrets, headers)
proyecto:
  id: proj
  titulo: Informe AppSec + PR de hardening con tests de regresión
---

# M18 — Seguridad del software (AppSec)

## Por qué existe

Es la **capa B** de la pista de ciberseguridad. Un ingeniero que “sabe hacer CRUDs” pero deja SQLi/XSS/IDOR **no es competente**. Aquí aprendes a **modelar amenazas, romper (solo tu sistema) y reparar**.

**En resumen:** amenazas → PoC en **tu** app → fix → test. Las siglas azules están en el glosario.


## Objetivos de aprendizaje

1. Hacer threat modeling ligero (STRIDE) de tu producto.
2. Explicar y mitigar el OWASP Top 10 en código real.
3. Diseñar auth (hashing, sesiones/JWT, CSRF) sin inventar crypto.
4. Meter seguridad en el pipeline (secrets, `npm audit`, headers).
5. Escribir tests que fallen si reaparece una vulnerabilidad básica.

## Cómo estudiar esta materia

- **Solo** atacas sistemas que tú controlas (localhost / tu staging).
- Ciclo fijo: amenaza → PoC en tu app → fix → test de regresión → documento.
- Lee OWASP en español; anota en tu vocabulario, no copies párrafos.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Threat model | 6–8 | STRIDE del producto |
| Exploits propios | 6–8 | Hallazgo → fix |
| CI seguridad | 4–6 | Audit/headers/secrets |
| Retro | 1 | Riesgo residual escrito |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Dibuja tu CRM (aunque esté a medias): actores, trust boundaries, datos sensibles.
2. Lista 5 activos (credenciales, PII, tokens, DB, admin).
3. Escribe `projects/m18-appsec/threat-model-v0.md` con 5 amenazas posibles.
4. Verifica que **no** tengas `.env` en git:
   ```bash
   git ls-files | rg -i 'env|secret|credential' || true
   ```
5. Lee OWASP Top 10 (overview ES) y marca cuáles aplican ya a tu diseño.

## Ejemplo — hashing de contraseñas (idea correcta)

```ts
// Usa una lib madura (p.ej. bcrypt / argon2). NUNCA MD5/SHA solo.
import bcrypt from "bcrypt";

export async function hashPassword(plain: string): Promise<string> {
  return bcrypt.hash(plain, 12);
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

## Ejemplo — IDOR (qué buscar)

Si `GET /api/citas/123` devuelve la cita **sin comprobar** que pertenece al usuario autenticado, tienes IDOR. Fix: autorización por `userId`/rol en el servidor, no solo ocultar botones en el front.

## Temario semanal

| Semana | Temas |
|--------|-------|
| 1 | Threat modeling STRIDE, activos, trust boundaries |
| 2 | Auth: registro, login, hashing, sesiones vs JWT |
| 3 | CSRF, cookies Secure/HttpOnly/SameSite |
| 4 | Injection: SQLi, XSS, command injection |
| 5 | IDOR, broken access control, rate limiting |
| 6 | SSRF, file upload, deserialización (intro) |
| 7 | Secrets, dependencias, headers, CSP básica |
| 8 | Secure SDLC + informe + tests de regresión |

## Lecturas

Canon: OWASP Top 10 + Cheat Sheets. Ver [bibliografía](../../bibliografia.md) y [hilo](../../hilos/seguridad.md).

| Semana | Lectura OWASP / recurso | Enfoque práctico |
|--------|------------------------|------------------|
| 1 | STRIDE / threat modeling (notas M18 + cheat sheet threat model) | Activos y boundaries del piloto |
| 2 | OWASP **A07 Identification and Authentication Failures** + Auth Cheat Sheet | Hashing, sesiones/JWT |
| 3 | CSRF Cheat Sheet + cookies Secure/HttpOnly/SameSite | Labs en tu app |
| 4 | **A03 Injection** + XSS Prevention Cheat Sheet | SQLi/XSS en tu stack |
| 5 | **A01 Broken Access Control** + IDOR | Rate limiting básico |
| 6 | SSRF / file upload (Cheat Sheets selectos) | Checklist de uploads |
| 7 | Secrets management + dependency + Security Headers / CSP | `npm audit`, headers |
| 8 | Secure SDLC overview + informe | Tests de regresión AppSec |

**Regla:** hallazgo → PoC en **tu** app → fix → test. Nada de “laboratorio genérico” sin trasladar.

## Prácticas

1. **P1:** Threat model v1 revisado (después de semana 2).
2. **P2:** Tabla hallazgo → PoC (en tu app) → commit de fix → test.
3. **P3:** CI con al menos: lint, test, `npm audit` (o equivalente), grep anti-secretos básico.

## Proyecto útil

Entrega en `projects/m18-appsec/`:

1. Informe AppSec (amenazas, hallazgos, mitigaciones, residual risk).
2. PR/commits de hardening en el repo del producto.
3. ≥3 tests automatizados de seguridad (ej. usuario A no lee recurso de B; input XSS escapado).

## Errores comunes

- “Security by obscurity” (ocultar rutas admin sin auth).
- Guardar JWT en `localStorage` sin entender XSS.
- Inventar cifrado casero.
- Atacar sitios ajenos (ilegal e inútil para tu egreso).

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — STRIDE:** Documento de threat model v1.
- **P2 — ≥5 hallazgos:** Tabla PoC → commit fix → test.
- **P3 — CI:** Lint+test+audit (+ grep secretos).
- **Proyecto — Informe:** `projects/m18-appsec/` + PRs hardening.

## Criterios de dominio

- [ ] Explicas SQLi y XSS con ejemplo y mitigación.
- [ ] Tu app no lee recursos cross-user (demo + test).
- [ ] No hay secretos en el historial de git del producto.
- [ ] Tienes checklist pre-deploy de seguridad y la usas.
