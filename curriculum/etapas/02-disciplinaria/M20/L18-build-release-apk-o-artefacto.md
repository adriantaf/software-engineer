---
id: L18
materia: M20
orden: 18
titulo: Build release APK o artefacto
horas: 5
semana: 5
lectura: "Release build oficial"
evidencia: "projects/m20-movil/build-evidence.md"
---

# L18 — Build release APK o artefacto

**~5 h · Semana 5**

## Objetivo

Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.

## Por qué importa

Emulador no basta para P3.

## Conceptos

- release
- minify opcional

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Comando exacto, tamaño APK, device modelo en build-evidence.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l18 build-release-apk-o-artefacto"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M20 P3 | — |

## Hecho cuando

1. Artefacto generado
2. Dispositivo real
3. SHA commit

## Errores comunes

- Solo debug
- API localhost

## Siguiente

[L19 — Release notes y demo cruzada con web](L19-release-notes-y-demo-cruzada-con-web.md)
