---
id: L25
materia: M17
orden: 25
titulo: Mapa OWASP Top 10 en el piloto
horas: 5
semana: 7
lectura: "OWASP Top 10 overview"
evidencia: "projects/m17-agenda-ops/docs/owasp-mapa.md"
---

# L25 — Mapa OWASP Top 10 en el piloto

**~5 h · Semana 7**

## Objetivo

Tabla: cada riesgo → mitigación actual o gap hacia M18.

## Por qué importa

M18 profundiza; hoy ubicas huecos.

## Conceptos

- OWASP.
- gap.
- mitigación.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

owasp-mapa.md con ≥8 filas honestas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l25 mapa-owasp-top-10-en-el-piloto"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| OWASP | Top 10 | hilo seguridad |

## Hecho cuando

1. owasp-mapa.md.
2. Gaps M18.
3. Commit.

## Errores comunes

- Marcar todo mitigado.
- Ignorar auth.

## Siguiente

[L26 — Headers de seguridad y CORS prod](L26-headers-de-seguridad-y-cors-prod.md)
