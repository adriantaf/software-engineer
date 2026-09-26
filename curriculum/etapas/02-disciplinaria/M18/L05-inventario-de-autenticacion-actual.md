---
id: L05
materia: M18
orden: 5
titulo: Inventario de autenticación actual
horas: 5
semana: 2
lectura: "OWASP A07 + Authentication Cheat Sheet"
evidencia: "projects/m18-appsec/auth-inventory.md"
---

# L05 — Inventario de autenticación actual

**~5 h · Semana 2**

## Objetivo

Documentar flujo real de registro/login/logout de Agenda Ops: transporte, almacenamiento de sesión, rotación y recuperación de contraseña.

## Por qué importa

No puedes endurecer lo que no has descrito. Esta lección es fotografía del estado antes de parches.

## Conceptos

- Credencial vs sesión vs token.
- Transporte HTTPS obligatorio.
- Mensajes de error uniformes.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

En `projects/m18-appsec/auth-inventory.md` describe paso a paso el happy path y 2 edge cases (password malo, usuario inexistente).

Captura (sin secretos) qué cookie/header usa la API. ¿El ID de usuario va en JWT payload? ¿Sesión en DB?

Lista endpoints: `POST /auth/login`, etc. Marca cuáles son públicos vs autenticados.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l05 inventario-de-autenticacion-actual"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | A07 + Auth Cheat Sheet | M10 cookies/sesiones |
| Catálogo | Entrada M18 | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

1. Inventario con endpoints reales.
2. Público vs autenticado claro.
3. Sin passwords en el doc.

## Errores comunes

- Inventario teórico sin abrir el código.
- Loguear tokens en dev.

## Siguiente

[L06 — Hashing de contraseñas con bcrypt o argon2](L06-hashing-de-contrasenas-con-bcrypt-o-argon2.md)
