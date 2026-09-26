---
id: L01
materia: M10
orden: 1
titulo: Modelo de capas y primer curl
horas: 5
semana: 1
lectura: "Tanenbaum — intro y capas (modelo OSI/TCP simplificado)"
evidencia: "projects/m10-redes/labs/semana-01.md + dia1.md con curl -v"
---

# L01 — Modelo de capas y primer curl

**~5 h · Semana 1**

## Objetivo

Dibujar un modelo de capas de cinco niveles y capturar con `curl -v` el viaje hasta la primera respuesta HTTP de un sitio HTTPS.

## Por qué importa

Sin mapa de capas, cada error de red se vuelve “el Wi‑Fi está mal”. Hoy instalas el diagrama mental que usarás hasta M18.

## Conceptos

- Encapsulación y desencapsulación entre capas.
- Diferencia entre **protocolo** y **servicio** expuesto.
- Puerto lógico vs dirección IP.
- Request/response en capa de aplicación (HTTP).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m10-redes/labs
curl -v https://example.com -o /dev/null 2>&1 | tee projects/m10-redes/labs/curl-example.log
```

En `projects/m10-redes/dia1.md` responde: ¿qué capas ves en la salida? (resolución, TCP, TLS, HTTP). Compara `http://example.com` vs `https://` (redirección).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l01 modelo-de-capas-y-primer-curl"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Tanenbaum | Introducción + capas | MDN *Overview of HTTP* (vista rápida) |
| Plan | [Hilo seguridad](../../../hilos/seguridad.md) (10 min) | — |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Existe `dia1.md` con qué protege TLS y qué **no** protege.
2. Log `curl -v` guardado en `labs/`.
3. Diagrama ASCII de capas en la bitácora.

## Errores comunes

- Pegar la salida entera sin resaltar líneas relevantes.
- Confundir TLS con “cifrado de la base de datos”.

## Siguiente

[L02 — IP, direccionamiento y enrutamiento intro](L02-ip-direccionamiento-y-enrutamiento-intro.md)
