---
id: L04
materia: M20
orden: 4
titulo: Errores de validación y flujo 401
horas: 5
semana: 1
lectura: "Interceptors HTTP"
evidencia: "commit + nota en auth-storage.md"
---

# L04 — Errores de validación y flujo 401

**~5 h · Semana 1**

## Objetivo

Manejar 401 global (logout), validación formulario, estados loading/error en login.

## Por qué importa

Auth móvil real no termina en login exitoso una vez.

## Conceptos

- interceptor
- navigator login

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementa interceptor 401 como ejemplo ficha M20. Prueba token expirado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l04 errores-de-validacion-y-flujo-401"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M20 ejemplo 401 | — |

## Hecho cuando

1. 401 redirige login
2. Loading/error UI
3. Commit

## Errores comunes

- Stack trace al usuario
- Ignorar 401

## Siguiente

[L05 — Lista de citas autenticada](L05-lista-de-citas-autenticada.md)
