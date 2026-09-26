---
id: L06
materia: M18
orden: 6
titulo: Hashing de contraseñas con bcrypt o argon2
horas: 5
semana: 2
lectura: "Password Storage Cheat Sheet"
evidencia: "commit en repo producto + nota en projects/m18-appsec/auth-hashing.md"
---

# L06 — Hashing de contraseñas con bcrypt o argon2

**~5 h · Semana 2**

## Objetivo

Verificar o implementar hashing con coste adecuado (bcrypt≥12 o argon2) y eliminar esquemas débiles (MD5/SHA plano).

## Por qué importa

A07 empieza en la tabla `users`: un leak de DB no debe regalar contraseñas.

## Conceptos

- Salt automático.
- Cost factor / memoria argon2.
- Nunca loguear `plain` password.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Audita el servicio de registro/login en tu API de Agenda Ops (repo M17). Si hay `bcrypt`/`argon2`, documenta parámetros en `projects/m18-appsec/auth-hashing.md`.

Si falta: implementa con lib madura, migra usuarios de prueba, añade test que el hash no es igual al plain.

```bash
# en repo producto
npm test -- --testPathPattern=auth 2>/dev/null || npm test
```

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l06 hashing-de-contrasenas-con-bcrypt-o-argo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Password Storage | Ejemplo ficha M18 |

## Hecho cuando

1. Hashing correcto en código o ADR si ya estaba.
2. Test o script que verifica compare.
3. Doc de parámetros.

## Errores comunes

- MD5/SHA1 para passwords.
- Cost 4 ‘para ir rápido’.

## Siguiente

[L07 — Sesiones server-side vs JWT en Agenda Ops](L07-sesiones-server-side-vs-jwt-en-agenda-ops.md)
