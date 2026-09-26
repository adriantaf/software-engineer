---
id: L02
materia: M14
orden: 2
titulo: Factory Method para notificadores de canal
horas: 5
semana: 1
lectura: "Refactoring.Guru Factory Method"
evidencia: "projects/m14-patrones/src/notificador-factory.ts"
---

# L02 — Factory Method para notificadores de canal

**~5 h · Semana 1**

## Objetivo

Encapsular creación de notificadores (email vs enlace WhatsApp) con Factory Method o factory simple en TS.

## Por qué importa

Agenda Ops enviará recordatorios por distintos canales sin que el dominio conozca detalles.

## Conceptos

- Factory Method.
- creación variable.
- dominio aislado.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea interfaz `Notificador` y factory `crearNotificador(canal)`. Test: factory devuelve implementación correcta por canal.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l02 factory-method-para-notificadores-de-can"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Refactoring.Guru | Factory Method | — |

## Hecho cuando

1. Factory con test por canal.
2. Sin `new` disperso en servicio de citas.
3. Commit feat(m14).

## Errores comunes

- Factory que solo hace `new` fijo.
- Lógica de negocio dentro del factory.

## Siguiente

[L03 — Singleton: cuándo NO usarlo](L03-singleton-cuando-no-usarlo.md)
