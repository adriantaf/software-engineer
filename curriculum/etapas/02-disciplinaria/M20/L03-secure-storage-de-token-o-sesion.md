---
id: L03
materia: M20
orden: 3
titulo: Secure storage de token o sesión
horas: 5
semana: 1
lectura: "Keychain / Keystore vía lib oficial"
evidencia: "projects/m20-movil/auth-storage.md"
---

# L03 — Secure storage de token o sesión

**~5 h · Semana 1**

## Objetivo

Persistir access token con flutter_secure_storage o equivalente RN; documentar qué guardas.

## Por qué importa

JWT en SharedPreferences plano es hallazgo M18.

## Conceptos

- secure storage
- no password disk

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

auth-storage.md: claves, refresh si aplica, borrado en logout.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l03 secure-storage-de-token-o-sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Mobile MASVS storage | M18 JWT |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. auth-storage.md
2. código referenciado
3. sin password claro

## Errores comunes

- Token en logs
- AsyncStorage plano

## Siguiente

[L04 — Errores de validación y flujo 401](L04-errores-de-validacion-y-flujo-401.md)
