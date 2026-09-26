---
id: L12
materia: M20
orden: 12
titulo: Deep link opcional a una cita
horas: 5
semana: 3
lectura: "Deep linking intro"
evidencia: "projects/m20-movil/deep-link.md"
---

# L12 — Deep link opcional a una cita

**~5 h · Semana 3**

## Objetivo

Configurar esquema o ruta para abrir detalle desde URL/notificación futura.

## Por qué importa

Preparación recordatorios WhatsApp futuro.

## Conceptos

- deep link
- routing

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

deep-link.md con formato URL y prueba manual (adb xcrun si aplica).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l12 deep-link-opcional-a-una-cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docs | deep linking | — |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Doc deep link
2. Prueba manual o N/A justificado
3. Commit config

## Errores comunes

- Deep link sin auth
- Abrir cita de otro user

## Siguiente

[L13 — Lista vacía con copy útil](L13-lista-vacia-con-copy-util.md)
