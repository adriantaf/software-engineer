---
id: L27
materia: M17
orden: 27
titulo: Rate limit en login
horas: 5.0
semana: 7
lectura: OWASP brute force
evidencia: rate limit middleware
---

# L27 — Rate limit en login

**~5.0 h · Semana 7**

Piloto público en internet necesita mínimo anti-fuerza bruta.

## Objetivo

Limitar intentos login por IP/usuario con respuesta 429 documentada.

## Conceptos clave

- rate limit
- 429
- login

## Pasos (hazlos en orden)

### 1. Rate limit login (70–90 min)

```ts
// p.ej. 5 intentos / 15 min por IP+email en POST /auth/login → 429
```

```bash
for i in $(seq 1 8); do
  curl -sS -o /dev/null -w "%{http_code}\\n" -X POST http://localhost:3000/auth/login \
    -H 'content-type: application/json' \
    -d '{"email":"owner@demo.local","password":"wrong"}'
done
# últimos → 429
```

### 2. Tests + commit (40 min)

```bash
npm test -- rate-limit
git add projects/m17-vitrina
git commit -m "feat(m17): L27 rate limit login"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP brute force | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `POST /auth/login` responde 429 tras ráfaga; test o script lo demuestra.
2. Commit `docs(m17): L27 rate-limit-en-login`.

## Errores comunes

- Rate limit solo en memoria sin doc de multi-instancia.
- 429 sin test.

## Siguiente

[L28 — Tests auth en CI o script local reproducible](L28-tests-auth-en-ci-o-script-local-reproducible.md)
