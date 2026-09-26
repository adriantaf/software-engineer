---
id: L11
materia: M10
orden: 11
titulo: Lab openssl y pinning conceptual
horas: 5
semana: 3
lectura: "MDN certificate pinning (advertencias) + hilo seguridad"
evidencia: "labs/openssl-lab.md"
---

# L11 — Lab openssl y pinning conceptual

**~5 h · Semana 3**

## Objetivo

Verificar manualmente un certificado contra el hostname y discutir por qué el pinning raramente se hace a mano en web apps.

## Por qué importa

Entender confianza del SO vs pinning evita modas peligrosas en apps móviles y APIs.

## Conceptos

- Hostname verification.
- Pinning vs CA store.
- MITM en redes captive portal.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Prueba `curl` contra un host con SNI correcto e incorrecto (`--resolve` si hace falta). Documenta error esperado.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m10): l11 lab-openssl-y-pinning-conceptual"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | [Hilo seguridad](../../../hilos/seguridad.md) | OWASP Transport Layer Protection (vista rápida) |
| Catálogo | Entrada M10 | [Bibliografía · M10](../../../bibliografia.md#m10-redes) |


## Hecho cuando

1. Experimento SNI/hostname documentado.
2. Opinión fundamentada sobre pinning.
3. Entrada P1 semana 3.

## Errores comunes

- Deshabilitar verificación TLS en prod “temporalmente”.
- Pinning sin plan de rotación.

## Siguiente

[L12 — MITM conceptual y amenazas de enlace](L12-mitm-conceptual-y-amenazas-de-enlace.md)
