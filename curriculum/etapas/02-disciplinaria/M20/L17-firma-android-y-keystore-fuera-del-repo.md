---
id: L17
materia: M20
orden: 17
titulo: Firma Android y keystore fuera del repo
horas: 5
semana: 5
lectura: "Android signing / iOS profiles"
evidencia: "projects/m20-movil/build-evidence.md (prep)"
---

# L17 — Firma Android y keystore fuera del repo

**~5 h · Semana 5**

## Objetivo

Crear keystore local ignorado; documentar variables CI futuras.

## Por qué importa

P3 requiere build instalable real.

## Conceptos

- keystore
- gradle signing

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

build-evidence.md sección signing sin subir keystore.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l17 firma-android-y-keystore-fuera-del-repo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docs | release build | — |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Keystore fuera git
2. gitignore
3. Doc comando

## Errores comunes

- Keystore commiteado
- Password en gradle commiteado

## Siguiente

[L18 — Build release APK o artefacto](L18-build-release-apk-o-artefacto.md)
