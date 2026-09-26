---
id: L27
materia: M17
orden: 27
titulo: Rate limit en login
horas: 5
semana: 7
lectura: "OWASP brute force"
evidencia: "rate limit middleware"
---

# L27 — Rate limit en login

**~5 h · Semana 7**

## Objetivo

Limitar intentos login por IP/usuario con respuesta 429 documentada.

## Por qué importa

Piloto público en internet necesita mínimo anti-fuerza bruta.

## Conceptos

- rate limit.
- 429.
- login.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Test 429 tras N intentos. No bloquear CI IPs — config test.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l27 rate-limit-en-login"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Authentication | — |

## Hecho cuando

1. Rate limit.
2. 429 test o manual.
3. Commit.

## Errores comunes

- Sin límite.
- Lockout permanente sin doc.

## Siguiente

[L28 — Tests auth en CI o script local reproducible](L28-tests-auth-en-ci-o-script-local-reproducible.md)
