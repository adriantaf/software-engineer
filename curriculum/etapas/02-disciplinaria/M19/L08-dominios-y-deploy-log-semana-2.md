---
id: L08
materia: M19
orden: 8
titulo: Dominios y deploy-log semana 2
horas: 5
semana: 2
lectura: "DNS del proveedor"
evidencia: "projects/m19-ops/dominios.md"
---

# L08 — Dominios y deploy-log semana 2

**~5 h · Semana 2**

## Objetivo

Registrar subdominios staging (y prod planificado); enlazar con deploy-log.

## Por qué importa

Trials M22 necesitan URL estable.

## Conceptos

- CNAME
- cert automático

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

dominios.md con registros y TTL. Verifica cert válido en navegador.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l08 dominios-y-deploy-log-semana-2"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M10 | DNS | — |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. dominios.md
2. Cert OK
3. deploy-log actualizado

## Errores comunes

- IP directa sin nombre
- Cert expirado ignorado

## Siguiente

[L09 — Promover configuración a producción](L09-promover-configuracion-a-produccion.md)
