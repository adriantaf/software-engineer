---
id: L22
materia: M18
orden: 22
titulo: Subida de archivos segura
horas: 5
semana: 6
lectura: "File Upload Cheat Sheet"
evidencia: "projects/m18-appsec/findings/005-upload.md"
---

# L22 — Subida de archivos segura

**~5 h · Semana 6**

## Objetivo

Revisar o diseñar upload (logo, adjunto) con validación tipo/tamaño, almacenamiento fuera de webroot y nombres aleatorios.

## Por qué importa

Un .php disfrazado de .jpg es folklore porque sigue pasando.

## Conceptos

- MIME sniffing.
- Tamaño máximo.
- Escaneo opcional.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Si el piloto no sube archivos, redacta checklist de aceptación en `005-upload.md` para cuando exista.

Si sube: prueba archivo malicioso en staging, verifica que no se sirve como script.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m18): l22 subida-de-archivos-segura"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | File Upload | — |

## Hecho cuando

1. Checklist o prueba real.
2. Ruta almacenamiento.
3. Sin ejecución de uploads.

## Errores comunes

- Guardar en `public/` con nombre usuario.
- Confiar en extensión.

## Siguiente

[L23 — Deserialización y JSON peligroso](L23-deserializacion-y-json-peligroso.md)
