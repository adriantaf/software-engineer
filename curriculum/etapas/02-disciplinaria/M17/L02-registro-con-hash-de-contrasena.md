---
id: L02
materia: M17
orden: 2
titulo: Registro con hash de contraseña
horas: 5
semana: 1
lectura: "OWASP Password Storage + bcrypt/argon2"
evidencia: "POST /auth/register"
---

# L02 — Registro con hash de contraseña

**~5 h · Semana 1**

## Objetivo

Implementar registro: validar email/password, hash fuerte, persistir usuario ligado al negocio piloto.

## Por qué importa

Auth real desde el MVP — no usuarios en texto plano.

## Conceptos

- hash.
- registro.
- validación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Zod (o similar) en body. Test integración 201 y 400 email inválido.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l02 registro-con-hash-de-contrasena"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Password Storage | m13 ADR auth |

## Hecho cuando

1. Register funciona.
2. Hash no reversible.
3. Test 400.

## Errores comunes

- MD5.
- Password en logs.

## Siguiente

[L03 — Login, sesión y GET /me protegido](L03-login-sesion-y-get-me-protegido.md)
