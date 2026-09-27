---
id: L04
materia: M20
orden: 4
titulo: Errores de validación y flujo 401
horas: 5.0
semana: 1
lectura: Interceptors HTTP
evidencia: commit + nota en auth-storage.md
---

# L04 — Errores de validación y flujo 401

**~5.0 h · Semana 1**

Auth móvil real no termina en login exitoso una vez.

## Objetivo

Manejar 401 global (logout), validación formulario, estados loading/error en login.

## Conceptos clave

- interceptor
- navigator login

## Pasos (hazlos en orden)

### 1. Interceptor 401 (70–90 min)

```ts
// si response.status === 401 → clearSecureStorage(); navigate('Login');
```

Mensajes de validación 400 legibles (campo email/password).

### 2. Prueba manual (30 min)

```bash
# 1) Login OK  2) Invalida token en storage  3) Pull lista → vuelve a Login
# Anota en auth-storage.md
git add projects/m20-movil/auth-storage.md
git commit -m "feat(m20): L04 flujo 401 y validacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Interceptors HTTP | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. 401 limpia storage y vuelve a Login; nota en auth-storage.md.
2. Commit `docs(m20): L04 errores-de-validacion-y-flujo-401`.

## Errores comunes

- 401 deja la sesión zombie.
- Mensajes de error opacos (‘Error’).

## Siguiente

[L05 — Lista de citas autenticada](L05-lista-de-citas-autenticada.md)
